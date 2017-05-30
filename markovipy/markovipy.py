#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import collections

from markovipy.utils import get_word_list
from markovipy.constants import PUNCTUATIONS


class MarkoviPy:
    def __init__(self, filename="", markov_length=2):
        """
        starting_word: keeps track of the words from which sentences would be
        starting out.

        TODO:
        - instead of storing final_mapping and middle_mapping on memory, put
          them on a tiny DB(Sqlite comes to my mind)

        :type markov_length: <int> defaults to 2
        :type filename: <str> defaults to an empty string
        """
        self.starting_words = []
        self.middle_mapping = collections.defaultdict(collections.Counter)
        self.final_mapping = {}
        self.markov_length = markov_length
        if os.path.exists(filename):
            self.filename = filename
        else:
            raise FileNotFoundError(
                "Please enter a valid file name for corpus")
        self.words_list = get_word_list(self.filename)

    def _normalise_mapping(self):
        """
        creates the self.final_mapping with the final probabilities in
        similar structure
         {
         ...
         ('with',): {'Till': 0.2,
                     'a': 0.2,
                     'darkness': 0.2,
                     'such': 0.2,
                     'whispering': 0.2},
         ('word',): {',': 0.6666666666666666, 'within': 0.3333333333333333},
         ('word', ','): {'Swaddled': 0.5, 'unable': 0.5},
         ...
         }
        :return:
        """
        for word_tuple, probable_word in self.middle_mapping.items():
            total = sum(probable_word.values())
            self.final_mapping[word_tuple] = \
                dict([(k, v / total) for k, v in probable_word.items()])

    def _build_middle_mapping(self, word_history, next_word):
        """Adds next_word to the list of possible next words after the
        sequence presented in word_history.

        maps the occurrence of the words after one another in a <dict> called
        'middle_mapping'. This would just be a <dict> which would contain a
        - <tuple> as the key, inside the <tuple> you would be having the
        sequence of the words one after the another
        - and the value would be <dict>

        eg: word_history = ["it", "rained", "on"] and next_word = "a", then
            it will create a mapping where for the sequences
            ["it", "rained", "on"], ["it", "rained"], ["rained", "on"] and
            ["on"]. The next word for them would be "a"

        Something like this
        self.middle_mapping -> {('Once', 'upon'): {'a': 1.0},
                                ('upon',): {'a': 1.0}}

        Finally,method builds something like this inside self.middle_mapping
        {
            ...
            ('youth',): {',': 1.0,
                         '.': 5.0,
                         'about': 1.0,
                         'and': 4.0,
                         'is': 1.0,
                         'saint': 1.0,
                         'stirred': 1.0,
                         'was': 1.0},
            ('youth', ','): {'a': 1.0},
            ...
        }

        :param word_history: <list> of contiguous words
        :param next_word: next word in the sequence of the <list> word_history
        :return:
        """
        while len(word_history) > 0:
            key = tuple(word_history)
            self.middle_mapping[key][next_word] += 1.0
            word_history = word_history[1:]

    def _iterate_through_word_list(self):
        """Picks out pair of words with accordance to the length of the markov
        chain to be created and passes the chain as a list and the next word to
        self._build_middle_mapping()
        :return:
        """
        self.starting_words.append(self.words_list[0])
        for i in range(1, len(self.words_list) - 1):
            if i < self.markov_length:
                word_history = self.words_list[:i + 1]
            elif i >= self.markov_length:
                word_history = \
                            self.words_list[i - self.markov_length + 1:i + 1]
            next_word = self.words_list[i + 1]
            # if the last word was a period, add the next word to
            # self.starting_word
            if word_history[-1] == "." and next_word not in list(PUNCTUATIONS):
                self.starting_words.append(next_word)

            self._build_middle_mapping(word_history, next_word)

        self._normalise_mapping()

    def _next(self, prev_list):
        """Decides on the next word to be selected for
        :param prev_list:
        :return: <str>
        """
        probabilty_sum = 0.0
        next_word = ""
        index = random.random()
        # Shorten prevList until it's in mapping
        while tuple(prev_list) not in self.final_mapping:
            prev_list.pop(0)
        # Get a random word from the mapping, given prevList
        for k, v in self.final_mapping[tuple(prev_list)].items():
            probabilty_sum += v
            if probabilty_sum >= index and next_word == "":
                next_word = k
                break
        return next_word

    def generate_sentence(self):
        """
        Returns a generic sentence using markov chains

        :return: Generated sentence
        :rtype: str
        """
        self._iterate_through_word_list()
        # Start with a random "starting word"
        current_word = random.choice(self.starting_words)
        sent = current_word.capitalize()
        prev_list = [current_word]
        # Keep adding words until we hit a period
        while (current_word != "."):
            current_word = self._next(prev_list)
            prev_list.append(current_word)
            # if the prevList has gotten too long, trim it
            if len(prev_list) > self.markov_length:
                prev_list.pop(0)
            if (current_word not in list(".,!?;")):
                sent += " "  # Add spaces between words (but not punctuation)
            sent += current_word
        return sent
