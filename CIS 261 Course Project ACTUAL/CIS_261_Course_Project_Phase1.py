#Christopher Morgan
#CIS 261
#Course Project Phase 1

def getEmpName():
    empName = input("Enter Employee Name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter Hours Worked: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate in whole percentage: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    grossPay = hours * hourlyRate
    incomeTax = grossPay * taxRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay

def printInfo(empName, hours, hourlyRate, grossPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grossPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
    
def printTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"\nTotal Number of Employees: {totalEmployees}")
    print(f"Total Hours: {totalHours}")
    print(f"Total Gross Pay: {totalGrossPay}")
    print(f"Total Tax: {totalTax}")
    print(f"Total Net Pay: {totalNetPay}")
    
if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    
    while True:
        empName = getEmpName()
        if  (empName.upper() == "END"):
            break
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        grossPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        
        printInfo(empName, hours, hourlyRate, grossPay, taxRate, incomeTax, netPay)
        
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grossPay
        totalTax += incomeTax
        totalNetPay += netPay
        
    printTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)
    
          
