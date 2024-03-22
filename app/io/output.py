# output.py

def consoleOutput(text):
    """Function to print text to the console."""
    print(text)

def fileOutput(text):
    """Function to write text to a file."""
    with open("output_file.txt", "w") as f:
        f.write(text)
