import os

script_name = __file__.split('\\')[-1:][0]
path = '.'

# We are starting the chapter from 00, because current directory is 00
# Then it will enter into the first directory inside the current directory
chapter = '00'
pre = 'C' + chapter + 'L'


def increment_chapter():
    global chapter
    global pre
    chapter = int(chapter)
    chapter += 1
    if chapter < 10:
        chapter = '0' + str(chapter)

    chapter = str(chapter)
    pre = 'C' + chapter + 'L'


def get_new_file_name(file_name):
    try:
        # ex. file_name = '2.1 Hello World.txt'

        # Spli the file name after the first space
        file_name_parts = file_name.split(' ', 1)
        # ex. file_name_parts = ['2.1', 'Hello World.txt']

        # If first part ends with '.'. Use slice [start:end]
        # Update the first part by keeping everthing without the last char
        if file_name_parts[0].endswith('.'):
            file_name_parts[0] = file_name_parts[0][:-1]
            # ex. file_name_parts[0] = '10.' -> '10'

        # If the first part is less than 10, add 0 at the beginning
        if float(file_name_parts[0]) < 10:
            file_name_parts[0] = '0' + file_name_parts[0]
        # ex. file_name_parts[0] = '2.1' -> '02.1'

        # Add the pre at the beginning of the first part
        file_name_parts[0] = pre + file_name_parts[0]
        # ex. file_name_parts[0] = 'C01L02.1'

        # Create name string from the name parts list
        new_file_name = ' '.join(file_name_parts)
        # ex. new_file_name = 'C01L02.1 Hello World.txt'

        return new_file_name

    except Exception:
        return file_name


def rename(file_name, new_file_name):
    try:
        os.rename(file_name, new_file_name)
    except OSError as e:
        print("Error:", e)


def main():
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file != script_name:
                file_name = os.path.join(r, file)
                new_file_name = os.path.join(r, get_new_file_name(file))
                # Because of encoding problem while printing, print() is commented.
                # print(file_name, new_file_name)
                rename(file_name, new_file_name)
        increment_chapter()


if __name__ == '__main__':
    main()
