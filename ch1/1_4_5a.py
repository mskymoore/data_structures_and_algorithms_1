import random, string, time, os

target = "methinks it is like a weasel"
bank = string.ascii_lowercase + " "

print(f'target: {target}\nchoices: "{bank}"')


# generates 27 character string
def str_gen():
    count = 0
    a_str = ''
    while count < 28:
        a_str += random.choice(bank)
        count += 1
    return a_str


# scores a_str by closeness to a_goal
def score_str(a_str, a_goal):
    if a_str == a_goal:
        return 100
    else:
        score = 0
        for i, a_chr in enumerate(a_str, start=0):
            if a_chr == a_goal[i]:
                score += 1
        return (score / 28)*100


# repeatedly calls str_gen and score_str until
# generated string matches target
def monkey_and_score(goal):
    count = 0
    best_str = ''
    best_score = 0
    start = time.time()
    while True:
        try:
            count += 1
            a_str = str_gen()
            a_score = score_str(a_str, goal)
            if a_score > best_score:
                if a_score == 100:
                    print(f'matched: {a_str}\niterations: {count}')
                    break
                best_score = a_score
                best_str = a_str
            if count % 1000 == 0:
                elapsed = time.time() - start
                os.system('clear')
                print(f'best string: {best_str}\nscore: {best_score:3.2f}%\niterations: {count}\nelapsed time: {elapsed:.3f}')
        except KeyboardInterrupt:
            print('Keyboard Interrupt')
            break


monkey_and_score(target)
