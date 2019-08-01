import distance
with open("task1.txt","r") as source, open("clean_kym_phases.txt","r") as table, \
    open("checkin.txt","w") as outfile:
    for line1 in source:
        table.seek(0)
        for line2 in table: 
            outfile.write(str(distance.hamming(line1.rstrip('\n'),line2.rstrip('\n')))+'\n')
            if(distance.hamming(line1.rstrip('\n'),line2.rstrip('\n'))<=5):
                print(line1 + '\t' +line2)
            #     with open("kym_phashes_classes.txt","r") as search_term:
            #         for meme2be in search_term:
            #             a = len(meme2be.rstrip('\n')) - 16
            #             if(meme2be[a:])==line1:
            #                 print(meme2be)