#Christopher Morgan
#CIS 261
#Course Project Phase 2

from datetime import datetime

FILENAME = "Employees.txt"

def getDatesWorked():
    while True:
        date_str = input("Enter start date for report (MM-DD-YYYY): ")
        try:
            fromDate = datetime.strptime(date_str, "%m-%d-%Y")
        except ValueError:
            print("Incorrect data format. Please try again")
            print()
            continue
        break
    
    while True:
        date_str = input("Enter end date for report (MM-DD-YYYY): ")
        try:
            toDate = datetime.strptime(date_str, "%m-%d-%Y")
        except ValueError:
            print("Incorrect data format. Please try again")
            print()
        if toDate <= fromDate:
            print("To date must be after from date. Try again.")
            print()
        else:
            break
    return fromDate, toDate

def getEmpName():
    empName = input("Enter Employee Name or END to finish entries: ")
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

def saveinfo(from_date,to_date,name,hours,hourly_rate,tax_rate):
    with open(FILENAME, 'a') as EmpInfo:
        EmpInfo.write(f"{from_date}|{to_date}|{name}|{hours}|{hourly_rate}|{tax_rate}\n")

def printInfo(employeeDetails):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    empTotals = {}
    
    with open(FILENAME, "r") as EmpFile:                
        
        while True:
            runDate = input("Enter star date for report (MM-DD-YYYY) or ALL for complete list in file: ")
            if (runDate.upper() == "ALL"):
                break
            try:
                runDate = datetime.strptime(runDate, "%m-%D-%Y")
                break
            except ValueError:
                print("Incorrect date format. Please try again.")
                print()
                continue
        while True:
            try:
                empDetail = EmpFile.readline()
            except:
                print("Cannot read file correctly. Try Again.")
            if not empDetail:
                print("No Information Available.")
                break
            empDetail = empDetail.rstrip("\n")
            empList = empDetail.split("|")             
            fromDate = empList[0]
            if (str(runDate).upper() != "ALL"):
                checkDate = datetime.strptime(fromDate, "%m-%d-%Y")
                if (checkDate < runDate):
                    continue
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
            DetailsPrinted = True
            if (DetailsPrinted):
                printTotals (empTotals)
            else:
                print("No details to print.")
 
def printTotals(empTotals):
    print(f"\nTotal Number of Employees: {empTotals['totEmp']}")
    print(f"Total Hours: {empTotals['totHours']}")
    print(f"Total Gross Pay: {empTotals['totGross']}")
    print(f"Total Tax: {empTotals['totTax']}")
    print(f"Total Net Pay: {empTotals['totNet']}")
    
if __name__ == "__main__":
#employeeDetails = []
    empTotals = {}
    DetailsPrinted = False
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        fromDate, toDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        fromDate = fromDate.strftime("%m-%d-%Y")
        toDate = toDate.strftime("%m-%d-%Y")
        saveinfo(fromDate,toDate,empName,hours,hourlyRate,taxRate)
        
        
    printInfo(DetailsPrinted)
        