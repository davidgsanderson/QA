
bandA = range(0,34500)
bandB = range(34501,150000)
personalAllowance = 11850
tax = 0

salary = int(input("please enter your yearly salary - £"))

def getIncomeTax(salary) :
    
    if salary < personalAllowance :
       return salary
    elif salary in bandA :
        tax = 20
    elif salary in bandB :
        tax = 40
    else :
        tax =45
    
    tax = salary / 100 * tax
    salary = salary - tax
    return salary

        
salary = getIncomeTax(salary)
print("you will make £" + str(salary) + " after tax.")

