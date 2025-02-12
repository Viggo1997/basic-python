import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        kode=[]
        for a in x:
            kode.append(hex(ord(a)))
        encoding = "".join(kode)
        print(encoding)

    case "decode":
        # Implement the decoding here
        ting=[]
        a=x.split("0x")
        a=a[1:len(a)]
        for p in a:
            e=int(p,base=16)
            ting.append(chr(e))   
        decoding = "".join(ting)
        print(decoding)
