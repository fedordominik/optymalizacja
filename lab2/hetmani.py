
print "Maximize "
n=8
f = True
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n + 1):
        if f:
            f = False
        else:
            print '+',
        print chr(x) + str(y),
        

print "\n"     
print "Subject To "



for y in range(1,n+1):
    f=True
    for x in range(ord('a'),ord('a')+n):
        if f:
            f=False
        else:
            print '+',
        print chr(x) + str(y),
    print ' <= 1\n',
    
for x in range(ord('a'), ord('a') + n):
    f=True
    for y in range(1,n+1):
        if f:
            f=False
        else:
            print '+',
        print chr(x) + str(y),
    print ' <= 1\n',

y=1
for i in range(1,n+1):
    f=True
    y=i
    for x in range(ord('a'), ord('a') + i):
        if f:
            f=False
        else:
            print '+',
        print chr(x) + str(y),
        y=y-1
    print'<=1'
    
y=1
for i in range(1,n+1):
    f=True
    y=i
    for x in range(ord('a'), ord('a') +i):
        if f:
            f=False
        else:
            print '+',
        print chr(x+n-i) + str(y+n-i),
        y=y-1
    print'<=1'
    
y=1
for i in range(1,n+1):
    f=True
    y=1
    for x in range(ord('a'), ord('a') +i):
        if f:
            f=False
        else:
            print '+',
        print chr(x+n-i) + str(y),
        y=y+1
    print'<=1'
    
y=1
for i in range(1,n+1):
    f=True
    y=1
    for x in range(ord('a'), ord('a') +i):
        if f:
            f=False
        else:
            print '+',
        print chr(x) + str(y+n-i),
        y=y+1
    print'<=1'
     
    
    
print '\nBounds'

for y in range(1,n+1):
    for x in range(ord('a'),ord('a')+n):
        print chr(x) + str(y),
        print ' <= 1',
        print'\n',
        
print'\nGenerals'

for y in range(1,n+1):
    for x in range(ord('a'),ord('a')+n):
        print chr(x) + str(y)
        
print'\nEnd'
