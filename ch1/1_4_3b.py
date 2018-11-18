word_list = ['cat','dog','rabbit']

def add_and_return(a_char, a_set):
    a_set.add(a_char)
    return a_char

seen = set()

print('Check:', [a_letter for a_word in word_list for a_letter in a_word])

print('Extra challenge:', [ add_and_return(a_letter, seen) for a_word in word_list for a_letter in a_word if a_letter not in seen ])
