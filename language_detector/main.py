# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    word_list = text.split()

    language_lists = []
    
    for lang in languages:
        lang_name = lang['name']
        lang_set = set(lang['common_words'])
        lang_word_list = list(filter(lambda x: x in lang_set, word_list))
        language_lists.append((len(lang_word_list), lang_name))
    
    language_lists.sort(reverse=True)
    return language_lists[0][1]

