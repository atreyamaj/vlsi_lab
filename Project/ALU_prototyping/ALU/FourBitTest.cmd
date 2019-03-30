w s_0 s_1 s_2 s_3 cout cin b_0 b_1 b_2 b_3 a_0 a_1 a_2 a_3 
vector In a_3 a_2 a_1 a_0 b_3 b_2 b_1 b_0 cin
logfile outputs.log
set vlist {000000000 001001100 010100010 011011110 100110010 101100001 110010001 111000001 111000011}
foreach vec $vlist {setvector in $vec ; s}
logfile
