# text_2_sql

# Natural Language to SQL Converter

This script converts natural language queries into SQL queries using the OpenAI API (GPT-4o model).

## Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Set up your OpenAI API Key:**
    You need to have an OpenAI API key. Set it as an environment variable named `OPENAI_API_KEY`.
    ```bash
    export OPENAI_API_KEY='your_api_key_here'
    ```
    Replace `your_api_key_here` with your actual OpenAI API key. To make this permanent, add this line to your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`).

3.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

Once the setup is complete, you can run the script:

```bash
python natural_to_sql.py
```

The script will prompt you to enter your natural language query. After you provide the input, it will output the generated SQL query.

Example:
```
Please enter your natural language query: show me all users from Canada
Generated SQL Query: SELECT * FROM users WHERE country = 'Canada';
```

## Deactivating the virtual environment (optional)
```bash
deactivate
```