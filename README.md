# Pipress
Compression of files in terms of Pi.

This is quite possibly the worst file storage algorithm ever made.
Requires MessagePack and Python3.

### Powerful features:
- Nothing.

### Limitations:  
- Unbelievably slow. It took about 3 minutes to compress a 50kb image.
- Usually makes files 3 to 5 times larger.
- You need the 1 GB file [pi-billion.txt](https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt) in order for this to work.

## Usage
First, download [pi-billion.txt](https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt) and put it in the same folder as pipress.py. Then, `cd` into your pipress directory and run:  
`python3 pipress.py yourinputfile.txt`

This outputs `yourinputfile.txt.pipress`

To decompress simply run the following:  
`python3 decompress.py yourinputfile.txt.pipress`

This will recreate the original file.
This works with any binary file. Images, zip archives, you name it!
Enjoy the future of compression.
