from os import system
import json
import time
import clictrl
import USTRINGS

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def rgbds_ins():
	system("sudo apt install make git gcc")
	system("sudo apt-get install pkg-config flex bison libpng-dev")
	if clictrl.allow_rgbds():	
		system("git clone https://github.com/rednex/rgbds")
		print(f"{bcolors.WARNING}Requires sudo to install to /usr{bcolors.ENDC}")
		system("cd rgbds && sudo make install")
	else:
		print(f"{bcolors.FAIL}RGBDS cloning was disabled. The libraries were installed but the folder was not created.{bcolors.ENDC}")
	print(f"{bcolors.BOLD}{bcolors.OKBLUE}Done!{bcolors.ENDC}")
	choose()
	
def rm():
	print(f"{bcolors.BOLD}{bcolors.OKGREEN}Printing readme...\n\n{bcolors.ENDC}")
	time.sleep(0.3)
	print(USTRINGS.readme())
	
# Get the games and put them into a folder
def redblue(red=True):
	if clictrl.allow_clone():
			if red == True:
				system("mkdir pokered")
				system("git clone https://github.com/pret/pokered")
			elif red == False:
				system("mkdir pokeblue")
				system("git clone https://github.com/pret/pokered ./pokeblue")
	else:
		print(f"{bcolors.FAIL}Cloning is disabled. Running alt code...{bcolors.ENDC}")
		print(f"{bcolors.OKGREEN}Checking dev mode flag...{bcolors.ENDC}")
		if clictrl.secrets():
			print("Dev mode enabled...")
			print(f"{bcolors.OKGREEN}Running code...{bcolors.ENDC}")
			system("cd rgbds && sudo make install && cd ../tets && make red")
		elif clictrl.secrets() == False:
			print(f"{bcolors.WARNING}Dev mode is not enabled.\nExiting...{bcolors.ENDC}")
		
# def goldsilver(gold=True):
	# if clictrl.allow_clone():
		# if gold == True:
			# system("mkdir pokegold")
			# system("git clone https://github.com/pret/pokegold")
		# elif gold == False:
			# system("mkdir pokesilver")
			# system("git clone https://github.com/pret/pokegold ./pokesilver")
	# else:
		# print(f"{bcolors.FAIL}Cloning is disabled. Running alt code...{bcolors.ENDC}")
		
def crystal():
	return "UNFINISHED AND UNDEFINED"	
def read_json(paramtr):
	with open('storedconfig.json', 'r') as testfile:
		readfile = json.load(testfile)
	return readfile[paramtr]
def write_json(game="0A"):
	data = {}
	data['gdata'] = game
	with open('storedconfig.json', 'w') as testfile:
		json.dump(data, testfile, indent=4)
# Main
def choose():
	choice = input(f"{bcolors.BOLD}{bcolors.HEADER}Choose an option (enter FOR README): {bcolors.ENDC}")
	if len(choice) > 0:
		if choice == "1":
			print(f"{bcolors.BOLD}{bcolors.OKGREEN}Installing libraries (may require sudo password){bcolors.ENDC}")
			rgbds_ins()
		elif choice == "2":
			print("Please choose your game. (Press enter for more info)")
			gaem = input("all lowercase: ")
			if len(gaem) < 1:
				rm()
			else:
				if gaem == "red":
					write_json("0A")
					print(f"{bcolors.OKBLUE}Done!{bcolors.ENDC}")
				elif gaem == "blue":
					write_json("0B")
					print(f"{bcolors.OKBLUE}Done!{bcolors.ENDC}")
				elif gaem == "gold":
					write_json("1A")
					print(f"{bcolors.OKBLUE}Done!{bcolors.ENDC}")
				elif gaem == "silver":
					write_json("1B")
					print(f"{bcolors.OKBLUE}Done!{bcolors.ENDC}")
				elif gaem == "crystal":
					write_json("1C")
					print(f"{bcolors.OKBLUE}Done!{bcolors.ENDC}")
				else:
					print("Invalid game!")
			choose()
		elif choice == "3":
			print("Getting games...\n")
			time.sleep(0.4)
			if read_json('gdata') == "0A":
				print("POKEMON RED DETECTED")
				redblue(True)
			elif read_json('gdata') == "0B":
				print("POKEMON BLUE DETECTED")
				redblue(False)
			elif read_json('gdata') == "00":
				print(f"{bcolors.FAIL}{bcolors.BOLD}NO GAME DETECTED{bcolors.ENDC}")
				rm()
			elif read_json('gdata') == "1A" or read_json('gdata') == "1B":
				print("POKEMON GOLD-SILVER DETECTED\nSorry, but GOLD-SILVER/ENGLISH isn't supported as of right now. Expect an update soon!")
			elif read_json('gdata') == "1C":
				print("POKEMON CRYSTAL DETECTED\nSorry, but CRYSTAL isn't supported as of right now. Expect an update soon!")
			else:
				print(f"{bcolors.FAIL}READ ERROR{bcolors.ENDC}")
		else:
			time.sleep(1)
			print(f"{bcolors.FAIL}Invalid option!{bcolors.ENDC}")
			choose()
	else:
		rm()
		
# First run only
choose()
