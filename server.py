import json
from flask import Flask
from random import SystemRandom

app = Flask(__name__)
rand = SystemRandom()
words = [_.strip('\n') for _ in open('word.list')]

@app.route("/")
def hello():
    return "diceware: dw/c/n/"

@app.route("/dw/<int:c>/<int:n>")
def dw(c, n, fmt='json'):
    c = c if c < 100 else 100
    n = n if n < 100 else 100
    pwds = '<br/>'.join(' '.join(words[rand.randrange(0, len(words))] for _ in xrange(n)) 
            for __ in xrange(c))
    return pwds

if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')

