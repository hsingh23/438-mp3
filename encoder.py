from sys import argv
import getopt
from random import randint, random
from timeit import timeit
from collections import defaultdict


def parse_input(argv):
    help = "python encoder.py -g # [-k # -d #]"
    try:
        opts, args = getopt.getopt(
            argv, "hd:g:k:d:", ["help"])
    except getopt.GetoptError:
        print help
        exit(2)
    g, k, d = (None,) * 3
    for opt, arg in opts:
        if opt in ['-h', "help"]:
            print help
            exit(2)
        elif opt in ("-g"):
            g = int(arg)
        elif opt in ("-k"):
            k = int(arg)
        elif opt in ("-d"):
            d = int(arg)
    if not g:
        print "OI! You didn't supply one of the required values!!!!"
        print help
        exit(2)
    return g, k, d


def blen(x):
    return len(bin(x)) - 2


def bstr(data, length):
    return "0" * (length - blen(data)) + str(bin(data))[2:]


def crc(data, g, k):
    glen = blen(g)
    d = data << (glen - 1)
    g_shift = k - 1
    while g_shift >= 0:
        shifted = (g << g_shift)
        d = d ^ shifted
        g_shift = blen(d) - glen
    result = (data << (glen - 1)) + d
    return result, bstr(result, k + glen - 1)[-(glen - 1):]


def generate_table():
    table = {}
    for i in xrange(2 ** 16):
        table[i] = crc(i, 9, 16)[1]
    return table


def random_crc():
    crc(randint(0, 2 ** 16 - 1), 9, 16)


def check_error(p, times):
    table = generate_table()
    g, k = 9, 8
    result = defaultdict(lambda: 0)
    for i in xrange(times):
        data = 0
        for i in xrange(11):
            data += (1 << i) if random() < p else 0
        # from ipdb import set_trace; set_trace()

        error = 'f' if data == 0 else 't'
        if data in table:
            d = int(table[data])
        else:
            d = int(crc(data, g, k)[1])
        detected = 'f' if d == 0 else 't'
        result[error + detected] += 1
    print "%s Probability with %s Executions\nError Detected: %s\nError Not Detected: %s" % (p, times, float(result["tt"]) / times, float(result["tf"]) / times)


def random_crc_table(table):
    table[randint(0, 2 ** 16 - 1)]

if __name__ == "__main__":
    g, k, d = parse_input(argv[1:])
    if not k:
        print "Stats - 1000000 runs - random data"
        print "CRC: ", timeit(random_crc)
        print "CRC Table: ", timeit("table[randint(0, 2 ** 16 - 1)]", setup="from __main__ import *; table = generate_table()")
        check_error(.1, 10000)
        check_error(.2, 10000)
        check_error(.3, 10000)
    else:
        print crc(d, g, k)[1]
