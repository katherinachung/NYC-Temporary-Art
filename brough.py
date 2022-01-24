import csv

with open ('Temporary_Art_Program.csv', 'r') as datafile:

	processed_csv = csv.reader (datafile)

	line_counter=0

	with open ('Temporary_Art_Program.csv','w') as csvout:

		writeable_csv = csv.writer(csvout)

		for row in processed_csv:

			print (line_counter)

			if line_counter==0:

				writeable_csv.writerow(row)

			if row [7] == 'Brooklyn' or row [7] == 'Manhattan' or row [7] == 'Queens' or row [7] == 'Staten Island' or row [7] == 'Bronx':

				writeable_csv.writerow(row)

			line_counter +=1