word_list = ['cat','dog','rabbit']
letter_list = []
letter_set = set()
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_set:
            letter_set.add(a_letter)
            letter_list.append(a_letter)
print(letter_list)
