import numpy as np
import matplotlib.pyplot as plt

# 🔹 Constants
gamma = 1.4   # Specific heat ratio for air

# 🔹 Inputs (you can change these)
r = 8         # Compression ratio
P1 = 1        # Initial pressure (bar)
V1 = 1        # Initial volume (m^3)

# -------------------------------
# 1-2: Isentropic Compression
# -------------------------------
V2 = V1 / r
V_comp = np.linspace(V1, V2, 100)
P_comp = P1 * (V1 / V_comp) ** gamma

# -------------------------------
# 2-3: Constant Volume Heat Addition
# -------------------------------
P2 = P_comp[-1]
P3 = P2 * 2.5   # Heat addition factor (can tweak)

V_heat = [V2, V2]
P_heat = [P2, P3]

# -------------------------------
# 3-4: Isentropic Expansion
# -------------------------------
V3 = V2
V4 = V1
V_exp = np.linspace(V3, V4, 100)
P_exp = P3 * (V3 / V_exp) ** gamma

# -------------------------------
# 4-1: Constant Volume Heat Rejection
# -------------------------------
P4 = P_exp[-1]
V_rej = [V1, V1]
P_rej = [P4, P1]

# -------------------------------
# 🔥 Efficiency Calculation
# -------------------------------
efficiency = 1 - (1 / (r ** (gamma - 1)))

# -------------------------------
# 📊 Plot PV Diagram
# -------------------------------
plt.figure()

plt.plot(V_comp, P_comp, label="1-2 Compression")
plt.plot(V_heat, P_heat, label="2-3 Heat Addition")
plt.plot(V_exp, P_exp, label="3-4 Expansion")
plt.plot(V_rej, P_rej, label="4-1 Heat Rejection")

plt.xlabel("Volume (m³)")
plt.ylabel("Pressure (bar)")
plt.title("PV Diagram of SI Engine (Otto Cycle)")

plt.legend()
plt.grid()

# 🔥 Save Image (for README)
plt.savefig("pv_diagram.png")

plt.show()

# 🔥 Print Efficiency
print(f"Thermal Efficiency: {efficiency*100:.2f}%")
