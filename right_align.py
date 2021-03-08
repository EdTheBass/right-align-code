import sys

if len(sys.argv) != 3:
    raise AttributeError("Input/output file not supplied.")

if not open(sys.argv[1], "r"):
    raise FileNotFoundError("File not found.")

with open(sys.argv[1], "r") as inp_f:
    with open(sys.argv[2], "w") as out_f:
        to_write = []
        for line in inp_f.readlines():
            ra_line = " " * (120 - len(line)) + line
            to_write.append(ra_line)
        out_f.writelines(to_write)
        out_f.close()
    inp_f.close()
