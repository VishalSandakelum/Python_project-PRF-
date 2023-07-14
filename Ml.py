import os

NamArray = []
IDArray = []
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
    while bool :
        Name = input("Enter Name :")
        if Name != "" :
            NamArray.append(Name)
        else :
            print("Please enter the name !") 
        
        id = input("Enter Id :")
        if id != " " :
            print("Id"+": "+id)
            if len(IDArray) == 0:
                IDArray.append(id)
            else:
                for i in range(len(IDArray)):
                    if id != IDArray[i] :
                        print(IDArray[i])
                        IDArray.append(id)
        else :
            print("Please enter the Id !")
            
        Decition = input("If you wan't to go back enter the 'y'/'n' : ")
        if Decition.__eq__("Y") or Decition.__eq__("y") :
            bool(False)
            PrintTerminal()
            Printmain()
        
            
def AddMarks():
    nam = input("Enter Student Name : ")
    if nam !="":
        print(nam)
        
    

class First:
    
    Printmain()
        
    
    
    
    
            