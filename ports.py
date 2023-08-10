import random

portDict = {
    "DHCP": "67/68",
    "DNS": "53",
    "FTP": "20/21",
    "HTTP": "80/443",
    "IMAP": "143/993",
    "LDAP": "389/636",
    "MySQL": "3306",
    "NetBIOS": "137/139",
    "NTP": "123",
    "POP3": "110/955",
    "RDP": "3389",
    "SIP": "5060/5061",
    "SMB": "445",
    "SMTP": "25/587",
    "SNMP Query": "161",
    "SNMP Trap": "162",
    "SQLNet": "1521",
    "SQL Srv": "1433",
    "SSH": "22",
    "Telnet": "23",
    "TFTP": "69",
}

Acronyms = {
	"Core 1": {
		"AC" : "Alternating Current",
		"ADF" : "Automatic Document Feeder",
		"AHCI " : "Advanced Host Controller Interface",
		"APIPA" : "Automatic Private Internet Protocol Address",
		"BD" : "Blu-ray Disc",
		"BIOS" : "Basic Input Output System",
		"CDMA" : "Code Division Multiple Access (no SIM card networks)",
		"CMOS" : "Complimentary Metal-Oxide Semiconductor",
		"CPU" : "Central Processing Unit",
		"CSM" : "Compatibility Support Module",
		"DC" : "Direct Current",
		"DHCP" : "Dynamic Host Configuration Protocol",
		"DIMM" : "Dual-Inline Memory Module",
		"DMZ" : "Demilitarized Zone",
		"DNS" : "Domain Name Service or Server",
		"DRAM" : "Dynamic Random Access Memory",
		"DSL" : "Digital Subscriber Line",
		"DVI" : "Digital Visual (Video) Interface",
		"ECC" : "Error Correcting Code",
		"FOSS" : "Free Open Source Software",
		"FQDN" : "Fully Qualified Domain Name",
		"FRU" : "Field Replaceable Unit",
		"FTTP" : "Fiber to the Premises",
		"GSM" : "Global System for Mobiles (SIM card networks)",
		"HBA" : "Host Bus Adapter",
		"HDD" : "Hard Disk Drive",
		"HID" : "Human Interface Device",
		"IaaS" : "Infrastructure as a Service",
		"IDE" : "Integrated Drive Electronics",
		"IIS" : "Internet Information Services",
		"IMEI" : "International Mobile Equipment Identifier (used with GSM)",
		"IMSI" : "International Mobile Subscriber Identifier (used with GSM)",
		"JBOD" : "Just a Bunch of Discs",
		"KVM" : "Keyboard-Video-Mouse",
		"LAN" : "Local Area Network",
		"MDIX" : "Medium Dependent Interface Crossover",
		"MEID" : "Mobile Equipment Identifier (used with CDMA)",
		"MFA" : "Multifactor Authentication",
		"MIDI" : "Musical Instrument Digial Interface",
		"MIMO" : "Multiple Input Multiple Output (802.11n)",
		"MTBF" : "Mean Time Between Failures",
		"MU-MIMO" : "Multi-User, Multiple Input Multiple Output (802.11ac)",
		"NAS" : "Network Attached Storage",
		"NAT" : "Network Address Translation",
		"NFC" : "Near Field Communication",
		"NTLM" : "New Technology LAN Manager",
		"NVMe" : "Non-volatile Memory Express",
		"NVMHCI" : "Non-volatile Memory Host Contoller Interface",
		"OCR" : "Optical Character Recognition",
		"OSD" : "On-Screen Display",
		"PaaS" : "Platform as a Service",
		"PATA" : "Parallel Advanced Technology Attachment",
		"PCI" : "Peripheral Component Interconnect",
		"PCIe" : "PCI Express",
		"PnP" : "Plug and Play",
		"POST" : "Power On Self-Test",
		"PSK" : "Pre-shared Key",
		"PSU" : "Power Supply Unit",
		"RAID" : "Redundant Array of Independent (Inexpensive) Disks",
		"RAM" : "Random Access Memory",
		"RDPRA" : "Remote Desktop Protocol Restricted Admin",
		"RFB" : "Remote Frame Buffer",
		"ROM" : "Read Only Memory",
		"RSSI" : "Received Signal Strength Indicator",
		"S.M.A.R.T." : "Self Monitoring Analysis and Reporting Technology",
		"SaaS" : "Software as a Service",
		"SAN" : "Storage Area Network",
		"SAS" : "Serial Attached SCSI",
		"SATA" : "Serial Advanced Technology Attachment",
		"SCCM" : "System Center Configuration Manager",
		"SCSI" : "Small Computer Systems Interface",
		"SDRAM" : "Synchronous Dynamic Random Access Memory",
		"SO-DIMM" : "Small Outline Dual Inline Memory Module",
		"SOHO" : "Small Office Home Office",
		"SSD" : "Solid State Drive",
		"SSID" : "Service Set IDentifier",
		"TFT" : "Thin Film Transistor",
		"TN" : "Twisted Nematic",
		"TWAIN" : "Technology Without An Interesting Name",
		"UPnP" : "Universal Plug and Play",
		"UTM" : "Unified Threat Management",
		"VDE" : "Virtual Desktop Environment",
		"VDI" : "Virtual Desktop Infrastructure",
		"VGA" : "Video Graphics Array",
		"vim" : "Vi IMproved",
		"WDS" : "Windows Deployment Services",
		"WIA" : "Windows Imaging Acquisition",
		"WLAN" : "Wireless Local Area Network",
		"WoL" : "Wake-on-LAN",
		"WSUS" : "Windows Server Update Services"
	},
	"Core 2":
	{
		"ACE": "Access Control Entries",
		"ACL": "Access Control List",
		"AES": "Advanced Encryption Standard",
		"AP": "Access Point",
		"APIPA": "Automatic Private IP Address",
		"APK": "Andoid Package",
		"ARP": "Address Resolution Protocol",
		"AUP": "Acceptable Use Policy",
		"BIA": "Burned In Address",
		"BITS": "Background Intelligent Transfer Service",
		"BYOD": "Bring Your Own Device",
		"CA": "Certificate Authority",
		"CAN": "Campus Area Network",
		"CAPTCHA": "Completely Automated Public Turing test to tell Computers and Humans Apart",
		"CDFS": "Compact Disc File System",
		"CLI": "Command Line Interface",
		"CRL": "Certificate Revocation List",
		"CSIRT": "Computer Security Incident Response Team",
		"DC": "Domain Controller",
		"DDoS": "Distributed Denial of Service",
		"DHCP": "Dynamic Host Configuration Protocol",
		"DISM": "Deployment Image Servicing and Management",
		"DLP": "Data Loss Prevention",
		"DMZ": "Demilitarized Zone",
		"DNS": "Domain Name Service or Server",
		"DRM": "Digital Rights Management",
		"ECC": "Error Correcting Code",
		"EFS": "Encrypting File System",
		"EoL": "End of Life",
		"ESD": "Electrostatic Discharge",
		"EULA": "End User License Agreement",
		"ext": "Extended File System",
		"FAT": "File Allocation Table",
		"FQDN": "Fully Qualified Domain Name",
		"FTP": "File Transfer Protocol",
		"GDPR": "General Data Protection Regulation",
		"GPO": "Group Policy Object",
		"GPT": "GUID Partition Table",
		"GUI": "Graphical User Interface",
		"GUID": "Globally Unique Identifier",
		"HCL": "Hardware Compatibility List",
		"HDD": "Hard Disk Drive",
		"HFS": "Hierarchical File System",
		"HIPS": "Host Instrusion Prevention System",
		"HTTP": "Hypertext Transfer Protocol",
		"HTTPS": "Hypertext Transfer Protocol Secure (HTTP/SSL)",
		"I/O": "Input Output",
		"ICM": "Information Content Management",
		"ICT": "Information Communication Technology",
		"IDS": "Intrusion Detection System",
		"IEEE": "Institute of Electrical and Electronics Engineers",
		"IMAP": "Internet Mail Access Protocol",
		"IP": "Internet Protocol",
		"IPS": "Intrusion Prevention System",
		"IRP": "Incident Response Plan",
		"ISP": "Internet Service Provider",
		"ITIL": "Information Technology Infrastructure Library",
		"KVM": "Keyboard-Video-Mouse",
		"LAN": "Local Area Network",
		"LDAP": "Lightweight Directory Access Protocol",
		"LPL": "Windows Logo'd Product List",
		"MAC": "Media Access Control",
		"MAN": "Metropolitan Area Network",
		"MBR": "Master Boot Record",
		"MBSA": "Microsoft Baseline Security Analyzer",
		"MDM": "Mobile Device Management",
		"MFA": "Multifactor Authentication",
		"MIME": "Multipurpose Internet Mail Exchange",
		"MITM": "Man-in-the-Middle",
		"MMC": "Microsoft Management Console",
		"MSDS": "Material Safety Data Sheet",
		"MSTSC": "Microsoft Terminal Services Client",
		"MTBF": "Mean Time Between Failures",
		"NAC": "Network Access Control",
		"NAT": "Network Address Translation",
		"NFC": "Near Field Communication",
		"NFS": "Network File System",
		"NTFS": "New Technology File System",
		"OS": "Operating System",
		"OSI": "Open Systems Interconnect",
		"OU": "Organizational Unit",
		"PAN": "Personal Area Network",
		"PAT": "Port Address Translation",
		"PCI": "Payment Card Industry",
		"PHI": "Personal Health Information",
		"PII": "Personally Identifiable Information",
		"PKI": "Public Key Infrastructure",
		"PMF": "Protected Management Frames",
		"PnP": "Plug and Play",
		"PoLP": "Principle of Least Privilege",
		"POP3": "Post Office Protocol 3",
		"POST": "Power On Self-Test",
		"PSU": "Power Supply Unit",
		"PXE": "Pre-execution Environment",
		"QoS": "Quality of Service",
		"RADIUS": "Remote Authentication Dial-in User Service",
		"RAID": "Redundant Array of Independent Discs",
		"RAM": "Random Access Memory",
		"RDP": "Remote Desktop Protocol",
		"RFID": "Radio Frequency Identification",
		"RSoP": "Resultant Set of Policies",
		"S.M.A.R.T.": "Self-Monitorning, Analysis, and Reporting Technology",
		"SAM": "Security Accounts Manager",
		"SFC": "System File Checker",
		"SMTP": "Simple Mail Transfer Protocol",
		"SNMP": "Simple Network Management Protocol",
		"SOP": "Standard Operating Procedure",
		"SSD": "Solid State Drive",
		"SSH": "Secure Shell",
		"SSL": "Secure Socket Layer",
		"SSO": "Single Sign-on",
		"TACACS": "Terminal Access Controller Access-Control System",
		"TCP": "Transmission Control Protocol",
		"TKIP": "Temporal Key Integrity Protocol",
		"TLS": "Transport Layer Security",
		"TPM": "Trusted Platform Module",
		"UAC": "User Account Control",
		"UDP": "User Datagram Protocol",
		"UEFI": "Unified Extensible Firmware Interface",
		"UNC": "Universal Naming Convention",
		"UPnP": "Universal Plug and Play",
		"UPS": "Uniterruptible Power Supply",
		"UTM": "Unified Threat Management",
		"VLAN": "Virtual Local Area Network",
		"VM": "Virtual Machine",
		"VNC": "Virtual Network Computing",
		"VoIP": "Voice of Internet Protocol",
		"VPN": "Virtual Private Network",
		"WAN": "Wide Area Network",
		"WAP": "Wireless Access Protocol/Wireless Access Point",
		"WDS": "Windows Deployment Services",
		"WEP": "Wired Equivalent Privacy",
		"WLAN": "Wireless Local Area Network",
		"WPA": "Wireless Protected Access",
		"WPA2": "WiFi Protected Access 2",
		"WPS": "WiFi Protected Setup",
		"WWAN": "Wireless Wide Area Network",
		"XML": "Extensible Markup Language"
	}
}

