def read_text_from_file(file_path):
    """Reads and returns the text from a .txt file."""
    with open(file_path, 'r') as file:
        text = file.read()
    return text
