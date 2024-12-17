# Scenario: Add an off-by-one error in a simple loop-based function.
# Goal: Use Copilot to suggest a fix or explain the issue.
# In a live demo, introduce the bug and ask Copilot for help.

def sum_first_n_numbers(n: int) -> int:
    # Intentional off-by-one bug: This should sum from 1 to n inclusive,
    # but currently it misses the last number.
    pass


if __name__ == "__main__":
    print(sum_first_n_numbers(5))  # Expect 15, currently returns 10 due to off-by-one error.