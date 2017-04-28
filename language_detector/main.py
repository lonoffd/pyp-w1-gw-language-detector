# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    word_list = text.split()
    word_set = set(word_list)
    word_counts = {word: word_list.count(word) for word in word_set}

    spanish_set = set(languages[0]['common_words'])
    german_set = set(languages[1]['common_words'])
    english_set = set(languages[2]['common_words'])
    is_spanish = list(filter(lambda x: x in spanish_set, word_list))
    is_german = list(filter(lambda x: x in german_set, word_list))
    is_english = list(filter(lambda x: x in english_set, word_list))
    language_lists = [(len(is_spanish), "Spanish"), (len(is_english), "English"), (len(is_german), "German")]
    language_lists.sort(reverse=True)
    return language_lists[0][1]

