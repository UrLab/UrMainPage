from sys import argv
from pathlib import Path

HTML_HEADER = "<head>\n\t<link rel=\"stylesheet\" type=\"text/css\" href=\"index.css\">\n</head>\n<body>\n\t<h1>Index</h1>\n\t<ul>\n"
HTML_TAIL = "\t</ul>\n</body>\n"
BULLET = "\t\t<li><a href=\"{0}\">{1}</a></li>\n"
OUTPUTFILE = Path.cwd() / "index.html"

class Service:
	def __init__(self, ip, port, name):
		self.port = int(port)
		if self.port < 0 or self.port >= 2**16:
			raise ValueError(f"Invalid port found for service {name} : {port}")
		self.name = name
		self.ip = ip
	
	def toHTML(self):
		return BULLET.format(f"http://{self.ip}:{self.port}", self.name)

	def __gt__(self, other): # self > other ?
		return self.port > other.port

def printSupport(givenSuffix):
	SUPPORTED = ".csv"
	SUPPORT = f"Your provided file has suffix '{givenSuffix}', but we currently support following suffixes : {SUPPORTED}"
	print(SUPPORT)

def usageExit():
	USAGE = f"Usage:\n\tpython3 src/{argv[0]} <ports-file>"
	print(USAGE)
	exit(1)

def checkArgv():
	if len(argv) != 3:
		usageExit()
	try:
		assert len(argv[2].split(".")) == 4
		for i in argv[2].split("."):
			a = int(i)
	except:
		raise ValueError("Second argument is not an IPv4")

def initFile(filename):
	return Path.cwd() / filename

def extractFromCSVFile(file):
	with open(file) as f:
		lines = f.read().split("\n")
	lines = [i.split(",") for i in lines if i != ""]
	services = [Service(i[0], i[1], i[2]) for i in lines]
	return sorted(services, key=lambda t:t.port)

def extractServicesFromFile(file):
	if file.suffix == ".csv":
		return extractFromCSVFile(file)
	else:
		printSupport(file.suffix)
		usageExit()

def listToHTML(services):
	html = HTML_HEADER
	for service in services:
		html += service.toHTML()
	html += HTML_TAIL
	return html

def handleError(exception):
	raise Exception
	print("The program encountered an error :")
	try:
		print(exception.message)
	except:
		print(exception)

def writeToHTMLIndexFile(content):
	with open(OUTPUTFILE, "w") as f:
		f.write(content)
	print(f"Written to {OUTPUTFILE}")

def main():
	try:
		#checkArgv()
		if len(argv) != 2:
			usageExit()
		file = initFile(argv[1])
		#ip = argv[2]
		services = extractServicesFromFile(file)
		content = listToHTML(services)
		writeToHTMLIndexFile(content)
	except Exception as e:
		handleError(e)
		exit(1)
	print("Done.")
	

if __name__ == "__main__":
	main()

