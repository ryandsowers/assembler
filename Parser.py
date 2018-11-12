#
#Parser.py
#
# CS2001   Project 6 Assembler
# 31 July 2013
# last updated 26 Aug 2016
#
# start code version
#

import re

'''Manages the mechanical work of breaking the input into tokens, and later further breaking
   down presented tokens into component chunks.  The Parser does not know what the chunks mean
   or what to do with them, it just knows how to slice-and-dice. '''

class Parser(object):

    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3

##########################################
#Constructor

    def __init__(self, fileName):
        loadedList = self.__loadFile__(fileName)
        
        self.toParse = self.__filterFile__(loadedList)

        ##self.toParse = loadedList
        self.__toTestDotTxt__()


##########################################
#public Methods

    
    def advance(self):
        '''reads and returns the next command in the input,
           returns false if there are no more commands.  '''
        #TODO  complete this function
        if len(self.toParse):
        	return self.toParse.pop(0)
        else:
        	return False
        
        


    def commandType(self, command):
        ''' returns type of the command
            A_COMMAND   @xxx
         or C_COMMAND   c-commands
         or L_COMMAND   a label e.g. (LABEL)
        '''
        result = 0   #initialized to a tattle-tail value
        if '@' in command:
        	result = Parser.A_COMMAND
        elif '=' in command or ';' in command:
        	result = Parser.C_COMMAND
        else: 
        	result = Parser.L_COMMAND

        return result



    def symbol(self, command):
        ''' returns
             symbol or decimal of an A-command
          or symbol of a label'''
        
        if (True):
            pass
        #TODO  complete this function
            if '@' in command:
            	result = command[1:]			#return symbol/variable or decimal
            elif '(' in command:
            	result = command[1:-1]			#return label
        else:
            #eliminate silent failures wherever possible
            raise RuntimeError("Error!!! parse.symbol(): We should never parse a symbol from a C_COMMAND")
            result = None
        
        return result



    def dest(self, command):
        ''' returns the dest mnemonic portion of the command '''

        #TODO  complete this function
        if '=' in command:
        	return command.split('=')[0]		
        else:
        	return 'null'
        pass

    
    def comp(self, command):
        ''' returns the comp mnemonic portion of the command '''
        
        #TODO  complete this function
        if ';' in command:
        	return command.split(';')[0]
        elif '=' in command:
        	return command.split('=')[1]
        else:
        	return 'null'
        pass


    
    def jump(self, command):
        ''' returns the jmp mnemonic portion of the command '''

        #TODO  complete this function
        if ';' in command:
        	return command.split(';')[1]
        else:
			return 'null'
        pass



    def processLabels(self):
        ''' Passes over the list of commands and removes labels from the code being parsed.
            as labels are identified they are added to a dictionary of <label, romAddress>
            pairs.  After passing over the entire file the dictionary is returned. '''        
        labels = {}

        #TODO  complete this function
        lineNum = 0

        while lineNum < len(self.toParse):					#while there are more lines to process...
        	line = self.toParse[lineNum]					#give that line
        	if self.commandType(line) == self.L_COMMAND:
        		labels[line[1:-1]] = lineNum				#if L command, add to labels and pop it off
        		self.toParse.pop(lineNum)
        	else:
        		lineNum	+= 1								#if not L command, continue counting lines
        return labels



##########################################
#private/local Methods



    def __toTestDotTxt__(self):
        '''this is just for outputting our stripped file as a test
           this function will not be active in the final program'''

        file = open("test.txt","w")
        file.write("\n".join(self.toParse))
        file.close() 



    def __loadFile__(self, fileName):
        '''Loads the file into memory.

           -fileName is a String representation of a file name,
           returns contents as a simple List.'''
        
        fileList = []
        
        #TODO  complete this function
        with open(fileName, 'r') as myFile:
            fileList = myFile.readlines()
        myFile.close()
        return fileList   



    def __filterFile__(self, fileList):
        '''Comments, blank lines and unnecessary leading/trailing whitespace are removed from the list.

           -fileList is a List representation of a file, one line per element
           returns the fully filtered List'''
        
        filteredList = []
        
        #TODO  complete this function
        for line in fileList:
            if re.match(r'^\s*$', line):    		#if the line is empty (has only the following: \t\n\r and whitespace), skip it
                continue
            elif line.startswith("//"):				#if it's a comment, skip it
                continue 
            else:
                head, separate, tail = line.partition('//')		#give me the code before the comment
                filteredList.append(head.strip())
          
        return filteredList   



    def __filterOutEOLComments__(self, line):
        '''Removes end-of-line comments and and resulting whitespace.

           -line is a string representing single line, line endings already stripped
           returns the filtered line, which may be empty '''

        #TODO  complete this function
        #taken care of in __filterFile__
            
