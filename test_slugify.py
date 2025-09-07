import pytest
from app import slugify

def test_basic_phrase():
    assert slugify("Hello World") == "hello-world"

def test_multiple_punctuation():
    assert slugify("Hello, World! How are you?") == "hello-world-how-are-you"

def test_string_with_emojis():
    assert slugify("Hello 😊 World 🚀!") == "hello-world"

def test_empty_string():
    assert slugify("") == ""

def test_only_punctuation():
    assert slugify("!!!...,,,") == ""

def test_numbers_in_string():
    assert slugify("Hello 123 World") == "hello-123-world"

def test_non_ascii_characters():
    assert slugify("Café Münsterländer") == "cafe-munsterlander"  # Adjust expectation if slugify preserves accents

def test_leading_trailing_spaces():
    assert slugify("  Hello World  ") == "hello-world"

def test_consecutive_spaces_and_punctuation():
    assert slugify("Hello    World!!!") == "hello-world"

def test_mixed_case():
    assert slugify("HeLLo WoRLd") == "hello-world"