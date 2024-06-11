############################################################### Intro Banner Only.
def banner():
	display_banner = """
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Welcome to the NMC Assistance Framework.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Instructions:
	Make your selection at the prompts when requested, enjoy! :)
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	"""
	print(display_banner)
############################################################### Main menu - User choice.
def user_choice():
	second_banner = """
	Main Menu
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Please select from the following: 
	[1] - Incoming phone calls
	[2] - Jupiter 1 and 2 issues
	[3] - Jupiter 3 and FUSION issues
	[4] - KU issues
	[5] - Email template generator
	[6] - IGT and XCI
	[7] - Escalation Paths 
	[8] - Tool login info
	[9] - Event Summary
	[10] - Site Access request
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Type 'exit' to exit program. Utilizing 'Ctrl+c' will break the script.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	  Suggestions and input are always encouraged, please let me know if there are
	 additional items that will assist any and all NMC newcomers and senior members
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
	  The name of the caller and where are they calling from? [ex: John from FSS]\n
	  The SAN or SID of the device with the issue. (SAN = Jupiter; SID = KU)\n
	  The SERIAL number for the device OR device(s)\n
	  WHAT is the issue that is occuring? WHAT steps have been taken so far?\n
	  Single site calls may have STATE CODES or NMS CODES.\n
	  Create a ticket based on the provided information, then escalate to the 
	  proper resources (CNE-GW, FUSION, SDG_Support, NLV, Etc.),
	"""
	print(phone_instruct) 
