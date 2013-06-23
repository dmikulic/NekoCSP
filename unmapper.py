#!/usr/bin/python
'''
UnMapper - 2013
Reads a map file
Reads a satisfiable formula

Prints satisfiable CSP values

2013 Darko Mikulic, All rights reserved
'''

csp_vars = {}
sat_vars = {}

def map_solution(var):
    for x in sat_vars:
        if var in sat_vars[x]:
            idx = sat_vars[x].index(var)
            print "%s: %s" % (x, csp_vars[x][idx])

def main():
    f1 = open("problem.map", 'r').read().splitlines()
    f2 = open("result.cnf", 'r').read().splitlines()

    for line in f1:
        if "=" in line:
            var, data = line.split("=")
            csp_vars[var] = map(int,data.split(','))
        elif "#" in line:
            var, data = line.split("#")
            sat_vars[var] = map(int,data.split(','))

    for line in f2:
        if line and line[0] in ['v']:
            line = line[2:]
            solution = map(int,line.split())
        else:
            solution = []

    if solution:
        s = [x for x in solution if x > 0]
        for x in s:
            map_solution(x)

if __name__ == "__main__":
    main()
    print "END"