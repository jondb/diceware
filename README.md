diceware
========

python implementation of diceware (using os.urandom)

see [diceware.com](http://world.std.com/~reinhold/diceware.html)

**Note on security of os.urandom():**

On many *nix machines, the underlying OS random number generator (/dev/random) is known to
produce slightly non-random results, or so I've been told... This may have some implications
as to how the words are selected.

server.py
---------
Run this to launch a simple Flask web app. The usage is as follows:
```
http://my.server.com:5000/dw/<# passphrases>/<# words in passphrase>
```

dw.py
-----
Command-line utility for much the same purpose. Usage:
```bash
$ python dw.py #_of_passphrases #_words_in_passphrase
```

