# Why is this file called USTRINGS?
# cuz i was too lazy to come up with a good name lol

# learn your colors again children
class bcolors:
  HEADERS = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

#other files will call this for readme hehe
def readme():
  # RETURN SUPER DUPER EXTRA DUCKING LONG STRING HAHAHAHAHAHAHAAHA
  	return (f'{bcolors.FAIL}{bcolors.BOLD}RED-INSTALL{bcolors.ENDC}{bcolors.OKGREEN}\n\n{bcolors.BOLD}OPTIONS:{bcolors.ENDC}{bcolors.OKBLUE}\n	First, you need to install the libraries. You only need to do this once. Type \'{bcolors.ENDC}{bcolors.OKGREEN}{bcolors.BOLD}{bcolors.UNDERLINE}1{bcolors.ENDC}{bcolors.OKBLUE}\' in the prompt.\n	Next, you need to choose the game with the \'{bcolors.ENDC}{bcolors.OKGREEN}{bcolors.BOLD}{bcolors.UNDERLINE}2{bcolors.ENDC}{bcolors.OKBLUE}\' option. The options are "{bcolors.UNDERLINE}red{bcolors.ENDC}{bcolors.OKBLUE}", "{bcolors.UNDERLINE}blue{bcolors.ENDC}{bcolors.OKBLUE}", "{bcolors.UNDERLINE}gold{bcolors.ENDC}"{bcolors.OKBLUE}, {bcolors.ENDC}"{bcolors.OKBLUE}{bcolors.UNDERLINE}silver{bcolors.ENDC}{bcolors.OKBLUE}", "{bcolors.UNDERLINE}crystal{bcolors.ENDC}{bcolors.OKBLUE}".{bcolors.ENDC}')
