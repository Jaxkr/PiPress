import json
import sys
import msgpack
import binascii
import quopri
import ntpath

def ASCII(s):
    x = ""
    for i in range(len(s)):
        x += '{0:08b}'.format(ord(s[i]))
    return int(x, 2)


def toChunks(inputString):
    output_array = []
    for i in range(0, len(inputString), 3):
        piece = inputString[i:i+3]
        output_array.append(piece)
    return output_array

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


pi_string = ""

with open('pi-billion.txt', 'r') as myfile:
    pi_string=myfile.read().replace('\n', '')

file_name = sys.argv[1]
start_string = ""
with open(file_name, 'rb') as myfile:
    start_string=myfile.read()

start_string = binascii.b2a_base64(start_string).decode("utf-8")


array_of_pieces = toChunks(start_string)
array_of_numbers = []
for chunk in array_of_pieces:
    print(chunk)
    array_of_numbers.append(ASCII(chunk))

final_output = []
counter = 0
for number in array_of_numbers:
    print("Approximately " + str((counter / len(array_of_numbers)) * 100) + "% complete")
    counter += 1
    index = pi_string.find(str(number))
    print("INDEX: " + str(index))
    length = len(str(number))
    final_output.append([index, length])

print(final_output)


output_object = final_output
output = msgpack.packb(output_object)

output_name = path_leaf(file_name)
text_file = open(output_name+'.pipress', "wb")
text_file.write(output)
text_file.close()
