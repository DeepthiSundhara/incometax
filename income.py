def income_tax(income):
    if income<383000:
        return 0 
    elif income>=383000 and income<1600000:
        return 0.1*income
    elif income>=1600000 and income<2000000:
        return 0.15*income
    else:
        return 0.2*income
        
t=int(input())
for i in range(t):
    income=int(input())
    income_task=income_tax(income)
    print(income_task)
    
