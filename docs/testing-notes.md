# Testing Notes

Use this checklist for manual testing before publishing changes.

Automated tests cover deterministic logic only, such as character lists and theme palette values. Real app insertion still needs manual testing in target applications.

## Basic Launch

- [ ] Run `python welsh_keys.py`
- [ ] Confirm the app opens
- [ ] Confirm the app stays on top
- [ ] Confirm the window is compact and fixed-size
- [ ] Confirm all Welsh character keys are visible on one row
- [ ] Confirm the footer contains only `Shift` and `Light` or `Dark`

## Insertion

- [ ] Notepad: click into a document, then click `â`
- [ ] Browser text box: click into a text field, then click `â`
- [ ] Browser text box: rapidly click `â` `û` `ŵ` `ŷ` `ö`
- [ ] Confirm the browser receives `âûŵŷö` without old clipboard text between characters
- [ ] Confirm the clipboard now contains `âûŵŷö`
- [ ] Word: click into a document, then click `â`
- [ ] Google Docs: click into a document, then click `â`
- [ ] Google Sheets: click into a cell, then click `â`
- [ ] Anki: click into a card field, then click `â`
- [ ] Confirm insertion works where the target app allows paste/focus automation
- [ ] Confirm that if automatic insertion fails, pressing `Ctrl+V` manually pastes the Welsh character
- [ ] Note: clipboard restoration is intentionally not performed in v0.1.0 for insertion reliability

## Shift Mode

- [ ] Click `Shift`
- [ ] Confirm the keys change to uppercase
- [ ] Click `Ŵ`
- [ ] Confirm insertion still works
- [ ] Click `Shift` again
- [ ] Confirm the keys return to lowercase

## Theme Mode

- [ ] Click `Light`
- [ ] Confirm the app changes to the light theme
- [ ] Confirm the theme button changes to `Dark`
- [ ] Click `Dark`
- [ ] Confirm the app returns to the dark theme
