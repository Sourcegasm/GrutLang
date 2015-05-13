import sys
import os.path


def convert(file):
    print("Converting %s" % (file))


if len(sys.argv) <= 1:
    print("No file specified. Aborting.")
    sys.exit()

for i in range(1, len(sys.argv)):
    if not os.path.isfile(sys.argv[i]):
        print("%s is not a file or it doesn't exist. Aborting" % (sys.argv[i]))
        sys.exit()

for i in range(1, len(sys.argv)):
    convert(sys.argv[i])
