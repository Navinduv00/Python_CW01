# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200502           
# Date:20/04/2021

status=1
progress=1
module_trailer=1
exclude=1
module_retriever=1
count=0
   
while status!="q": #program will continue to execute until the character 'q' is entered
    try:
         
            pass_credit=int(input("Please enter the credits at passs"))
            if pass_credit in range (0,121,20): #range is checked, if the input is higher than 120 it will repeat  
                 pass
                
            else:
                 print("Range error")
                 continue
                                  
            
            defer_credit=int(input("Please enter the credits at defer"))
            if defer_credit <=120:
                pass
                
            else:
                print("Range error")
                pass
            fail_credit=int(input("Plese eneter the credits at fail"))
            if fail_credit <=120:
                pass
                
            else:
                print("Range error")
                continue
            
            total= pass_credit+defer_credit+fail_credit
            if ((pass_credit%20==0)and(defer_credit%20==0)and(fail_credit%20==0)): #range is checked
                 if total==120:
                      if fail_credit >=80:
                         print("exclude")
                         exclude+=1
                      elif pass_credit==120:
                         print("Progress")
                         progress+=1
                      elif pass_credit==100:
                          print("progress(module trailer)")
                          module_trailer+=1
                      elif pass_credit <=80:
                          print("Progress – module retriever ")
                          module_retriever+=1
 
                     
                 else:
                     print("Total incorrect")
                     continue
                             

            else:
                print("Range error")
                continue
            count= count+1
            status=input("Enter q to quit or press enter to continue adding")#only charachter "q" will break the loop
            while status!="" and status !="q":
                status=input("invalid input enter q or press enter to continue adding")
        
    except:
        print("invalid syntax")



