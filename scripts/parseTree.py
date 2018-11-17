from stat_parser import Parser
from nltk.tree import Tree
import re

parser = Parser()

def main():
	with open('../data/Bernstein-Ratner87-words') as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	utterances = [x.strip().lower() for x in content]

	with open('../evaluation/Bernstein-Ratner87-parsed-tree', 'w') as w:
		for utterance in utterances:
			print(utterance)
			try:
				result = str(parser.parse(utterance))
				# # get rid of capital letters
				# result = re.sub(r'\b[A-Z]+\b', '', result)

				# # garb preprocessing.
				# # too lazy to think about regular expressions
				# result = result.replace("+", "")
				# result = result.replace("$", "")
				# result = result.replace(" ", "")
				# result = result.replace("\n", "")

				# # convert ( => [ and ) => ]
				# result = result.replace("(", "[")
				# result = result.replace(")", "]")
				# print(result)
				w.write("UTTERANCE: " + utterance + "\n")
				w.write("TREE: " + "\n" + str(result) + "\n\n")
			except:
				w.write("UTTERANCE: " + utterance + "\n")
				w.write("ERROR: FIX IT LATER" + "\n\n")

# def testSimple(utterance):
# 	print(str(parser.parse(utterance)))

main()
