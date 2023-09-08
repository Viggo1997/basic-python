
# Print the pattern


for n in range(1,10):
    if n==1:
        b="*"
    elif n>=6:
        p=9-n
        j="*"
        b=j+" *"*p
    else:
        b+=" *"
    print(b)
    