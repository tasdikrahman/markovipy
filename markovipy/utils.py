#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs


def fix_caps(word):
    """Used to compare words, irrespective of their capitalisation

    :param word: the word to be fixed
    :type word: <str>
    :return: <str>
    """
    if word.isupper() and word != "I":
        """eg: word -> 'AAA', result -> 'aaa'
        """
        word = word.lower()
    elif word[0].isupper():
        """eg: word -> 'AvA', result -> 'Ava'
        """
        word = word.lower().capitalize()
    else:
        """eg: word -> 'aVA', result -> 'ava'
        """
        word = word.lower()
    return word


def get_word_list(file):
    """Used to get the words inside the corpus file and generate a list of
    words by parsing it

    Something like = ["once", "upon", "a", ...]

    Check the regex on https://regex101.com/ with any file inside the
    corpus/ dir

    \w matches any word character (equal to [a-zA-Z0-9_])
    ' matches the character ' literally (case sensitive)
    .,!?; matches a single character in the list .,!?; (case sensitive)

    :param file: the file being passed to create the list of words
    :type file: <str>
    :return: <list>
    """
    try:
        # fixes UnicodeDecodeError while reading files instead of using the
        # normal open()
        with codecs.open(file, 'r', encoding='utf-8') as f:
            words_list = \
                [fix_caps(w) for w in re.findall(r"[\w']+|[.,!?;]", f.read())]
        return words_list
    except OSError:
        return "Did you pass a valid file name/path?"


def list_to_tuple(list_obj):
    """As lists are not hashable, converting the list explicitly to a tuple

    :param list_obj: <list> object to be hashed
    :type list_obj: <list>
    :return: <tuple>
    """
    return tuple(list_obj)
