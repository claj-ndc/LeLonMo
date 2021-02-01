import unicodedata
from os import path

from .persist_data import DATA as settings


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


word_list = None
program_path = path.abspath(path.join(path.dirname(__file__),"."))

def check_dict(word, language="fr"):
    global word_list
    if word_list is None:
        word_list = open(
            f"{program_path}{path.sep}dict{path.sep}dict_{language}.txt", "r", encoding="UTF-8").readlines()
    if settings["debug"]["ACCEPT_ANY_WORD"]:
        return True
    word = word.lower()
    for w in word_list:
        if remove_accents(word) == remove_accents(w).replace("\n", ""):
            return True
    return False


def check_list(word, letters):
    if settings["debug"]["ACCEPT_ANY_LETTER"]:
        return True
    for l in remove_accents(word):
        if not l.lower() in letters:
            return False
    return True
