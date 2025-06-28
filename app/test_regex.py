import re

def test_regex(regex, test_string):
    try:
        pattern = re.compile(regex)
        match = pattern.search(test_string)
        return bool(match)
    except re.error as e:
        print(f"Regex Error: {e}")
        return False
