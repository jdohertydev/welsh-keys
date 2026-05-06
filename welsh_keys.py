import time

import customtkinter as ctk
import pyautogui
import pygetwindow as gw
import pyperclip


LOWERCASE_CHARS = ["â", "ê", "î", "ô", "û", "ŵ", "ŷ", "ï", "ö"]
UPPERCASE_CHARS = ["Â", "Ê", "Î", "Ô", "Û", "Ŵ", "Ŷ", "Ï", "Ö"]

APP_BACKGROUND = "#1b1b1b"
KEY_BACKGROUND = "#303030"
KEY_HOVER = "#3a3a3a"
KEY_BORDER = "#4a4a4a"
MAIN_TEXT = "#f2f2f2"
FONT_FAMILY = "Segoe UI"

BUTTON_STYLE = {
    "fg_color": KEY_BACKGROUND,
    "hover_color": KEY_HOVER,
    "text_color": MAIN_TEXT,
    "border_width": 1,
    "border_color": KEY_BORDER,
    "corner_radius": 2,
}


class WelshKeys(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Welsh Keys")
        self.geometry("480x90")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        ctk.set_appearance_mode("dark")

        self.uppercase = False
        self.insert_mode = True
        self.previous_window_title = None
        self.key_buttons = []

        self.build_ui()
        self.track_active_window()

    def build_ui(self):
        self.configure(fg_color=APP_BACKGROUND)
        self.grid_columnconfigure(0, weight=1)

        keys_frame = ctk.CTkFrame(self, fg_color=APP_BACKGROUND)
        keys_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(8, 6))
        keys_frame.grid_columnconfigure(tuple(range(len(LOWERCASE_CHARS))), weight=1)

        for index, char in enumerate(LOWERCASE_CHARS):
            button = ctk.CTkButton(
                keys_frame,
                text=char,
                width=42,
                height=38,
                font=(FONT_FAMILY, 20),
                **BUTTON_STYLE,
                command=lambda c=char: self.handle_key(c),
            )
            button.grid(row=0, column=index, sticky="ew", padx=2)
            self.key_buttons.append(button)

        controls = ctk.CTkFrame(self, fg_color=APP_BACKGROUND)
        controls.grid(row=1, column=0, pady=(0, 8))

        self.shift_button = ctk.CTkButton(
            controls,
            text="Shift",
            width=92,
            height=30,
            font=(FONT_FAMILY, 12),
            **BUTTON_STYLE,
            command=self.toggle_shift,
        )
        self.shift_button.grid(row=0, column=0, padx=4)

        self.mode_button = ctk.CTkButton(
            controls,
            text="Insert",
            width=92,
            height=30,
            font=(FONT_FAMILY, 12),
            **BUTTON_STYLE,
            command=self.toggle_mode,
        )
        self.mode_button.grid(row=0, column=1, padx=4)

    def track_active_window(self):
        try:
            active_window = gw.getActiveWindow()

            if active_window and active_window.title:
                if "Welsh Keys" not in active_window.title:
                    self.previous_window_title = active_window.title

        except Exception:
            pass

        self.after(250, self.track_active_window)

    def current_characters(self):
        return UPPERCASE_CHARS if self.uppercase else LOWERCASE_CHARS

    def refresh_keys(self):
        for button, char in zip(self.key_buttons, self.current_characters()):
            button.configure(
                text=char,
                command=lambda c=char: self.handle_key(c),
            )

    def toggle_shift(self):
        self.uppercase = not self.uppercase
        self.refresh_keys()

    def toggle_mode(self):
        self.insert_mode = not self.insert_mode
        self.mode_button.configure(
            text="Insert" if self.insert_mode else "Copy"
        )

    def handle_key(self, char):
        if self.insert_mode:
            self.insert_at_cursor(char)
        else:
            pyperclip.copy(char)

    def insert_at_cursor(self, char):
        previous_clipboard = None

        try:
            previous_clipboard = pyperclip.paste()
        except Exception:
            pass

        try:
            pyperclip.copy(char)

            if self.previous_window_title:
                windows = gw.getWindowsWithTitle(self.previous_window_title)

                if windows:
                    windows[0].activate()
                    time.sleep(0.2)

            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.2)

            if previous_clipboard is not None:
                pyperclip.copy(previous_clipboard)

        except Exception:
            pyperclip.copy(char)


if __name__ == "__main__":
    app = WelshKeys()
    app.mainloop()
