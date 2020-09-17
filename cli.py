from os import system
import json
import time

def rgbds_ins():
	system("sudo apt install make git gcc")
	system("sudo apt-get install pkg-config flex bison libpng-dev")
	print("Done!")
	choose()
	
def rm():
	print(f"Printing readme...\n\n")
	time.sleep(0.3)
	system("more README.txt")
	
# Get the games and put them into a folder
def redblue(red=True):
	system("git clone https://github.com/rednex/rgbds")
	if red == True:
		system("mkdir pokered")
		system("git clone https://github.com/pret/pokered")
	elif red == False:
		system("mkdir pokeblue")
		system("git clone https://github.com/pret/pokered ./pokeblue")
def goldsilver(gold=True):
	system("git clone https://github.com/rednex/rgbds")
	if gold == True:
		system("mkdir pokegold")
		system("git clone https://github.com/pret/pokegold")
	elif gold == False:
		system("mkdir pokesilver")
		system("git clone https://github.com/pret/pokegold ./pokesilver")
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
	choice = input("Choose an option (enter FOR README): ")
	if len(choice) > 0:
		if choice == "1":
			print("Installing libraries (may require sudo password)")
			rgbds_ins()
		elif choice == "2":
			print("Please choose your game. (Press enter for more info)")
			gaem = input("all lowercase: ")
			if len(gaem) < 1:
				rm()
			else:
				if gaem == "red":
					write_json("0A")
					print("Done!")
				elif gaem == "blue":
					write_json("0B")
					print("Done!")
				elif gaem == "gold":
					write_json("1A")
					print("Done!")
				elif gaem == "silver":
					write_json("1B")
					print("Done!")
				elif gaem == "crystal":
					write_json("1C")
					print("Done!")
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
				print("NO GAME DETECTED")
				rm()
			elif read_json('gdata') == "1A" or read_json('gdata') == "1B":
				print("POKEMON GOLD-SILVER DETECTED\nSorry, but GOLD-SILVER/ENGLISH isn't supported as of right now. Expect an update soon!")
			elif read_json('gdata') == "1C":
				print("POKEMON CRYSTAL DETECTED\nSorry, but CRYSTAL isn't supported as of right now. Expect an update soon!")
			else:
				print("READ ERROR")
		else:
			time.sleep(2)
			print("Invalid option!")
			choose()
	else:
		rm()
		
# First run only
choose()
