# import dependencies
import numpy as np

# import affine scaling method from HW5
def affine_scaling(x, A, c, tol = 1e-9):
    """
    Solves a linear programming problem using the affine scaling method.
    Inputs:
        x: Initial feasible solution (i.e. Ax = b) (numpy array)
        A: Coefficient matrix (numpy array)
        c: Cost vector (numpy array)
        tol: Tolerance for convergence (default is 1e-5)
    Outputs:
        x: Optimal solution (numpy array)
    """
    alpha = 0.9 # step size reduction factor (other option is 0.99)
    x = x
    n = x.shape[0]

    while True:
        # create D_k
        D = np.diag(x)

        # compute A_hat_k
        A_hat = A @ D

        # compute projection P_hat_k
        P_hat = np.identity(n) - A_hat.T @ np.linalg.inv(A_hat @ A_hat.T) @ A_hat

        # compute gradient direction d_k
        d = -D @ P_hat @ D @ c

        # calculate largest step size
        r = np.min(- x[d < 0] / d[d < 0])
        a = alpha * r

        # calculate new point
        x_new = x + a * d

        # check tolerance
        if np.abs(np.dot(c, x_new) - np.dot(c, x)) / max(1, np.abs(np.dot(c,x))) < tol:
            break
        else:
            x = x_new
    return x 

def two_phase_affine_scaling(A, b, c, u):
    """
    Solves a linear programming problem using the two-phase affine scaling method.
    Inputs:
        A: Coefficient matrix (numpy array)
        b: Right-hand side vector (numpy array)
        c: Cost vector (numpy array)
        u: aribitrary positive vector (numpy array)
    Outputs:
        x: feasible solution (numpy array)
    """
    # check if u is already a feasible solution
    v = b - A @ u
    if np.linalg.norm == 0:
        return u

    n = A.shape[1]

    # create variables for affine scaling of artifical problem 
    A_hat = np.column_stack((A, v.reshape(-1, 1)))
    c_hat = np.append(np.zeros(n), 1.0)
    x_hat = np.append(u, 1.0)

    # solve the artificial problem using affine scaling
    x_0 = affine_scaling(x_hat, A_hat, c_hat)[:n]

    # perform phase 2 using x_0 as initial feasible point 
    x = affine_scaling(x_0[:n], A, c)
    return x