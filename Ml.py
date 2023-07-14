import os

NamArray = []
IDArray = []
pythonArray = []
javaArray = []
bool(True)
Iput = ""

def callMethod():
    Iput = input("ENTER NUMBER :")
    if Iput.__eq__("1") :
        PrintTerminal()
        AddStudent()
        
    elif Iput.__eq__("2"):
        PrintTerminal()
        AddMarks()


def Printmain() :
    print("1) Add Student"+"\t"+"2) Add Marks");
    print(IDArray)
    callMethod()
    
def PrintTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def AddStudent():
    check = ""
    nam = ""
    while bool :
        Name = input("Enter Name :")
        if Name != "" :
            nam = "ok"
        else :
            print("Please enter the name !") 
        
        id = input("Enter Id :")
        if id != " " :
            print("Id"+": "+id)
            if len(IDArray) == 0:
                IDArray.append(id)
                NamArray.append(Name)
            else:
                for i in range(len(IDArray)):
                    if id != IDArray[i] :
                        print(IDArray[i])
                        check = "ok"
                    else :
                        check = "no"
                        break
                if check.__eq__("ok"):   
                    IDArray.append(id)
                    NamArray.append(Name)
                else :
                    print("Something wrong !")
        else :
            print("Please enter the Id !")
            
        Decition = input("If you wan't to go back enter the 'y'/'n' : ")
        if Decition.__eq__("Y") or Decition.__eq__("y") :
            bool(False)
            PrintTerminal()
            Printmain()
        
            
def AddMarks():
    while True:
        id = input("Enter Student Id : ")
        if id !="":
            for i in range(len(IDArray)):
                if id==IDArray[i]:
                    print(NamArray)
                    print("Name : "+""+NamArray[i])
                    python = int(input("Enter the Python marks : "))
                    if (python>=0) & (python<=100):
                        pythonArray.append(python)
                    else:
                        print("Please enter valid (python) marks");
                
                    java = int(input("Enter the Java marks : "))
                    if (java>=0) & (java<=100):
                        javaArray.append(java)
                    else:
                        print("Please enter valid (java) marks.")
                else:
                    print("Something Wrong ! (Please check & enter the valid ID.)")
            
            if input("If you wan't to go back enter the 'y'/'n' : ").__eq__("y"):
                PrintTerminal()
                Printmain()
                break
            
        
        
    

class First:
    
    Printmain()
        
    
    
    
    
            