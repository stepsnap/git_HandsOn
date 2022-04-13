
import sys, re
from argparse import ArgumentParser #import the library

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA') #create one ArgumentParser
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") #add the first argument
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") #add the second argument

if len(sys.argv) == 1: #print the help message only if no arguments are supplied on the command line
    parser.print_help()
    sys.exit(1) 

args = parser.parse_args() #parser the argument

args.seq = args.seq.upper() #convert the sequence  in upper case 

if 'U' in args.seq and 'T' in args.seq: #if it finds U and T in the sequence return a message that the sequence have a mutagenic bases 
	print ('The sequence have a mutagenic bases') # if it finds this condition it does not execute the others command line
	sys.exit () 

if re.search('^[ACGTU]+$', args.seq): #search in the sequence the pattern within the string
    if re.search('T', args.seq): #if it finds T in the sequence return a message that the sequence is DNA 
        print ('The sequence is DNA') 
    elif re.search('U', args.seq): 
        print ('The sequence is RNA') #if it finds U in the sequence return a message that the sequence is RNA
    else:
        print ('The sequence can be DNA or RNA') #if it finds T and  U in the sequence return a message that the sequence can be DNA or RNA 
else:
    print ('The sequence is not DNA') #else the sequence is not DNA

if args.motif:
    args.motif = args.motif.upper() #converte the motif in upper case
    print(f'Motif search enabled: looking for motif in sequence') #to find simple motifs in the sequence, besides printing the type of molecule (DNA or RNA)
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")

