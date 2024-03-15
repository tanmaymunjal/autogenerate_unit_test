import os
from openai import OpenAI

# from tokenise import tokenise_code
from extract import extract_python_code_blocks
from utils import read_file, write_file

GPT4_UN_LAZIED_VERSION = "gpt-4-0125-preview"


class UnitTestGenerator:
    def __init__(self, model=GPT4_UN_LAZIED_VERSION, max_context=10 ** (8)):
        self.__model = model
        self.__client = OpenAI()
        self.max_context = max_context

    def call_open_api(self, prompt: str) -> str:
        """
        Call the OpenAI API to generate a summary based on the provided prompt.

        Args:
            prompt (str): The prompt to be used for generating the summary.

        Returns:
            str: The generated summary.
        """
        response = self.__client.chat.completions.create(
            model=self.__model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()

    @staticmethod
    def get_subset(text, i: int, j: int):
        """
        Get a subset of the text based on the specified indices.

        Args:
            text (str): The input text.
            i (int): The start index.
            j (int): The end index.

        Returns:
            str: The subset of the text.

        Note:
            - Returns empty string if start index is more than length of text
        """
        if i < len(text) - 1:
            return text[i:j]
        return ""

    @staticmethod
    def format_prompt(prompt: str):
        """
        Format the prompt for summarization.

        Args:
            prompt (str): The prompt to be formatted.

        Returns:
            str: The formatted prompt.
        """
        addition = """Can you please generate fully working unit tests for the following code? Generate full code, it will becopy pasted as such.
        The tests will be placed in a tests/ folder in the directory where the folder is, make sure to include that in your coding.
        Module name is clii
        """
        return addition + prompt

    def generate_tests(self, filename: str):
        code = read_file(filename)
        i = 0
        j = self.max_context
        subset = UnitTestGenerator.get_subset(code, i, j)
        index = 0
        while subset != "":
            prompt = UnitTestGenerator.format_prompt(code)
            code = self.call_open_api(prompt)
            code = extract_python_code_blocks(code)
            new_filename = "tests/test_" + filename.split(".py")[0] + f"_{index}.py"
            write_file(new_filename, code)
            i += self.max_context
            j += self.max_context
            subset = UnitTestGenerator.get_subset(code, i, j)
            index += 1
