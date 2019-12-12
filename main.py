#main.py
#used to run the rest of the program as well as display results of program
import os
import sys

home = os.getcwd()
sys.path.append(home)

import textProcessing as tpm
import naivebayes as nb



if __name__ == "__main__":

	tp = tpm.textProcessing()
	docs_df = tp.importDocs()
	le = tp.prepDocs(docs_df) # labeled entries, as dataframe

	# Naive Bayes classification
	c = nb.NBCalssification() # classifier
	data_sets = c.create_data_sets(le)
	c.classify(data_sets)

