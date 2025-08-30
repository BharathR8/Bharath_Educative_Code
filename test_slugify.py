import pytest
from app import slugify

def test_basic_phrase():
    assert slugify("Hello World") == "hello-world"

def test_multiple_punctuation():
    assert slugify("Hello, World! How are you?") == "hello-world-how-are-you"

def test_string_with_emojis():
    assert slugify("Hello 😊 World 🚀!") == "hello-world"