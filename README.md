# Welsh Keys

Welsh Keys is a small Windows desktop utility for typing Welsh accented characters. It provides a compact always-on-top keyboard window with insert-at-cursor and copy-only modes.

## Screenshot

Screenshot coming later. The current prototype is intentionally minimal: one row of Welsh keys and compact control buttons.

## Features

- Compact fixed-size desktop window
- Always-on-top behavior
- Dark Windows keyboard-inspired styling
- Lowercase and uppercase Welsh accented characters
- Shift toggle for character case
- Insert mode using clipboard paste into the previously active app
- Copy mode for apps where direct insertion is unreliable
- Compact Light/Dark theme toggle

## Characters Supported

Lowercase:

```text
â ê î ô û ŵ ŷ ï ö
```

Uppercase:

```text
Â Ê Î Ô Û Ŵ Ŷ Ï Ö
```

## Requirements

- Windows
- Python 3.10 or newer
- Dependencies listed in `requirements.txt`

## Installation

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run

```powershell
python welsh_keys.py
```

## Testing

Install development dependencies:

```powershell
python -m pip install -r requirements-dev.txt
```

Run the automated tests:

```powershell
pytest
```

The automated tests cover deterministic module data only. They do not automate external applications or insertion behavior.

## Usage

1. Open Welsh Keys.
2. Click in the app where you want to type.
3. Click a Welsh character key.
4. Use `Shift` to switch between lowercase and uppercase characters.
5. Use `Insert` / `Copy` to switch between direct insertion and copy-only mode.
6. Use `Light` / `Dark` to switch between dark and light themes.

## Known Limitations

- Insert mode depends on clipboard paste and active-window focus behavior.
- Some apps may block automated paste or focus changes.
- Copy mode is the fallback when insertion is unreliable.
- This is currently a Windows-focused prototype, not a packaged installer.

## Privacy And Security

Welsh Keys runs locally and does not send network requests. Insert mode temporarily places the selected character on the clipboard, sends `Ctrl+V`, and then attempts to restore the previous clipboard contents. The app tracks the previously active window title locally so it can return focus before pasting.

## Prototype Status

This is a v0.1 prototype focused on the core typing workflow. Packaging, system tray support, advanced character tools, and app-specific helpers are intentionally out of scope for now.

## Development Notes

- Keep the app small and focused.
- Avoid adding features before the core workflow has been manually tested in common Windows apps.
- Run a basic syntax/import check before publishing changes:

```powershell
.venv\Scripts\python.exe -m py_compile welsh_keys.py
.venv\Scripts\python.exe -c "import welsh_keys; print('import ok')"
```

## License

MIT License. See `LICENSE` for details.
