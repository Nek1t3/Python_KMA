from app.io.input import consoleInput, fileInput, pandasInput
from app.io.output import consoleOutput, fileOutput

def main():
    consoleOutput(consoleInput())
    fileOutput(consoleInput())

    consoleOutput(fileInput())
    fileOutput(fileInput())

    consoleOutput(pandasInput())
    fileOutput(pandasInput())

if __name__ == "__main__":
    main()