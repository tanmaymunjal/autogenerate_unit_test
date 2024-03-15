def extract_python_code_blocks(text):
    code_blocks = []
    start_marker = "```python"
    end_marker = "```"
    start_index = 0

    while True:
        start_index = text.find(start_marker, start_index)
        if start_index == -1:  # No more code blocks found
            break
        end_index = text.find(end_marker, start_index + len(start_marker))
        if end_index == -1:  # No ending marker found after the starting marker
            break  # This could be considered an error in the input format
        code_block = text[start_index + len(start_marker) : end_index].strip()
        code_blocks.append(code_block)
        start_index = end_index + len(
            end_marker
        )  # Move past this code block for the next iteration

    return "\n".join(code_blocks)
