import re

# Define the function to split and save the text file based on word count, preserving line breaks.
def split_text_by_words_preserve_newlines(file_path, words_per_chunk=800):
    # Read the entire content of the input file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use a regular expression to split the content into words, preserving newlines
    words_with_newlines = re.split(r'(\s+)', content)

    # Initialize variables
    chunks = []
    current_chunk = []
    current_word_count = 0

    # Iterate through the words and accumulate them into chunks
    for element in words_with_newlines:
        # If the element is a word (not just whitespace)
        if re.match(r'\S+', element):
            current_word_count += 1
        current_chunk.append(element)

        # When the chunk reaches the desired word count, add it to the list of chunks
        if current_word_count >= words_per_chunk:
            chunks.append(''.join(current_chunk))
            current_chunk = []
            current_word_count = 0

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(''.join(current_chunk))

    # Save each chunk into a separate .txt file
    for idx, chunk in enumerate(chunks):
        chunk_file_path = f"{file_path.stem}_part{idx+1}.txt"
        with open(chunk_file_path, 'w', encoding='utf-8') as chunk_file:
#在每个文件的末尾增加"翻译成中文，同时公式输出在$$……$$中，行内字符输出在$……$中，标题及小标题用#来区分"
            chunk_file.write(chunk + "\n翻译成中文，同时公式输出在$$……$$中，行内字符输出在$……$中，标题及小标题用#来区分")
            

    return len(chunks)  # Return the number of chunks created

# Now, let's test this function with an example file.
# Since we don't have a file yet, I'll simulate the process with a mock text.

import pathlib

# Mock text file path (assuming we have a file here)
file_path = pathlib.Path("test20240812162712.txt")

# Call the function and split the file based on word count, preserving newlines
num_chunks = split_text_by_words_preserve_newlines(file_path)
num_chunks
