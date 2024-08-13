# Converter
# Project-1-Converter.py
This program is written in Python3 language.
This program is a CLI and can convert Hexadecimal, Octal, Binary to Decimal and Decimal to Hexadecimal, Binary, and Octal, and even encode and Decode Morse codes.

This is my first project written in Python3 language and easy to use......

While working on the newer version, I figured out some bug or problems in the older one:
1. Decimal to Hexadecimal is not working properly and showing reversed results. Solution, Add  "dechexstr = dechexstr[::-1]" line before printing hexa in hexdec().
2. Morsedecode and Morseencode doing opposite jobs. Solution, replace their functions with each other in mach case.
