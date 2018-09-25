# Sequences
Generate Sequences

generate all possible variation of a given sequence after inserting one gap 
example: generateOneGapAlignment('AB') -->['-AB', 'A-B', 'AB-']

Also score an alignment of two sequences
1-If there is a gap and a character, score = -1
2-If the two characters are different, score = 0
3-If the two characters are equal to ‘A’ or ‘G’, score = 1
4-If the two characters are equal to ‘C’ or ‘T’, score = 2
