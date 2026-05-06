import time
import customtkinter as ctk
import pyautogui
import pygetwindow as gw
import pyperclip


LOWERCASE_CHARS = ["â", "ê", "î", "ô", "û", "ŵ", "ŷ", "ï", "ö"]
UPPERCASE_CHARS = ["Â", "Ê", "Î", "Ô", "Û", "Ŵ", "Ŷ", "Ï", "Ö"]


class WelshKeys(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Welsh Keys")
        self.geometry("610x220")
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
        self.configure(fg_color="#1b1b1b")

        title = ctk.CTkLabel(
            self,
            text="Welsh Keys",
            font=("Segoe UI", 20, "bold"),
            text_color="#f2f2f2",
        )
        title.pack(pady=(14, 4))

        helper = ctk.CTkLabel(
            self,
            text="Click where you want to type, then click a Welsh key.",
            font=("Segoe UI", 12),
            text_color="#cfcfcf",
        )
        helper.pack(pady=(0, 12))

        keys_frame = ctk.CTkFrame(self, fg_color="#1b1b1b")
        keys_frame.pack(pady=(0, 14))

        for char in LOWERCASE_CHARS:
            button = ctk.CTkButton(
                keys_frame,
                text=char,
                width=54,
                height=48,
                fg_color="#303030",
                hover_color="#3a3a3a",
                text_color="#f2f2f2",
                border_width=1,
                border_color="#4a4a4a",
                corner_radius=2,
                font=("Segoe UI", 23),
                command=lambda c=char: self.handle_key(c),
            )
            button.pack(side="left", padx=4)
            self.key_buttons.append(button)

        controls = ctk.CTkFrame(self, fg_color="#1b1b1b")
        controls.pack(pady=(0, 8))

        self.shift_button = ctk.CTkButton(
            controls,
            text="Shift: off",
            width=120,
            height=34,
            fg_color="#303030",
            hover_color="#3a3a3a",
            text_color="#f2f2f2",
            border_width=1,
            border_color="#4a4a4a",
            corner_radius=2,
            font=("Segoe UI", 12),
            command=self.toggle_shift,
        )
        self.shift_button.pack(side="left", padx=5)

        self.mode_button = ctk.CTkButton(
            controls,
            text="Mode: Insert",
            width=140,
            height=34,
            fg_color="#303030",
            hover_color="#3a3a3a",
            text_color="#f2f2f2",
            border_width=1,
            border_color="#4a4a4a",
            corner_radius=2,
            font=("Segoe UI", 12),
            command=self.toggle_mode,
        )
        self.mode_button.pack(side="left", padx=5)

        self.status = ctk.CTkLabel(
            self,
            text="Ready",
            font=("Segoe UI", 12),
            text_color="#cfcfcf",
        )
        self.status.pack()

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
        self.shift_button.configure(
            text="Shift: ON" if self.uppercase else "Shift: off"
        )
        self.refresh_keys()

    def toggle_mode(self):
        self.insert_mode = not self.insert_mode
        self.mode_button.configure(
            text="Mode: Insert" if self.insert_mode else "Mode: Copy"
        )
        self.status.configure(
            text="Insert mode" if self.insert_mode else "Copy mode"
        )

    def handle_key(self, char):
        if self.insert_mode:
            self.insert_at_cursor(char)
        else:
            pyperclip.copy(char)
            self.status.configure(text=f"Copied: {char}")

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

            self.status.configure(text=f"Inserted: {char}")

        except Exception:
            pyperclip.copy(char)
            self.status.configure(text=f"Insert failed. Copied: {char}")


if __name__ == "__main__":
    app = WelshKeys()
    app.mainloop()