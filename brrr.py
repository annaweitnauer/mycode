#Introduction
print("----------------- ********INFO ONLY******** -----------------")
print()
print("About this program:")
print("This was developed to help calculate the most useful ratios ") 
print("and metrics to consider when evaluating a property for ")
print("investment purposes.")
print("Read more at the article from where the calculations come: ")
print("https://www.biggerpockets.com/blog/2016-01-13-top-8-real-estate-calculations?utm_source=newsletter")
print()
print("----------------- ********INFO ONLY******** -----------------")
print()
print()

#Assumptions
vacancyRate = .05

#Purchase Price
purchasePrice = input("Enter the purchase price (in thousands): ")
purchasePrice_float = float(purchasePrice)*1000
print("The purchase price is $", purchasePrice_float, sep ='')

#Rehab Cost
rehabCost = input("Enter the cost to rennovate (in thousands): ")
rehabCost_float = float(rehabCost)*1000
print("The rehabilitation cost is $", rehabCost_float, sep ='')

#Expected Rental Income
monthlyRent = input("Enter the expected monthly rent to be collected from tenant (in thousands): ")
monthlyRent_float = float(monthlyRent)*1000
noi_float = round(monthlyRent_float*12*(1-vacancyRate),2)
print("The expected net operating income (with an assumed 5% vacancy) is $", noi_float, sep ='')

#Total Costs (rennovation and purchase price)
cost = rehabCost_float+purchasePrice_float
capRate = round(noi_float/(cost),6)
print("The Cap Rate is ", round((capRate)*100,2), "%", sep ='')

#Rent/Cost
rentByCost = round(monthlyRent_float/cost,6)
print("The Rent/Cost is ", round((rentByCost)*100,2), "%", sep ='')

#Gross Yield
grossYield = round((monthlyRent_float*12)/cost,6)
print("The Gross Yield is ", round((grossYield)*100,2), "%", sep ='')

#Guidelines for Rent/Cost and Cap Rate
if rentByCost*100 < 1:
   print("Rent/Cost is less than 1; do not advise purchase.")
else:
  print ("Rent/Cost is acceptable (as it is greater than 1%).")
if capRate*100 < 8:
   print("Cap rate is less than 8; do not advise purchase.")
else:
  print("Cap rate is acceptable (as it is greater than 8%).")

#Debt Service Amount
debtService = input("Enter the monthly mortgage amount = principal + interest (in thousands): ")
debtService_float = float(debtService)*1000
print("The debt service amount annually is $", debtService_float*12, sep ='')

#Debt Service Ratio
debtServiceRatio = round(noi_float/(debtService_float*12),6)
print("The debt service ratio is ", round(debtServiceRatio,2))

#Guidelines for Debt Service Ratio
if debtServiceRatio < 1.2:
   print("Debt service ratio is less than 1.2; do not advise purchase.")
else:
  print("Debt service ratio is acceptable (as it is greater than 1.2).")

#Cash Flow/Cash in Deal
cashFlow = noi_float-(debtService_float*12)
cashInDeal = input("Enter the cash into deal amount (in thousands): ")
cashInDeal_float = float(cashInDeal)*1000
print("Cash into deal amount is $", cashInDeal_float, sep ='')
cashOnCash = round(cashFlow/cashInDeal_float,6)
print("Cash on Cash is ", round((cashOnCash)*100,2), "%", sep='')

#70% rule
afterRepairValue = input("What do you expect the after repair value to be (in thousands)? ")
afterRepairValue_float = float(afterRepairValue)*1000
print("Strike price is $", ((.7*afterRepairValue_float)-rehabCost_float), sep ='')

#Ask user if Export to file is wanted
exportAnswer = input("Do you want to save this information/property to a file for export? ")
if exportAnswer in ['y','yes', 'Yes', 'YES', 'Y']:
  nameOfFile = input("What do you name your file? ")
  nameOfProperty = input("Within the file a column will be given for the name of this property. What do you want to use as the identifier for this property? ")
if exportAnswer in ['n','no', 'No', 'NO', 'N']:
  print("End of program")

print()
print("----------------- ********INFO ONLY******** -----------------")
print()
print("If the file is not seen in the left sidebar as named, ")
print("then perhaps you are not running this from within repl.it. ")
print("Please go to https://repl.it/@AnnaWeitnauer/BRRR ")
print("and run the program by pressing the \"run >\" button at the ")
print("top middle of the screen.")
print()
print("----------------- ********INFO ONLY******** -----------------")


#Create the file with data
import csv
with open(nameOfFile+".csv",'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(["Name of Property", "Purchase Price", "Rehabilitation Cost", "Expected Monthly Rent", "Net Operating Income (assumed 5% vacancy)", "Cap Rate (%)", "Rent/Cost (%)", "Gross Yield (%)", "Monthly Mortgage Amount = Principal + Interest", "Debt Service Annual Amount", "Debt Service Ratio", "Cash into deal Amount", "Cash on Cash (%)", "After Repair Value", "Strike Price"])
  writer.writerow([nameOfProperty, purchasePrice_float, rehabCost_float, monthlyRent_float, noi_float, capRate, rentByCost, grossYield, debtService_float, debtService_float*12, debtServiceRatio, cashInDeal_float, cashOnCash, afterRepairValue_float, ((.7*afterRepairValue_float)-rehabCost_float)])
