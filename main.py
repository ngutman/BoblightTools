import sys
import re

def main():
    H = int(sys.argv[1])
    V = int(sys.argv[2])
    conf = open(sys.argv[3], "rb").read()

    lights = re.compile("\[light\].*?hscan.*?(\d*?) (\d*?)\s*?vscan\s*?(\d*?) (\d*?)\s", re.S).findall(conf)

    print "LED \t |\tHPOS\t|\tVPOS|"
    print "-------------------------------------"

    for i in xrange(len(lights)):
        light = lights[i]
        hpos_per = (int(light[0]) + int(light[1])) / 2.0
        vpos_per = (int(light[2]) + int(light[3])) / 2.0

        hpos = H * (hpos_per / 100.0)
        vpos = V - V * (vpos_per / 100.0)

        print "LED #" + str(i + 1).ljust(3),
        print "|\t" + str(hpos) + "\t|\t" + str(vpos)



if __name__ == "__main__":
    main()
