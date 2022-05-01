import numpy as np
input_matrix=[[12.7,38.1,1498.6,1,0,0,0,0,-2286,-6858,-269748,-180],
   [0,0,0,0,12.7,38.1,1498.6,1,-660.4,-1981.2,-77927.2,-52],
  [38.1,12.7,1498.6,1,0,0,0,0,-5867.4,-1955.8,-230784.4,-154],
   [0,0,0,0,38.1,12.7,1498.6,1,-2933.7,-4889.5,-115392.2,-77],
[63.5,38.1,1498.6,1,0,0,0,0,-11366.5,-6819.9,-268249.4,-179],
   [0,0,0,0,63.5,38.1,1498.6,1,-6477,-3886.2,-152857.2,-102],
    [88.9,12.7,1498.6,1,0,0,0,0,-9494,-6363,-101,-153],
   [0,0,0,0,88.9,12.7,1498.6,1,-12502,-8379,-133,-123],
[114.3,38.1,1498.6,1,0,0,0,0,-9494,-6363,-101,-179],
   [0,0,0,0,114.3,38.1,1498.6,1,-12502,-8379,-133,-154],
   [139.7,12.7,1498.6,1,0,0,0,0,-9494,-6363,-101,-152],
   [0,0,0,0,139.7,12.7,1498.6,1,-12502,-8379,-133,-175]]
input_matrix=np.array(input_matrix)

# computing multiplication of A-transpose and A to find the smallest value in each row

Homo=[]
def scalar(input_matrix):
    Result_matrix= np.dot(input_matrix.T,input_matrix)
    Result = np.linalg.eig(Result_matrix)
    p_matrix=Result[1][np.where(Result[0]==min(Result[0]))[0][0]]
    p_matrix=np.array(p_matrix).reshape((3,4))
    return p_matrix
print(scalar(input_matrix))


#fundamental matrix computation:



