with open("identified.txt", "r") as infile, open("kym_phashes_classes.txt") as dataset ,\
    open("memes_found.txt","w") as outfile:
        for line1 in infile:
            dataset.seek(0)
            for line2 in dataset:         
                a = len(line2.rstrip('\n')) - 16
                hexa = (line2[a:].rstrip('\n'))
                if(line1.rstrip('\n') == hexa):
                    print(line2.rstrip('\n'))
