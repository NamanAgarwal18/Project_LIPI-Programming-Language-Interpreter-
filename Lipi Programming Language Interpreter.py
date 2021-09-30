# -*- coding: utf-8 -*-
"""
    @author: Naman Agarwal
"""
from datetime import datetime
import random, string


#####################   Some global initialisations  ##########################

# Line no to keep track of what line of code we are on
lineNo = 0

#functions -> name: (start,end)
functions = {}

#start Parenthesis -> start: end
startParenthesis = {}

#end Parenthesis -> end: start
endParenthesis = {}

#A stack full of function objects
functionStack = []

#Time to determine timeout
time = None

# declare array elements
arrayElements = { }

##############################  Class Function  ###############################

'''
    The function class holds -> Name of the fucntion
                                Start line number of the fucntion
                                End line number of the fucntion
                                Variables declared in fucntion and their values
'''

class function:
    
    def __init__(self,Name,Start,End,parameters):
        self.start = Start
        self.end = End
        self.name = Name
        self.variables = {}
        for arg in parameters:
            self.variables[arg[0]] = arg[1]
            
    def print(self):
        print("Name -> ", self.name, "\nStart -> ", self.start, " , End -> ", self.end)
        print("Variables -> ", self.variables)

#################################  Checkers  ##################################

def generateRandomVariable():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(5))
    return x

def isParenthesisWord(word):
    li = ["LOOP", "IS", "NONE"]
    if word in li:
        return True
    return False
        
def isVariable(word):
    if len(word)==0:
        return False
    if word[0] == "$":
        j = 0
        while j < len(word) and word[j]!="-":
            j+=1
        if j == len(word):
            return True
        elif j + 4 == len(word) and word[j+1] == 'l' and word[j+2] == 'e' and word[j+3] == 'n':
            return True
        else:
            return False
    return False

def isOperator(word):
    # .. -> and
    # ++ -> or
    # <> -> equal to
    # >< -> not equal to
    # [] -> absolute value equal to
    # ][ -> absolute value not equal to
    li = ['+', '-', '*', '/','%',"**","<>",">=","<=",">","<","..","++","><","[]", "][","//"]
    if word in li:
        return True
    return False

def isBracket(word):
    li = ['(',')']
    if word in li:
        return True
    return False

def isKeyword(word):
    li = ["IN","OUT", "IS", "NONE", "LOOP", "EXIT", "CALL", "RET", "ARR"]
    if word in li:
        return True
    return False

def isNumber(word):
    word = str(word)
    li = ['0','1','2','3','4','5','6','7','8','9']
    dot = False
    count = 0
    for i in word:
        if i in li:
            continue
        elif i=='.':
            if not dot:
                dot = True
            else:
                return False
        elif count==0 and i =='-':
            return True
        else:
            return False
        count +=1
    return True

def isArray(word,obj,ret):
    left=""
    middle=""
    j = 0
    while j<len(word) and word[j]!="[":
        left = left + word[j]
        j+=1
    #print(left,middle)
    if j>=len(word) or word[j] != "[":
        return False
    j+=1
    
    while j < len(word) and word[j]!="]":
        middle = middle + word[j]
        j = j + 1
    #print(left,middle)
    if j>=len(word) or word[j] != "]" or j+1 != len(word):
        return False
    if not isVariable(left):
        return False
    temp = left + "-len"
    if isVariable(middle):
        if middle in obj.variables.keys():
            if temp in obj.variables.keys():
                temp = obj.variables.get(temp)
                j = 0
                left = ""
                while j<len(temp) and temp[j]!="-":
                    left = left + temp[j]
                    j+=1
                temp = left + "-len"
                if int(arrayElements.get(temp)) > int(obj.variables.get(middle)) and isNumber(obj.variables.get(middle)):
                    left = left + "-" + str(int(obj.variables.get(middle)))
                else:
                    raise Exception("Error at " + str(lineNo) + " -> Array not found")
            else:
                raise Exception("Error at " + str(lineNo) + " -> Index out of bounds")
        else:
            return False
        if ret:
            #print(left)
            return left
        else:
            return True
    elif isNumber(middle):
        if int(middle) >= 0:
            if temp in obj.variables.keys():
                temp = obj.variables.get(temp)
                j = 0
                left = ""
                while j<len(temp) and temp[j]!="-":
                    left = left + temp[j]
                    j+=1
                temp = left + "-len"
                if arrayElements.get(temp) > int(middle):
                    left = left + "-" + str(int(middle))
            else:
                raise Exception("Error at " + str(lineNo) + " -> Index out of bounds")
            
            #print(left,middle)
        else:
            return False
        if ret:
            #print(left)
            return left
        else:
            return True
    else:
        return False
    
def isArrayLen(word):
    length = len(word)
    if length < 5:
        return False
    
    if word[0]=="$" and word[length-1] == "n" and word[length-2] == "e" and word[length-3] == "l" and word[length-4] == "-":
        return True
    return False


