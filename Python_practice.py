voting_data = []


voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data[1] = {"county":"El Paso", "registered_voters": 461149}

print(voting_data)

voting_data.pop(0)