############################################################### Intro Banner Only.
def banner():
	display_banner = """
	Welcome to the NMC Assistance Framework.

	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Instructions:
	Make your selection at the prompts when requested
	"""
	print(display_banner)
############################################################### Main menu - User choice.
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
############################################################### Submenu - Incoming Phone calls.
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
############################################################### Submenu - Jupiter 1 and 2 Issues. 
def jupiter1and2_issues():
	while True:
		jupiter_banner = """
		~~~
		Jupiter Issues Submenu: 
		[a] - Single site call
		[b] - Terminal Drops
		[c] - BGP Peers
		[d] - Move Allows
		exit - exit Jupiter Issues Submenu
		"""
		print(jupiter_banner)
		choice = input("-> Jupiter Issues --> Your selection: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a': 	##########Single site calls
			print(f"\n --> {choice} - Single site")
			print("\nYou are likely on a phone call....")
			print("\nGather the following during this call: ")
			print("The site SAN, and the SERIAL numbers of the terminal(s) -> There may be more than one")
			print("Log into DSS (hns-unsername:PIN+RSA) and navigate the sidebar to 'Jupiter Dashboard'")
			print("Select 'Jupiter Dashboard', then enter the SAN or the ESN of the site into DSS to gather more information,")
			print("such as, Radio_ESN, Gateway_IDs, Beam_IDs for your ticket and for engineers")
			print("Depending on what the Single site issue is, this will affect your escalation path")
			print("Is the terminal stuck in activation stages? -> Escalate to CNE-NMS")
			print("Is the terminal ")
		elif choice.lower() == 'b':		##########Terminal Drops
			print(f"\n --> {choice} - Terminal Drops")
		elif choice.lower() == 'c':		##########BGP Peering
			print(f"\n --> {choice} - BGP Peering Issues")
			print(" Within SL1, note the interface and BGP neighbour")
			print(" If the link is a backbone link to a carrier ISP,")
			print(" then escalate to the appropriate carrier\n")
			print(" Level3|CenturyLink|Lumen - Login portal")
			print(" -> controlcenter.lumen.com/enterprise/dashboard\n")
			print("```")
			print("Verizon - Login Portal")
			print(" -> enterprise.verizon.com/public/index.html#/repairsqf/tickets/find\n")
			print("```")
			print("\nGTT Communitcation - Login Portal")
			print(" -> ethervision.gtt.net/sign-in\n")
			print("```")
		else:
			print(f"Processing Jupiter 1/2 Issue : {choice}")
############################################################### Submenu - Jupiter 3 Issues.
def jupiter3_issues():
	while True:
		jupiter3_banner = """
		~~~
		Jupiter 3 Issues Submenu: 
\n---> If tasked with a Jupiter 3 issue, IMMEDIATELY escalate to CNE-GW Engineers! <---
              ---> This happens prior to ticket creation, FULL STOP! <---\n

		[a] - Single site call
		[b] - Terminal Drops
		[c] - Terminal Move Allows
		exit - exit Jupiter 3 Issues Submenu
		"""
		print(jupiter3_banner)
		choice = input("-> Jupiter 3 Issues --> Your selection: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - Single site\n")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - Terminal Drops\n")
		elif choice.lower() == 'c':
			print(f"\n --> {choice} - Terminal Move Allows\n")
			print("Open Putty and 'ssh' into 172.16.193.11\n")
			print("Login: nmcuser:nmcuser123!@#\n")
			print("Type: './MoveAllowed.sh <DEVICE SAN>' then execute the script.\n")
			print("Enter your Jupiter 3 Username and Passwords when prompted.")
			print("A successful Move allow will state that the 'CTS for <DEVICE SAN> processed successfully.'")
		else:
			print(f"Processing Jupiter 3 Issue : {choice}")
############################################################### Submenu - KU Issues.
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
############################################################### Submenu - IGT and XCI Issues.
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
############################################################### Submenu - Email Instruction Banner Only.
def emailer():
	email_banner = """
	----------------------
	Generic Email Template
	======================
	Instructions:
	(1) Enter the Salesforce case # (If generated, if none, press 'Enter'),
	(2) Enter the TEAM to contact (CNE-GW, SDG_Support, NI, Etc.)
	(3) Paste the DEVICE affected (J2ALB047HPAIGW1104, j3yumpr01host01, Etc.)
	(4) Paste the ALARM (Swap utilization, Critical Pings, GW Terminal Drops, Etc.)
	This will generate a Subject line and a email body to send.
	"""
	print(email_banner)
############################################################### Submenu - Email Template Generator
def template():
	while True:
		ticket_num = input("-> Salesforce case number: ")
		team_name = input("-> Team to escalate to: ")
		device_name = input("-> Device name that is alarming: ")
		alarm_decription = input("-> Alarm Decription: ")
	
		email_subject = f" {ticket_num} - {device_name} - {alarm_decription}"
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

		choice = input("-> Email Template finished --> Type 'exit' to return to main menu, Press 'Enter' to process another email: ")
		if choice.lower() == 'exit':
			break
		else:
			print(f"Processing Email Template : {choice}")
############################################################### Submenu - Escalation Path. 
def escalations():
	while True:
		escalations_banner = """
		~~~
		Escalation Path Submenu: 
		[a] - SDG_Support
		[b] - CNE_Team
		[c] - NI
		[d] - ESE [ENOC]
		[e] - EDSE
		[f] - HNSec
		[g] - HNSoc
		[h] - NE
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
			print("\n -Call Babu 1(240)328-8946, if all else fails.")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - CNE Team")
			print("\n -Gateway Engineers -> Dial ext:4140")
			print("\n -Aero Engineers -> Dial ext:4160")
			print("\n -All others -> Dial ext:5998, then follow the prompts.")
			print("\n -Additional last option ext:5999")
		elif choice.lower() == 'c':
			print(f"\n --> {choice} - NI Team")
			print("\n Network Infrastructure -> Call centers are different based on time of day.")
			print("\n -> From 0900 - 2100 hours EST - call ext:5809")
			print("\n -> From 2100 - 0900 hours EST - call ext:3972")
		elif choice.lower() == 'd':
			print(f"\n --> {choice} - ESE/ENOC Team")
			print("\n -Primary ext:4143")
			print("\n -Secondary ext:4144")
		elif choice.lower() == 'e':
			print(f"\n --> {choice} - EDSE Team")
			print("\n -Primary ext:4110")
			print("\n -Secondary ext:4111")
		elif choice.lower() == 'f':
			print(f"\n --> {choice} - HNSec Team")
			print("\n -Primary ext:3688")
		elif choice.lower() == 'g':
			print(f"\n --> {choice} - HNSoc Team")
			print("\n -Primary ext:2666")
		elif choice.lower() == 'h':
			print(f"\n --> {choice} - Network Engineering Team")
			print("\n -Primary ext:6386")
			print("\n -Secondary ext:6387")
		else:
			print(f"Processing Escalation Path : {choice}")
############################################################### Main Program
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
############################################################### Init
if __name__ == "__main__":
	main()		

