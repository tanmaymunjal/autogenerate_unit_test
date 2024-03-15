def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        content = f.read()
    return content


def write_file(filename: str, text: str):
    with open(filename, "a") as f:
        f.write(text)
