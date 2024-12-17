# Scenario: Paste a complex piece of code, like a regex pattern.
# Goal: Use Copilot to explain the code in plain language.
#
# In a live demo, you could paste a complex regex and ask Copilot to comment on it.

import re

# Complex regex for matching an email:
email_regex = re.compile(
    r"^(?:[a-zA-Z0-9_'^&/+-])+(?:\.[a-zA-Z0-9_'^&/+-]+)*"
    r"@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
)

# Ask Copilot: "Explain the above regex in plain language."
# Copilot might generate a helpful comment:
# This regex matches a string that:
# 1. Starts with one or more alphanumeric or allowed special characters.
# 2. Allows optional dot-separated sequences of similar characters.
# 3. Includes an '@' symbol followed by one or more domain-like parts (words separated by dots).
# 4. Ends with a top-level domain of at least two alphabetical characters.

def is_valid_email(email: str) -> bool:
    return email_regex.match(email) is not None

if __name__ == "__main__":
    print(is_valid_email("user@example.com"))  # Expect True
    print(is_valid_email("user@@example..com"))  # Expect False