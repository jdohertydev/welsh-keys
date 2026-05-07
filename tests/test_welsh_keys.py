import importlib

import welsh_keys


def test_lowercase_chars_are_expected():
    assert welsh_keys.LOWERCASE_CHARS == ["â", "ê", "î", "ô", "û", "ŵ", "ŷ", "ï", "ö"]


def test_uppercase_chars_are_expected():
    assert welsh_keys.UPPERCASE_CHARS == ["Â", "Ê", "Î", "Ô", "Û", "Ŵ", "Ŷ", "Ï", "Ö"]


def test_character_lists_have_matching_lengths():
    assert len(welsh_keys.LOWERCASE_CHARS) == len(welsh_keys.UPPERCASE_CHARS)


def test_module_import_does_not_launch_app():
    module = importlib.import_module("welsh_keys")

    assert module.WelshKeys.__name__ == "WelshKeys"


def test_theme_definitions_include_required_ui_values():
    expected_keys = {
        "app_background",
        "key_background",
        "key_hover",
        "border",
        "text",
    }

    assert set(welsh_keys.THEMES) == {"dark", "light"}
    assert set(welsh_keys.THEMES["dark"]) == expected_keys
    assert set(welsh_keys.THEMES["light"]) == expected_keys

    assert welsh_keys.THEMES["dark"] == {
        "app_background": "#1b1b1b",
        "key_background": "#303030",
        "key_hover": "#3a3a3a",
        "border": "#4a4a4a",
        "text": "#f2f2f2",
    }
    assert welsh_keys.THEMES["light"] == {
        "app_background": "#f3f3f3",
        "key_background": "#ffffff",
        "key_hover": "#e8e8e8",
        "border": "#c8c8c8",
        "text": "#1f1f1f",
    }


def test_pending_insert_buffer_combines_fast_clicks():
    buffer = welsh_keys.PendingInsertBuffer()

    for char in welsh_keys.LOWERCASE_CHARS[:5]:
        buffer.append(char)

    assert buffer.pop_all() == "".join(welsh_keys.LOWERCASE_CHARS[:5])


def test_pending_insert_buffer_clears_after_pop():
    buffer = welsh_keys.PendingInsertBuffer()

    buffer.append(welsh_keys.LOWERCASE_CHARS[0])

    assert buffer.has_text()
    assert buffer.pop_all() == welsh_keys.LOWERCASE_CHARS[0]
    assert not buffer.has_text()
    assert buffer.pop_all() == ""
