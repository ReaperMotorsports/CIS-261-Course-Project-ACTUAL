#Christopher Morgan
#CIS 261
#Course Project Phase 2

def getDatesWorked():
    fromDate = input("Please enter start date (MM/DD/YYYY): ")
    toDate = input("Please enter end date (MM/DD/YYYY): ")
    return fromDate, toDate

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

def printInfo(employeeDetails):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    
    for empList in employeeDetails:
        fromDate = empList[0]
        toDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        grossPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, toDate, empName, f"{hours:,.2f}", f"{grossPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grossPay
        totalTax += incomeTax
        totalNetPay += netPay
        
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
 
def printTotals(empTotals):
    print(f"\nTotal Number of Employees: {empTotals['totEmp']}")
    print(f"Total Hours: {empTotals['totHours']}")
    print(f"Total Gross Pay: {empTotals['totGross']}")
    print(f"Total Tax: {empTotals['totTax']}")
    print(f"Total Net Pay: {empTotals['totNet']}")
    
if __name__ == "__main__":
   employeeDetails = []
   empTotals = {}    
   while True:
        empName = getEmpName()
        if  (empName.upper() == "END"):
             break
        fromDate, toDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, toDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        employeeDetails.append(empDetail)
    
   printInfo(employeeDetails)
   printTotals(empTotals)
        
        