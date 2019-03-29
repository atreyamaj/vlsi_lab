import os
cmdfile = "test_file.cmd"
file = open(cmdfile,"w")

sim_file = "fulladder_4bit.sim"
in1_vector = "a_3 a_2 a_1 a_0"
in2_vector = "b_3 B_2 b_1 b_0"
in3_vector = "cin"
out = "cout s_3 s_2 s_1 s_0"

file.write("w " + out + " " + in1_vector + " "+ in2_vector + " " + in3_vector + "\n")
file.write("vector In "+ in1_vector + " "+ in2_vector + " " + in3_vector + "\n")
file.write("set vlist {")
for i in range(0,2**9,1):
    file.write(str(bin(i)[2:].zfill(9)) + " ")
file.write("}\n")
file.write("foreach vec $vlist {setvector in $vec ; s}")
file.close()
os.system("irsim "+ sim_file + " -"+cmdfile)
