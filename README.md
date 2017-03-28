# hangman_game

A simple hangman game built in python2 and pygame.

Rules
--------
+ The program randomly picks a word from `VocabHungmanGame.txt`.
+ The user types one letter at a time to guess the word
+ The user is allowed to make eight incorrect guesses.


Install
--------
1. python2
2. pygame


Usage
--------
1. Close this repo
2. `python HangmanGame.py` to start the game

Pygame install tips
--------

Installing a pygame is tricky. If you are using `anaconda`, you can try `conda install pygame`.

If you get a following error:
```
Error: from pygame.base import * ImportError: dlopen
.....
...SDL Error - missing/usr/local/lib/libSDL-1.2.0.dylib...
....

```
You can try `pip install pygame`

if you could not load an image (with the following error)
```
pygame.error: Failed loading libpng.dylib: dlopen(libpng.dylib, 2): image not found
```
You can try, `brew install libpng`

Reference: [MacBook Python Pygame Anaconda – issues](https://inlovewithcode.wordpress.com/2016/10/14/macbook-python-pygame-anaconda-issues/)
