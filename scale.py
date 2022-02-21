import numpy as np
input_matrix=[[13,25,1,0,0,0,-247,-475,-19],
   [0,0,0,13,25,1,-455,-875,-35],
  [32,53,1,0,0,0,-1376,-2279,-43],
   [0,0,0,32,53,0,-1792,-2968,-56],
  [60,75,1,0,0,0,-3660,-4575,-61],
  [0,0,0,60,75,0,-4860,-6075,-81]]
input_matrix=np.array(input_matrix)

# computing multiplication of A-transpose and A to find the smallest value in each row

Homo=[]
def scalar(input_matrix):
    Result_matrix= np.dot(input_matrix.T,input_matrix)
    for i in Result_matrix:
        Homo.append(min(i))
    print(Homo)
scalar(input_matrix)
