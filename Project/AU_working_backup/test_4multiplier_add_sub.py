# sel = 0 does multiplication
# cin=0 does addition, cin=1 does 
import os
import time
import sys

if(len(sys.argv)<2):
    print("Error. Please provide the .sim file as command line argument")

cmdfile = "test_file.cmd"
#sim_file = "multiplier_mux.sim"
sim_file = sys.argv[1]
logfile = "output.log"
in1_vector = "a_3 a_2 a_1 a_0"
in2_vector = "b_3 b_2 b_1 b_0"
sel_vector = "sel cin"
p_vector = "p_7 p_6 p_5 p_4 p_3 p_2 p_1 p_0"
out = "out_7 out_6 out_5 out_4 out_3 out_2 out_1 out_0"
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
    cin_txt = eachline[eachline.find('cin')+4]
    sel_txt = eachline[eachline.find('sel')+4]
    out_0_txt = eachline[eachline.find('out_0')+6]
    out_1_txt = eachline[eachline.find('out_1')+6]
    out_2_txt = eachline[eachline.find('out_2')+6]
    out_3_txt = eachline[eachline.find('out_3')+6]
    out_4_txt = eachline[eachline.find('out_4')+6]
    out_5_txt = eachline[eachline.find('out_5')+6]
    out_6_txt = eachline[eachline.find('out_6')+6]
    out_7_txt = eachline[eachline.find('out_7')+6]
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
    
    if(out_7_txt == 'X' or out_6_txt == 'X' or out_5_txt == 'X' or out_4_txt == 'X' or out_3_txt == 'X' or out_2_txt == 'X' or out_1_txt == 'X' or out_0_txt == 'X'):
        print("dont cares!!")
        print(out_7_txt+out_6_txt+out_5_txt+out_4_txt+out_3_txt+out_2_txt+out_1_txt+out_0_txt)
    
    else:
        if(sel_txt=='0'): 
            result = int(out_7_txt+out_6_txt+out_5_txt+out_4_txt+out_3_txt+out_2_txt+out_1_txt+out_0_txt,2)
            product = int(a*b)
            if(result!=product):
                print("******************************************")
                print("Error")
                print(str(a)+"*"+str(b)+ " failed")
                print("Obtained " + out_7_txt+out_6_txt+out_5_txt+out_4_txt+out_3_txt+out_2_txt+out_1_txt+out_0_txt + " = "+ str(result))
                print("Expected " + bin(product)[2:].zfill(8) + " = " + str(product))
                print("******************************************")
                #sys.exit()
            else:
                print("Success " +  str(a) + "*" + str(b) + "=" + str(product))
                counter = counter + 1
            '''
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
            '''
        else:
            if(cin_txt=='0'):
                result = int(out_4_txt+out_3_txt+out_2_txt+out_1_txt+out_0_txt,2)
                add = int(a+b)
                if(result!=add):
                    print("******************************************")
                    print("Error")
                    print(str(a)+"+"+str(b)+ " failed")
                    print("Obtained " + out_7_txt+out_6_txt+out_5_txt+out_4_txt+out_3_txt+out_2_txt+out_1_txt+out_0_txt + " = "+ str(result))
                    print("Expected " + bin(add)[2:].zfill(8) + " = " + str(add))
                    print("******************************************")
                    #sys.exit()
                else:
                    print("Success " +  str(a) + "+" + str(b) + "=" + str(add))
                    counter = counter + 1
            else:
                result = int(out_3_txt+out_2_txt+out_1_txt+out_0_txt,2)
                if(out_4_txt=='0'):
                    result=result-(1<<4)
                sub = int(a-b)
                if(result!=sub):
                    print("******************************************")
                    print("Error")
                    print(str(a)+"-"+str(b)+ " failed")
                    print('Obtained ' + out_7_txt+out_6_txt+out_5_txt+out_4_txt+out_3_txt+out_2_txt+out_1_txt+out_0_txt + " = "+ str(result))
                    print("Expected " + bin(sub)[2:].zfill(8) + " = " + str(sub))
                    print("******************************************")
                    #sys.exit()
                else:
                    print("Success " +  str(a) + "-" + str(b) + "=" + str(sub))
                    counter = counter + 1

with open(cmdfile,"w") as file:
    file.write("logfile "+ logfile +"\n")
    file.write("stepsize 1000\n")
    file.write("w " + out + " " + sel_vector + " "+p_vector + " "+in1_vector + " "+ in2_vector + "\n")
    file.write("vector In "+ sel_vector + " " + in1_vector + " "+ in2_vector + "\n")
    file.write("set vlist {")
    for j in range(0,4,1):
        for i in range(0,totalnumofvectors,1):
            file.write(str(bin(j)[2:].zfill(2))+str(bin(i)[2:].zfill(8)) + " ")
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

print("Accuracy " + str(counter/(4*totalnumofvectors)*100) + "%")