# Pipress
Compression of text files in terms of Pi.

This is quite possibly the worst file storage algorithm ever made.
Requires MessagePack and Python3.

## Powerful features:
- ?

## Limitations:  
- Can only "compress" ASCII or UTF-8 encoded text files.
- Usually makes files 2 to 3 times larger.
- You need the 1 GB file [pi-billion.txt](https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt) in order for this to work.

# Example

Given the following input file:  
`CHECK`

the following output will be produced:
`[[13731565, 7], [35842, 5]]`

This tells the decompressor to look at the 13,731,565th digit of Pi and take 7 characters. Then, that 7 character integer will be converted to a 24 bit binary string, which is split into three 8 bit ints which are converted to ASCII using the `chr()` function.

This process is repeated for the second element. Regardless of number length, the Pi excerpt is always converted to a 24 bit int, and a byte of `00000000` is silently ignored.

This output is then packed to binary using MessagePack. The textual representation of this in hex is the following:  
`9292ce00d186ed0792cd8c0205`


Through the use of the Pipress algorithm we turned a 5 byte file to a 13 byte file. Incredible!
