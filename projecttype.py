import csv

with open('Temporary_Art_Program', 'r') as datafile:
	parsed_csv = csv.reader(datafile)

	for a_row in parsed_csv:

	project_type = a_row[4]

	if artist_name == 'Artist'
			continue

	if artist_name in total_counter:
			pass

	else:
		total_counter{artist_name} = {}

	project_type = a_row[7]

	if project_type == 'Project Type':
			continue


	if project_type in total_counter{artist_name}:
		total_counter{artist_name}[project_type] = total_counter{artist_name}[project_type] + 1

	else:
		total_counter{artist_name}[project_type] = 1

print (total_counter)


