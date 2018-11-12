#
#Assembler.py
#
# CS2001   Project 6 Assembler
# 31 July 2013
# last updated 26 Aug 2016
#
# start code version
#


from Code import *
from SymbolTable import *
from Parser import *


'''Manages the assembly process, used the Parser to do the mechanical tokenizing and then
   determines the semantically correct thing to do with those tokens. Then uses the Parser
   to break tokens into appropriate components and requests the translations of those
   components from the Code module. Labels are passed to the SymbolTable to get mapped
   against addresses.'''
class Assembler(object):

##########################################
#Constructor

    def __init__(self, target):

        index = target.find('.asm')
        if ( index < 1):
            raise RuntimeError( "error, cannot use the filename: " + target )

        self.inputFileName = target
        self.outputFileName = self.inputFileName[:index] + '.hack'

        self.parser = Parser(self.inputFileName)

        self.code = Code()
        self.st = SymbolTable()




##########################################
#public methods

    def assemble(self):
        '''Does the assembly and creates the file of machine commands,
           returning the name of that file '''
        self.__firstPass__()
        return  self.__output__( self.__secondPass__() )







##########################################
#private/local methods
 
    def __output__(self, codeList):
        ''' outpute the machine code codeList into a file and returns the filename'''

        file = open(self.outputFileName,"w")
        file.write("\n".join(codeList))
        file.close()
        return self.outputFileName


    def __firstPass__(self):
        ''' Passes over the file contents to populate the symbol table'''
        #MUST prevent the Assembler reaching into the parser
        #while also not requiring the parser to become semantically aware
        #so let parser do mechanical work
        #   and let Assembler do the semantic part on the returned results

        #TODO  complete this function
        #update the symbol table with the processLabels dict
        self.st.table.update(self.parser.processLabels()) 
        


    def __secondPass__(self):
        ''' Manage the translation to machine code, returning a list of machine instructions'''
        
        machineCode = []

        command = self.parser.advance()
        while( command ):

            if (True):
            #TODO  complete this loop body
                if self.parser.commandType(command) == Parser.C_COMMAND:
                    bitString = self.__assembleC__(command)         #translate C command
                    result = bitString
                elif self.parser.commandType(command) == Parser.A_COMMAND:
                    if self.st.contains(command[1:]):           
                        bitString = self.__assembleA__(command)     #if A command in table, process
                    elif self.parser.symbol(command).isdigit():
                        bitString = self.__assembleA__(command[1:]) #if A command is digit, process
                    else:
                        self.st.addEntry(command[1:], self.st.getNextVariableAddress())
                        bitString = self.__assembleA__(command)     #if A command is new variable, add it to table and process
                    result = bitString
                machineCode.append(result)
            else:
                symStr = self.parser.symbol()
                raise RuntimeError( 'There should be no labels on second pass, errant symbol is ' + symStr)

            command = self.parser.advance()
        return machineCode



    def __assembleC__(self, command):
        ''' Do the mechanical work to translate a C_COMMAND, returns a string representation
            of a 16-bit binary word.'''
        
        #TODO  complete this function
        return '111' + self.code.comp(self.parser.comp(command)) + self.code.dest(self.parser.dest(command)) + self.code.jump(self.parser.jump(command))
        pass

         
    def __assembleA__(self, command):
        ''' Do the mechanical work to translate an A_COMMAND, returns a string representation
            of a 16-bit binary word.'''

        #TODO  complete this function
        if command.isdigit():
            symVal = command
            result = '0' + "{0:015b}".format(int(symVal))           #translate the digit
        else:
            symVal = self.st.getAddress(self.parser.symbol(command))
            result = '0' + "{0:015b}".format(symVal)                #translate the address from symbol table
        return result      
        
       
    




#################################
#################################
#################################
#this kicks off the program and assigns the argument to a variable
#
if __name__=="__main__":

    target = sys.argv[1]         # use this one for final deliverable
    
##    target = 'add/Add.asm'       # for internal IDLE testing only
##    target = 'max/MaxL.asm'      # for internal IDLE testing only
##    target = 'max/Max.asm'       # for internal IDLE testing only
##    target = 'rect/RectL.asm'    # for internal IDLE testing only
##    target = 'rect/Rect.asm'     # for internal IDLE testing only
##    target = 'pong/PongL.asm'    # for internal IDLE testing only
##    target = 'pong/Pong.asm'     # for internal IDLE testing only
   
    assembler = Assembler(target)
    print('done parsing, assembled file is:', assembler.assemble() )

