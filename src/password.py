import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
if len(password)<16 and len(password)>6:
    (b,c,d,e)=0,0,0,0
    for a in password:
        if a.islower():
            b=1
        elif a.isupper():
            c=1
        elif a.isnumeric():
            d=1
        elif a in"$#@":
            e=1
    if b+c+d+e==4:
        is_valid=True

    

print(is_valid)
