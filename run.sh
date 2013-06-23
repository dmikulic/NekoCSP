#!/bin/sh


if [ -f /tmp/foo.txt ]; then
    echo "File not found!"
fi

PASSED=$1

if [ -f "${PASSED}" ] ; then
	python nekocsp.py ${PASSED}
	python zeptosat.py problem.cnf > result.cnf
	#cryptominisat problem.cnf > result.cnf
	python unmapper.py
	rm problem.cnf problem.map result.cnf
else
	echo "Argument missing or not a file"
fi
