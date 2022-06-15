from database import *

#A function to display options
def welcome():
     
    print("\tWELCOME TO THE HOSPITAL'S DATABASE INFO")
    print("\t1. VIEW MY DATA")
    print("\t2. ADD DATA")
    print("\t3. UDPATE DATA")
    print("\t4. QUIT")



#A function to view patient data   
def view_patient_data():
     
     print('Enter your name ')
     name=input()
     print("")
     if name in illness:
            print("Illness: "+ illness[name])
            print("ID: " + ID[name])
            print('\n')
     else:
            print("Sorry there is no medical record for this patient")
            print('\n')
            
            
# A function to add patient data
def add_patient_data():
    
    print("Name of patient ")
    name3=input()
    name=name3
    
    print("Enter illness of patient ")
    ill3=input()
    illness[name]=ill3
    
    
    print("Input ID")
    idlel=input()
    ID[name]=idlel
    
    print("")
    
    print('Patient data added successfully!!! ')
    print("")
    
    print("name: " +name)
    print('Illness: ' +illness[name])
    print('ID: ' + ID[name])
    print("\n")
    

# A function to update patient data
def update_patient_data():
    
    print('Enter name ')
    name1=input()
    name=name1
    
    print('Update illness ')
    ill=input()
    illness[name]=ill
    
    print("Update ID")
    idlell=input()
    ID[name]=idlell
    
    print("")
    
    print('Patient database updated!!! ')
    print("")
    
    print(name,  ' is being diagnosed of ' + illness[name] )
    print("ID: " + ID[name])
    print("\n")
    
    

  
while True:
    welcome()

    print("Input your option ")
    view=input()
    if view=='1':
        
       view_patient_data()
       
    elif view=='2':
        
         add_patient_data()
              
    elif view=='3':
        
        update_patient_data()  
                  
    elif view=='4':
        break
    
        
    
        
        
            



    

        
            
