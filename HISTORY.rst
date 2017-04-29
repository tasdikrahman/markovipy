=======
History
=======

0.2.0 (2017-04-29)
------------------

* ``self.middle_value`` mapping becomes a ``defaultdict``
* ``list_to_tuple()`` was removed to use just the ``tuple()``
* moved ``self.words_list = get_word_list(self.filename)`` to `__init__()`

0.1.1 (2017-04-14)
------------------

* fixes ``UnicodeDecodeError`` while reading files instead of using the normal ``open()``

0.1.0 (2017-04-11)
------------------

* First release on PyPI.