###########################  Initiation of the Code ##########################

'''
    Here we recieve the code line by line and we check 
    where each curly brace starts and where it ends.
    
    We also fill up -> 1. 'functions' dictionary with each function detail
                       2. 'startParenthesis' dictionary with the start and 
                                          corresponding end of each block.
                       3. 'endParenthesis' dictionary with the end and
                                        corresponding start of each block.
'''

stack = []
def initiate(line,name,type):
    global lineNo
    words = line.split(" ")
    if words[0] == "FN":
        if type == None:
            type = "FN"
            name = words[1]
        else:
            raise Exception("Error at " + str(lineNo) + " Compile time Error with parenthesis " + words[0])
    elif isParenthesisWord(words[0]):
        if type==None:
            type = words[0]
            name = None
        else:
            raise Exception("Error at " + str(lineNo) + " Compile time Error with parenthesis " + words[0])
    elif len(words[0])==1 and words[0]=="{":
        if  type!=None:
            stack.append([type,name,lineNo-1])
            name = None
            type = None
        else:
            raise Exception("Error at " + str(lineNo) + " Compile time Error with parenthesis " + words[0])
    elif len(words[0])==1 and words[0]=="}":
        if type==None and len(stack)!=0:
            temp= stack.pop()
            if temp[0] == "FN":
                if temp[1] not in functions.keys():
                    functions[temp[1]] = (temp[2],lineNo)
                else:
                    raise Exception("Error at " + str(lineNo) + " Compile time Error -> fucntion overloading not allowed" + words[0])
            startParenthesis[temp[2]] = lineNo
            endParenthesis[lineNo] = temp[2]
        else:
            raise Exception("Error at " + str(lineNo) + " Compile time Error with parenthesis " + words[0])
    else:
        type=None
        name=None
    return name,type
    
##########################  Evaluatte expressions  ############################

#To check the precedence of each operator
def precedence(op):
    if op =="++":
        return 1
    if op == "..":
        return 2
    if op == "<>" or op=="<" or op==">" or op==">=" or op=="<=" or op=="><" or op=="[]" or op=="][":
        return 3
    if op == '+' or op == '-':
        return 4
    if op == '*' or op == '/' or op == '%' or op=="//":
        return 5
    if op == "**":
        return 6
    return 0

#To apply the operation of each operator
def applyOp(a, b, op):
     
    if op == '+': 
        if not isNumber(str(a)) or not isNumber(str(b)):
            return str(a) + str(b)
        else:
            return a + b
    if op == '-': 
        if isNumber(str(a)) and isNumber(str(b)):
            return a - b
        elif  isNumber(str(a)) and a > 0 and a<=len(str(b)):
            temp = ""
            j = 0
            while j < int(a):
                temp += str(b)[j]
                j+=1
            return temp
        elif isNumber(str(b)) and b > 0 and b<=len(str(a)):
            temp = ""
            j = len(str(a)) - int(b)
            while j < len(str(a)):
                temp += str(a)[j]
                j+=1
            return temp
        else:
            raise Exception("Error at " + str(lineNo) + " '-' operator not used correctly on strings")
    if op == '*':
        if isNumber(str(b)):
            return a * b
        else:
            raise Exception("Error at " + str(lineNo) + " '*' operator not applicable on 2 strings")
    if op == '/': 
        if isNumber(str(a)) and isNumber(str(b)):
            return a / b
        elif isNumber(str(a)) and a > 0:
            if a >= len(str(b)):
                return 0
            else:
                temp = ""
                j = int(a)
                while j < len(str(b)):
                    temp = temp + str(b)[j]
                    j=j+1
                return temp
        elif isNumber(str(b)) and b > 0:
            if b >= len(str(a)):
                return 0
            else:
                temp = ""
                i = len(str(a)) - b
                j = 0
                while j < i:
                    temp = temp + str(a)[j]
                    j=j+1
                return temp
        else:
            raise Exception("Error at " + str(lineNo) + " '/' operator not applicable on strings")
    if op == "//": 
        if isNumber(str(a)) and isNumber(str(b)):
            return a // b
        else:
            raise Exception("Error at " + str(lineNo) + " '//' operator not applicable on strings")
    if op == '%': 
        if isNumber(str(a)) and isNumber(str(b)):
            return a % b
        else:
            raise Exception("Error at " + str(lineNo) + " '%' operator not applicable on strings")
    if op == "**":
        if isNumber(str(a)) and isNumber(str(b)):
            return a ** b
        else:
            raise Exception("Error at " + str(lineNo) + " '**' operator not applicable on strings")
    if op == "[]": 
        if isNumber(str(a)) and isNumber(str(b)):
            if abs(a) == abs(b):
                return 1
            else:
                return 0
        else:
            a = str(a).lower()
            b = str(b).lower()
            if a == b:
                return 1
            else:
                return 0
    if op == "][": 
        if isNumber(str(a)) and isNumber(str(b)):
            if abs(a) != abs(b):
                return 1
            else:
                return 0
        else:
            a = str(a).lower()
            b = str(b).lower()  
            if a != b:
                return 1
            else:
                return 0
    if op == "<>": 
        if a == b:
            return 1
        else:
            return 0
    if op == "><": 
        if a != b:
            return 1
        else:
            return 0
    if op == "<": 
        if a < b:
            return 1
        else:
            return 0
    if op == ">": 
        if a > b:
            return 1
        else:
            return 0
    if op == ">=": 
        if a >= b:
            return 1
        else:
            return 0
    if op == "<=": 
        if a <= b:
            return 1
        else:
            return 0
    if op == "..":
        if (a and b):
            return 1
        else:
            return 0
    if op == "++":
        if (a or b):
            return 1
        else:
            return 0
    
