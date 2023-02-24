import random
import sys
import urllib.request
import cowsay

def bullscows(guess: str, secret: str) -> (int, int):
    bulls = 0
    for i in range(len(guess)):
        bulls += (guess[i] == secret[i])
    cows = 0
    g_set = set(guess)
    s_set = set(secret)
    for w in g_set:
        cows += (w in s_set)
    return (bulls, cows)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = words[random.randint(0, len(words) - 1)]
    b, c = 0, 0
    num = 0
    while b < len(word):
        users_word = ask("Введите слово: ", words)
        num += 1
        b, c = bullscows(users_word, word)
        inform("Быки: {}, Коровы: {}", b, c)
    return num


def ask(prompt: str, valid: list[str] = None) -> str:
    creeper = cowsay.read_dot_cow(open('creeper.cow', 'r'))
    print(cowsay.cowsay(prompt, cowfile=creeper))
    wrd = input()
    if valid:
        while wrd not in valid:
            wrd = input(prompt)
    return wrd
    
    
def inform(format_string: str, bulls: int, cows: int) -> None:
    rand_cow = cowsay.list_cows()[random.randint(0, len(cowsay.list_cows()) - 1)]
    print(cowsay.cowsay(format_string.format(bulls, cows), cow=rand_cow))
    
    
if len(sys.argv) == 3:
    voc, ln = sys.argv[1], int(sys.argv[2])
else:
    voc, ln = sys.argv[1], 5
try:
    words = open(voc, 'r').read().split()
except:
    response = urllib.request.urlopen(voc)
    words = response.read().decode().split()
words = [word for word in words if len(word) == ln]
print(gameplay(ask, inform, words))
