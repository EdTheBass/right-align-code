import sys

if len(sys.argv) != 3:
    raise Exception("Usage: python right_align.py input-file output-file.")

if not open(sys.argv[1], "r"):
    raise FileNotFoundError("Input file not found.")

with open(sys.argv[1], "r") as inp_f:
    with open(sys.argv[2], "w") as out_f:
        to_write = []
        for line in inp_f.readlines():
            ra_line = " " * (100 - len(line)) + line
            to_write.append(ra_line)
        out_f.writelines(to_write)
