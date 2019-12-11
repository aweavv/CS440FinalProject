#textProcessing.py
#Contains function to import training & test documents, as well as function for text parsing.

# imports
import requests
import pandas as pd



#Class
class textProcessing:

	def importDocs(self):
		'''
		Imports the documents
		Reference file must be in specific format.

		Output: dataframe with author, text, etc.
		'''
		# Reference books
		ref_path = r"Book References.xlsx"
		br = pd.read_excel(ref_path)
		count = br.shape[0]
		print('Total # of books: {}'.format(count))
		br = br.drop('Path',axis=1)
		br = br.head(10)

		br['Text'] = br.apply(lambda row: pull_online_text(row,count),axis=1)

		return br


	def prepDocs(self,df):
		'''
		input: document dataframe
		output: entry dataframe
		'''

		# Clean text in input dataframe
		df['Text'] = df.apply(lambda row: clean_text(row.Text),axis=1)
		df['Text'] = df.apply(lambda row: split_to_list_of_paragraphs(row.Text),axis=1)
		df['Text'] = df.apply(lambda row: trim_text(row),axis=1)

		# Create new dataframe
		g_id = list(set(df.Genre))
		g_id = {g_id[i]:i for i in range(len(g_id))}
		a_id = list(set(df.Author))
		a_id = {a_id[i]:i for i in range(len(a_id))}

		genre = []
		genre_id = []
		author = []
		author_id = []
		text = []

		for i,row in df.iterrows():
		    all_p = row.Text
		    for p in all_p:
		        genre.append(row.Genre)
		        genre_id.append(g_id[row.Genre])
		        author.append(row.Author)
		        author_id.append(a_id[row.Author])
		        text.append(p)
		        
		frame = {'Genre':genre,'Genre ID':genre_id,'Author':author,'Author ID':author_id,'Text':text}
		return pd.DataFrame(frame)
        
# Functions
def pull_online_text(row,count):
    ref_id = row['GP Ref #']
    title = row.Title
    auth = row.Author
    i = row.name
    
    print('Pulling text {} of {}: "{}" by {}'.format(i+1,count,title,auth))
    
    basepath = r'https://www.gutenberg.org'
    end1 = r'/files/{0}/{0}-0.txt'.format(ref_id)
    end2 = r'/cache/epub/{0}/pg{0}.txt'.format(ref_id)
    ends = [end1,end2]
    for end in ends:
        path = basepath + end
        r = requests.get(path) # response
        if r.status_code == 200:
            r.encoding = 'utf-8' # encoding of the text per Gutenburg website
            txt = r.text
    try:
        return txt
    except:
        print('No text found for "{}" by {}'.format(title,auth))

def clean_text(text):
    text = text.lower()
    td = {'?': '.', ':': '.', '!': '.', ',': None,';': None, '_': None,
          '"': None,'-': ' ','(':None,')':None,"'":None} # translation dictionary
    td = str.maketrans(td)
    text = text.translate(td)
    
    return text
    
def split_to_list_of_paragraphs(text):
    text = text.replace('\ufeff','') # gets rid of starting characters
    
    if '\n\n\n\n' in text:
        text = text.split('\n\n\n\n') # split paragraphs, creates list of text
        text = [x for x in text if x!=''] # get rid of blanks in the list
        text = [x.replace('\n\n',' ') for x in text] # get rid of new lines within paragraphs
    elif '\r\n\r\n' in text:
        text = text.split('\r\n\r\n') # split paragraphs, creates list of text
        text = [x for x in text if x!=''] # get rid of blanks in the list
        text = [x.replace('\r\n',' ') for x in text] # get rid of new lines within paragraphs
    else:
        print('No paragraph markers found')
        return None
    
    return text

def trim_text(row, min_len = 500):
    '''
    This function will look to get rid of introductory paragraphs and paragraphs at the end of the text file.
    After running this function, there will only be the actual text of the book.
    
    This function also joins small paragraphs together so that there is more to analyze
    '''
    ind = []
    paras = row.Text
    
    # Find the beginning and ends
    for i in range(len(paras)):
        if '***' in paras[i]:
            ind.append(i)
    
    paras = paras[ind[0]+1:ind[1]]
    
    # Combine paragraphs
    cps = []
    c = ''
    for p in paras:
        if not c:
            c=p
        elif len(c)<min_len:
            c = c+' '+p
        else:
            cps.append(c)
            c = ''
            
    return cps