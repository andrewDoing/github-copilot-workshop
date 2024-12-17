# Scenario: Write a comment describing a function that converts a string to camelCase.
# Goal: Let Copilot generate the function based on the comment.
# In a live demo, you would write the comment and rely on Copilot's suggestion.

def to_camel_case(s: str) -> str:
    # Convert a given string to camelCase:
    # 1. Split on non-alphanumeric characters.
    # 2. Lowercase all parts except the first character of each word after the first word.
    # 3. Concatenate them together.
    pass

if __name__ == "__main__":
    print(to_camel_case("Hello World"))  # Expect "helloWorld"