#To evaluate the infix expression
def evaluate(tokens):
    values = []
    ops = []
    i = 0
     
    while i < len(tokens):
         
        # Current token is a whitespace,
        # skip it.
        if tokens[i] == ' ':
            i += 1
            continue
         
        # Current token is an opening
        # brace, push it to 'ops'
        elif tokens[i] == '(':
            ops.append(tokens[i])
         
        # Could be a negtive number or a normal negative sign
        elif  tokens[i]=='-':
            if tokens[i+1] == " ":
                # if normal negative sign
                tok = tokens[i]
                if tokens[i+1]!=" ":
                    tok = tok + tokens[i+1]
                    i+=1
                while (len(ops) != 0 and
                    precedence(ops[-1]) >=
                       precedence(tok)):
                             
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                     
                    values.append(applyOp(val1, val2, op))
                 
                # Push current token to 'ops'.
                ops.append(tok)
            elif tokens[i+1].isdigit():
                i=i+1
                val = 0
                while (i < len(tokens) and
                    tokens[i].isdigit()):
                    val = (val * 10) + int(tokens[i])
                    i += 1
                if tokens[i]=='.':
                    i+=1
                    flagValue = 0
                    while (i < len(tokens) and
                        tokens[i].isdigit()):
                        val = (val * 10) + int(tokens[i])
                        flagValue+=1
                        i += 1
                    val = val / (10 ** flagValue)
                val = val * (-1)
                values.append(val)
                i=i-1
            
            
        # Current token is a number, push
        # it to stack for numbers.
        elif tokens[i].isdigit():
            val = 0
             
            # There may be more than one
            # digits in the number.
            
            while (i < len(tokens) and
                tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1
            if tokens[i]=='.':
                i+=1
                flagValue = 0
                while (i < len(tokens) and
                    tokens[i].isdigit()):
                    val = (val * 10) + int(tokens[i])
                    flagValue+=1
                    i += 1
                val = val / (10 ** flagValue)
            
             
            values.append(val)
             
            # right now the i points to
            # the character next to the digit,
            # since the for loop also increases
            # the i, we would skip one
            #  token position; we need to
            # decrease the value of i by 1 to
            # correct the offset.
            i=i-1
         
        # Closing brace encountered,
        # solve entire brace.
        elif tokens[i] == ')':
         
            while len(ops) != 0 and ops[-1] != '(':
             
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                 
                values.append(applyOp(val1, val2, op))
             
            # pop opening brace.
            ops.pop()
         
        elif tokens[i]=='\"':
            text = ""
            i+=1
            while tokens[i]!='\"':
                text = text + tokens[i]
                i+=1
                #print(text)
            values.append(text)
            #print(values)
            
        
        # Current token is an operator.
        else:
         
            # While top of 'ops' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'ops'
            # to top two elements in values stack.
            tok = tokens[i]
            if tokens[i+1]!=" ":
                tok = tok + tokens[i+1]
                i+=1
            #print(ops)
            while (len(ops) != 0 and
                precedence(ops[-1]) >=
                   precedence(tok)):
                         
                val2 = values.pop()
                val1 = values.pop()
                #print(val2,val1)
                op = ops.pop()
                 
                values.append(applyOp(val1, val2, op))
             
            # Push current token to 'ops'.
            ops.append(tok)
         
        i += 1
     
    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops) != 0:
         
        val2 = values.pop()
        val1 = values.pop()
        #print(val2,val1)
        op = ops.pop()
                 
        values.append(applyOp(val1, val2, op))
     
    # Top of 'values' contains result,
    # return it.
    
    return values[-1]

