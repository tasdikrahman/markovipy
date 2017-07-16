===============================
markovipy
===============================


.. image:: https://img.shields.io/pypi/v/markovipy.svg
        :target: https://pypi.python.org/pypi/markovipy

.. image:: https://img.shields.io/travis/tasdikrahman/markovipy.svg
        :target: https://travis-ci.org/tasdikrahman/markovipy

.. image:: https://readthedocs.org/projects/markovipy/badge/?version=latest
        :target: https://markovipy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/tasdikrahman/markovipy/shield.svg
     :target: https://pyup.io/repos/github/tasdikrahman/markovipy/
     :alt: Updates


|logo|


She tries striking conversations with you with her cohesive sentences after you have given her fill of text to her. And no she won’t complain about how big your corpus is. Also, don’t ask her if she can pass the turing test. She might not talk to you again.

I `wrote a blog post <http://tasdikrahman.me/2017/05/06/Making-of-trumporate-using-markovipy-generating-sentences-using-markov-chains-part-1/>`__ explaining the motivation and what is there behind the scenes if you are interested

====
Demo
====

.. image:: http://tasdikrahman.me/content/images/2017/05/markovipy.png
     :target: https://github.com/tasdikrahman/markovipy
     :alt: Demo

============
Installation
============

To install markovipy, run this command in your terminal:

.. code-block:: console

    $ pip install markovipy

This is the preferred method to install markovipy, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


=====
Usage
=====

To use markovipy in a project::

    >>> from markovipy import MarkoviPy
    >>>
    >>> # create MarkoviPy object
    >>> obj = MarkoviPy("/Users/tasrahma/development/projects/markovipy/corpus/ts_eliot/Gerontion_utf8.txt", 3)
    >>>
    >>>
    >>> # arguments passed, is the initial corpus file and the markov chain length(defaults to 2 if nothing passed)
    >>> obj.generate_sentence()
    'Cammel, whirled Beyond the circuit of the shuddering Bear In fractured atoms.'
    >>>
    >>> obj.generate_sentence()
    'After such knowledge, what forgiveness? Think now History has many cunning passages, contrived corridors And issues, deceives with whispering ambitions, Guides us by vanities.'
    >>>
    >>> obj.generate_sentence()
    'Gull against the wind, in the windy straits Of Belle Isle, or running on the Horn, White feathers in the snow, the Gulf claims, And an old man, a dull head among windy spaces.'
    >>>
    >>> obj.generate_sentence()
    'Silvero With caressing hands, at Limoges Who walked all night in the field overhead; Rocks, moss, stonecrop, iron, merds.'
    >>>
    >>> obj.generate_sentence()
    "Gives too soon Into weak hands, what's thought can be dispensed with Till the refusal propagates a fear."


* Free software: GNU General Public License v3
* Documentation: https://markovipy.readthedocs.io.


Features
--------

* More tests to be added. As of now, some minimal tests have been written. Contributions more than welcome.
* Create a web-interface with some fancy buttons/UI which would give you random quotes.


Links
-----

* `Blog post <http://tasdikrahman.me/2017/05/06/Making-of-trumporate-using-markovipy-generating-sentences-using-markov-chains-part-1/>`__

.. |logo| image:: http://i.imgur.com/cTY2kTK.png
   :target: https://markovipy.readthedocs.io

Donation 
--------

If you have found my little bits of software being of any use to you, do consider helping me pay my internet bills :)

|Paypal badge|

|Instamojo|

|gratipay|

|patreon|

.. |Paypal badge| image:: https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg
   :target: https://www.paypal.me/tasdik
.. |gratipay| image:: https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png
   :target: https://gratipay.com/tasdikrahman/
.. |Instamojo| image:: https://www.soldermall.com/images/pic-online-payment.jpg
   :target: https://www.instamojo.com/@tasdikrahman
.. |patreon| image:: http://i.imgur.com/ICWPFOs.png
   :target: https://www.patreon.com/tasdikrahman/
