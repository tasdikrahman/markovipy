#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from markovipy.utils import fix_caps
from markovipy.utils import get_word_list

CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CURRENT_DIR)


class TestFixCaps:
    def test_utils_fix_caps_AaAaA(self):
        assert ("Aaaaa" == fix_caps("AaAaA"))

    def test_utils_fix_caps_aAAAA(self):
        assert ("aaaaa" == fix_caps("aAAAA"))

    def test_utils_fix_caps_AAAA(self):
        assert ("aaaa" == fix_caps("AAAA"))

    def test_utils_ffix_caps_nOOb(self):
        assert ("noob" == fix_caps("nOOb"))

    def test_utils_fix_caps_nooB(self):
        assert ("noob" == fix_caps("nooB"))

    def test_utils_fix_caps_I(self):
        assert ("I" == fix_caps("I"))


class TestWordList:
    """Checks whether my regex would be returning a list of words or not"""
    def test_utils_check_list_len(self):
        assert (
            len(get_word_list(
                os.path.join(ROOT_DIR,
                             "corpus/shakespeare/hamlet_utf8.txt"))
            ) > 0)
