diceware
========

python implementation of diceware (using os.urandom)

see [diceware.com](http://world.std.com/~reinhold/diceware.html)

**Note on security of os.urandom():**

On many linux servers, the underlying OS random number generator is known to
produce slightly non-random results, or so I've been told...

server.py
---------
Run this to launch a simple Flask server. The usage is as follows:
```
http://my.server.com:5000/dw/<# passphrases>/<# words in passphrase>
```

dw.py
-----
Command-line utility for much the same purpose. Usage:
```sh
> python dw.py <# passphrases> <# words in passphrase>
```

