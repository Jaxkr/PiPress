import json
import sys
import binascii
import msgpack
import ntpath

with open(sys.argv[1], 'rb') as myfile:
    input_string=myfile.read()

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

input_object = msgpack.unpackb(input_string, encoding='utf-8')
pi_string = ""
file_output_name = path_leaf(sys.argv[1])[:-8]
print(file_output_name)

with open('pi-billion.txt', 'r') as myfile:
    pi_string=myfile.read().replace('\n', '')


data = input_object
final_output_string = ""

for couple in data:
    chunk = int(pi_string[couple[0]:couple[0]+couple[1]])
    binary = bin(chunk)[2:].zfill(24)
    print(binary)
    for i in range(0, len(binary), 8):
        number = int(str(binary[i:i+8]), 2)
        if (number != 0):
            char = chr(number)
            final_output_string += char


output_file = open(file_output_name, 'wb')
output_file.write(binascii.a2b_base64(final_output_string))
