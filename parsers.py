################################################################################
# PART #1
################################################################################


#I only did parts 1 and 2, per what I remember in class!


def countWordsUnstructured(filename):
    import string
    d = {}
    for line in open('state-of-the-union-corpus-1989-2017/Bush_1989.txt','r'):
        t = line.split(' ')
        for i in t:
            try:
                d[i.strip(string.punctuation+':.\n\t')]+=1
            except:
                d[i.strip(string.punctuation+':.\n\t')]=1
    return d
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    
# Test your part 1 code below.

################################################################################
# PART 2
################################################################################
    
def generateSimpleCSV(targetfile, wordCounts): 
    try:
        with open(targetfile,'a') as fout:
            fout.write("Word,Count\n")
            for key,value in wordCounts.items():
                fout.write(str(key)+","+str(value)+'\n')
    except:
        print("You done messed up!")
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    
# Test your part 2 code below
    
################################################################################
# PART 3
################################################################################
def countWordsMany(directory): 
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    
# Test your part 3 code below

################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile): 
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
# Test your part 4 code below
    
################################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile): 
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    
# Test your part 5 code below

################################################################################
# PART 6
################################################################################
def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value