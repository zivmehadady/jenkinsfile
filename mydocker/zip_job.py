import os
import sys
import zipfile

arr = ['a', 'b', 'c', 'd']

# Get the value of the VERSION environment variable
version = os.environ.get('VERSION', '1.2.0')

# Create the text files & Check that all the text files have been created
for elem in arr:
    with open(elem + '.txt', 'w') as f:
        pass
    if not os.path.exists(elem + '.txt'):
        print("Error: File {}.txt does not exist".format(elem))
        sys.exit(1)
    with zipfile.ZipFile(elem + '-' + version + '.zip', 'w') as z:
       z.write(elem + '.txt')
    if not os.path.exists(elem + '-' + version + '.zip'):
        print("Error: File {}.zip does not exist".format(elem))
        sys.exit(1)



print("All ZIP files have been created successfully")