#To replace all the variables with their values and create a infix equation
def createBool(words,obj,leave):
    global lineNo
    #print(words)
    variables = obj.variables
    temp = ""
    shouldVariable = True
    for i in range(2,len(words)-leave, +1):
        if len(words[i]) == 0:
            continue
        if isVariable(words[i]) and shouldVariable:
            shouldVariable = False
            wording = words[i]
            if isArray(word = wording, obj = obj, ret = False):
                wording = isArray(word = wording, obj = obj, ret = True)
                if wording in arrayElements.keys():
                    if isNumber(str(arrayElements.get(wording))):
                        temp = temp + str(arrayElements.get(wording)) + " "
                    else:
                        temp = temp + "\"" + str(arrayElements.get(wording)) + "\" "
                else:
                    raise Exception("Error at " + str(lineNo) + " -> Variable " + words[i] + " not found") 
            elif wording in variables.keys():
                if isNumber(str(variables.get(wording))):
                    temp = temp + str(variables.get(wording)) + " "
                elif isArrayLen(wording):
                    temp = temp + str(arrayElements.get(variables.get(wording))) + " "
                else:
                    temp = temp + "\"" + str(variables.get(wording)) + "\" "
            else:
               raise Exception("Error at " + str(lineNo) + " -> Variable " + words[i] + " not found") 
        elif isOperator(words[i]) and not shouldVariable:
            shouldVariable = True
            temp = temp + words[i] + " "
        elif isNumber(words[i]) and shouldVariable:
            shouldVariable = False
            temp = temp + words[i] + " " 
        elif isBracket(words[i]):
            temp = temp + words[i] + " " 
        elif words[i][0]=="\"":
            temp = temp + words[i] + " "
        else:
            raise Exception("Error at " + str(lineNo) + " -> Expression does not make sense " + words[i])
    #print(temp)
    return temp

def resizeArray(word,obj,value):
    value = int(value)
    if value < 0:
        raise Exception("Error at " + str(lineNo) + " -> Array size cant be negative")
    if word in obj.variables.keys():
        prev = obj.variables.get(word)
        word = prev
        prev = int(arrayElements.get(prev))
        
        wording = ""
        j = 0
        while j < len(word) and word[j]!="-":
            wording+=word[j]
            j+=1
        if prev == value:
            return
        elif prev < value:
            j = prev
            arrayElements[word] = value
            while j < value:
                text = wording + "-" + str(j)
                arrayElements[text] = 0
                j+=1
        else:
            j = value
            arrayElements[word] = value
            while j < prev:
                text = wording + "-" + str(j)
                arrayElements.pop(text)
                j+=1
            
    else:
        raise Exception("Error at " + str(lineNo) + " -> No such array exists")

#To put value into a variable
def addVariable(words,obj):
    global lineNo
    variables = obj.variables
    
    name = words[0]
    #print(name)
    if words[1] != '=':
        raise Exception("Error at " + str(lineNo) + " -> Equality not found")
    temp = createBool(words,obj,0)
    #print("temp -> ",temp)
    value = evaluate(temp)
    if isArray(word = name, obj = obj, ret = False):
        name = isArray(word = name, obj = obj, ret = True)
        arrayElements[name] = value
        return
    if isNumber(value) and isArrayLen(words[0]):
        resizeArray(words[0],obj,value)
    else:
        variables[name] = value
    
#############################  Process Keywords  ##############################

#find what type of a keyword it is and call the appropreate functions
def processKeyword(words,obj,code):
    global lineNo, time
    if words[0] == "IN" or words[0] == "OUT":
        processIO(words,obj)
        return True
    elif words[0] == "IS":
        processIf(words,obj,code)
        return True
    elif words[0] == "LOOP":
        processLoop(words,obj,code)
        return True
    elif words[0] == "EXIT":
        return processExit(words,obj,code)
    elif words[0] == "CALL":
        processFucntion(words,obj,code)
        return True
    elif words[0] == "RET":
        return processRet(words, obj, code)
    elif words[0] == "ARR":
        processArr(words,obj,code)
        return True
    else:
        raise Exception("Error at " + str(lineNo) + " -> Invalid Syntax " + words[0])

