import copy
import random
from turtle import pos, up
from warnings import catch_warnings

# pos_vals = {}
# letters = []
# normal_words = {}
# translated_words = {}
# global_dict = {}

# ALPHABET DEFINED:
pos_vals = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
letters = ["v", "i", "s", "m", "a", "p", "h", "e", "n", "l"]

# WORDS BEFORE BEING TRANSLATED TO NUMBERS:
normal_words = {"visma": ["v", "i", "s", "m", "a"], "saas": ["s", "a", "a", "s"], "api": ["a", "p", "i"], "ai": [
    "a", "i"],  "heaven": ["h", "e", "a", "v", "e", "n"]}

# TRANSLATED WORDS:
translated_words = {"visma": [], "saas": [],
                    "api": [], "ai": [],  "heaven": []}

# GLOBAL DICT FOR FINAL SOLUTION:
global_dict = {}


# updates the global dictionary with a new locked value, and removes these values
# from possible values.

def retry(letters, pos_vals):
    letters = []
    letters += ["v", "i", "s", "m", "a", "p", "h", "e", "n", "l"]
    normal_words = {"visma": ["v", "i", "s", "m", "a"], "saas": ["s", "a", "a", "s"], "api": ["a", "p", "i"], "ai": [
        "a", "i"],  "heaven": ["h", "e", "a", "v", "e", "n"]}
    print(f"letters: {letters}")
    for x in range(0, 10):
        if x not in pos_vals:
            pos_vals.add(x)
    print(f"vals: {pos_vals}")
    global_dict.clear()


def update_dict(key, value):
    global_dict[key] = value
    pos_vals.discard(value)
    if letters.__contains__(key):
        letters.remove(key)
    # TODO FINNES IKKE I LISTE????

# chooses letters from possible values


def choose_letter(vals):
    try:
        val = random.sample(vals, 1)[0]
        # print(val)
        vals.remove(val)
        return val
    except:
        print("value error")


def check_restraint(i, val):
    # TODO: fix bug here
    if i == "a" and val == 1 or i == "m" and val == 2:
        new_val = choose_letter(pos_vals)
        pos_vals.add(val)
        return new_val
    else:
        return val


def map_letters(letters, pos_vals):
    #print("map letters:")
    dict = {}  # empty dictioary
    vals_copy = copy.deepcopy(pos_vals)
    letters_copy = copy.deepcopy(letters)
    for i in letters_copy:
        # TODO FIKSE DETTE AT DE ikke fjerner permanent fra mapen
        dict[i] = choose_letter(vals_copy)
        #dict[i] = check_restraint(i, choose_letter(vals_copy))
    # print(dict)
    return dict


def translate(try_dict):
    print(len(global_dict))
    if len(global_dict) != 0:
        try_dict.update(global_dict)
    for word in normal_words:
        # print(word)
        word_val = []
        for letter in word:
            # print(letter)
            val = try_dict.get(letter)
            word_val.append(val)
        translated_words[word] = word_val
    return translated_words


def compute(translated_words):
    sumword = [0, 0, 0, 0, 0, 0]
    i = 5
    carry = False
    comp_copy = copy.deepcopy(translated_words)
    while i > 0:
        if carry:
            val = 1
            carry = False
        else:
            val = 0
        for word in comp_copy:
            #print(f"word: {word}")
            if len(comp_copy[word]) == 0:
                #print("breaking here")
                break
            # print(comp_copy[word])
            number = comp_copy[word].pop()
            # print(number)
            val += number
        if val > 9:
            val = val - 10
            carry = True
        sumword[i] = val
        i -= 1
    return sumword


def lock(i):
    #print(f" value to be locked = {i}")
    for word in normal_words:
        if word in {"heaven"}:
            continue
        #print(f"normal w: {normal_words}")
        if len(word) >= i:
            # print(word)
            # print(word[i])  # key
            # print(f"translated w: {translated_words}")

            lock = translated_words.get(word)
            #print(f"word getting locked:  {lock}")
            # print(f"letter getting locked: {lock[i]}")  # val
        update_dict(word[i], lock[i])


def comp_last_vals(i, s, m, a, p):
    n = a + 2*i + s
    e = 0
    v = 0
    if n > 10:
        n = n-10
        e += 1
    e += m + p + 2*a
    if e > 10:
        v += 1
    v += s + 2*a
    if (i+s != a):
        return False
    else:
        update_dict('n', n)
        update_dict('e', e)
        update_dict('v', v)
        return True


def do():
    doing = True
    while doing:
        solved = False
        tries = 0
        while not solved:
            translate(map_letters(letters, pos_vals))
            # print(translated_words)

            correct = translated_words.popitem()[1]
            print(translated_words)
            computed = compute(translated_words)

            #print("translated words should be same:")
            # print(translated_words)

            print("------------------------")
            print(f"correct solution for 'heaven': {correct}")
            print(f"computed solution for 'heaven': {computed}")

            locked_var = 0
            for i in range(5, 0, locked_var-1):
                if correct[i] != computed[i]:
                    solved = False
                    break
                else:
                    lock(i-6)
                    locked_var += 1
            if len(global_dict) >= 4:
                print("found sufficient letters. ")
                print(global_dict)
                if not comp_last_vals(global_dict.get('i'), global_dict.get(
                        's'), global_dict.get('m'), global_dict.get('a'), global_dict.get('p')):
                    print("not right sol.")
                    #retry(letters, pos_vals)
                    #solved = False
                    print(global_dict)
                else:
                    solved = True

            print(f"Current global dict: {global_dict}")
            print(f"vals: {pos_vals}")
            tries += 1

            print(f"tries: {tries}")
            if not solved:
                print("------------------------")
                print("----trying again ...----")
            else:
                doing = False


do()
