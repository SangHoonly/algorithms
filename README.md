# algorithms
studied algorithms(university, by myself, etc)

examples for greedy algorithms.
1. Pinning Problem
Q) If "n" sticks are given, we try to put them with pins with minimum number. In this time, what is the minimum number of pins?
A) Similar with Activity Selection Problem, we can sort sticks by their right-end number.
   After sorting, we can select the fastist one's(sticks which will be standard) right-end number and compare with the other's left-end number. 
   If the other's left-end number is bigger than standard's right-end number, 1 pin should be needed.
