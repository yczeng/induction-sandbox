import ast

'''
PROBABLY SCRAP THIS LATER. REPRESENTING IT AS A STRING LIST OF LIST MAKES NO SENSE BECAUSE:
1) benefits of representation in a tree structure can't be taken advantaged of
2) also looking at data, removing i.e. np and vp is removing too much information. I can't distinguish between very different sentences anymore. Obvious examples are questions. Now I can't distinguish them based on their grammar alone.
'''


def findGivenLen(length):
    with open('../evaluation/Bernstein-Ratner87-parsed') as f:
        content = f.readlines()
            
        utterances = [x.strip().lower() for x in content]
        
        with open('../evaluation/Bernstein-Ratner87' + '-' + str(length), 'w') as w:

            for utterance in utterances:
                if utterance != "ERROR: FIX IT LATER":
                    print(utterance)

                    stringInput = makeStrings(str(utterance))
                    print(stringInput)
                    array = ast.literal_eval(stringInput)
                    print(array)
                    exit()
                    if len(array) == length:
                        w.write(utterance)

def makeStrings(utterance):
    newString = ""

    for count, letter in enumerate(utterance):
        if count == 0:
            newString += letter
        else:
            if (utterance[count] == "'" or utterance[count].isalpha()) and utterance[count-1] == "[":
                newString += '"' + utterance[count]
            elif utterance[count] == "]" and utterance[count - 1].isalpha():
                newString +=  '"' + utterance[count]
            else:
                newString += utterance[count]
    return newString

print(makeStrings('[[is][[[that]][[for][[the][doggie]]]]]'))
# findGivenLen(3)