aPlusTerms = {
	"AC": "Alternating Current",
	"ADF": "Automatic Document Feeder",
	"AHCI ": "Advanced Host Controller Interface",
	"APIPA": "Automatic Private IP Address",
	"BD": "Bluray Disc",
	"BIOS": "Basic Input Output System",
	"CDMA": "Code Division Multiple Access (no SIM card networks)",
	"CMOS": "Complimentary Metal Oxide Semiconductor",
	"CPU": "Central Processing Unit",
	"CSM": "Compatibility Support Module",
	"DC": "Domain Controller",
	"DHCP": "Dynamic Host Configuration Protocol",
	"DIMM": "Dual Inline Memory Module",
	"DMZ": "Demilitarized Zone",
	"DNS": "Domain Name Service or Server",
	"DRAM": "Dynamic Random Access Memory",
	"DSL": "Digital Subscriber Line",
	"DVI": "Digital Visual (Video) Interface",
	"ECC": "Error Correcting Code",
	"FOSS": "Free Open Source Software",
	"FQDN": "Fully Qualified Domain Name",
	"FRU": "Field Replaceable Unit",
	"FTTP": "Fiber to the Premises",
	"GSM": "Global System for Mobiles (SIM card networks)",
	"HBA": "Host Bus Adapter",
	"HDD": "Hard Disk Drive",
	"HID": "Human Interface Device",
	"IaaS": "Infrastructure as a Service",
	"IDE": "Integrated Drive Electronics",
	"IIS": "Internet Information Services",
	"IMEI": "International Mobile Equipment Identifier (used with GSM)",
	"IMSI": "International Mobile Subscriber Identifier (used with GSM)",
	"JBOD": "Just a Bunch of Discs",
	"KVM": "Keyboard Video Mouse",
	"LAN": "Local Area Network",
	"MDIX": "Medium Dependent Interface Crossover",
	"MEID": "Mobile Equipment Identifier (used with CDMA)",
	"MFA": "Multifactor Authentication",
	"MIDI": "Musical Instrument Digial Interface",
	"MIMO": "Multiple Input Multiple Output (802.11n)",
	"MTBF": "Mean Time Between Failures",
	"MU-MIMO": "Multi User, Multiple Input Multiple Output (802.11ac)",
	"NAS": "Network Attached Storage",
	"NAT": "Network Address Translation",
	"NFC": "Near Field Communication",
	"NTLM": "New Technology LAN Manager",
	"NVMe": "Nonvolatile Memory Express",
	"NVMHCI": "Nonvolatile Memory Host Contoller Interface",
	"OCR": "Optical Character Recognition",
	"OSD": "On Screen Display",
	"PaaS": "Platform as a Service",
	"PATA": "Parallel Advanced Technology Attachment",
	"PCI": "Payment Card Industry",
	"PCIe": "PCI Express",
	"PnP": "Plug and Play",
	"POST": "Power On Self Test",
	"PSK": "Pre shared Key",
	"PSU": "Power Supply Unit",
	"RAID": "Redundant Array of Independent Discs",
	"RAM": "Random Access Memory",
	"RDPRA": "Remote Desktop Protocol Restricted Admin",
	"RFB": "Remote Frame Buffer",
	"ROM": "Read Only Memory",
	"RSSI": "Received Signal Strength Indicator",
	"S.M.A.R.T.": "Self Monitorning, Analysis, and Reporting Technology",
	"SaaS": "Software as a Service",
	"SAN": "Storage Area Network",
	"SAS": "Serial Attached SCSI",
	"SATA": "Serial Advanced Technology Attachment",
	"SCCM": "System Center Configuration Manager",
	"SCSI": "Small Computer Systems Interface",
	"SDRAM": "Synchronous Dynamic Random Access Memory",
	"SO-DIMM": "Small Outline Dual Inline Memory Module",
	"SOHO": "Small Office Home Office",
	"SSD": "Solid State Drive",
	"SSID": "Service Set IDentifier",
	"TFT": "Thin Film Transistor",
	"TN": "Twisted Nematic",
	"TWAIN": "Technology Without An Interesting Name",
	"UPnP": "Universal Plug and Play",
	"UTM": "Unified Threat Management",
	"VDE": "Virtual Desktop Environment",
	"VDI": "Virtual Desktop Infrastructure",
	"VGA": "Video Graphics Array",
	"vim": "Vi IMproved",
	"WDS": "Windows Deployment Services",
	"WIA": "Windows Imaging Acquisition",
	"WLAN": "Wireless Local Area Network",
	"WoL": "Wake on LAN",
	"WSUS": "Windows Server Update Services",
	"ACE": "Access Control Entries",
	"ACL": "Access Control List",
	"AES": "Advanced Encryption Standard",
	"AP": "Access Point",
	"APK": "Andoid Package",
	"ARP": "Address Resolution Protocol",
	"AUP": "Acceptable Use Policy",
	"BIA": "Burned In Address",
	"BITS": "Background Intelligent Transfer Service",
	"BYOD": "Bring Your Own Device",
	"CA": "Certificate Authority",
	"CAN": "Campus Area Network",
	"CAPTCHA": "Completely Automated Public Turing test to tell Computers and Humans Apart",
	"CDFS": "Compact Disc File System",
	"CLI": "Command Line Interface",
	"CRL": "Certificate Revocation List",
	"CSIRT": "Computer Security Incident Response Team",
	"DDoS": "Distributed Denial of Service",
	"DISM": "Deployment Image Servicing and Management",
	"DLP": "Data Loss Prevention",
	"DRM": "Digital Rights Management",
	"EFS": "Encrypting File System",
	"EoL": "End of Life",
	"ESD": "Electrostatic Discharge",
	"EULA": "End User License Agreement",
	"ext": "Extended File System",
	"FAT": "File Allocation Table",
	"FTP": "File Transfer Protocol",
	"GDPR": "General Data Protection Regulation",
	"GPO": "Group Policy Object",
	"GPT": "GUID Partition Table",
	"GUI": "Graphical User Interface",
	"GUID": "Globally Unique Identifier",
	"HCL": "Hardware Compatibility List",
	"HFS": "Hierarchical File System",
	"HIPS": "Host Instrusion Prevention System",
	"HTTP": "Hypertext Transfer Protocol",
	"HTTPS": "Hypertext Transfer Protocol Secure (HTTP/SSL)",
	"I/O": "Input Output",
	"ICM": "Information Content Management",
	"ICT": "Information Communication Technology",
	"IDS": "Intrusion Detection System",
	"IEEE": "Institute of Electrical and Electronics Engineers",
	"IMAP": "Internet Mail Access Protocol",
	"IP": "Internet Protocol",
	"IPS": "Intrusion Prevention System",
	"IRP": "Incident Response Plan",
	"ISP": "Internet Service Provider",
	"ITIL": "Information Technology Infrastructure Library",
	"LDAP": "Lightweight Directory Access Protocol",
	"LPL": "Windows Logo'd Product List",
	"MAC": "Media Access Control",
	"MAN": "Metropolitan Area Network",
	"MBR": "Master Boot Record",
	"MBSA": "Microsoft Baseline Security Analyzer",
	"MDM": "Mobile Device Management",
	"MIME": "Multipurpose Internet Mail Exchange",
	"MITM": "Man in the Middle",
	"MMC": "Microsoft Management Console",
	"MSDS": "Material Safety Data Sheet",
	"MSTSC": "Microsoft Terminal Services Client",
	"NAC": "Network Access Control",
	"NFS": "Network File System",
	"NTFS": "New Technology File System",
	"OS": "Operating System",
	"OSI": "Open Systems Interconnect",
	"OU": "Organizational Unit",
	"PAN": "Personal Area Network",
	"PAT": "Port Address Translation",
	"PHI": "Personal Health Information",
	"PII": "Personally Identifiable Information",
	"PKI": "Public Key Infrastructure",
	"PMF": "Protected Management Frames",
	"PoLP": "Principle of Least Privilege",
	"POP3": "Post Office Protocol 3",
	"PXE": "Preexecution Environment",
	"QoS": "Quality of Service",
	"RADIUS": "Remote Authentication Dial in User Service",
	"RDP": "Remote Desktop Protocol",
	"RFID": "Radio Frequency Identification",
	"RSoP": "Resultant Set of Policies",
	"SAM": "Security Accounts Manager",
	"SFC": "System File Checker",
	"SMTP": "Simple Mail Transfer Protocol",
	"SNMP": "Simple Network Management Protocol",
	"SOP": "Standard Operating Procedure",
	"SSH": "Secure Shell",
	"SSL": "Secure Socket Layer",
	"SSO": "Single Sign on",
	"TACACS": "Terminal Access Controller Access Control System",
	"TCP": "Transmission Control Protocol",
	"TKIP": "Temporal Key Integrity Protocol",
	"TLS": "Transport Layer Security",
	"TPM": "Trusted Platform Module",
	"UAC": "User Account Control",
	"UDP": "User Datagram Protocol",
	"UEFI": "Unified Extensible Firmware Interface",
	"UNC": "Universal Naming Convention",
	"UPS": "Uniterruptible Power Supply",
	"VLAN": "Virtual Local Area Network",
	"VM": "Virtual Machine",
	"VNC": "Virtual Network Computing",
	"VoIP": "Voice of Internet Protocol",
	"VPN": "Virtual Private Network",
	"WAN": "Wide Area Network",
	"WAP": "Wireless Access Point",
	"WEP": "Wired Equivalent Privacy",
	"WPA": "Wireless Protected Access",
	"WPA2": "WiFi Protected Access 2",
	"WPS": "WiFi Protected Setup",
	"WWAN": "Wireless Wide Area Network",
	"XML": "Extensible Markup Language"
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
			with open("needsworkPorts.csv", "r") as infile:
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

		with open("needsworkPorts.csv", "w") as outfile:
			outfile.write(needswork[:-1])

		print(f"You got {correctAnswers} out of {numKeys} correct!")

		quit = input("Press <Enter> to try again or 'q' to quit: ")

		if quit == 'q':
			break


def QuizAcronyms():
	while True:
		keys = list(aPlusTerms.keys())
		numKeys = len(keys)
		correctAnswers = 0

		incorrectKeys = []
		needsPractice = []
		round = 1

		try:
			with open("needsworkAcronyms.csv", "r") as infile:
				needsPractice = infile.read().split(",")
		except:
			pass

		if needsPractice == [""]:
			needsPractice = []

		if len(needsPractice) > 0:
			resp = input("Would you like to test the items that need improvement? ")

			if len(resp) > 0 and resp[0] == 'y':
				keys = needsPractice
			else:
				needsPractice = []

		print("Enter the correct name for the given acronym...")

		while len(keys) > 0:
			selectedKey = keys[random.randint(0, len(keys)-1)]
			keys.remove(selectedKey)

			answer = input(f"{selectedKey}: ")

			if answer.lower() == aPlusTerms[selectedKey].lower():
				print("Correct!\n")
				if selectedKey not in needsPractice:
					correctAnswers += 1
			else:
				print(f"Wrong, the correct answer was {aPlusTerms[selectedKey]}.\n")
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

		with open("needsworkAcronyms.csv", "w") as outfile:
			outfile.write(needswork[:-1])

		print(f"You got {correctAnswers} out of {numKeys} correct!")

		quit = input("Press <Enter> to try again or 'q' to quit: ")

		if quit == 'q':
			break


if __name__ == "__main__":
	response = input("Would you like to test ports(1) or acronyms(2)? ")

	if response == '1':
		QuizPorts()

	if response == '2':
		QuizAcronyms()