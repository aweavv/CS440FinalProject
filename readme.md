readme.md

CS440 Fall 2019
Austen Weaver and Carlos Garcia

Program to analyze a given text, create a language model, then apply machine learning to further the language model
accuracy at which point it will be used to predict other texts authors.

To be written in Python.

Three parts:
1 - Import/ load all text files automatically from project gutenberg
    	    - I think it is unreasonable to manually download the amount of
	    books we are wanting to cover
	    - Your notebook program may already do this with ease, does it?
2 - Parse through files removing all unwanted characters/white space/etc..
3 - Build language models with training texts.
4 - test using logistic regression (maybe SVM's)
5 - test using artificial neural networks
6 - Give result (print out)
7 - Main function that drives all this


The above can either go in one big .py file or we can break it into multiple
files for easier code management and viewing.  I'm thinking multiple files
that each contain it's own class. EX: import class, parse class, train class,
test class, and a main that would handle running it all and giving the results.
