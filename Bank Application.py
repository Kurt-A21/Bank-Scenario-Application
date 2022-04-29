#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import sys

print("Welcome to Capitec ATM\nWould you like to make a transaction (enter y for yes or n for no)")
date= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
trans_list = open('transaction_file.txt' , "a")
ans = input()

if(ans == "y", "yes"):
     print("Proceeding to transaction...")

else:
    print("Transaction failed" )
    print("Take your card")
    print("================Enjoy your day==================\n\n")
    sys.exit()


print("Would you like to make a deposit or withdrawal?(enter d for deposit and w for withdrawal)")
option = input()

if (option == "d"):
    print( "How much would you like to deposit?")
    amount = input() 
    with open ("transaction_file.txt", "a") as trans_list:
        trans_list.write("Deposited:R" + str(amount) + "@" + date + "\n\n")
    bal1 = 600
    f_amount = float(amount)
    
    d_amount = bal1 + f_amount
    print("Deposit successful...")
    print("Current balance: R", d_amount)
    print("Take your card\n")
    print("================Enjoy your day==================")



elif (option == "w"):
    print("How much would you like to withdraw?")
    amount1 = input()
    with open ("transaction_file.txt", "a") as trans_list:
        trans_list.write("Withdrew:R" + str(amount1)  + "@" + date + "\n\n")
    bal2 = 600
    float(bal2)
    f_amount1 = float(amount1)
    
    w_amount = bal2 - f_amount1
    if(f_amount1 > bal2):
        print("Insufficient funds\nTake your card")
    
    else:
        print("Withdrawal successful...")
        print("Current balance: R", w_amount)
        print("Take your card\n")
        print("================Enjoy your day==================")
    



# In[ ]:





# In[ ]:




