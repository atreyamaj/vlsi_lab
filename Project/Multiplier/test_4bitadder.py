import os
import time
import sys

cmdfile = "test_file.cmd"
sim_file = "fulladder_4bit.sim"
logfile = "output.log"

in1_vector = "a_3 a_2 a_1 a_0"
in2_vector = "b_3 B_2 b_1 b_0"
in3_vector = "cin"
out = "cout s_3 s_2 s_1 s_0"
counter = 0
def evaluate(eachline):
    global counter
    cin_txt = eachline[eachline.find('cin')+4]
    a_0_txt = eachline[eachline.find('a_0')+4] 
    a_1_txt = eachline[eachline.find('a_1')+4] 
    a_2_txt = eachline[eachline.find('a_2')+4]
    a_3_txt = eachline[eachline.find('a_3')+4]
    b_0_txt = eachline[eachline.find('b_0')+4]
    b_1_txt = eachline[eachline.find('b_1')+4]
    b_2_txt = eachline[eachline.find('b_2')+4]
    b_3_txt = eachline[eachline.find('b_3')+4]
    s_0_txt = eachline[eachline.find('s_0')+4]
    s_1_txt = eachline[eachline.find('s_1')+4]
    s_2_txt = eachline[eachline.find('s_2')+4]
    s_3_txt = eachline[eachline.find('s_3')+4]
    cout_txt = eachline[eachline.find('cout')+5]
    cin = int(cin_txt,2)
    a = int(a_3_txt+a_2_txt+a_1_txt+a_0_txt,2)
    b = int(b_3_txt+b_2_txt+b_1_txt+b_0_txt,2)
    result = int(cout_txt+s_3_txt+s_2_txt+s_1_txt+s_0_txt,2)
    sum_ab = a+b+cin
    if(result!=sum_ab):
        print("*************************")
        print("Error")
        print(str(a)+"+"+ str(b) + "+" + str(cin))
        print("*************************")
        sys.exit()
    else:
        print(str(a) + "+" + str(b) + "+" + str(cin) + "=" + str(sum_ab))
        counter = counter + 1

with open(cmdfile,"w") as file:
    file.write("logfile "+ logfile +"\n")
    file.write("w " + out + " " + in1_vector + " "+ in2_vector + " " + in3_vector + "\n")
    file.write("vector In "+ in1_vector + " "+ in2_vector + " " + in3_vector + "\n")
    file.write("set vlist {")
    for i in range(0,2**9,1):
        file.write(str(bin(i)[2:].zfill(9)) + " ")
    file.write("}\n")
    file.write("foreach vec $vlist {setvector in $vec ; s}\n")
    file.write("logfile\n")
    file.close()

os.system("irsim "+ sim_file + " -"+cmdfile+" &")
print("Waiting for irsim to write output log file....")
input("Press any key once irsim is done evaluating....")
eachline = ""
with open(logfile,"r") as fp:
    print("Log file loaded. Evaluating..")
    line = fp.readline()
    while line:
        if('time' in line):
            evaluate(eachline)
            line = fp.readline()
            eachline = ""
        else:
            eachline = eachline + line
            line = fp.readline()
    fp.close()

print("Accuracy " + str(counter/(2**9)*100) + "%")