#Process the 'IN' and 'OUT' keywords
def processIO(words,obj):
    global time
    variables = obj.variables
    if words[0] == "IN":
        i = 1
        while i<len(words):
            if words[i][0] == "\"":
                text = ""
                #words[i] = words[i][1:]
                word = words[i][1:]
                while word[-1]!="\"" and i<len(words):
                    text = text + word + " "
                    i+=1
                    word = words[i]
                if i==len(words):
                    raise Exception("Error at " + str(lineNo) + " -> \" never closed " + words[i])
                #words[i] = words[i][:-1]
                text = text + word[:-1]
                if i+1 == len(words):
                    raise Exception("Error at " + str(lineNo) + " -> No input asked " + words[i])
                print(text, end=" ")
            elif isVariable(words[i]):
                value = input()
                wording = words[i]
                if isArray(word = wording, obj = obj, ret = False):
                    wording = isArray(word = wording, obj = obj, ret = True)
                    arrayElements[wording] = value
                elif isNumber(value) and isArrayLen(wording):
                    resizeArray(wording,obj,value)
                else:
                    variables[wording] = value
            else:
                raise Exception("Error at " + str(lineNo) + " -> Invalid Syntax " + words[i])
            i+=1
        time= datetime.now()
        time = time.strftime("%M")
    elif words[0] == "OUT":
        text = ""
        isParanthesis = False
        i = 0
        #print(words)
        for word in words:
            #print(word,len(word))
            if len(word)==0:
                continue
            if i!=0:
                if isVariable(word) and not isParanthesis: 
                    wording = word
                    if isArray(word = wording, obj = obj, ret = False):
                        wording = isArray(word = wording, obj = obj, ret = True)
                        text = text + str(arrayElements.get(wording)) + " "
                    elif (wording in variables.keys() and not isArrayLen(wording)):
                        text = text + str(variables.get(wording)) + " "
                    elif (wording in variables.keys() and isArrayLen(wording)):
                        text = text + str(arrayElements.get(variables.get(wording))) + " "
                    else:
                        raise Exception("Error at " + str(lineNo) + " -> Invalid Syntax " + words[i])
                    
                elif isVariable(word) and isParanthesis:
                    wording = word
                    if wording[-1]=="\"":
                        #print("innnn")
                        isParanthesis = False
                        wording = wording[:-1]
                    text = text + wording + " "
                   
                elif isParanthesis:
                    wording = word
                    #print("in",word,len(word))
                    if wording[-1]=="\"":
                        #print("innnn")
                        isParanthesis = False
                        wording = wording[:-1]
                    text = text + wording + " "

                elif not isParanthesis and word[0]=="\"":
                    isParanthesis = True
                    wording = word[1:]
                    if wording[-1]=="\"":
                        isParanthesis = False
                        wording = wording[:-1]
                    text = text + wording + " "
                        
                else:
                    raise Exception("Error at " + str(lineNo) + " -> Invalid Syntax " + words[i])
            i+=1
            #print(isParanthesis)
            
        if isParanthesis:
            raise Exception("Error at " + str(lineNo) + " -> Error with \" " + str(words))
        print(text)
        
#Process the 'IS' and 'NONE' keywords
def processIf(words,obj,code):
    global lineNo
    text = createBool(words, obj,1)
    result = evaluate(text)
    if result == 1:
        result = True
    elif result == 0:
        result = False
    else:
        raise Exception("Error at " + str(lineNo) + " -> Compile time error -> Condition not valid " + code[lineNo])
    #print("lineNo -> ",lineNo)
    #print(lineNo , " ->-> ",code[lineNo])
    if result:
        lineNo+=1
        #print(lineNo , " ->-> ",code[lineNo])
        if lineNo in startParenthesis:
            end = startParenthesis.get(lineNo)
            #print("Lines -> ",lineNo," ",code[lineNo],end-1," ",code[end-1])
            startExecution(mainStart = lineNo, mainEnd=end-1, code=code, obj=obj)
            #print("coming out ", code[lineNo])
            
            lineNo = lineNo+1
            line = code[lineNo]
           
            if line == "NONE":
                #print("in -> ",line)
                if (lineNo+1) in startParenthesis.keys():
                    lineNo = startParenthesis[lineNo+1]
                    lineNo = lineNo-1
                    #print("393",lineNo,code[lineNo])      
            else:
                lineNo = lineNo -1
                #print(lineNo,code[lineNo])
                
        else:
            raise Exception("Error at " + str(lineNo) + " -> Not Indexed Correctly")
    else:
        lineNo+=1
        #print(lineNo , " ->-> ",code[lineNo])
        if lineNo in startParenthesis.keys():
            lineNo = startParenthesis[lineNo]
            #print(lineNo , " ->-> ",code[lineNo])
            if code[lineNo] == "NONE":
                lineNo+=1
                #print(lineNo, "---> ", code[lineNo])
                end = startParenthesis.get(lineNo)
                #print(end-1, " end = ", code[end-1])
                startExecution(mainStart = lineNo, mainEnd = end -1, code = code, obj=obj)
            else:
                #print(lineNo)
                lineNo = lineNo - 1
                
        else:
            raise Exception("Error at " + str(lineNo) + " -> Not Indexed Correctly")
          
#Process the 'LOOP' keyword
def processLoop(words,obj,code):
    global lineNo
    #print("lno" ,lineNo)
    text = createBool(words, obj,1)
    result = evaluate(text)
    if result == 1:
        result = True
    elif result == 0:
        result = False
    else:
        raise Exception("Error at " + str(lineNo) + " -> Compile time error -> Condition not valid " + code[lineNo])
    #print(result)
    continueEndLoop = True
    startingPosition = lineNo
    while result:
        lineNo+=1
        #print(lineNo , " ->-> ",code[lineNo])
        if lineNo in startParenthesis:
            end = startParenthesis.get(lineNo)
            #print("Lines -> ",lineNo," ",code[lineNo],end-1," ",code[end-1])
            continueEndLoop = startExecution(mainStart = lineNo, mainEnd=end-1, code=code, obj=obj)
            #print("coming out ", code[lineNo], " -> ",lineNo)
            if not continueEndLoop:
                lineNo = startingPosition+1
                lineNo = startParenthesis.get(lineNo) -1
                return
            start = endParenthesis.get(lineNo+1)
            lineNo = start-1
            #print(lineNo)
            text = createBool(words, obj,1)
            
            result = evaluate(text)
            if result == 1:
                result = True
            elif result == 0:
                result = False
            else:
                raise Exception("Error at " + str(lineNo) + " -> Compile time error -> Condition not valid " + code[lineNo])
        else:
            raise Exception("Error at " + str(lineNo) + " -> Not Indexed Correctly") 
    if not result:
        lineNo = lineNo +1
        #print(lineNo)
        lineNo = startParenthesis.get(lineNo)
        #print(lineNo)
        lineNo = lineNo -1   
    
