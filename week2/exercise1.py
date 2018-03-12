"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']
# I think it will print a word from some word
for word in some_words:
    print(word)# it print a what
# it will pick a word from range
for x in some_words:
    print(x)# it print does

print(some_words)# i think it will print all words in some word

if len(some_words) > 3:#i think it will print some_words contains more than 3 words
    print('some_words contains more than 3 words')# it is

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
