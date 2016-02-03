list1 = [('files', 'FIL_ID,FIL_TEAM,FIL_FILE,FIL_SIZE'), ('logs', 'LOG_ID,LOG_IP,LOG_PERSON,LOG_data,LOG_text'), ('persons', 'PER_ID,PER_FIRSTH_NAME,PER_LAST_PASS,PER_EMAIL,PER_TEAM,PER_ACTIVE,PER_LEADER'), ('teams', 'TEAM_ID,TEAM_NAME,TEAM_PASS,TEAM_EMAIL,TEAM_PROJECT_NAME,TEAM_DESCRIPTION,TEAM_TYPE,TEAM_blocked,TEAM_BLOCKED_DATE,TEAM_SESSION')]

list2 = [[['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']], [['LOG_PERSON', '2015-02-13'], ['LOG_data', '50'], ['PER_EMAIL', 'PLN']]]

list3 = ['teams', 'files', 'logs', 'persons']


insertArray = []
insertArraySchema = []
valueList=""
insertString=""


for x in list3:
	for y in list1:
		if x is y[0]:
			insertArraySchema.append(y)
print(insertArraySchema)


for y in list2:
	insertString2=""
	for x in insertArraySchema:
		insertString=""
		insertValues=""
		for z in y:
			# print(z[0]+ "== "+x[1])
			if z[0] in x[1]:
				# print("weszlo")
				insertValues = insertValues+z[0]+"',"
				insertString=insertString+z[1]+"',"
		print(insertValues)
		insertValues=insertValues[0:-2]
		insertString=insertString[0:-2]
		insertString2 = "INSERT INTO "+x[0]+" ('"+insertValues+"') VALUES ('"+insertString+"')"
		insertArray.append(insertString2)

for x in insertArray:
	print(x)
		