#Process the 'EXIT' keyword
def processExit(words,obj,code):
    global lineNo
    #print(lineNo)
    text = createBool(words, obj,1)
    result = evaluate(text)
    if result == 1:
        #print(False)
        return False
    elif result == 0:
        return True
    else:
        raise Exception("Error at " + str(lineNo) + " -> Compile time error -> Condition not valid " + code[lineNo])
    
#Process the 'CALL' keyword
def processFucntion(words,obj,code):
    global lineNo
    if len(words)==1:
        raise Exception("Error at " + str(lineNo) + " -> Fucntion name not given")
    if words[1] in functions.keys():
        functionLineStart,functionLineEnd = functions.get(words[1])
        functionLineStart = functionLineStart -1
        #print(functionLineStart,functionLineEnd)
        wordFunction = code[functionLineStart]
        wordFunction = wordFunction.split(" ")
        argumentNeeded = len(wordFunction) - 2
        argumentGiving = len(words) - 2
        #print(wordFunction)
        #print(words)
        #print(argumentGiving,argumentNeeded)
        if argumentGiving < argumentNeeded:
            raise Exception("Error at " + str(lineNo) + " -> Function '" + words[2]+"' needs "+argumentNeeded+" arguments but only "+argumentGiving+"arguments given")
        elif argumentGiving == argumentNeeded or (argumentGiving == argumentNeeded + 2 and words[len(words)-2]=="->"):
            list = []
            for i in range(argumentNeeded):
                if isVariable(words[2+i]):
                    if words[2+i] in obj.variables.keys() and not isArrayLen(words[2+i]):
                        pair  = ( wordFunction[2+i] , obj.variables.get(words[2+i]) )
                        list.append( pair )
                    elif isArray(word = words[2+i], obj=obj, ret = False):
                        wording = isArray(word = words[2+i], obj=obj, ret = True)
                        if wording in arrayElements.keys():
                            pair  = ( wordFunction[2+i] , arrayElements.get(wording) )
                            list.append( pair )
                        else:
                            raise Exception("Error at " + str(lineNo) + " -> Invalid index for thee array " + words[i+2])
                    elif isArrayLen(words[2+i]):
                        if isArrayLen(wordFunction[2+i]):
                            pair  = ( wordFunction[2+i] , obj.variables.get(words[2+i]) )
                            list.append( pair )
                        else:
                            pair  = ( wordFunction[2+i] , arrayElements.get(obj.variables.get(words[2+i])) )
                            list.append( pair )
                elif isNumber(words[2+i]):
                    pair  = ( wordFunction[2+i] , words[2+i] )
                    list.append( pair )
                else:
                    raise Exception("Error at " + str(lineNo) + " -> Invalid argument to the '" + words[2]+"' fucntion call")
                    
            FunStart = functions[words[1]]
            FunEnd = FunStart[1]
            FunStart = FunStart[0]
            objectNew = function(words[1],FunStart,FunEnd,list)
            functionStack.append(obj)
            if len(functionStack) > 31:
                #Stack Full after 30 recursive calls
                raise Exception("Stack Overflow (Only 31 fucntion calls at a time allowed)")
            rememberOldLine = lineNo
            returning = startExecution(mainStart = FunStart, mainEnd = FunEnd-1, code = code, obj = objectNew)
            lineNo = rememberOldLine
            functionStack.pop()
            del objectNew
            if argumentGiving == argumentNeeded + 2:
                if returning == True:
                    returning = 1
                elif returning == False:
                    returning = 0
                if isVariable(words[len(words)-1]):
                    if isArray(word = words[len(words) -1], obj = obj, ret = False):
                        wording = isArray(word = words[len(words) -1], obj = obj, ret = True)
                        if wording in arrayElements.keys():
                            arrayElements[wording] = returning
                        else:
                            raise Exception("Error at -> " + lineNo +" Array index out of bounds " + words[len(words)-1])
                    else:
                        obj.variables[words[len(words)-1]] = returning
                else:
                    raise Exception("Error at " + str(lineNo) + " -> "+ words[len(words)-1]+" not a variable")
                
        else:
            raise Exception("Error at " + str(lineNo) + " -> Inappropreate number of arguments given to function '" + words[2]+"' ")
            
    else:
        raise Exception("Error at " + str(lineNo) + " -> Function '" + words[2]+"' not found")

