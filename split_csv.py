
#Use with file in directory where csv file stored
import csv
import os

#get current working directory
path=os.getcwd()
print(path)
print(os.listdir(path))
#select file from printed list above
file = input("Please type file name from list above: ")

#open file for to read and delete products with 0 quantity. 
with open(path+'\\'+ file) as csvfile:
	reader = csv.DictReader(csvfile,delimiter=';') #
	headers = reader.fieldnames
	print(headers)
    #select column from list above
    col = input("Please type column name from list above: ")
	#identify index of column
    index_col= headers.index(col)
# code - create copy of csv goods with quantuty not equal 0
	with open(path+'\\new_'+ file, 'w', newline='') as outfile:
		writer = csv.DictWriter(outfile, fieldnames=headers, delimiter=';', extrasaction='ignore')
		writer.writeheader()
		for row in reader:	
			if row[headers[index_col]] != '0': 
				writer.writerows([row])

#split csv file created  
import pandas as pd   #  conda install pandas | pip install pandas

df = pd.read_csv(path+'\\new_'+ file, encoding="cp1251", delimiter=";", index_col=False)

_ = df.groupby("Бренд").apply(lambda x: x.to_csv(fr"{path}\\{x.name}.csv", index=False))