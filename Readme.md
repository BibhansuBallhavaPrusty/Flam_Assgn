# Parametric Curve Fit — Unknowns (θ, M, X)

**Fitted parameters** (bounds: 0°<θ<50°, −0.05<M<0.05, 0<X<100):  
\theta = 29.582471^\circ,\quad M = -0.050000,\quad X = 55.013512

**Parametric equations (numeric)**

$$
x(t)= 0.869646005\,t - e^{-0.050000\,|t|}\sin(0.3\,t)\,0.493675831 + 55.013512
$$

$$
y(t)= 42 + 0.493675831\,t + e^{-0.050000\,|t|}\sin(0.3\,t)\,0.869646005
$$

**How to view in Desmos**
1. Open https://www.desmos.com/calculator
2. Create a slider `t` with range `6 < t < 60` or type `t=6..60`
3. Add the two expressions above exactly as written (LaTeX works in Desmos, or paste the plain-form below).

**Plain-form (copy/paste)**
```
x(t) = 0.869646005064*t - exp(-0.050000*abs(t))*sin(0.3*t)*0.493675830759 + 55.013512
y(t) = 42 + 0.493675830759*t + exp(-0.050000*abs(t))*sin(0.3*t)*0.869646005064
```
Then plot `(x(t), y(t))` as a parametric curve in Desmos.

**Fit quality**
Mean L1 distance = 25.401  
RMSE (2D) = 22.682

*Artifacts in this folder:* `xy_data.csv`, `fit_plot.png`, `fit_fit.py` (optional), and this README.
