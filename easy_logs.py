/*
Easy Logs Python Kata 8 kyu

Description:

Add two logs with base X, with the value of A and B. Example log A + log B where the base is X.

*/


/* Solution: */

import math
def logs(x, a, b):
    logs = (math.log(a * b)/ math.log(x))
    return logs
    pass