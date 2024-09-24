def match_words(words):
    
    counter = 0
    lst = []
    
    for word in words:
        
        if len(word) > 1 and word[0] == word[-1]:
            counter = counter + 1
            lst.append(word)
            
    print("List of words with first and last characters same\n", lst)
    return counter
    
    
list1 = ['ábc', 'cfc', 'xyz', 'aba', '1221']
count = match_words(list1)
print("Number of words having first and last characters same:", count)