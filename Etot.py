import os
import argparse
#Tell argparse to handle argument

parser=argparse.ArgumentParser(description="Hunts down Etot in mdout files")

#Tell argparse what arguments what to expect
parser.add_argument("path", help="The file path to the mdout file you want") 
#get arguments from the user
args= parser.parse_args()
filename= args.path
f= open(filename, 'r')
# Read the data in the file.
data = f.readlines()

# Close the file.
f.close()

# Open a file for writing
f_write = open('Etot.txt', 'w+')

# Loop through the lines
for line in data:
    split_line = line.split()
    if 'Etot' in line:
        print(split_line[2])
        f_write.write(f'{split_line[2]}\n')

f_write.close()
