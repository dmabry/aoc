#!/usr/bin/env python3
import sys
from optparse import OptionParser
from pprint import PrettyPrinter


# Here we go!!!


def read_input(input_file):
    try:
        items = []
        with open(input_file) as f:
            for item in f:
                items.append(int(item))
    except:
        items = None

    return items


def part1(a):
    # add all items in an array and return sum
    try:
        out = sum(a)
    except:
        out = None

    return out


def part2(a):
    # add all items in an array and return sum
    found = False
    fqs = set()
    count = 0
    prev_fq = 0
    cur_fq = 0
    cur_sum = 0
    prev_sum = 0
    try:
        while not found:
            count = count + 1
            prev_sum = cur_sum
            for fq in a:
                prev_fq = cur_fq
                cur_fq = prev_fq + fq
                if cur_fq in fqs:
                    found = True
                    print(str(cur_fq))
                    break
                else:
                    fqs.add(cur_fq)

            cur_sum = cur_fq
            if (count % 10) == 0:
                print(str(count) + ", " + str(cur_sum))

        out = cur_fq, count
    except:
        out = None

    return out


if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option("-p", "--part", action="store", default=1,
                      dest="part", help="The API URL path to be used against the given management server API")
    parser.add_option("-i", "--input", action="store", default=None,
                      dest="inputfile", help="input file")

    (options, args) = parser.parse_args()

    if options.inputfile:
        input = read_input(options.inputfile)
        if not input:
            print("Oops! Something is wrong with the input file!")
            sys.exit(2)
    else:
        print("Please supply an input file to read from")
        sys.exit(1)

    pp = PrettyPrinter(indent=2)
    # pp.pprint(config)

    if options.part:
        part = int(options.part)
    else:
        part = 1

    # pp.pprint(input)

    if part == 1:
        # Part 1
        output = part1(input)
    else:
        # Part 2
        output = part2(input)

    # The result!
    pp.pprint(output)
