"""This is the entry point of the program."""


def create_box(height, width, character):
    if height >= 1 and width >= 1:
        return (character*width + '\n')*height
    else: 
        return 'height & width must be greater than or equal to 1'

#Add error checking to make sure the width and height is greater or equal to 1
#Add an extra unit test for the third case in the tests file
#make it so only the outer border of the box shows and it is not filled in.

if __name__ == '__main__':
    create_box(3, 4, '*')
