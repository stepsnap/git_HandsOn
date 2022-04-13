import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Calculate the percentage of each nucleotide in the sequence')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    u= args.seq.count("U") #this counts the U Percentage
    a= args.seq.count("A") #this counts the A Percentage
    c= args.seq.count("C") #this counts the C Percentage
    t= args.seq.count("T") #this counts the T Percentage
    g= args.seq.count("G") #this counts the G Percentage

    print ("% of U in sequence is:", (u / len(args.seq)) * 100)#Calulate and Print the U Percentage
    print ("% of A in sequence is:", (a / len(args.seq)) * 100)#Calculate and Print the A Percentage
    print ("% of C in sequence is:", (c / len(args.seq)) * 100)#Calculate and Print the C Percentage
    print ("% of T in sequence is:", (t / len(args.seq)) * 100)#Calculate and Print the T Percentage
    print ("% of G in sequence is:", (g / len(args.seq)) * 100)#Calculate and Print the G Percentage

else:
    print ('The sequence is not DNA or RNA')
    
