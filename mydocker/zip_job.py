import os
import sys
import zipfile

arr = ['a', 'b', 'c', 'd']



# Create the text files
for elem in arr:
    with open(elem + '.txt', 'w') as f:
        pass


# Check that all the text files have been created
for elem in arr:
    if not os.path.exists(elem + '.txt'):
        print("Error: File {}.txt does not exist".format(elem))
        sys.exit(1)

# Get the value of the VERSION environment variable
version = os.environ.get('VERSION', '1.0.0')

# Create the ZIP files
for elem in arr:
    with zipfile.ZipFile(elem + '-' + version + '.zip', 'w') as z:
       z.write(elem + '.txt')
       
# Check that all the text files have been created
for elem in arr:
    if not os.path.exists(elem + '-' + version + '.zip'):
        print("Error: File {}.zip does not exist".format(elem))
        sys.exit(2)

print("All ZIP files have been created successfully")