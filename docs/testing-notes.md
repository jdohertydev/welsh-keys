# Testing Notes

Use this checklist for manual testing before publishing changes.

Automated tests cover deterministic logic only, such as character lists and theme palette values. Real app insertion still needs manual testing in target applications.

## Basic Launch

- [ ] Run `python welsh_keys.py`
- [ ] Confirm the app opens
- [ ] Confirm the app stays on top
- [ ] Confirm the window is compact and fixed-size
- [ ] Confirm all Welsh character keys are visible on one row

## Insert Mode

- [ ] Notepad: click into a document, then click `â`
- [ ] Browser text box: click into a text field, then click `â`
- [ ] Word: click into a document, then click `â`
- [ ] Google Docs: click into a document, then click `â`
- [ ] Google Sheets: click into a cell, then click `â`
- [ ] Anki: click into a card field, then click `â`
- [ ] Confirm insertion works where the target app allows paste/focus automation
- [ ] Confirm failed insertion falls back to copying where applicable

## Copy Mode

- [ ] Click `Insert` to switch to copy mode
- [ ] Confirm the mode button changes to `Copy`
- [ ] Click `ŵ`
- [ ] Paste manually into Notepad
- [ ] Confirm the pasted character is `ŵ`

## Shift Mode

- [ ] Click `Shift`
- [ ] Confirm the keys change to uppercase
- [ ] Click `Ŵ`
- [ ] Confirm insert or copy behavior still works
- [ ] Click `Shift` again
- [ ] Confirm the keys return to lowercase

## Theme Mode

- [ ] Click `Light`
- [ ] Confirm the app changes to the light theme
- [ ] Confirm the theme button changes to `Dark`
- [ ] Click `Dark`
- [ ] Confirm the app returns to the dark theme