############################################################### Submenu - Jupiter 1 and 2 Issues. 
def jupiter1and2_issues():
	while True:
		jupiter_banner = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		Jupiter Issues Submenu: 
		[a] - Single site call
		[b] - Terminal Drops
		[c] - BGP Peers
		[d] - Move Allows
		[e] - HTTP | DNS Failures
		exit - exit Jupiter Issues Submenu
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		print(jupiter_banner)
		choice = input("-> Jupiter Issues --> Your selection, Type 'exit' to return to the main menu: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a': 	##########Single site calls
			print(f"\n --> {choice} - Single site")
			print("\n  You are likely on a phone call....")
			print("\n  Gather the following during this call: ")
			print("  The site SAN, and the SERIAL numbers of the terminal(s) -> There may be more than one")
			print("  Log into DSS (hns-unsername:PIN+RSA) and navigate the sidebar to 'Jupiter Dashboard'")
			print("  Select 'Jupiter Dashboard', then enter the SAN or the ESN of the site into DSS to gather more information,")
			print("  such as, Radio_ESN, Gateway_IDs, Beam_IDs for your ticket and for engineers")
			print("  Depending on what the Single site issue is, this will affect your escalation path")
			print("  Is the terminal stuck in activation stages? -> Escalate to CNE-NMS")
			print("  Is the terminal within FAP? -> Escalate to the SDG_Support Team")
		elif choice.lower() == 'b':		##########Terminal Drops
			print(f"\n --> {choice} - Terminal Drops")
			print("  Within the SL1 alarm, select the performance tab at the top of the window,")
			print("  Select the >Hughes Jupiter IGW menu and look for 'NumAsocTerminals'")
			print("  Note the number of terminals that are on the IPGW, should there be only a few registered Terminals on the IPGW")
			print("  Ask a senior collegue if the number of terminals on the GW is sufficent, if they are then ignore the alarm, if not create a  ticket and escalate")
		elif choice.lower() == 'c':		##########BGP Peering
			print(f"\n --> {choice} - BGP Peering Issues")
			print("  IF this is a Jupiter 3 alarm, check Ansible for circuit information, else continue....\n")
			print("  Within SL1, note the interface and BGP neighbour")
			print("  If the link is a backbone link to a carrier ISP,")
			print("  then escalate to the appropriate carrier\n")
			print("  Level3|CenturyLink|Lumen - Login portal")
			print("  -> controlcenter.lumen.com/enterprise/dashboard\n")
			print("```")
			print("Verizon - Login Portal")
			print("  -> enterprise.verizon.com/public/index.html#/repairsqf/tickets/find\n")
			print("  ```")
			print("\n  GTT Communitcation - Login Portal")
			print("   -> ethervision.gtt.net/sign-in\n")
			print("  ```")
		elif choice.lower() == 'd':
			print(f"\n --> {choice} - Move Allow Requests\n")
			print("  Teleperformance SHOULD have the ability to perform these moves.")
		elif choice.lower() == 'e':
			print(f"\n --> {choice} - HTTP | DNS Failures\n")
			print("  Note the Platform and Gateway (YUM,BIL,J2CHY,J2MIS)")
			print("  Browse to platform Jovian logging in with your creds.\n")
			print("  On the left hand sidebar, navigate to the platform affected,")
			print("  Select the 'GM' icon, locate your problem device likely an IGW,")
			print("  Select the 'Device Web GUI' icon, on the left sidebar, navigate to,")
			print("  Mgmt > Logs > CDT Log Display and select the log file.\n")
			print("  Analyze the log file for the FAILURE.")
			print("\n  ---> DNS_FAILURES | HTTPS_IP6_FAILURE")	
		else:
			print(f"Processing Jupiter 1/2 Issue : {choice}")
############################################################### Submenu - Jupiter 3 Issues.
def jupiter3_issues():
	while True:
		jupiter3_banner = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		Jupiter 3 Issues Submenu: 
		[a] - Single site call
		[b] - Terminal Drops
		[c] - Terminal Move Allows
		[d] - HTTP | DNS Failures
		exit - exit Jupiter 3 Issues Submenu
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		print(jupiter3_banner)
		choice = input("-> Jupiter 3 Issues --> Your selection, Type 'exit' to return to the main menu: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - Single site\n")
			print("")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - Terminal Drops\n")
		elif choice.lower() == 'c':
			print(f"\n --> {choice} - Terminal Move Allows\n")
			print("  Open Putty and 'ssh' into 172.16.193.11\n")
			print("  Login: nmcuser:nmcuser123!@#\n")
			print("  Type: './MoveAllowed.sh <DEVICE SAN>' then execute the script.\n")
			print("  Enter your Jupiter 3 Username and Passwords when prompted.")
			print("  A successful Move allow will state that the 'CTS for <DEVICE SAN> processed successfully.'")
		elif choice.lower() == 'd':
			print(f"\n --> {choice} - HTTP | DNS Failures\n")
			print("  Note the Platform and Gateway (YUM,BIL,J2CHY,J2MIS)")
			print("  Browse to platform Jovian logging in with your creds.\n")
			print("  On the left hand sidebar, navigate to the platform affected,")
			print("  Select the 'GM' icon, locate your problem device likely an IGW,")
			print("  Select the 'Device Web GUI' icon, on the left sidebar, navigate to,")
			print("  Mgmt > Logs > CDT Log Display and select the log file.\n")
			print("  Analyze the log file for the FAILURE.")
			print("\n  ---> DNS_FAILURES | HTTPS_IP6_FAILURE")
		else:
			print(f"Processing Jupiter 3 Issue : {choice}")
############################################################### Submenu - KU Issues.
def ku_issues():
	while True:
		ku_banner = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		KU Issues Submenu: 
		[a] - Enterprise
		[b] - Timing and power
		[c] - VSAT down/Outage
		[d] - Decommission Requests
		exit - exit KU Issues Submenu
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		print(ku_banner)
		choice = input("-> KU Issues --> Your selection, Type 'exit' to return to the main menu: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - Enterprise")
			print("  Gather the information regarding the site.")
			print("  Such as SiD | Serial | Error codes or messages ")
			print("  Generate a Salesforce ticket, reach out to a senior collegue for clarity")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - Timing and Power")
			print("  Gather the information from the technician, SiD and Serial")
			print("  Log into the corresonding NOC Element Manager (National, Diversity(GTN, NLV), HX, Gilbert)")
			print("  Open the RDP Connections.msc icon and select the corresonding DNCC")
			print("  Go to the 'DNCC Logging' tab and then select the 'DNCC Transient Log' tab(Near the bottom of the window)")
			print("  Right-click and select 'Ranging Filter', Select the 'Configuration' tab and note the Bandwidth Allocation: Inroute Groups,")
			print("  Move to the 'General' tab and choose the [StartRange] from the drop-down menu, input the serial into the 'Serial No:' )field: ")
			print("  Then input the Inroute group number in the 'Group' field, then click 'Send'.")
			print("  Move back to the 'DNCC Logging' tab and note the information for the VSAT. Ask a senior collegue if the timing and power are sufficent ")
		elif choice.lower() == 'c':
			print(f"\n --> {choice} - VSAT down/Outage")
			print("  Note the SID, Serials and other pertinent information(ie: Local weather, maintenances, power, etc.)")
			print("  Generate a Salesforce ticket and look in the Project Management spreadsheet for the correct team to escalate to.")		
		elif choice.lower() == 'd':
			print(f"\n --> {choice} - Decommission Requests")
			print("  Gather the SID and Serial numbers of the terminal that is to be decommissioned.")
			print("  Log into the corresonding Vision server via NOC_FORMS (Quickest) or via RDC to the Server itself.")
			print("  Navigate to the ACS Lite tab, select Manual Decommission then input the SID, Serial, Your operator name, Requester name (FSS, WWTS, etc) is fine")
			print("  Requester Department is the same as Requester name, and the Reason code for ALL Decommissions is C22 - Decommissioned: Technical Troubleshooting.")
			print("  Then Execute the process, allow for the server to respond, then copy the 'Successful Decommision' information into the service ticket for closure.")
		else:
			print(f"Processing KU Issue : {choice}")
############################################################### Submenu - IGT and XCI Issues.
def igt_issues():
	while True:
		igt_banner = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		IGT and XCI Issues Submenu: 
		[a] - IGT issue?
		[b] - XCI issue?
		exit - exit IGT/XCI Issues Submenu
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		print(igt_banner)
		choice = input("-> IGT/XCI Issues --> Your selection, Type 'exit' to return to the main menu: ")
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
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Generic Email Template
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Instructions:
	(1) Enter the Salesforce case # (If generated, if none, press 'Enter'),
	(2) Enter the TEAM to contact (CNE-GW, SDG_Support, NI, Etc.)
	(3) Paste the DEVICE affected (J2ALB047HPAIGW1104, j3yumpr01host01, Etc.)
	(4) Paste the ALARM (Swap utilization, Critical Pings, GW Terminal Drops, Etc.)
	This will generate a Subject line and a email body to send.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
		f"  Hello {team_name},\n\n"
		f"  This email is to provide visibility on {device_name}, which is currently alarming within SL1."
		f"  Alarm: {alarm_decription} \n\n\n"
		f"  Please take the required actions to address this issue and relay the corrective actions to the NMC\n"
		f"  Thank you very much!\n\n"
		f"  Regards,\n\n"
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
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		print(escalations_banner)
		choice = input("-> Escalations Issues --> Your selection, Type 'exit' to return to the main menu: ")
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
############################################################### Login info
def login_info():
	while True:
		login_banner = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		Login info Submenu: 
		[a] - Jupiter 1 and 2
		[b] - Ku | Terrestrial
		[c] - Jupiter 3
		exit - exit Login Info Submenu
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		print(login_banner)
		choice = input("-> Login Info --> Your selection, Type 'exit' to return to the main menu: ")
		if choice.lower() == 'exit':
			break
		elif choice.lower() == 'a':
			print(f"\n --> {choice} - Jupiter 1 abnd 2")
			print(" ~~~Jupiter 1 and 2 Jovian~~~")
			print(" username:PIN+RSA token")
			print(" ~~~    NAD DSS   ~~~")
			print(" hns-username:PIN+RSA")
		elif choice.lower() == 'b':
			print(f"\n --> {choice} - KU | Terrestrial")
			print("For KU use the NOC_FORMS for Decommissions, and RDC into the specific servers for other issues. (ie: Timing and Power, etc.)")
		elif choice.lower() == 'c':
			print(f"\n --> {choice} - Jupiter 3")
			print(" Your Assigned Jupiter3 username:password  ---> NOT PIN+RSA")
		else:
			print(f"Processing Login information request : {choice}")
############################################################### Submenu - Site access requests and event summary
def event_template():
	while True:
		template_banner = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		Event Summary Template : Enter in information at the requested fields. 
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		print(template_banner)
		event_type = input("-> Event Type [Outage, Degradation, Investigation]: ")
		start_date = input("-> Event Start DATE [12/12/23]: ")
		start_time = int(input("-> Event Start TIME [1200] 24 hour format: "))
		end_date = input("-> Event End DATE [12/12/23]: ")
		end_time = int(input("-> Event End TIME [1400] 24 hour format: "))
		service_type = input("-> Service Type: [Transport, Ordering, Management] ")
		cust_affected = input("-> Customers Affected: [SHP, CEN, OXY] ")
		sites_affected = input(" -> Number of sites affected: ")
		alerts = input(" -> Alert method: [Customer called in, SL1] ")
		summary = input(" -> What what the event summary?: [The NMC responded to alarms......] ")
		root_cause = input(" -> What was the Root cause for this issue?: ")
		sw_vers = input(" -> What was the software version?: ")	
		
############# Time calculator
		start_hour = start_time // 100
		start_minute = start_time % 100
		end_hour = end_time // 100
		end_minute = end_time % 100
		# Convert times to minutes
		start_minutes = start_hour * 60 + start_minute
		end_minutes = end_hour * 60 + end_minute
		# Calculate duration in minutes
		total_duration_minutes = end_minutes - start_minutes
		# Convert total duration to hours and minutes
		total_duration_hours = total_duration_minutes // 60
		total_duration_minutes %= 60

		event_body = (
		f"  Event Type: {event_type},\n"
		f"  Event Duration: {start_date} @ ({start_time}) - {end_date} @ ({end_time}), Duration: [{total_duration_hours}H:{total_duration_minutes}M] \n"
		f"  Type of Service: {service_type} \n"
		f"  Customers Affected: {cust_affected} \n"
		f"  Numbers of sites: {sites_affected} \n"
		f"  Alerts: {alerts} \n"
		f"  Event Summary: {summary} \n"
		f"  Root Cause: {root_cause} \n"
		f"  S/W Version: {sw_vers} \n"
		)
		
		print("\nEvent Summary Template\n\n")
		print(f"{event_body}")

		choice = input("-> Event Summary Template finished --> Type 'exit' to return to main menu, Press 'Enter' to process another event summary: ")
		if choice.lower() == 'exit':
			break
		else:
			print(f"Processing Event Summary Template : {choice}")
###############################################################
def site_access():
	while True:
		event_site_banner = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		Site Access Request Template
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		requester = input("Who requested the site access: ")
		visitor = input("Who is the visitor: ")
		req_comp = input("What company is the requester from: ")
		vist_comp = input("What company is the visitor from: ")
		req_phone = input("What is the requesters phone number: ")
		visit_phone = input("What is the visitors phone number: ")
		req_date = input("Date of request: ")
		visit_citizen = input("What citizenship does the visitor hold: ")
		arrival_date = input("When will the visitor arrive: ")
		depart_date = input("When will the visitor depart: ")
		equip_check = input("Is equipment being sent to the site: ")
		visit_purpose = input("What is the purpose of the visit: ")
		smarthands = input("Is Smarthands required to be dispatched: ")
		###
		requesting_info = (
		f"\n  Now cut and paste this into a site access request ticket.\n"
		f"\n  Requester name: {requester}\n"		
		f"  Visitor name: {visitor}\n"
		f"  Requesting company: {req_comp}\n"
		f"  Visitor company: {vist_comp}\n"
		f"  Requester phone number: {req_phone}\n"
		f"  Visitor phone number: {visit_phone}\n"
		f"  Date of request: {req_date}\n"
		f"  Citizenship of Visitor: {visit_citizen}\n"
		f"  Arrival Date: {arrival_date}\n"
		f"  Departure Date: {depart_date}\n"
		f"  Is equipment being sent to the site: {equip_check}\n"
		f"  Purpose of the visit: {visit_purpose}\n"
		f"  Smarthands: {smarthands}\n\n"
		)
		###
		print(requesting_info)

		choice = input("-> Site Access Template finished --> Type 'exit' to return to main menu, Press 'Enter' to process another event summary: ")
		if choice.lower() == 'exit':
			break
		else:
			print(f"Processing Site Access Request Template : {choice}")

############################################################### Main function
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
		elif choice == 8:
			login_info()
		elif choice == 9:
			event_template()
		elif choice == 10:
			site_access()
		else:
			print("Processing bases on your choice -> ", choice)
############################################################### Init
if __name__ == "__main__":
	main()		

