
import random

# generate random DNA sequence
def randomDNA(length):
    bases = ['A', 'T', 'C', 'G']
    sequence = ""
    for i in range(length):
        sequence = sequence + bases[random.randint(0,3)];
    return sequence

# return two random sequences, the shorter sequence first
def getSequences():
    length1 = int(input('Enter length of sequence 1: '))
    length2 = int(input('Enter length of sequence 2: '))
    
    if length1 < length2:
        sequence1 = randomDNA(length1)
        sequence2 = randomDNA(length2)
    else:
        sequence1 = randomDNA(length2)
        sequence2 = randomDNA(length1)
    return sequence1, sequence2

# print a list of elements, each element in a separte line
def printList(inputList):
    for i in range(len(inputList)):
        print(inputList[i])

def insertionSort(inputList):
    for marker in range(1, len(inputList)):
        currentValue = inputList[marker]
        previousIndex = marker - 1
        #slide back the list until find the smallest
        while previousIndex >=0:
            if currentValue < inputList[previousIndex]:
                # swap
                temp = inputList[previousIndex]
                inputList[previousIndex] = inputList[previousIndex + 1]
                inputList[previousIndex + 1] = temp
                previousIndex = previousIndex - 1
            else:
                break
    return list(inputList)

#remove all elments that are duplicates
# the output will be a list of all distinct elements
def removeDuplicates(inputList):
    return insertionSort(list(set(inputList)))


# insert a gap at position "pos" in a given sequence
def insertGap(sequence, pos):
    if pos > len(sequence)+1 or pos < 0:
        return 'Error: Invalid position'
    return sequence[0:pos]+'-'+sequence[pos:len(sequence)]

# generate all possible variation of a given sequence
# after inserting one gap
# example: generateOneGapAlignment('AB') -->
# ['-AB', 'A-B', 'AB-']
def generateOneGapAlignments(sequence):

    if (sequence ==""):
        print('Error: Invalid input')
    else:
        
        oneGapSequence=[]
        for i in range (len(sequence)+1):
            oneGapSequence =[insertGap(sequence,i)]+oneGapSequence

        return(oneGapSequence)
            
def align(seq1, seq2):
    if (seq1==""):
        print('Error: Invalid input: seq1 is empty')
    elif (seq2==""):
        print('Error: Invalid input:seq2 is empty')
    elif (seq2 < seq1):
        print('Error: Invalid input:seq2 is shorter then seq1')
    
    else :
        gaps=''
        alignTimes = len(seq2)-len(seq1)
        for i in range (alignTimes):
            gaps=gaps+'-'
        align = gaps+seq1
        return (align)

            
# score an alignment of two sequences
# 1-If there is a gap and a character, score = -1
# 2-If the two characters are different, score = 0
# 3-If the two characters are equal to ‘A’ or ‘G’, score = 1
# 4-If the two characters are equal to ‘C’ or ‘T’, score = 2
def score(seq1, seq2):
    if (len(seq1)!= len(seq2)):
        print ("Error: the two sequences are not aligned")
    else:
        score=0

        for index in range (len(seq1)):
            if (seq1[index]=="A"or 'G' or seq2[index]=="A"or 'G'):
                sum=1
            if (seq1[index]=="C"or 'T' or seq2[index]=="C"or 'T'):
                sum=2
            if (seq1[index]==seq2[index]):
                score = score+sum
            if (seq1[index]=='-' and seq2[index]=='-'):
                score=score-1
            if (seq1[index]=='-' or seq2[index]=='-'):
                score=score-1
        return (score)
    


# generate all possible insertions of two gaps into that sequence
def generateTwoGapAlignments(sequence):
    twoGapSequence=[]
    
    oneGapSequence=generateOneGapAlignments(sequence)
  
    for i in range (len(sequence)+1):
        
        for x in range ((len(sequence)+1)):
            twoGapSequence=[insertGap(oneGapSequence[i-x],i)]+twoGapSequence
            
            
    twoGapSequence=removeDuplicates(twoGapSequence)
        
    return(twoGapSequence)
 

# given a sequence and two alignments - check which alignments give a better score
def compareAlignments(alignment1, alignment2, sequence):
    if (alignment1=='' or alignment2 =='' or sequence==''):
        return('Error:aligment-sequence length mismatch')
    com1=score(alignment1,sequence)
    com2=score(alignment2, sequence)
    if (alignment1=='' or alignment2 =='' or sequence==''):
        print('Error:aligment-sequence length mismatch')
    elif (com1>com2):
        print ("Alignment ",alignment1, " has better alignment score " ,com1)
    elif (com2>com1):
        print ("Alignment ",alignment2," has better alignment score " , com2)
    elif (com1==com2):
        print ("Alignment ", alignment1, " and" ,alignment2,'have the same score',com1)


    
