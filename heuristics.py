# =============================
# Student Names:
# Group ID:
# Date:
# =============================
# CISC 352 - W23
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

1. ord_dh (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Degree heuristic

2. ord_mv (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Minimum-Remaining-Value heuristic


var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    Variables and constraints of the problem. The assigned Variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return next Variable to be assigned according to the Degree Heuristic '''
    # IMPLEMENT
    variable = None
    degree = 0 
    unassigned_vars = csp.get_all_unasgn_vars()  
    
    

    for var in unassigned_vars:
        cons_list = csp.get_cons_with_var(var)
        
        fixed_cons_list = [con for con in cons_list if con.get_n_unasgn() > 1]
        
        if len(fixed_cons_list) > degree:
            variable = var
            degree = len(fixed_cons_list)
        elif len(fixed_cons_list) == degree:
            if variable is None or len(var.cur_domain()) < len(variable.cur_domain()):
                variable = var
            
    
    return variable

def ord_mrv(csp):
    ''' return Variable to be assigned according to the Minimum Remaining Values heuristic '''
    # IMPLEMENT
    variable = None
    degree = float('inf') 
    unassigned_vars = csp.get_all_unasgn_vars()
    
    for var in unassigned_vars:
        domain_size = var.cur_domain_size()
        if domain_size < degree:
            variable = var
            degree = domain_size
            
    
    return variable
