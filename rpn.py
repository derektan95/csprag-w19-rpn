#!/usr/bin/env pythn3
#don't need semicon!
#very useful for prototyping

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def calculate(arg1, arg2, operator):      #':' with indentation means block
    my_stack = Stack()
#    print ("stack created")
#    for token in arg.split():
#        try:
#            token = int(token)
#            my_stack.push(token)
#        except ValueError:
    
    my_stack.push(arg1)
    my_stack.push(arg2)

    first_num = my_stack.pop()
    sec_num = my_stack.pop()

    if operator == '+': 
        my_stack.push(first_num + sec_num)
#        print ("plus sign called")
        return first_num + sec_num
    elif operator == '-':
        my_stack.push(first_num - sec_num)
#        print ("minus sign called")
        return first_num - sec_num
    elif operator == '^':
        my_stack.push(first_num ** sec_num)
        return first_num ** sec_num

#          function = operators[token]
#            arg2 = my_stack.pop()
#            arg1 = my_stack.pop()
#            result = function(arg1, arg2)
#            my_stack.append(result)

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':       #no need for if (...)
    main()                      # means that you run 'main' whenever filename is called
