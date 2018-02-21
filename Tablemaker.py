import numpy as np


lijst = [21, 52, 53283, 5081, 282, 13, 5257, 5503, 2099, 5035, 5609, 40, 5280, 417, 5188, 5008, 104, 2639, 255, 2448, 10674, 60152, 64, 5567]
b = np.zeros(shape=(24,62))


for i in range(len(lijst)):
    
    name = "home/roozemond/Desktop/AGNfitter-master/OUTPUT/" + str(lijst[i]) + "/parameter_outvalues_" + str(lijst[i]) + ".txt"
    a = np.loadtxt(name, skiprows = 4)
    
    b[i][0] = i
    b[i][1] = lijst[i]
    
    #First the minimum (error) "parameter_e":
    for j in range(20):
        b[i][j+2] = a[2][j]
    
    #The maximum error "parameter_ep":
    for j in range(20):
        b[i][j+22] = a[3][j]
        
    #The "actual" value "parameter":
    for j in range(20):
        b[i][j+42] = a[1][j]
        
np.savetxt("THETABLE.txt", b)
