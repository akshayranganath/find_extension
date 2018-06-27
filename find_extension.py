import gzip
import re
import argparse

def extract_extension(url_string):
	file_extension = re.compile("(?:[^\?]+\.)([a-zA-Z0-9]+)(?:$|\?)")
	# Regex explained
	# (?:[^\?]+\.) - match everything until the last '.' 
	# ([a-zA-Z0-9]+) - capture the extension bit
	# (?:$|\?) - ensure that the extension is followed by a '?' or a end of string. This will prevent setting the extension as 'abc' for a string like 1.abc.png 
	matches = file_extension.match(url_string)
	if matches != None:
		extension = list(matches.groups())[0]
		return extension


def find_extensions(file_name):
	'''
		Using a single regex, find the extension from a set of URLs or ARLs
		It can be useful for assessments.

		Parameter: 
			file_name: Name of the gzip file to extract the URLs
	'''
	extensions = set()	
	
	try:
		# try to extract as a gzip file. Gzip is only detected at 'read' So the ugly work-around
		with gzip.open(file_name,'r') as f:			
			for line in f:
				extension = extract_extension(line)
				if extension != None:
					extensions.add(extension)		

	except IOError:
		# this is not a gzip file - so treat is as a plain text
		with open(file_name,'r') as f:
			for line in f:
				extension = extract_extension(line)
				if extension != None:
					extensions.add(extension)

	for extension in extensions:
		print extension


if __name__=="__main__":
        parser = argparse.ArgumentParser(description='Print extension from a set of URLs/ARLs')
        parser.add_argument('--file', help="File containing list of URLs/ARLs",required=True )
        args = parser.parse_args()                
        find_extensions(args.file)