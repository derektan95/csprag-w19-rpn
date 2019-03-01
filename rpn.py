#!/usr/bin/env python3
#don't need semicolon!
#very useful for prototyping using simple code

def calculate(arg):      #':' with indentation means block
    pass                 # means do nothing. auto exit block
                         # when indentation restores

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':       #no need for if (...)
    main()                      # means that you run 'main' whenever filename is called


