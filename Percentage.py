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
    percent_U=float(float(U*100)/float(len(args.seq)))
    percent_A=float(float(A*100)/float(len(args.seq)))
    percent_C=float(float(C*100)/float(len(args.seq)))
    percent_T=float(float(T*100)/float(len(args.seq)))
    percent_G=float(float(G*100)/float(len(args.seq)))
    print ("% of U in sequence is:", (u / len(args.seq)) * 100)#Calulate and Print the U Percentage
    print ("% of A in sequence is:", (a / len(args.seq)) * 100)#Calculate and Print the A Percentage
    print ("% of C in sequence is:", (c / len(args.seq)) * 100)#Calculate and Print the C Percentage
    print ("% of T in sequence:", percent_T, "%")#Print the T Percentage
    print ("% of G in sequence:", percent_G, "%")#Print the G Percentage
else:
    print ('The sequence is not DNA or RNA')
    
    
