
instance = ((0,0,0,0,9,4,0,3,0),
            (0,0,0,5,1,0,0,0,7),
            (0,8,9,0,0,0,0,4,0),
            (0,0,0,0,0,0,2,0,8),
            (0,6,0,2,0,1,0,5,0),
            (1,0,2,0,0,0,0,0,0),
            (0,7,0,0,0,0,5,2,0),
            (9,0,0,0,6,5,0,0,0),
            (0,4,0,9,7,0,0,0,0))



arr = [ ["x%s%s" % (i+1, j+1) for j in range(9) ] for i in range(9) ]

for x in arr:
    for name in x:
        csp_variables[name] = range(1,10)


for i in range(9):
    alldifferent(arr[i])

for i in range(9):
    alldifferent([x[i] for x in arr])

for i0 in range(3):
    for j0 in range(3):
         alldifferent([ arr[3*i0 + i][3*j0 + j] for i in range(3) for j in range(3) ])


for i in range(9):
    for j in range(9):
        if instance[i][j] != 0:
            isequal(arr[i][j], instance[i][j])