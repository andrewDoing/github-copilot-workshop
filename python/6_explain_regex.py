# Scenario: Paste a complex piece of code, like a regex pattern.
# Goal: Use Copilot to explain the code in plain language.

import re

# Complex regex for matching an email:
email_regex = re.compile(
    r"^(?:[a-zA-Z0-9_'^&/+-])+(?:\.[a-zA-Z0-9_'^&/+-]+)*"
    r"@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
)

# Ask Copilot: "Explain the above regex in plain language."
def is_valid_email(email: str) -> bool:
    return email_regex.match(email) is not None

if __name__ == "__main__":
    print(is_valid_email("user@example.com"))  # Expect True
    print(is_valid_email("user@@example..com"))  # Expect False