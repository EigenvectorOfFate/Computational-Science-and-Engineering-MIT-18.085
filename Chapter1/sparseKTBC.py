import numpy as np
from scipy.sparse import spdiags
from scipy.linalg import toeplitz

def sparseKTBC(dtype = 'K', n = 10, sparse = False):
    """
    sparceKTBC Create finite difference model matrix.
    K=sparseKTBC(DTYPE,N,SPARSE) creates model matrix TYPE
    of size N-by-N. TYPE is one of the characters 'K', 'T'
    'B', or 'C'. The matrix is dense unless SPARSE is true.

    K=FDMODEL uses the defaults TYPE='K', N=10, and
    SPARSE=false.
    """
    e = np.ones(n)
    K = spdiags([[*-e], [*2*e], [*-e]], [-1,0,1], n, n, format='lil')
    if dtype == 'K':
        None
    elif dtype == 'T':
        K[0,0] = 1
    elif dtype == 'B':
        K[0,0] = 1
        K[n-1,n-1] = 1
    elif dtype == 'C':
        K[0,n-1] = -1
        K[n-1,0] = -1
    else:
        print('Unknown matrix type.')
            
    if sparse == False:
        return K.toarray()
    else:
        return K
