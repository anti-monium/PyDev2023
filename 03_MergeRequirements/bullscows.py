import random

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
