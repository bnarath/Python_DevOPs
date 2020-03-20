import numpy as np

def levenshtein_dist(str1, str2):
    '''
    Input: Two strings
    Output: lavenshtein matrix, lavenshtein dist 
    '''
    str1=str1.lower()
    str2=str2.lower()
    a, b = len(str2), len(str1)
    #Create a matrix of size(a+1, b+1)
    M=np.zeros(shape=(a+1,b+1), dtype=int)
    #Fill the 0th row and column
    M[:,0] = range(a+1)
    M[0,:] = range(b+1)
    #Fill the raws one by one
    for i in range(1,a+1):
        for j in range(1,b+1):
            #Last digit equal
            if str1[j-1]==str2[i-1]:
                M[i,j]=M[i-1, j-1]
            else:
                M[i,j] = min(M[i, j-1], M[i-1, j-1], M[i-1, j])+1
    return M, M[a,b]