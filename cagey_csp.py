# =============================
# Student Names:
# Group ID:
# Date:
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc:
#

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all Variables in the given csp. If you are returning an entire grid's worth of Variables
they should be arranged linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional Variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 0.5/3 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *
from itertools import permutations
from itertools import product

def binary_ne_grid(cagey_grid):
    ##IMPLEMENT
    n = cagey_grid[0]
    variables = []
    csp = CSP('binary_ne_grid')
    domain = list(range(1,n+1))

    for row in range(1,n+1):
        for col in range(1,n+1):
            variable_name = f"cell_{row}_{col}"
            var = Variable(variable_name, domain)
            variables.append(var)
            csp.add_var(var)

    satisfying_tuples = []
    for cell1, cell2 in product(domain,domain):
        if cell1 != cell2:
            satisfying_tuples.append((cell1,cell2))

    for row in range(1,n+1):
        for col in range(1,n+1):
            if col != n:
                for row_constraint in range(col+1, n+1):
                    cell1 = variables[(row-1) * n + (col - 1)]
                    cell2 = variables[(row-1) * n + (row_constraint - 1)]
                    constraint_name = f'Row_{row}_Constraint_{col}_{row_constraint}'
                    constraint = Constraint(constraint_name, [cell1, cell2])
                    constraint.add_satisfying_tuples(satisfying_tuples)
                    csp.add_constraint(constraint)
            if row != n:
                for col_constraint in range(row+1, n+1):
                    cell1 = variables[(row-1) * n + (col - 1)]
                    cell2 = variables[(col_constraint - 1) * n + (col - 1)]
                    constraint_name = f'Col_{col}_Constraint_{row}_{col_constraint}'
                    constraint = Constraint(constraint_name, [cell1, cell2])
                    constraint.add_satisfying_tuples(satisfying_tuples)
                    csp.add_constraint(constraint)
    return csp, variables


def nary_ad_grid(cagey_grid):
    ## IMPLEMENT
    N, cages = cagey_grid
    csp = CSP("N-ary_Grid_Only_Cagey")
    variables = []
    
    domain = []
    for i in range(1, N+1):
        domain.append(i)

  
    for row in range(1, N + 1):
        rows = []
        for column in range(1, N + 1):
            var = Variable("V{}{}".format(row,column), domain)
            rows.append(var)
            csp.add_var(var)
        variables.append(rows)

    tuple_list=[]
    for tuple in permutations(list(range(1, N + 1)), N):
        tuple_list.append(tuple)
        
    for i in range(N):
        row_vars = variables[i]
        con = Constraint(f"Row_{i}", row_vars)
        con.add_satisfying_tuples(tuple_list)
        csp.add_constraint(con)

        col_vars = [variables[j][i] for j in range(N)]
        con = Constraint(f"Col_{i}", col_vars)
        con.add_satisfying_tuples(tuple_list)
        csp.add_constraint(con)

    return csp, variables

def cagey_csp_model(cagey_grid):
    ##IMPLEMENT
    pass
