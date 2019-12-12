# Naive bayes

# Imports
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import BernoulliNB, ComplementNB, MultinomialNB
from sklearn import metrics

import random

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score, recall_score, f1_score

# Class
class NBCalssification:

	def __init__(self,pct_train=.80):
		self.pct_train = pct_train
	
	def create_data_sets(self,le_df):
		'''
		input: labeled entries, dataframe
		output: tuple of data sets, (train_x,train_y,test_x,test_y)
		'''
		# Authors
		aid = list(le_df['Author ID'])
		texts = list(le_df.Text)
		data = [(aid[i],texts[i]) for i in range(len(aid))]

		training_data = []

		for i in range(int(round(len(aid)*self.pct_train,0))):
		    training_data.append(data.pop(random.randint(0,len(data)-1)))

		testing_data = data

		training_data_x = [b for a,b in training_data]
		training_data_y = [a for a,b in training_data]
		testing_data_x = [b for a,b in testing_data]
		testing_data_y = [a for a,b in testing_data]

		return training_data_x, training_data_y, testing_data_x, testing_data_y


	def classify(self, data):
		x1,y1,x2,y2 = data

		# Vectorize x data
		vectorizer = HashingVectorizer(stop_words='english', alternate_sign=False)
		xvec_train = vectorizer.transform(x1)
		xvec_test = vectorizer.transform(x2)

		# Create multinomial naive bayes
		nb = MultinomialNB(alpha=0.01)
		nb.fit(xvec_train,y1)
		pred = nb.predict(xvec_test)

		print(classification_report(y2, pred))



