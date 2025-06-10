import openai
import os

def get_natural_language_query():
    """Prompts the user for a natural language query and returns the input."""
    query = input("Please enter your natural language query: ")
    return query

def convert_natural_language_to_sql(natural_language_query):
    """
    Converts a natural language query to an SQL query using the OpenAI API.

    Args:
        natural_language_query: The natural language query string.

    Returns:
        The SQL query string, or None if an error occurs.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        return None

    openai.api_key = api_key

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert assistant that translates natural language text into SQL queries. Only return the SQL query and nothing else."},
                {"role": "user", "content": f"Translate the following natural language query into an SQL query. Natural language query: {natural_language_query}"}
            ],
            temperature=0,
            max_tokens=150
        )
        sql_query = response.choices[0].message.content.strip()
        return sql_query
    except openai.APIError as e:
        print(f"OpenAI API Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    natural_query = get_natural_language_query()
    if natural_query:
        # Optional: echo the input
        # print(f"Original query: {natural_query}")
        sql_query = convert_natural_language_to_sql(natural_query)
        if sql_query:
            print(f"Generated SQL Query: {sql_query}")
        # Error messages from convert_natural_language_to_sql will be printed if it fails
    else:
        print("No input provided. Exiting.")
