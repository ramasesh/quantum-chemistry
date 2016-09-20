import numpy as np
from __future__ import division

rho_unconst = blah;


"""extract eigenvalues and eigenvectors of the unconstrained matrix.   In general the estimate we get from the unconstrained MLE method will be unphysical, i.e. will have negative eigenvalues.  If this is not the case, the unconstrained estimate is the correct ML density matrix, so we go ahead and use it."""
[eigvals_un, eigvecs_un ] = np.linalg.eig(rho_unconst)
d = len(eigvalus_un) # the dimension of the Hilbert space
""" check if an eigenvalues is negative"""
if min(eigvals_un) >= 0:
    rho_const = rho_unconst
else:
    """in the case where the unconstrained estimate was unphysical, we find the nearest (in the sense of the 2-norm) physical density matrix to the unconstrained estimate rho_unconst.  We use the algorithm specified by PhysRevLett.108.070502"""
    """Because the 2-norm is basis independent, it is easy to see that the rho_const and rho_unconst must have the same eigenbasis.  So the problem is just to find the eigenvectors of rho_const, all of which must be greater than or equal to zero, which give the smallest 2-norm distance to rho_unconst"""
    """First, we sort the eigenvalues and eigenvectors by the eigenvalue"""
    eigvals_un_sort = sorted(eigvals_un)
    eigvecs_un_sort = [y for (x,y) in sorted(zip(eigvals_un,eigvecs_un), key = lambda pair: pair[0])]


    eigvals_un_sort = sorted(eigvals_un)
    eigvals_un_sort.reverse()

    """Then we proceed with the algorithm in the above reference"""
    eigvals_sort = list(eigvals_un_sort)
    i = d
    a = 0 #accumulator
    while eigvals_un_sort[i-1]+a/i < 0:
        eigvals_sort[i-1]=0
        a = a + eigvals_un_sort[i-1]
        i = i -1
    for j in range(i):
        eigvals_sort[j] = eigvals_sort[j] + a/i

    """Now we form the new matrix"""
    rho_const = sum([y*dot(z,z.get(H)) for (y,z) in zip(eigvals_sort, eigvecs_un_sort)])









