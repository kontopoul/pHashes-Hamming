from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--source", dest='source', help="source file that contains the hexademical pHash string(s) to be converted")
parser.add_option("-d", "--destination", dest='destination', default='int_pHashes.txt',help="file to store the converted int pHashes")

(options, args) = parser.parse_args()

hex_DIR = options.source
int_pHashes = options.destination

print("Converting hex strings to integers: " + hex_DIR + ' -> ' + int_pHashes)

#Strips \n from each line of the source file,then converts the remaining hexademical string representation to an integer for later use (XOR). 
with open(hex_DIR, "r") as infile, \
    open(int_pHashes,"w") as outfile:
    for line in infile:
        b = int(line.rstrip('\n'),16)
        outfile.write(str(b)+'\n')