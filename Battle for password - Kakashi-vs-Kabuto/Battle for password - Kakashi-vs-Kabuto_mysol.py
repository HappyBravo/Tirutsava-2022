numbers = [str(i) for i in range(10)]
symbols = ["#", "*", "&"]
alphabets = [chr(i) for i in range(97,123)]
# our_pass = ""
# print(alphabets, number, symbol)

testcase, stringlen = map(int, input().split())
inputstrings = []
number_index = []
symbol_index = []
alphabet_index = []

def check(s):
    for _ in range(len(list(s))):
        done = 0
        if list(s)[_] in numbers:
            number_index.append(_)
            done = 1
            # break
        if list(s)[_] in alphabets:
            alphabet_index.append(_)
            done = 1
            # break
        if list(s)[_] in symbols:
            symbol_index.append(_)
            done = 1
            # break
        # if done==1:
        #     break
        
    
def check_num(s):
    # print(s)
    for _ in range(len(list(s))):
        if list(s)[_] in numbers:
            number_index.append(_)
            break
            
def check_alpha(s):
    # print(s)
    for _ in range(len(list(s))):
        if list(s)[_] in alphabets:
            alphabet_index.append(_)
            break

def check_sym(s):
    # print(s)
    for _ in range(len(list(s))):
        if list(s)[_] in symbols:
            symbol_index.append(_)
            break
            

for i in range(testcase):
    inputstring = input()
    # check_num(inputstring)
    # check_alpha(inputstring)
    # check_sym(inputstring)
    check(inputstring)
# print(number_index)
# print(alphabet_index)
# print(symbol_index)

print(min(number_index)+min(alphabet_index)+min(symbol_index))
