# Run-Length-Encoding

Imagine you are presented with a sequence of digits. You may create a new sequence by reading aloud the
previous sequence and using that reading as the next sequence, summarizing any run of x identical digits d as ”x d”.
For example, 3 1 1 is read as ”one three, two ones”, which becomes 1 3 2 1 (1 3, 2 1s). You may continue generating
sequences iteratively, using the previous value as input for the next step. For each step, take the previous value,
and replace each run of identical digits (like 4 4 4) with the number of digits (e.g., 3) followed by the digit itself (4).
For example:

1 becomes 1 1 (1 copy of digit 1).  
1 1 becomes 2 1 (2 copies of digit 1).  
2 1 becomes 1 2 1 1 (one 2 followed by one 1).  
1 2 1 1 becomes 1 1 1 2 2 1 (one 1, one 2, and two 1s).  
1 1 1 2 2 1 becomes 3 1 2 2 1 1 (three 1s, two 2s, and one 1).  

Create a module sequenceprop.py containing a function sequence prop 30() that takes an integer which represents
your original sequence of digits (i.e., the integer 522 represents the sequence ”5 2 2”) and determines how
many digits are in the final result after this iterative replacement process has been repeated 30 times.
