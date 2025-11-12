
import numpy as np, pandas as pd
from math import sin, cos, exp, radians
from scipy.optimize import least_squares

df = pd.read_csv("xy_data.csv")
n = len(df)
t = np.linspace(6, 60, n)
x_obs = df["x"].values
y_obs = df["y"].values

def model(p):
    th_deg, M, X = p
    th = radians(th_deg)
    s = np.sin(0.3*t)
    e = np.exp(M*np.abs(t))
    x = t*np.cos(th) - e*s*np.sin(th) + X
    y = 42 + t*np.sin(th) + e*s*np.cos(th)
    return x, y

def residuals(p):
    x,y = model(p)
    return np.concatenate([x-x_obs, y-y_obs])

lb=[0.0,-0.05,0.0]; ub=[50.0,0.05,100.0]
x0=[20.0,0.0,50.0]
res = least_squares(residuals, x0, bounds=(lb,ub))
th_deg, M, X = res.x
print(f"Theta(deg)={th_deg:.6f}, M={M:.6f}, X={X:.6f}")
