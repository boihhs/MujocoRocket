import numpy as np

def convertThrust(thrust):
    p = np.linalg.norm(thrust)
    degree = np.atan(thrust[1]/thrust[0])/np.pi*180
    phi = np.acos(thrust[2]/p)/np.pi*180
    print("mag: " + str(p) + ", degree: " + str(degree) + ", phi: " + str(phi))
    
def limitThrust(thrust, thrustLimit, phiLimit): #everything is in radians
    p = np.linalg.norm(thrust)
    degree = np.atan(thrust[1]/thrust[0])
    phi = np.acos(thrust[2]/p)
    phiDeg = phi/np.pi*180
    
    if (p > thrustLimit and phi > phiLimit):
        return np.array([thrustLimit*np.sin(phiLimit)*np.cos(degree), thrustLimit*np.sin(phiLimit)*np.sin(degree), thrustLimit*np.cos(phiLimit)])
    
    elif (p > thrustLimit):
        return np.array([thrustLimit*np.sin(phi)*np.cos(degree), thrustLimit*np.sin(phi)*np.sin(degree), thrustLimit*np.cos(phi)])
    
    elif (phi > phiLimit):
        return np.array([p*np.sin(phiLimit)*np.cos(degree), p*np.sin(phiLimit)*np.sin(degree), p*np.cos(phiLimit)])
    
    else:
        return thrust