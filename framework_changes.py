def banner():
	display_banner = """
	Welcome to the NMC Assistance Framework.

	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Instructions:
	Make your selection at the prompts when requested
	"""
	print(display_banner)

def user_choice():
	second_banner = """
	Main Menu
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Please select from the following: 
	[1] - Incoming phone calls
	[2] - Jupiter 1 and 2 issues
	[3] - Jupiter 3 and FUSION issues
	[4] - KU issues
	[5] - Email template generator
	[6] - IGT and XCI
	[7] - ESCALATION PATHS 
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Type 'exit' to exit program. 
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	"""
	print(second_banner)
	selection = input("-> What is your selection : ")
	if selection.lower() == 'exit':
		return None
	else:
		return int(selection) 

def phone_calls():
	phone_instruct = """
	Gather the following:
	-The name of the caller and where are they calling from? [ex: John from FSS]
	-The SAN or SID of the device with the issue. (SAN = Jupiter; SID = KU)
	-The SERIAL number for the device OR device(s)
	-WHAT is the issue that is occuring? WHAT steps have been taken so far?
	-Single site calls may have STATE CODES or NMS CODES.
	-Create a ticket based on the provided information, then escalate to the 
	proper resources (CNE-GW, FUSION, SDG_Support, NLV, Etc.),
	"""
	print(phone_instruct) 

def jupiter1and2_issues():
	while True:
		jupiter_banner = """
		~~~
		Jupiter Issues Submenu: 
		[a] - Single site call
		[b] - Terminal Drops
		exit - exit Jupiter Issues Submenu
		"""
		print(jupiter_banner)
		choice = input("-> Jupiter Issues --> Your selection: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - Single site")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - Terminal Drops")
		else:
			print(f"Processing Jupiter Issue : {choice}")

def jupiter3_issues():
	while True:
		jupiter3_banner = """
		~~~
		Jupiter 3 Issues Submenu: 
		[a] - Single site call
		[b] - Terminal Drops
		exit - exit Jupiter 3 Issues Submenu
		"""
		print(jupiter3_banner)
		choice = input("-> Jupiter 3 Issues --> Your selection: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - Single site")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - Terminal Drops")
		else:
			print(f"Processing Jupiter 3 Issue : {choice}")

def ku_issues():
	while True:
		ku_banner = """
		~~~
		KU Issues Submenu: 
		[a] - Enterprise
		[b] - Timing and power
		[c] - VSAT down/Outage
		exit - exit KU Issues Submenu
		"""
		print(ku_banner)
		choice = input("-> KU Issues --> Your selection: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - Enterprise")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - Timing and Power")
		elif choice.lower() == 'c':
			print(f"\n --> {choice} - VSAT down/Outage")
		else:
			print(f"Processing KU Issue : {choice}")

def igt_issues():
	while True:
		igt_banner = """
		~~~
		IGT and XCI Issues Submenu: 
		[a] - IGT issue?
		[b] - XCI issue?
		exit - exit IGT/XCI Issues Submenu
		"""
		print(igt_banner)
		choice = input("-> IGT/XCI Issues --> Your selection: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - IGT Issues")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - XCI Issues")
		else:
			print(f"Processing IGT/XCI Issue : {choice}")

def emailer():
	email_banner = """
	----------------------
	Generic Email Template
	======================
	Instructions:
	(1) Enter the Salesforce case # (If generated, else press 'Enter'),
	(2) Enter the TEAM to contact (CNE-GW, SDG_Support, NI, Etc.)
	(3) Enter the DEVICE affected (J2ALB047HPAIGW1104, j3yumpr01host01, Etc.)
	(4) Enter the ALARM (Swap utilization, Critical Pings, GW Terminal Drops, Etc.)
	This will generate a Subject line and a email body to send.
	"""
	print(email_banner)

def template():
	while True:
		ticket_num = input("-> Salesforce case number: ")
		team_name = input("-> Team to escalate to: ")
		device_name = input("-> Device name that is alarming: ")
		alarm_decription = input("-> Alarm Decription: ")
	
		email_subject = f"{ticket_num} - {device_name} - {alarm_decription}"
		email_body = (
		f"Hello {team_name},\n\n"
		f"This email is to provide visibility on {device_name}, which is currently alarming within SL1."
		f"Alarm: {alarm_decription} \n\n\n"
		f"Please take the required actions to address this issue and relay the corrective actions to the NMC\n"
		f"Thank you very much!\n\n"
		f"Regards,\n\n"
		)
		
		print("\nEmail Subject and Body\n\n")
		print(f"{email_subject}\n")
		print(f"{email_body}")

		choice = input("-> Email Template finished --> Type 'exit' to return to main menu: ")
		if choice.lower() == 'exit':
			break
		else:
			print(f"Processing Jupiter Issue : {choice}")

def escalations():
	while True:
		escalations_banner = """
		~~~
		Escalation Path Submenu: 
		[a] - SDG_Support
		[b] - CNE_Team
		[c] - NI
		[d] - ESE
		[d] - EDSE
		exit - exit Escalations Path Submenu
		"""
		print(escalations_banner)
		choice = input("-> Escalations Issues --> Your selection: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - SDG Support")
			print("\n -Call 1(866)245-7059 for first tier.")
			print("\n -Call 1(831)402-5408 for escalations.")
			print("\n -Call Babu 1(240)328-8946 if all else fails ")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - CNE Team")
			print("\n -Gateway Engineers -> Dial ext:4140")
			print("\n -Aero Engineers -> Dial ext:4160")
			print("\n -All others -> Dial ext:5998, then follow the prompts")
		elif choice.lower() == 'c':
			print(f"\n --> {choice} - NI Team")
			print("\n Network Infrastructure -> Call centers are different based on time of day")
			print("\n -> From 0900 - 2100 hours EST - call ext:5809")
			print("\n -> From 2100 - 0900 hours EST - call ext:3972")
		elif choice.lower() == 'd':
			print(f"\n --> {choice} - ESE Team")
		elif choice.lower() == 'e':
			print(f"\n --> {choice} - EDSE Team")
		else:
			print(f"Processing Escalation Path : {choice}")

def main():
	banner()
	while True:
		choice = user_choice()
		if choice is None:
			print("Shutting down program.")
			break
		elif choice == 1:
			phone_calls()
		elif choice == 2:
			jupiter1and2_issues()
		elif choice == 3:
			jupiter3_issues()
		elif choice == 4:
			ku_issues()
		elif choice == 5:
			emailer()
			template()
		elif choice == 6:
			igt_issues()
		elif choice == 7:
			escalations()
		else:
			print("Processing bases on your choice -> ", choice)

if __name__ == "__main__":
	main()		

