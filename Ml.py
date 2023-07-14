import os

NamArray = []
GradeArray = []
bool(True)
Iput = ""

def callMethod():
    Iput = input("ENTER NUMBER :")
    if Iput.__eq__("1") :
        PrintTerminal()
        AddStudent()


def Printmain() :
    print("1) Add Student"+"\t"+"2) Add Marks");
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
        
        Grade = input("Enter Grade :")
        if Grade != "" :
            GradeArray.append(Grade)
        else :
            print("Please enter the Grade !")
            
        Decition = input("If you wan't to go back enter the 'y'/'n' : ")
        if Decition.__eq__("Y") or Decition.__eq__("y") :
            bool(False)
            PrintTerminal()
            Printmain()

class First:
    
    Printmain()
        
    
    
    
    
            