#main.py
#used to run the rest of the program as well as display results of program
import os
import sys

home = os.getcwd()
sys.path.append(home)

import textProcessing as tpm



if __name__ == "__main__":

	tp = tpm.textProcessing()
	docs_df = tp.importDocs()
	entries = tp.prepDocs(docs_df)

	print(entries.head())
	print(entries.shape)

