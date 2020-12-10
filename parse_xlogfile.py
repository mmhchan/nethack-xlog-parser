import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help = 'input xlogfile name')
    parser.add_argument('output', help = 'output csv name')
    args = parser.parse_args()

    #'xlogfile.nh361.csv'
    with open(args.input, "r") as input_file:
        first_line = True

        for line in input_file:
            # Need a header
            if first_line == True:
                header = re.findall('[\w]+(?=\=)', line)
                out_string = ','.join(header)
                first_line = False

            # Values
            m = re.findall('(?<==)[\w+.-]+', line)
            out_string += '\n' + ','.join(m)

    with open(args.output, "w") as output_file:
        output_file.write(out_string)

if __name__ == "__main__":
    main()