=====
Usage
=====

To use markovipy in a project::

    >>> from markovipy import MarkoviPy
    >>> # create MarkoviPy object
    >>> obj = MarkoviPy("/Users/tasrahma/development/projects/markovipy/corpus/ts_eliot/Gerontion_utf8.txt", 3)
    >>> # arguments passes is the initial corpus file and the markov chain length(defaults to 2 if nothing passed)
    >>> obj.generate_sentence()
    'Cammel, whirled Beyond the circuit of the shuddering Bear In fractured atoms.'
    >>> obj.generate_sentence()
    'After such knowledge, what forgiveness? Think now History has many cunning passages, contrived corridors And issues, deceives with whispering ambitions, Guides us by vanities.'
    >>> obj.generate_sentence()
    'Gull against the wind, in the windy straits Of Belle Isle, or running on the Horn, White feathers in the snow, the Gulf claims, And an old man, a dull head among windy spaces.'
    >>> obj.generate_sentence()
    'Silvero With caressing hands, at Limoges Who walked all night in the field overhead; Rocks, moss, stonecrop, iron, merds.'
    >>> obj.generate_sentence()
    "Gives too soon Into weak hands, what's thought can be dispensed with Till the refusal propagates a fear."
    >>>

