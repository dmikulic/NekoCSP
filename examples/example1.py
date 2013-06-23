

csp_variables['x'] = [2,3,4,5,6]
csp_variables['y'] = [2,3,4,5,6]

constraints = [
    lambda x, y: x + y <= 7,
    lambda x, y: x == 3 and y == 4,
]