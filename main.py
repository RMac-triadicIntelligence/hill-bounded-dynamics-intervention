import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Hill-type activation function (bounded, nonlinear)
def sigma(x, gamma=10.0, k=0.5, n=6):
    return gamma * x**n / (k**n + x**n)

# Coupled dynamical system
def model(y, t, gamma=10.0, k=0.5, n=6, beta=0.2, delta=0.2):
    r, i = y
    drdt = sigma(i, gamma, k, n) * (1 - r) - beta * r
    didt = sigma(r, gamma, k, n) * (1 - i) - delta * i
    return [drdt, didt]

# Time domain
t_full = np.linspace(0, 50, 500)
intervention_time = 25
idx_intervene = np.searchsorted(t_full, intervention_time)

# Pre-intervention evolution
t_pre = t_full[:idx_intervene]
y0_closed = [0.2, 0.1]
sol_pre = odeint(model, y0_closed, t_pre)

# Apply intervention (state perturbation only)
y_intervene = sol_pre[-1].copy()
y_intervene[0] = min(y_intervene[0] + 0.5, 1.0)

# Post-intervention evolution
t_post = t_full[idx_intervene:]
sol_post = odeint(model, y_intervene, t_post)

# Combine trajectories
t_intervention = np.concatenate((t_pre, t_post))
sol_intervention = np.vstack((sol_pre, sol_post))

# Baseline (no intervention)
sol_closed = odeint(model, y0_closed, t_full)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t_full, sol_closed[:, 0], '--', label='Receptivity (No Intervention)')
plt.plot(t_full, sol_closed[:, 1], '--', label='Integration (No Intervention)')
plt.plot(t_intervention, sol_intervention[:, 0], label='Receptivity (With Intervention)')
plt.plot(t_intervention, sol_intervention[:, 1], label='Integration (With Intervention)')
plt.axvline(x=intervention_time, linestyle=':', label='Intervention')
plt.xlabel('Time')
plt.ylabel('Level (0–1)')
plt.title('Triadic Intervention in Hill-Bounded Dynamics')
plt.legend()
plt.grid()
plt.show()

# Late-time averages
avg_no_int_r = np.mean(sol_closed[-100:, 0])
avg_no_int_i = np.mean(sol_closed[-100:, 1])
avg_int_r = np.mean(sol_intervention[-100:, 0])
avg_int_i = np.mean(sol_intervention[-100:, 1])

print(f"No Intervention: Receptivity ≈ {avg_no_int_r:.3f}, Integration ≈ {avg_no_int_i:.3f}")
print(f"With Intervention: Receptivity ≈ {avg_int_r:.3f}, Integration ≈ {avg_int_i:.3f}")
