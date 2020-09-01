string = input("Enter the Sequence")
kmer = int(input("Enter the k-mer length"))

i=0
count = 0
for i in range(0,len(string)):



    if len(string[i:kmer+i])== kmer:
        print(string[i:kmer+i],end=" ")
        count = i +1
    else :
        pass

print ("\nTotal kmers possible ",count)
