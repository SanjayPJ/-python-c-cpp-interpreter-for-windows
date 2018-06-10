import os
os.system("mode con:cols=80 lines=40")
os.system("title cpp-interpreter")
def maincpp():
	with open("cpp-demo.cpp","w") as cppfile:
		os.system("g++ --version")
		cppfile.write('#include<iostream>\nusing namespace std;int main(){')
		while(True):
			string = input(">>> ")
			if string=="":
				cppfile.write("return 0;}")
				cppfile.close()
				break
			else:
				cppfile.write(string+"\n")
		os.system("g++ cpp-demo.cpp")
		print("Result :: ")
		os.system("a.exe")
		opt2()
def opt2():
	opt2  = input("Do you wish to continue (y/n) :: ")
	if opt2=="y" or opt2=="Y":
		main()
	elif opt2=="n" or opt2=="N":
		os.system("exit")
	else:
		print("Enter a valid option.")
		opt2()

	
def main():
	print("===============================================================================")
	print("================================cpp-interpreter================================")
	print("===============================================================================")
	maincpp()
main()
