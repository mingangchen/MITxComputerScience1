#problem1 Counting Vowels
s = 'azcbobobegghakl'
vowels = 'aeiou'
def vowelsCount(s):
    count = 0
    for a in s:
        if a in vowels:
            count = count + 1
    return count

total = vowelsCount(s)
print "Number of vowels: " + str(total)


#problem2 Counting Bobs
s = 'azcbobobegghakl'

def countBobs(s):
    numBobs = 0
    for i in range(1, len(s)-1):
        if s[i-1:i+2]=='bob':
            numBobs += 1
    return numBobs
bobs = countBobs(s) 
print 'Number of times bob occurs is:', bobs


#problem3 Counting and Grouping
order = "salad water hamburger salad hamburger"

def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    
    startspace = 0    
    space = 0
    while space > -1:
        space = order.find(' ', startspace)
        if space == -1:
            word = order[startspace:]
        else:
            word = order[startspace:space]
        if word == "salad":
            salad += 1
        if word == "hamburger":
            hamburger += 1
        if word == "water":
            water += 1
        startspace = space+1
    neworder = "salad:"+str(salad)+" hamburger:"+str(hamburger)+" water:"+str(water)
    return neworder

s = item_order(order)
print s
    
    
    




