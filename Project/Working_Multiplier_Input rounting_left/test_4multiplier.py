import os
import time
import sys

if(len(sys.argv)<2):
    print("Error")

cmdfile = "test_file.cmd"
#sim_file = "fulladder_4bit.sim"
sim_file = sys.argv[1]
logfile = "output.log"

in1_vector = "a_3 a_2 a_1 a_0"
in2_vector = "b_3 b_2 b_1 b_0"
out = "p_7 p_6 p_5 p_4 p_3 p_2 p_1 p_0"
totalnumofvectors = 2**8
counter = 0
def evaluate(eachline):
    global counter
    a_0_txt = eachline[eachline.find('a_0')+4] 
    a_1_txt = eachline[eachline.find('a_1')+4] 
    a_2_txt = eachline[eachline.find('a_2')+4]
    a_3_txt = eachline[eachline.find('a_3')+4]
    b_0_txt = eachline[eachline.find('b_0')+4]
    b_1_txt = eachline[eachline.find('b_1')+4]
    b_2_txt = eachline[eachline.find('b_2')+4]
    b_3_txt = eachline[eachline.find('b_3')+4]
    p_0_txt = eachline[eachline.find('p_0')+4]
    p_1_txt = eachline[eachline.find('p_1')+4]
    p_2_txt = eachline[eachline.find('p_2')+4]
    p_3_txt = eachline[eachline.find('p_3')+4]
    p_4_txt = eachline[eachline.find('p_4')+4]
    p_5_txt = eachline[eachline.find('p_5')+4]
    p_6_txt = eachline[eachline.find('p_6')+4]
    p_7_txt = eachline[eachline.find('p_7')+4]
    a = int(a_3_txt+a_2_txt+a_1_txt+a_0_txt,2)
    b = int(b_3_txt+b_2_txt+b_1_txt+b_0_txt,2)
    result = int(p_7_txt+p_6_txt+p_5_txt+p_4_txt+p_3_txt+p_2_txt+p_1_txt+p_0_txt,2)
    product = int(a*b)
    if(result!=product):
        print("******************************************")
        print("Error")
        print(str(a)+"*"+str(b)+ " failed")
        print('Obtained ' + p_7_txt+p_6_txt+p_5_txt+p_4_txt+p_3_txt+p_2_txt+p_1_txt+p_0_txt + " = "+ str(result))
        print("Expected " + bin(product)[2:].zfill(8) + " = " + str(product))
        print("******************************************")
        #sys.exit()
    else:
        print("Success " +  str(a) + "*" + str(b) + "=" + str(product))
        counter = counter + 1

with open(cmdfile,"w") as file:
    file.write("logfile "+ logfile +"\n")
    #file.write("vsupply 3.3")
    file.write("stepsize 15\n")
    file.write("w " + out + " " + in1_vector + " "+ in2_vector + "\n")
    file.write("vector In "+ in1_vector + " "+ in2_vector + "\n")
    file.write("set vlist {")
    for i in range(0,totalnumofvectors,1):
        file.write(str(bin(i)[2:].zfill(8)) + " ")
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

print("Accuracy " + str(counter/totalnumofvectors*100) + "%")
