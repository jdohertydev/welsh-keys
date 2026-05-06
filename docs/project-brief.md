# Project Brief

## Purpose

Welsh Keys helps Windows users type Welsh accented characters from a small always-on-top desktop utility.

## Target Users

- Welsh learners and teachers
- Bilingual writers
- People using keyboards without convenient Welsh character shortcuts
- Users entering Welsh text into notes, documents, browsers, spreadsheets, or flashcard tools

## MVP Scope

- Compact fixed-size desktop window
- Dark keyboard-style interface
- Welsh accented character buttons
- Shift toggle for lowercase and uppercase characters
- Insert-at-cursor mode
- Copy-only fallback mode

## Current Features

- Lowercase characters: â ê î ô û ŵ ŷ ï ö
- Uppercase characters: Â Ê Î Ô Û Ŵ Ŷ Ï Ö
- Insert mode uses the clipboard and `Ctrl+V` to place characters in the previously active app
- Copy mode copies the selected character to the clipboard
- Fixed compact layout with all character keys on one row

## Non-Goals For v0.1

- Most-used memory
- Recent row
- Advanced accent tabs
- Anki helper
- Installer
- System tray
- Generated binaries

## Roadmap

- Broaden manual testing across common Windows apps
- Improve focus and paste reliability where practical
- Add packaging only after the prototype workflow is stable
- Consider optional productivity features after v0.1 feedback
