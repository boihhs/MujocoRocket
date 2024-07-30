import numpy as np
import copy

class LQR:
    
    def __init__(self, A, B, Q, Qfinal, R, dt, seconds):
        self.A = A
        self.B = B
        self.Q = Q
        self.Qfinal = Qfinal
        self.R = R
        self.dt = dt
        self.seconds = seconds
        self.steps = int(seconds/dt)
        
    def inv(self,a):
        return np.linalg.inv(a)
        
    def fhlqr(self):
        P = np.zeros((self.steps, self.A.shape[0], self.A.shape[1]))
        K = np.zeros((self.steps - 1, self.B.shape[1], self.A.shape[1]))

        P[self.steps-1] = copy.deepcopy(self.Qfinal)

        for i in range(self.steps-2, -1, -1):
            K[i] = self.inv(self.R + self.B.T@P[i+1]@self.B)@self.B.T@P[i+1]@self.A
            P[i] = self.Q + self.A.T@P[i+1]@(self.A-self.B@K[i])

        return K