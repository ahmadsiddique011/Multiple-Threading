# Multiple-Threading

Creates four threads other than main thread. 
1. Input thread 
2. Reverse thread 
3. Capital thread 
4. Shift thread 
Input thread will take string input from user, reverse thread will reverse the string and output it, 
capital thread will capitalize the characters of string and output it and shift thread will shift each 
characters of the string two time (e.g. a will become c) and output it. All the threads wait for input 
thread when input thread finishes his task all the waiting thread start their work simultaneously. 
You also have to handle the exceptions of input thread. Also take care the state of each thread. Do 
not waste your memory resources.