#Process the 'RET' keyword
def processRet(words,obj,code):
    global lineNo
    #print(words)
    if words[1] == "(":
        text = createBool(words= words, obj = obj, leave = 2)
        result = evaluate(text)
        #print(result)
        if result == 1:
            if words[len(words)-1] in obj.variables.keys() and not isArrayLen(words[len(words)-1]):
                return obj.variables.get(words[len(words)-1])
            elif isNumber(words[len(words)-1]):
                #print(words[len(words)-1])
                i = 0
                token = words[len(words)-1]
                if token[i].isdigit():
                    val = 0
                    while (i < len(token) and
                        token[i].isdigit()):
                        val = (val * 10) + int(token[i])
                       # print(val)
                        i += 1
                    if i<len(token) and token[i]=='.':
                        i+=1
                        flagValue = 0
                        while (i < len(token) and
                            token[i].isdigit()):
                            val = (val * 10) + int(token[i])
                            #print(val)
                            flagValue+=1
                            i += 1
                        val = val / (10 ** flagValue)
                        #print(flagValue,val)
                elif token[i] == "-":
                    i+=1
                    val = 0
                    #(words[len(words)-1])
                    while (i < len(token) and
                        token[i].isdigit()):
                        val = (val * 10) + int(token[i])
                        #print(val)
                        i += 1
                    if i<len(token) and token[i]=='.':
                        i+=1
                        flagValue = 0
                        while (i < len(token) and
                            token[i].isdigit()):
                            val = (val * 10) + int(token[i])
                            #print(val)
                            flagValue+=1
                            i += 1
                        val = val / (10 ** flagValue)
                        #print(val)
                    val = val * (-1)
                else:
                    raise Exception("Error at " + str(lineNo) + " -> Number '"+words[1]+"' doesn't exist")
                #print(val)
                return val
            elif isArray(word = words[len(words)-1], obj = obj, ret = False):
                word = isArray(word = words[len(words)-1], obj = obj, ret = True)
                return arrayElements.get(word)
            else:
                raise Exception("Error at " + str(lineNo) + " -> Variable '"+words[len(words)-1]+"' doesn't exist")
        elif result == 0:
            return None
    elif words[1] in obj.variables.keys() and not isArrayLen(words[1]):
        return obj.variables.get(words[1])
    elif isNumber(words[1]):
        i = 0
        token = words[1]
        if token[i].isdigit():
            val = 0
            while (i < len(token) and
                token[i].isdigit()):
                val = (val * 10) + int(token[i])
                i += 1
            if i<len(token) and token[i]=='.':
                i+=1
                flagValue = 0
                while (i < len(token) and
                    token[i].isdigit()):
                    val = (val * 10) + int(token[i])
                    flagValue+=1
                    i += 1
                val = val / (10 ** flagValue)
        elif token[i] == "-":
            i+=1
            val = 0
            while (i < len(token) and
                token[i].isdigit()):
                val = (val * 10) + int(token[i])
                i += 1
            if i<len(token) and token[i]=='.':
                i+=1
                flagValue = 0
                while (i < len(token) and
                    token[i].isdigit()):
                    val = (val * 10) + int(token[i])
                    flagValue+=1
                    i += 1
                val = val / (10 ** flagValue)
            val = val * (-1)
        else:
            raise Exception("Error at " + str(lineNo) + " -> Number '"+words[1]+"' doesn't exist")
        #print(val)
        return val
    elif isArray(word = words[1], obj = obj, ret = False):
        word = isArray(word = words[1], obj = obj, ret = True)
        return arrayElements.get(word)
    else:
        raise Exception("Error at " + str(lineNo) + " -> Variable '"+words[1]+"' doesn't exist")
 
def processArr(words,obj,code):
    if (len(words)<3):
        raise Exception("Error at " + str(lineNo) + " -> Invalid Syntax " + words[0])
    if isVariable(words[1]):
        if isNumber(words[2]) and int(words[2])>0:
            j = 0
            text = words[1] + "-len"
            inmemory = generateRandomVariable()
            texting = "$" + inmemory + "-len"
            arrayElements[texting] = int(words[2])
            obj.variables[text] = texting
            while j < int(words[2]):
                text = "$" + inmemory + "-" + str(j)
                arrayElements[text] = 0
                j+=1
        elif isVariable(words[2]) and words[2] in  obj.variables.keys():
            num = int(obj.variables.get(words[2]))
            j = 0
            text = words[1] + "-len"
            inmemory = generateRandomVariable()
            texting = "$" + inmemory + "-len"
            arrayElements[texting] = int(num)
            obj.variables[text] = texting
            while j < int(num):
                text = "$" + inmemory + "-" + str(j)
                arrayElements[text] = 0
                j+=1
        else:
            raise Exception("Error at " + str(lineNo) + " -> Invalid Length of Array ")
    else:
        raise Exception("Error at " + str(lineNo) + " -> Invalid Array Name ")
    ##print("variables -> ", obj.variables, "\nArray Elements -> ",arrayElements)
        
 
