import shutil
import os


def main():
    """Cleanup inconsistent song Lyrics file names"""

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.strip()
    filename = ' '.join(filename.split())
    filename = filename.replace(" ", "_")
    filename = filename.replace("(", "_(")
    filename = filename.replace(")", ")_")
    underline_blocks = filename.split("_")
    filename = ""
    for str_block in underline_blocks:
        if str_block != "":
            filename += str_block + "_"
    filename = filename.strip("_")
    filename_base = ""
    filename_point = filename.split(".")
    if len(filename_point) < 2:
        filename_base = filename
        file_extension = "txt"
    elif len(filename_point) == 2:
        filename_base = filename_point[0]
        file_extension = filename.split(".")[-1].lower()
    else:
        file_extension = filename.split(".")[-1].lower()
        for i in range(len(filename_point) - 1):
            filename_base += filename_point[i] + "."
        filename_base = filename_base.strip(".")

    filename_base = filename_base.strip("_")
    name_blocks = filename_base.split("_")
    for i in range(len(name_blocks)):
        temp_name = ""
        for j in range(len(name_blocks[i])):
            if name_blocks[i][j].isupper() and temp_name != '' and (temp_name[-1].isupper() or temp_name[-1].islower()):
                temp_name += "_" + name_blocks[i][j]
            else:
                temp_name += name_blocks[i][j]
        name_blocks[i] = temp_name.title()
    new_name = ""
    for i in range(len(name_blocks)):
        new_name += name_blocks[i]
        if i != len(name_blocks) - 1:
            new_name += "_"
    return new_name + "." + file_extension


if __name__ == "__main__":
    print(get_fixed_filename("Away In A Manger.mp3"))
    print(get_fixed_filename("SilentNight.txt"))
    print(get_fixed_filename("A little town of bethlehem.TXT"))

