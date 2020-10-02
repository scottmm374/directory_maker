
# Driver function
import os
# if __name__ == "__main__":
for (root, dirs, files) in os.walk('/Users/michellescott/Documents/Lambda/practice_script/testing/', topdown=True):
    print(root)
    print(dirs)
    print(files)
    print('--------------------------------')
