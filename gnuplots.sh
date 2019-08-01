python calculate_phashes.py --directory test_images
python hex2int.py -s phashes.txt -d int_pHashes.txt
python dist.py -s int_pHashes.txt -t int_kym_phashes.txt -d 15
perl -pi -e 'chomp if eof' distances.txt
python graph_script.py
gnuplot -e "set style data histograms;set style fill solid;plot 'graph.data' using 2:xtic(1) title 'Values by Color';pause -5"