import numpy as np
input_matrix=[[21.5,21.5,215,1,0,0,0,0,-1698.5,-1698.5,-20210,-94],
   [0,0,0,0,21.5,21.5,215,1,-1354.5,-1354.5,-13545,-63],
  [43,43,215,1,0,0,0,0,-5117,-5117,-25585,-119],
   [0,0,0,0,43,43,215,1,-3784,-3784,-18920,-88],
  [64.5,64.5,215,1,0,0,0,0,-9288,-9288,-30960,-144],
   [0,0,0,0,64.5,64.5,215,1,-7224,-7224,-24080,-112],
    [86,86,215,1,0,0,0,0,-14620,-14620,-36550,-170],
   [0,0,0,0,86,86,215,1,-12040,-12040,-30100,-140],
    [107.5,107.5,215,1,0,0,0,0,-20855,-20855,-41710,-194],
   [0,0,0,0,107.5,107.5,215,1,-17845,-17845,-35690,-166],
    [129,129,215,1,0,0,0,0,-28251,-28251,-47085,-219],
   [0,0,0,0,129,129,215,1,-24639,-24639,-41065,-191]]
input_matrix=np.array(input_matrix)

# computing multiplication of A-transpose and A to find the smallest value in each row

trans = []
def scalar(input_matrix):
    Homo=[]
    #print(input_matrix.shape)
    Result_matrix= np.dot(input_matrix.T,input_matrix)
    Result = np.linalg.eig(Result_matrix)
    p_matrix=Result[1][np.where(Result[0]==min(Result[0]))[0][0]]
    p_matrix=np.array(p_matrix).reshape((4,3))
    Homo = p_matrix
    return Homo
Homo = scalar(input_matrix)
#print(scalar(input_matrix))


def translation(intrinsic):
    k = np.array(intrinsic)
    inv_k = np.linalg.inv(k)
    #print(inv_k.shape)
    x,y = Homo.shape
    #print(np.dot(inv_k,trans))

intrinsic = [[1973.7366,230.4184,286.7137],[0,1942.5625,300.4901],[0,0,1]]
for i in range(1,len(Homo)+1):
    if(i%4 == 0):
        #print(Homo[i-1])
        trans.append(Homo[i-1])
        trans=np.array(trans).reshape((3,1))
translation(intrinsic)
arr = [[0.000,-0.003,-0.030],[0.004,0.000,0.095],[0.040,0.092,0.9800]]
print(arr)
