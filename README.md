# pHash Processing Pipeline


## Prerequisites

The pipeline relies on the following packages:
```
Imagehash library == 3.5 (https://github.com/JohannesBuchner/imagehash)
Gnuplot 5.2
Perl v5.28.1

```
For the Imagehash we ***strongly recommend*** using the library's 3.5 version. This is because they changed the pHash generation in versions greater than 3.5, hence the generated phashes will be incompatible with pHashes generated with the versions > 3.5.Have in mind that the KYM
dataset contains 700k hashes generated by the 3.5 version.

## Running the pipeline

Brief explanation of how to run the pipeline,followed by a description of each script.Note that you can use :
```
./gnuplots.sh
```
It's a script that does the job for you,without manually typing the following commands.

### Calculating pHashes
```
python calculate_phashes.py --directory test_images
```
This script iterates over all images in the `test_images` directory and calculates their pHashes using the Imagehash library. At the end, you should see a new file called `phashes.txt`, which contains the images path and the generated pHash. Note that you can change the output file using the option `--output`.

### Converting the generated hex pHashes to integers for later XOR
```
python hex2int.py -s phashes.txt -d int_pHashes.txt
```
This script iterates through the `phashes.txt` file and converts each hexademical string represantation to an integer.The output can be found in the `int_pHashes.txt` file. Note that you can change the input/output file using the option `-s` and `-d` .

### Getting the Hamming distance through bitwise XOR & getting a list of the Dataset's memes that have a distance less than "X".
```
python dist.py -s int_pHashes.txt -t int_kym_phashes.txt -d 15
```
This script compares each pHash found in `int_pHashes.txt` with the KYM int pHash dataset `int_kym_phashes.txt`. It XORs between the integers from the source file and the dataset,returning an int (xor_int).Then it converts xor_int to it's equivalent binary string,counting the '1's to calculate the Hamming distance. Through the `-d` option you can input the max distance to list any potential meme identified. The output distances can be found in `distances.txt` and the memes identified can be found in `identified.txt`.Note that the default max distance is 8.

### Strip a trailing newline from distances.txt EOF
```
perl -pi -e 'chomp if eof' distances.txt
```
Self-explanatory shell command.

### Format the distances.txt to a proper one for GNUplot to use
```
python graph_script.py
```
This script formats the distances.txt to a histogram-like one for GNUplot to use.The output can be found in `graph.data`.

### If GNUplot's installed then : 
```
gnuplot -e "set style data histograms;set style fill solid;plot 'graph.data' using 2:xtic(1) title 'Values by Color';pause -5"
```
This shell command will just plot a histogram of the graph.data.

## Dataset
The KYM dataset contains all the image URLs and pHashes for all the images that Cypriot's got from the site.The `kym_phashes_classes.txt` contains the original format of "link metadata pHash" .In `int_kym_phashes.txt` you can find the int representation of the hexademical KYM phashes.In `hex_kym_phases.txt` you can find the hex format stripped from the original dataset.