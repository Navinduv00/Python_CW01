# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200502           
# Date:20/04/2021

row=0
status=0
progress=0
module_trailer=0
exclude=0
module_retriever=0
count=0
def print_star(num_students): #num_students=number of students in each progression outcome
    if row<num_students:
        star_space="*"
    else:
        star_space=""
    return(star_space)

def star_calculation(progress,module_trailer,module_retriever,exclude): #printing stars and spaces in rows
    global row
    max_row=max(progress,module_trailer,module_retriever,exclude)
    while row<max_row:
        print(f'{"":2} { print_star(progress):11} { print_star(module_trailer):10} { print_star(module_retriever):10} { print_star(exclude):}')
        row=row+1
print("Welcome! Enter your credits to get your progression outcome! \n")   
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
else:
    print("\n_____VERTICAL HISTOGRAM_____") #histogram is created 
    print("\nProgress",progress,"Trailing",module_trailer ,"Retriever",module_retriever ,"Excluded",exclude)
    star_calculation(progress,module_trailer,module_retriever,exclude)
    print("\n",count,"outcomes in total ")
    


