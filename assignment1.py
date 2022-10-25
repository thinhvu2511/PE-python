# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

if __name__ == '__main__':
    try:
        text = input("Input: ")
        list = text.split()
        print("The last word is " + f'"{list[-1]}"' + " with length " + str(len(str(list[-1]))))
    except:
        print('Input a string.')
