from sys import argv


def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)


def checksum(words):
    s = 0
    for w in words:
        s = carry_around_add(s, w)
    return ~s & 0xffff

if __name__ == "__main__":
    words = map(int, argv[1:])
    cksum = checksum(words)
    print "checksum: %s %s" % (cksum, bin(cksum))
