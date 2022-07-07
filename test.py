#List of dictionaries

voting_data = []

#Add each dictionary to list

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#Add El Paso to second position

voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})

#Remove Arapahoe

voting_data.pop(0)

#Make Denver the third item, make Jefferson the second item

voting_data[1] , voting_data[2] = voting_data[2] , voting_data[1]

#Add Arapahoe

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

print(voting_data)
