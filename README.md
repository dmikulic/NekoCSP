### Instructions

NekoCSP uses Direct encoding to convert the CSP problem to the CNF form
and then utilizes a SAT solver to find a solution

python nekocsp.py examples/example1.py 

python zeptosat.py problem.cnf > result.cnf
OR
cryptominisat problem.cnf > result.cnf

python unmapper.py




The other option is to run the shell script "run.sh"

./run.sh examples/example1.py 



To install CryptoMiniSat go to:
https://github.com/msoos/cryptominisat


