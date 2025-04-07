import numpy as np
import matplotlib.pyplot as plt

class GeneralWindTurbine():
    def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name=None):
        self.rotor_diameter = rotor_diameter    # [m]
        self.hub_height = hub_height            # [m]
        self.rated_power = rated_power          # [kW]
        self.v_in = v_in                        # [m/s]
        self.v_rated = v_rated                  # [m/s]
        self.v_out = v_out                      # [m/s]
        self.name = name

    def get_power(self, v):
        if v < self.v_in or v > self.v_out:
            P = 0
        elif self.v_in <= v < self.v_rated:
            P = self.rated_power*(v/self.v_rated)**3
        elif self.v_rated <= v <= self.v_out:
            P = self.rated_power
        return P


class WindTurbine():
    def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, power_curve_data, name=None):
        GeneralWindTurbine.__init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name=None)
        self.power_curve_data = power_curve_data

    def get_power(self, v):
        P = np.interp(v, self.power_curve_data[:, 0], self.power_curve_data[:, 1])
        return P


Turbine1 = GeneralWindTurbine(164, 110, 8000, 4, 12.5, 25, 'Leanwind 8 MW RWT')

power_data = np.loadtxt('./week09_classes_inheritance_and_OOP/LEANWIND_Reference_8MW_164.csv', delimiter=',', skiprows=1)
Turbine2 = WindTurbine(164, 110, 8000, 4, 12.5, 25, power_data, 'Leanwind 8 MW RWT')

# Choosing wind speeds to calculate
wind_speeds = np.linspace(0, 25, 100)

# Use built in function to get their respective power curves
power1 = [Turbine1.get_power(v) for v in wind_speeds]
power2 = [Turbine2.get_power(v) for v in wind_speeds]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(wind_speeds, power1, label='Turbine1 - General Model')
plt.plot(wind_speeds, power2, label='Turbine2 - From Power Curve', linestyle='--')
plt.xlabel('Wind Speed [m/s]')
plt.ylabel('Power Output [kW]')
plt.title('Wind Turbine Power Curves Comparison')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()