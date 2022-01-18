
import os


def main():
    """Move the files into the folder where the user wants to store files"""
    os.chdir("FilesToSort")
    extension_of_category = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_of_category:
            category = input(f"What category would you like yo sort {extension} files into? ")
            extension_of_category[extension] = category
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print(f"{extension}/{filename}")
        os.rename(filename, f"{extension}/{filename}")


main()