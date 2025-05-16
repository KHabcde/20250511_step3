from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY が設定されていません")

client = OpenAI(api_key=api_key)

def natural_to_macro(text: str) -> str:
    """
    Converts natural language text to macro syntax using OpenAI's ChatGPT API.

    Args:
        text (str): The natural language command.

    Returns:
        str: The converted macro syntax.
    """
    try:
        # Load the prompt template from an external file
        with open("prompt_template.txt", "r", encoding="utf-8") as file:
            prompt_template = file.read()

        # Format the template with the input text
        prompt = prompt_template.format(text=text)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        if not response.choices or not response.choices[0].message.content.strip():
            raise ValueError("Empty response from the API.")
        macro_syntax = response.choices[0].message.content.strip()
        return macro_syntax
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return "Error: Empty response from the API."
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Error: API call failed."

def parse_macro_line(line: str) -> dict:
    """
    Parses a macro line into its components.

    Args:
        line (str): A single line of macro syntax.

    Returns:
        dict: A dictionary with keys 'cmd', 'arg', 'ext1', 'ext2', 'ext3'.
    """
    parts = line.split('\t')  # Split by tab
    keys = ['cmd', 'arg', 'ext1', 'ext2', 'ext3']
    parsed = {key: parts[i] if i < len(parts) else None for i, key in enumerate(keys)}
    return parsed
