import random

portDict = {
    "FTP": "20/21",
    "SSH": "22",
    "Telnet": "23",
    "SMTP": "25/587",
    "DNS": "53",
    "DHCP": "67/68",
    "HTTP": "80",
    "HTTPS": "443",
    "LDAP": "389",
    "POP3": "110/955",
    "IMAP": "143/993",
    "NetBIOS": "137/139",
    "SMB": "445",
    "SNMP Query": "161",
    "SNMP Trap": "162",
    "LDAP": "389",
    "RDP": "3389",
}

def QuizPorts():
	while True:
		keys = list(portDict.keys())
		numKeys = len(keys)
		correctAnswers = 0

		incorrectKeys = []
		needsPractice = []
		round = 1

		try:
			with open("needswork.csv", "r") as infile:
				needsPractice = infile.read().split(",")
		except:
			pass

		if needsPractice == [""]:
			needsPractice = []

		if len(needsPractice) > 0:
			resp = input("Would you like to test the items that need improvement? ")

			if resp[0] == 'y':
				keys = needsPractice
			else:
				needsPractice = []

		print("Enter the correct port number for the given service...")

		while len(keys) > 0:
			selectedKey = keys[random.randint(0, len(keys)-1)]
			keys.remove(selectedKey)

			answer = input(f"{selectedKey}: ")

			if answer in portDict[selectedKey].split("/"):
				print("Correct!\n")
				if selectedKey not in needsPractice:
					correctAnswers += 1
			else:
				print(f"Wrong, the correct answer was {portDict[selectedKey]}.\n")
				incorrectKeys.append(selectedKey)
				if selectedKey not in needsPractice:
					needsPractice.append(selectedKey)

			if len(keys) == 0:
				if round == 1:
					keys = incorrectKeys
					incorrectKeys = []
					round = 2
				else:
					if len(needsPractice) > 0:
						print("Here are the items you should practice:")
						print(needsPractice)
						print()

					else:
						print("Congratulations, you got them all correct!")

		needswork = ""
		for i in needsPractice:
			needswork += i + ","

		with open("needswork.csv", "w") as outfile:
			outfile.write(needswork[:-1])

		print(f"You got {correctAnswers} out of {numKeys} correct!")

		quit = input("Press <Enter> to try again or 'q' to quit: ")

		if quit == 'q':
			break

if __name__ == "__main__":
	QuizPorts()