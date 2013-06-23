#!/usr/bin/python
'''
ZeptoSAT - 2013
# f - forumla
# c - clause
# l - literal
# r - result

2013 Darko Mikulic, All rights reserved
'''

def dpll(f,r):
    f, r = unitpropagate(f,r)
    f, r = pureLiteralAssign(f,r)
    if not f:
        return sorted(r, key=abs)
    elif [] in f:
        return False
    else:
        l = chooseLiteral(f)
        t = dpll(simplify(f,l),[l]+r)
        return t if t else dpll(simplify(f,-l),[-l]+r)

def simplify(f, l):
    simplifyClause = lambda c,l: [lx for lx in c if lx != -l]
    return [simplifyClause(c, l) for c in f if not l in c]

def chooseLiteral(f):
    literals = [l for c in f for l in c]
    return literals[0] if literals else None


def unitpropagate(f,r):
    u = next(iter(c[0] for c in f if len(c) == 1), None)
    if u:
        return unitpropagate(simplify(f, u), [u]+r)
    else:
        return f,r

def pureLiteralAssign(f,r):
    literals = list(set([l for c in f for l in c]))
    pure = [l for l in literals if not -l in literals]
    eliminate = lambda c: list(set(pure).intersection(c))
    return [c for c in f if not eliminate(c)], pure + r


def parse_dimacs(data):
    data = [x.strip() for x in data]
    data = [x[:-2].split() for x in data if x and x[0] not in ['c','p','%','0']]
    toint = lambda li: [int(x) for x in li]
    data = [toint(x) for x in data]
    return data


def main():
    import sys
    if len(sys.argv) > 1:
        #try:
            f = open(sys.argv[1], 'r')
            cnf = parse_dimacs(f.read().splitlines())
            out = dpll(cnf, [])
            if out:
                print "v " + " ".join(map(str, out))
            else:
                print out
        #except:
        #    print "Wrong format"
    else:
        print "No argument"

if __name__ == "__main__":
    main()