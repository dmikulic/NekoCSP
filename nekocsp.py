#!/usr/bin/python
'''
NekoCSP - 2013

2013 Darko Mikulic, All rights reserved
'''

from itertools import product, combinations

sat_var_counter = 1

csp_variables = {}
sat_variables = {}

constraints = []
cnf_formula = []

def init_sat_variables():
    global sat_var_counter
    for var in sorted(csp_variables.keys()):
        var_len = len(csp_variables[var])
        sat_variables[var] = range(sat_var_counter, sat_var_counter + var_len)
        sat_var_counter += var_len


def at_least_one():
    for var in csp_variables:
        cnf_formula.append(sat_variables[var])


def at_most_one():
    for var in csp_variables:
        for c in combinations(sat_variables[var], 2):
            cnf_formula.append([-x for x in c])


def convert_consraints():
    for f in constraints:
        fvars = f.func_code.co_varnames
        fdoms = tuple([csp_variables[var_name] for var_name in fvars])
        doms_product = product(*fdoms)

        for values in doms_product:
            issat = f(*values)
            if not issat:
                idxs     = [csp_variables[var].index(val) for var,val in zip(fvars,values)]
                sat_vars = [sat_variables[var][idx] for var,idx in zip(fvars,idxs)]
                clause = [-x for x in sat_vars]
                cnf_formula.append(clause)


def alldifferent(li):
    pairs = combinations(li,2)
    for x in pairs:
        tmp = "constraints.append(lambda %(1)s,%(2)s: %(1)s != %(2)s)"
        for f,s in pairs:
            exec(tmp % {'1':f, '2':s})

def isequal(var, value):
    tmp = "constraints.append(lambda %(1)s: %(1)s == %(2)s)"
    exec(tmp % {'1': var, '2':value})


#################

def main():
    import sys
    if len(sys.argv) > 1:
        #try:
            ulaz = open(sys.argv[1],'r').read()
            exec ulaz in globals()

            init_sat_variables()
            at_least_one()
            at_most_one()
            convert_consraints()


            num_clause = len(cnf_formula)
            num_literals = sum([len(csp_variables[x]) for x in csp_variables])

            f = open("problem.cnf", 'w')
            f.write("p cnf %s %s\n" % (num_literals, num_clause))
            for x in cnf_formula:
                line = " ".join(map(str, x + [0])) + '\n'
                f.write(line)
            f.close()

            f = open("problem.map", 'w')
            for var in sorted(sat_variables.keys()):
                cvals = csp_variables[var]
                svals = sat_variables[var]
                cout = "%s=%s\n" % (var, ",".join(map(str, cvals)))
                sout = "%s#%s\n" % (var, ",".join(map(str, svals)))
                f.write(cout)
                f.write(sout)
            f.close()
        #except:
        #    print "Wrong format"
    else:
        print "No argument"

if __name__ == "__main__":
    main()