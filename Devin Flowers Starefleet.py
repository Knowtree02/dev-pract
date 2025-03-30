
GPA =float(input("enter GPA: 1.0 - 4.0:"))
SAT =float(input("enter SAT :0 - 1000:"))
Age =int(input("enter Age: 16 - 18:"))
Race =(input("enter Race? Human, Vulcans, Klingon, Romulan?"))

if GPA>=2.0:
       
    if SAT>=800:
        
        if Race != "Romulan":    
        
            if (Race == "Vulcan" and Age==16) or (Age==17 and (Race == "Human" or  Race == "Klingon")):
                print("pass")
            else:
                print("reject")

        else:
            print("reject")
    else:
        print("reject")
 
else:
    print("reject")
