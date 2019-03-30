w p_0 p_1 p_2 p_3 p_4 p_5 p_6 p_7 b_0 b_1 b_2 b_3 a_0 a_1 a_2 a_3 
stepsize 50
vector In a_3 a_2 a_1 a_0 b_3 b_2 b_1 b_0
logfile outputs.log
set vlist {00000000 00100110 01010001 01101111 10011001 10110000 11001000 11100000 11100001}
foreach vec $vlist {setvector in $vec ; s}
logfile
