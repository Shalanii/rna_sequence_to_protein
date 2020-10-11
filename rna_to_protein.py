def main():
    sequence = input("Enter RNA Sequence : ")
    count = 0
    sequence = clean_sequence(sequence)
    if(len(sequence)<3):
        print("ERROR : Sequence length is not sufficient to proceed.")
    else:
        sequences = find_sequences(sequence)
        print(sequences)
        for seq in sequences:
            codons = split_to_codons(seq)
            protein = ""
            for codon in codons:
                protein = protein+" "+find_protein(codon)
            print("Reading Frame "+str(count)+" : "+protein)
            count+=1

def clean_sequence(sequence):
    sequence = sequence.upper()
    cleaned_sequence = ""
    flag = 0
    for char in sequence:
        if (not(char=="A" or char=="U" or char=="C" or char=="G")):
            print("Invalid character detected -> "+char)
            flag = 1
        else:
            cleaned_sequence = cleaned_sequence+char
    if flag==1:
        print("Sequence is modified. Modified sequence is "+cleaned_sequence)
    return cleaned_sequence
            
def find_sequences(sequence):
    sequences = []
    sequence_length = len(sequence)
    if sequence_length%3 == 0 :
        sequences.extend([sequence,sequence[1:]+sequence[0],sequence[2:]+sequence[:2]])
    elif sequence_length%3 == 1 :
        sequences.extend([sequence[:sequence_length-1],sequence[1:],sequence[2:]+sequence[0]])
    else:
        sequences.extend([sequence[:sequence_length-2],sequence[1:sequence_length-1],sequence[2:]])
    return sequences


def split_to_codons(sequence):
    length = len(sequence)
    codons = []
    for i in range(0,length,3):
        codons.append(sequence[i:i+3])
    return codons

def find_protein(codon):
    output = "ERR"
    thisdict = {"Gly": ["GGG","GGA","GGC","GGU"],"Glu": ["GAG","GAA"],
                "Asp": ["GAU","GAC"],"Ala":["GCG","GCA","GCC","GCU"],
                "Val":["GUG","GUA","GUC","GUU"],"Met":["AUG"],
                "Arg":["AGG","AGA","CGG","CGA","CGC","CGU"],
                "Ser":["AGC","AGU","UCU","UCC","UCA","UCG"],
                "Lys":["AAG","AAA"],"Asn":["AAC","AAU"],
                "Thr":["ACG","ACA","ACC","ACU"],"Gln":["CAG","CAA"],
                "Ile":["AUA","AUC","AUU"],"His":["CAC","CAU"],
                "Pro":["CCU","CCC","CCA","CCG"],"Cys":["UGU","UGC"],
                "Leu":["CUU","CUC","CUA","CUG","UUG","UUA"],
                "Tyr":["UAU","UAC"],"Phe":["UUC","UUU"],
                "Trp":["UGG"],"STP":["UGA","UAA","UAG"]}
    for key,value in thisdict.items():
        if codon in value:
            output = key
            break
    return output
        
        

if __name__ == "__main__":
    main()
