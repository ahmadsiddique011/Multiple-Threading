import threading

def input_thread(): #snake_case
    string = input("\nEnter a string: ")     # Take input from user
    return string

def ReverseThread(string): #PascalCase
    print("Reversed string:", string[::-1])  #Reverse input string

def capitalThread(string): #camelCase
    print("Capitalized string:", string.upper()) #Capitalize user input

def shift_thread(string): #snake_case
    ShiftString = ""
    # Shift character of the string by two and print shifted output
    for char in string:
        shifted_char = chr(ord(char) + 2)
        ShiftString += shifted_char
    print("Shifted string:", ShiftString)

#Create the threads
input_t = threading.Thread(target=input_thread,)
reverse_t = threading.Thread(target=ReverseThread,)
capital_t = threading.Thread(target=capitalThread,)
shift_t = threading.Thread(target=shift_thread,)
#calling
string = input_thread()
ReverseThread(string)
capitalThread(string)
shift_thread(string)
#Start the input thread
input_t.start()
input_t.join()
#Start remaning thread
reverse_t.start()
capital_t.start()
shift_t.start()
#joining other thread
reverse_t.join()
capital_t.join()
shift_t.join()
