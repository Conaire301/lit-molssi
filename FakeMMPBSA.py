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
base_filename=filename.split('.')[0]
output_filename= F'{base_filename}_Etot.txt'  
f_write = open(output_filename, 'w+')
print(F'Writing output to {output_filename}')
etot= []
# Loop through the lines
for line in data:
    split_line = line.split()
    if 'Etot' in line:
        etot.append(split_line[2])
etot=etot[:-2]

for energy in etot:
    f_write.write(F"{energy}\n")

f_write.close()
