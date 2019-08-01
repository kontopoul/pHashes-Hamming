
import time
from optparse import OptionParser


#Line 16: XOR between the integers from the source file and the dataset,returns an int (xor_int).
#Line 17: Convert xor_int to it's equivalent binary string,then count the '1's to calculate the hamming distance. 
#Line 19: If distance < x then writes to a file the dataset's hex fingerprint in order to identify if it relates somehow to the source.
def xor(source,dataset,max_dist):
    memes_list = []
    with open(source,"r") as source, open(dataset,"r") as dataset, \
        open("distances.txt","w") as distances :
        for line1 in source:
            dataset.seek(0)
            for line2 in dataset:
                xor_int = int(line1) ^ int(line2)
                z = str(bin(xor_int)).count('1')
                distances.write(str(z)+'\n')
                if z <= max_dist : 
                    hex_string = '0x{:02x}'.format(int(line2))
                    memes_list.insert(0,hex_string[2:].zfill(16))
    return memes_list
                


parser = OptionParser()
parser.add_option("-s", "--source", dest='source', help="source file that contains the int string(s) to be compared")
parser.add_option("-t", "--table", dest='table', default='int_kym_phashes.txt',help="Int dataset that source is going to be compared with")
parser.add_option("-d", "--distance", dest='distance', default='8', help="Maximum distance")

(options, args) = parser.parse_args()

source = options.source
dataset = options.table
max_dist = int(options.distance)

print("Calculating overall distances")
start = time.time()
memes_list = xor(source,dataset,max_dist)
end = time.time()
print("Distance execution time: "+ str(end-start))
with open('identified.txt', 'w') as output:
    for item in memes_list:
        output.write("%s\n" % item)
