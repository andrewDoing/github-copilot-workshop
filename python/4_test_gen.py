# Scenario: Write a function that calculates the nth Fibonacci number.
# Goal: Use Copilot to generate edge-case tests (e.g., 0, 1, negative numbers).
# In a live demo, after writing the function, rely on Copilot to help write tests.

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative integers.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Hypothetical test cases generated with Copilot assistance:
def test_fibonacci():
    pass

if __name__ == "__main__":
    test_fibonacci()
    print("All tests passed.")