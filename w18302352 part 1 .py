# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200502           
# Date:20/04/2021
#clculates only for one student in 1 run 
total=1
pass_credit=1
defer_credit=1
fail_credit=1
        
def progresion_calculation(): #function that calculates the progression outcomes  
    if fail_credit >=80:
        print("exclude")
    elif pass_credit==100:
        print("progress(module trailer) ")
    elif pass_credit <=80:
        print("Progress – module retriever")
    elif pass_credit==120:
        print("Progress")

try:
     while total!=120 and (pass_credit%20!=0)and(defer_credit%20!=0) and (fail_credit%20!=0):
        pass_credit=int(input("Please enter the credits at passs"))
        defer_credit=int(input("Please enter the credits at defer"))
        fail_credit=int(input("Plese eneter the credits at fail"))
        total= pass_credit+defer_credit+fail_credit
        if ((pass_credit%20==0)and(defer_credit%20==0)and(fail_credit%20==0)):#range is checked 
            if total==120:
                progresion_calculation()
            else:
               print("Total incorrect")
        else:
             print("Out of Range")
except:
      print("Integer reguired")
