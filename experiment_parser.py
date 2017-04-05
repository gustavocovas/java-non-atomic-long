import sys

with open(sys.argv[1], 'rU') as f:
    lines = f.readlines()

longs = [l.strip("\n") for l in lines]

unique_longs = set(longs)

print("Read {} values, {} unique: ".format(len(longs), len(unique_longs)))
for long_str in unique_longs:
    print(long_str)
