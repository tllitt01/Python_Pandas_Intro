#PyRamen
from pathlib import Path
import csv

#set path for menu and sales data
menu_path = ('menu_data.csv')
sales_path = ('sales_data.csv')

#initialize menu and sales list and report dictionary
menu = []
sales = []
report = {}

#passing menu file through csvreader, skipping header
with open (menu_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csv_reader)

#adding rows to menu list    
    for row in csv_reader:
        menu.append(row)

#passing sales file through csvreader, skipping header   
with open (sales_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)    

#adding rows to sales list
    for row in csvreader:
        sales.append(row)

#adding variable names to columns
#creating keys in dictionary
for row in sales:
    quantity = row[3]
    sales_item = row[4]

    if sales_item not in report:
            report[sales_item] = {"01-count":0,
                                 "02-revenue":0,
                                 "03-cogs":0,
                                 "04-profit":0
                                 }

#adding variable names to columns in lists
#calculating count, revenue, cogs, profit
for row in sales:
    quantity = row[3]
    sales_item = row[4]

    for row in menu:
        menu_item = row[0]
        price = row[3]
        cost = row[4]

        if sales_item in menu_item:
            report[sales_item]["01-count"] += int(quantity)
            report[sales_item]["02-revenue"] += (int(price) * int(quantity))
            report[sales_item]["03-cogs"] += (int(cost) * int(quantity))
            report[sales_item]["04-profit"] += (int(price)-int(cost)) * int(quantity)
        else:
            print(f"{sales_item} does not match {menu_item}")


#creating output and writing report to it
output = 'pyramenhw.txt'

with open(output, 'w') as file:
    for key in report:
        file.write(f"{key} {report[key]}\n")
    
    

             

         
                 
                    
                    
                   
                

            
            
            


        



    
           

        

              
                    
    
    

    
    

                



            
            
                                
    




#set output
#output = 'pyramenhw.txt'

#with open(output, 'w') as file:
    #file.write(report)

        
        

    
  
        
    
        
            
    
        
   
                    
            
                
        
        

             
     
            
            


        
 
        
        



    

    


        

        
        

    
  
        
    
        
            
    
        
   
                    
            
                
        
        

             
     
            
            
