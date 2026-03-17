from sys import argv

class Service:
	def __init__(self, port, name):
		self.port = int(port)
		if port < 0 or port >= 2**16:
			raise ValueError(f"Invalid port found for service {name} : {port}")
		self.name = name
	
	def __gt__(self, other): # self > other ?
		return self.port > other.port

def printSupport(givenSuffix):
	SUPPORTED = ".csv"
	SUPPORT = f"Your provided file has suffix '{givenSuffix}', but we currently support following suffixes : {SUPPORTED}"
	print(SUPPORT)

def usageExit():
	USAGE = f"Usage:\n\tpython3 src/{argv[0]} <host-name> <ports-file>"
	print(USAGE)
	exit(1)

def checkArgv():
	if len(argv) != 2:
		usageExit()

def extractFromCSVFile(file):
	with open(file) as f:
		text = f.read()
	services = [Service(i.split(",")) for i in text.split("\n")]
	return sorted(services, key=lambda t:t.port)

def extractServicesFromFile(file):
	if file.suffix == ".csv":
		services = extractFromCSVFile(file)
	else:
		printSupport(file.suffix)
		usageExit()

def listToHTML(services):
	html = ""
	for service in services:
		

def handleError(exception):
	print("The program encountered an error :")
	if hasattr(exception, message):
		print(e.message)
	else:
		print(e)

def main():
	try:
		checkArgv()
		file = initFile(argv[1])
		services = extractServicesFromFile(file)
		content = listToHTML(services)
		html = buildHTMLIndex(content)
		writeToHTMLIndexFile(html)
	except Exception as e:
		handleError(e)
		exit(1)
	print("Done.")
	

if __name__ == "__main__":
	main()

