"""This is the entry point of the program."""


def create_box(height, width, character):
    return (character*width + '\n')*height

if __name__ == '__main__':
    create_box(3, 4, '*')