#############################  Execution Module  ##############################

'''
    This module deals with unpacking each line to be executed
    and then interpret the line and execute it.
'''

# It interprets each line clasifies the line as a 'addVariable' job 
# or a 'processKeyword' job and calls these methords accordingly
def interpret(line,obj,code):
    global lineNo,time
    timenow= datetime.now()
    timenow = timenow.strftime("%M")
    sub = int(str(timenow)) - int(str(time))
    
    #Time Out 
    if sub > 1:
        raise Exception("Runtime Error -> Time Out")
    
    words = line.split(" ")
    if len(line)==0:
        return
    
    if isVariable(words[0]):
        addVariable(words,obj)
        return True
    
    elif isKeyword(words[0]):
        return processKeyword(words,obj,code)
    
    else:
        raise Exception("Error at " + str(lineNo) + " -> Line starts with an unidentified line " + line)
        
# It processes each line of the code and send it to the interpretter to
# interpret. It does that until it reaches the end of the block its in.
def startExecution(mainStart,mainEnd,code,obj):
    global lineNo
    lineNo = mainStart
    lineNo = lineNo+1
    line = code[lineNo]
    while len(line)==0:
        lineNo += 1
        line = code[lineNo]
    notExitFromLoop = True
    while lineNo!=mainEnd:
        
        notExitFromLoop = interpret(line,obj,code)
        #print("variables -> ", obj.variables, "\nArray Elements -> ",arrayElements)
        #print()
        #print()
        

        if len(line) > 3 and line[0]=="R" and line[1]=="E" and line[2]=="T":
            if notExitFromLoop !=None:
                return notExitFromLoop
            
        if not notExitFromLoop:
            if(line[0] == "E" and line[1]=="X" and line[2]=="I" and line[3]=="T"):
                #print("EXIT")
                return False
        #print(lineNo,line)
        lineNo+=1
        
            
        line = code[lineNo]
        while len(line)==0:
            lineNo+=1
            line = code[lineNo]
         
    return True

##############################  Main Module  ##################################

# It preprocesses the code and removes all the indentation from it.
# Then it feeds the code starting from the main block.
def main():
    global lineNo, time
    file = input("Enter the file name: ")
    #file = "Normal Search.txt"
    file = open(file, "r")
    code = file.readlines()
    file.close()
    #print("                   Code\n")
    #print(code,"\n\n")
    name,type=None,None
    while lineNo < len(code):
        line = code[lineNo]
        
        if line[-1]=='\n':
            line = line.rsplit(line[-1])
            line = line[0]
            code[lineNo] = line
        if len(line)>0:
            i =0
            while len(line)>i and (line[i]==' ' or line[i] == '\t'):
                i+=1
                #print(i)
            
            if i!=0:
                temp = ""
                while i<len(line):
                    temp+=line[i]
                    i+=1
                line = temp
                code[lineNo]=line
            #print(lineNo,"\t-> ",line)
          
        lineNo +=1
        if(len(line)==0):
            continue
        if(line[0]=="#"):
            #print("in",code[lineNo-1])
            code.pop(lineNo-1)
            lineNo = lineNo - 1
            continue
            
           
        name,type=initiate(line,name,type)
        #print("Line -> ",lineNo)
        #print("functions -> ", functions)
        #print("Start Parenthesis -> ", startParenthesis)
        #print("End Parethesis -> ", endParenthesis)
        #print("Stack -> ", stack)
        #print()
        #print()
    #print(code)
    #print("functions -> ", functions)
    #print("##############################################################")
    if len(stack)!=0:
        raise Exception("Compile time Error with parenthesis -> Closinng Parenthesis Missing")
    for fun1 in functions:
        for fun2 in functions:
            if fun1!=fun2:
                (start1,end1) = functions.get(fun1)
                (start2,end2) = functions.get(fun2)
                if start1 > start2 and start1 < end2:
                    raise Exception("Error at " + str(start1) + " Compile time Error with fucntions -> funtion '" + fun1 + "' declared inside funtion '" + fun2 +"'")
                    
    if "main" in functions:
        mainStart = functions["main"]
        mainEnd = mainStart[1]
        mainStart = mainStart[0]
        obj = function("main",mainStart,mainEnd,[])
        functionStack.append(obj)
        #print(mainStart," -> ",code[mainStart])
        #print(mainEnd-1," -> ",code[mainEnd-1])
        print()
        print("                   Output\n")
        time= datetime.now()
        time = time.strftime("%M")
        
        
        startExecution(mainStart,mainEnd-1,code,obj)
        
    else:
        raise Exception("Compile time Error -> no 'main' found")

# It starts the whole process and makes sure that if an exception 
# is thrown then it catches it and desplays it properly.
#main()

try:
    main()
    inp = input()
except Exception as e:
    print("###########################################################\n",e)
    inp = input()
