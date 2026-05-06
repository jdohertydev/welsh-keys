# Welsh Keys - Agent Instructions

## Project summary

Welsh Keys is a small Windows desktop utility for typing Welsh accented characters.

The MVP is a compact always-on-top keyboard-style app. The user clicks a Welsh character and the character should insert at the cursor in the previously active app. A copy-only fallback mode should also be available.

## Technology

Use Python.

Current preferred packages:
- customtkinter for the GUI
- pyperclip for clipboard handling
- pyautogui for sending Ctrl+V
- pygetwindow for active window tracking

## Current status

There is already a working prototype in `welsh_keys.py`.

Do not rewrite the entire project unless necessary. Make small, reviewable improvements.

## MVP scope

Required features:
- Always-on-top window
- Dark keyboard-style interface
- Core Welsh character buttons:
  - â ê î ô û ŵ ŷ ï ö
  - Â Ê Î Ô Û Ŵ Ŷ Ï Ö
- Shift toggle for uppercase/lowercase
- Insert-at-cursor mode
- Copy-only fallback mode
- Status message after each action

## Current requested improvement

Make the app resizable and responsive.

Requirements:
- The window should be user-resizable.
- The app should have a sensible minimum size.
- The Welsh key buttons should resize or reflow cleanly as the window changes size.
- Text should remain readable at smaller sizes.
- Existing insert/copy/shift behaviour must continue working.
- Keep the visual style dark and keyboard-like.

## Do not add yet

Do not add these in this task:
- Most-used memory
- Recent row
- Advanced accent tabs
- Anki helper
- Installer
- System tray
- Icon

## UX wording

App name: Welsh Keys

Instruction text:
Click where you want to type, then click a Welsh key.

Status examples:
- Ready
- Inserted: ŵ
- Copied: ŵ
- Insert failed. Copied: ŵ

## Visual style

Use a Windows On-Screen Keyboard inspired look:
- Dark background
- Dark grey rectangular keys
- Light text
- Subtle borders
- Segoe UI font
- Compact layout

Suggested colours:
- App background: #1b1b1b
- Key background: #303030
- Key hover: #3a3a3a
- Border: #4a4a4a
- Main text: #f2f2f2
- Secondary text: #cfcfcf

## Manual testing

Test manually in this order:
1. Run `python welsh_keys.py`
2. Confirm the app opens.
3. Confirm the window can be resized.
4. Confirm keys remain usable when resized smaller and larger.
5. Confirm clicking â inserts into Notepad.
6. Confirm Shift changes keys to uppercase.
7. Confirm Copy mode copies characters.