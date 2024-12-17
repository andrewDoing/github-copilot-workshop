# Scenario: Write part of a SQL query to fetch the top 5 highest-paid employees.
# Goal: Let Copilot complete the query.

# In a live demo, start typing the SQL query as a string and let Copilot suggest completion.
# Although we won't run the query here, we can show what Copilot might produce:

def get_top_5_employees_sql() -> str:
    # Start typing and let Copilot help:
    # "SELECT first_name, last_name, salary FROM employees"
    # Copilot might complete:
    query = """
    SELECT first_name, last_name, salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 5;
    """
    return query

if __name__ == "__main__":
    print(get_top_5_employees_sql())