Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> "dont" + "forget" + "to" + "converse" + "water"
'dontforgettoconversewater'
>>> "the"*3
'thethethe'
>>> ' the' + 3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ' the' + 3
TypeError: Can't convert 'int' object to str implicitly
>>> ' the' + 3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ' the' + 3
TypeError: Can't convert 'int' object to str implicitly
>>> "the"*3 + "beautiful" + "earth"
'thethethebeautifulearth'
>>> 2*"true"
'truetrue'
>>> a='save;
SyntaxError: EOL while scanning string literal
>>> a='save'
>>> b='the'
>>> c='planet
SyntaxError: EOL while scanning string literal
>>> a='save'
>>> b='the'
>>> c='earth'
>>> print(a+b+c)
savetheearth
>>> a + b + c
'savetheearth'
>>> a+' '+b+' '+c
'save the earth'
>>> a = 4
>>> b = 'panda bears'
>>> a + b
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(a) + b
'4panda bears'
>>> test = " i love meet"
>>> "a" + b
'apanda bears'
>>> test = "i love bears"
>>> len(test)
12
>>> test.upper
<built-in method upper of str object at 0x7f215c593830>
>>> test.upper()
'I LOVE BEARS'
>>> test
'i love bears'
>>> test = test.upper()
>>> test
'I LOVE BEARS'
>>> test.lower()
'i love bears'
>>> test.capitalize()
'I love bears'
>>> test.swapcase()
'i love bears'
>>> test.replace("o","i")
'I LOVE BEARS'
>>> test.replace("i","o")
'I LOVE BEARS'
>>> test.replace("love","bears")
'I LOVE BEARS'
>>> test.replace("I","O")
'O LOVE BEARS'
>>> 
>>> 
>>> 


>>> 

>>> 
>>> 
>>> 
>>> a="MEET"
>>> b="meet
SyntaxError: EOL while scanning string literal
>>> b="meet"
>>> c="meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a !=b
True
>>> a !=c
True
>>> b !=c
True
>>> a=a.lower()
>>> a==b
True
>>> my_string+"bananayellowthinkhatgreybigcaliforna314"
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    my_string+"bananayellowthinkhatgreybigcaliforna314"
NameError: name 'my_string' is not defined
>>> my_string="bananayellowthinkhatgreybigcaliforna314"
>>> my_string[
