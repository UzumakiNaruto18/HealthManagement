import datetime
def gettime():
    """A Function To Print Current Date And Time """
    return datetime.datetime.now()
Ask=int(input("Press 1 To Lock \n 2 To Retrieve:\n"))
if (Ask==1):
 name=int(input("Press 1 For Harry\n 2 For Rohan\n 3 For Hammad \n"))
 if(name==1):
    H_activity=int(input("Enter 1 For Exercise\n 2 For Food \n"))
    if (H_activity==1):
         H_excersise=input("Enter The Excerise:\n")
         HS = open("Harry_exercise.txt", "a")
         HS.write(str([str(gettime())])+": "+H_excersise+"\n")
         HS.close() 
         print("Successfully Added")
    elif(H_activity==2):
        H_food=input("Enter The Food:\n")
        HF=open("Harry_Food.txt","a")
        HF.write(str([str(gettime())])+": "+H_food+"\n")
        HF.close()
        print("Successfully Added")
 elif(name==2):
    R_activity=int(input("Enter 1 For Exercise\n 2 For Food \n"))
    if(R_activity==1):
        R_Excercise=input("Enter The Exercise:\n")
        RS=open("Rohan_Exercise.txt","a")
        RS.write(str([str(gettime())])+": "+R_Excercise+"\n")
        RS.close
        print("Successfully Added")
    elif(R_activity==2):
        R_Food=input("Enter The Food You Ate:\n")
        RF=open("Rohan_Food.txt","a")
        RF.write(str([str(gettime())])+": "+R_Food+"\n")
        RF.close()
        print("Successfully Added")
 elif(name==3):
    Ha_activity=int(input("Enter 1 For Exercise\n 2 For Food \n"))
    if(Ha_activity==1):
         Ha_Exercise=input("Enter the Excercise:\n")
         HE=open("Hammad_Exercise.txt","a")
         HE.write(str([str(gettime())])+": "+Ha_Exercise+"\n")
         HE.close
         print("Successfully Added")
    elif(Ha_activity==2):
         Ha_Food=input("Enter The Food:\n")
         HAF=open("Hammad_Food.txt","a")
         HAF.write(str([str(gettime())])+": "+Ha_Food+"\n") 
         HAF.close
         print("Successfully Added")
elif(Ask==2):
    def retri(client):
        client=int(input("Enter For Which Client You Want To Retreive \n 1 For Harry\n 2 For Rohan\n 3 For Hammad:\n"))
        if(client==1):
            H_ask=int(input("Enter 1 For Exercise\n 2 For Food \n"))
            if(H_ask==1):
                ho=open("Harry_exercise.txt","rt")
                print(ho.read())
                ho.close()
            elif(H_ask==2):
                hf=open("Harry_Food.txt","a")
                print(hf.read())
                hf.close()   
        if(client==2):
            R_ask=int(input("Enter 1 For Exercise\n 2 For Food \n"))    
            if(R_ask==1):
                ho=open("Rohan_Exercise.txt","rt")
                print(ho.read())
                ho.close()
            elif(R_ask==2):
                hf=open("Rohan_Food.txt","a")
                print(hf.read())
                hf.close()
        if(client==3):
            Ha_Ask=int(input("Enter 1 For Exercise\n 2 For Food \n"))
            if(Ha_Ask==1):
                ho=open("Hammad_Exercise.txt","a")
                print(ho.read())
                ho.close()
            elif(Ha_Ask==2):
                hf=open("Hammad_Food.txt","a")
                print(hf.read())
                hf.close()
