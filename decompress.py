import json
import sys
import binascii
import msgpack
import quopri

with open(sys.argv[1], 'rb') as myfile:
    input_string=myfile.read()


input_object = msgpack.unpackb(input_string, encoding='utf-8')
pi_string = ""

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

print(final_output_string)
