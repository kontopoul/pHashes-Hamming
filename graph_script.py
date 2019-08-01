from collections import Counter

#Script to output a graph.data file with the proper format to use later in GNUPlot.Also prints a (dist:counts) dictionary just for a clearer
#visual representation
with open("distances.txt","r") as infile:
    a = ''
    for line in infile:
        a+=line.replace("\n",",")
text = a.split(',')
letter_counts = dict(Counter(text))
letter_counts = {int(k):int(v) for k,v in letter_counts.items()}
print(letter_counts)
with open("graph.data","w") as outfile:
    outfile.write("#Distance    Count\n")
    for k in letter_counts:
        outfile.write(str(k) + '\t' + str(letter_counts[k]) + '\n')