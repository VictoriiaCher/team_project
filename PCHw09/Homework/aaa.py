import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--add")
parser.add_argument("--change")
args = parser.parse_args()
print(args.add)
