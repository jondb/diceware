#!/usr/bin/env python
"""Super simple function to choose the words."""

from random import SystemRandom

import wordlist


def mkphrase():
    """Generate the phrase.

    Returns:
        10-word array
    """
    ran = SystemRandom()
    phrase = []

    for i in range(10):
        # Roll the dice
        dice_no = ran.randrange(0,len(wordlist.words))
        # Select the word
        word = wordlist.words[dice_no]
        # Add to phrase
        phrase.append(word)
    return phrase


if __name__ == "__main__":
    phrase = mkphrase()
    print '.'.join(phrase)