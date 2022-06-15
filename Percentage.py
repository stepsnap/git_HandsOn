import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Calculate the percentage of each nucleotide in the sequence')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

args = parser.parse_args()
seq = seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    u= seq.count("U") #this counts the U Percentage
    a= seq.count("A") #this counts the A Percentage
    c= seq.count("C") #this counts the C Percentage
    t= seq.count("T") #this counts the T Percentage
    g= seq.count("G") #this counts the G Percentage

    u_content= (u/len(seq)) * 100 #Calculate the U percentage 
    a_content= (a/len(seq)) * 100 #Calculate the A percentage
    c_content= (c/len(seq)) * 100 #Calculate the C percentage
    t_content= (t/len(seq)) * 100 #Calculate the T percentage
    g_content= (g/len(seq)) * 100 #Calculate the G percentage
    
    print (f"The % of U in sequence is: {u_content}") #Print the U Percentage
    print (f"The % of A in sequence is: {a_content}") #Print the A Percentage
    print (f"The % of C in sequence is: {c_content}") #Print the C Percentage
    print (f"The % of T in sequence is: {t_content}") #Print the T Percentage
    print (f"The % of G in sequence is: {g_content}") #Print the G Percentage

else:
    print ('The sequence is not DNA or RNA')
    
