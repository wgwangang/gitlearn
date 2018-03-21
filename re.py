import re

def refunc():
	subject = "aasdasdfw2323233aasdfaerqewrgjakdsf45239999)))))dasfads"
	regex = "dasf"
	result = re.split(regex, subject)
	print(result)
	return

	
		
	regex=r"..."
	if re.search(regex, subject):
	  do_something()
	else:
	  do_anotherthing()

	
	regex=r"...\Z" 
	if re.match(regex, subject):
	  do_something()
	else:
	  do_anotherthing()

	regex=r"xxx"
	match = re.search(regex, subject)
	if match:
	  # match start: match.start()
	  # match end (exclusive): match.end()
	  # matched text: match.group()
		do_something()
	else:
	  	do_anotherthing()


	regex=r"..."
	match = re.search(regex, subject)
	if match:
	  result = match.group()
	else:
	  result = ""

	regex=r"..."
	match = re.search(regex, subject)
	if match:
	  result = match.group(1)
	else:
	  result = ""

	regex=r"..."
	match = re.search(regex, subject)
	if match:
	  result = match.group("groupname")
	else:
	  result = ""


def main():
	refunc()

if __name__ == '__main__':
	main()
