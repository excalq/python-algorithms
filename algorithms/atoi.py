    # Write atoi() in Python3... 
# Spec: print an integer, ignore non-int/sign chars w/o raising exception
#
# To solve:
# convert ascii val to int
# 1. Each position is base * int (1,10,100,1000, etc...)
# 2. Sign will be '-' (start assuming first char)
# 3. Discard non int chars (letters, decimals, etc. (Do decimals later as atof()))
# 4. When we gat to 'atoi(1.34)' start with -> 134, refactor to -> 1

def atoi(astr, base=10):
    """takes a string and prints the numeric value found in it
    
    For example: atoi('8') -> 8; atoi('-32') -> -32; atoi('fred') -> 0
    """
    res = 0
    sign = -1 if astr[0] == '-' else 1 # Assuming first char is sign
    for i in astr:
        if i < '0' or i > '9':
            if res != 0: # The '1.34' -> 1 refactor
                break # Return what we've parsed already
            else:
                continue # Keep iterating until a number is found
        res = (res * base) + (ord(i) - ord('0'))
    return sign * res

print(atoi('5'))       # 5
print(atoi('50'))      # 50
print(atoi('93893'))   # 93893
print(atoi('-1'))      # -1
print(atoi('1.34'))    # 134 (ignore decimals for now. 1 would be better!)
print(atoi('0'))       # 0
print(atoi('bob0'))    # 0
print(atoi('hunter2')) # 2