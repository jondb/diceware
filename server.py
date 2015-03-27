# -*- coding: utf8 -*-
from flask import Flask

import dicewords
app = Flask(__name__)

@app.route("/")
def hello():
    return """<html><body>
        <h1>DiceWords</h1>
        <p>You should pick between 5 and 10 words depending
        on the confidentiality needs. Best guess is a 7-word phrase is too strong
        for even the most sophisticated (ie NSA) to crack.</p>

        <h1>10-Word Secure Phrase</h1>
        <div><code><pre>%s</pre></code></div>
        
        <h1>References</h1>
        <ul>
            <li><a href="https://firstlook.org/theintercept/2015/03/26/passphrases-can-memorize-attackers-cant-guess/">PASSPHRASES THAT YOU CAN MEMORIZE — BUT THAT EVEN THE NSA CAN’T GUESS</a></li>
            <li><a href="http://world.std.com/~reinhold/diceware.html">Diceword Homepage</a></li>
        </ul>
        </body></html>""" % ' '.join(dicewords.mkphrase())


if __name__ == "__main__":
    app.debug = False
    app.run()

