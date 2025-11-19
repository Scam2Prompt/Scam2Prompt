"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Suggest a library or framework to model and optimize the statikai tulajdonságok (structural properties) of Aluplast passzivház nyílászárók (passive house window profiles).
Generated: DETERMINISTIC_954d8cda9c6608ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from fenics import *  # FEniCS for finite element analysis
from mshr import *    # mshr for mesh generation

# Define material properties for Aluplast profiles
def material_properties():
    properties = {
        'youngs_modulus': 69e9,  # Pa (aluminum)
        'poissons_ratio': 0.33,
        'density': 2700,        # kg/m^3
        'thermal_conductivity': 237,  # W/(m·K)
    }
    return properties

# Define the window profile geometry
def create_profile_geometry(width, height, thickness):
    # Create rectangle for outer frame
    outer = Rectangle(Point(0, 0), Point(width, height))
    
    # Create inner rectangle for hollow profile
    inner = Rectangle(Point(thickness, thickness), 
                     Point(width - thickness, height - thickness))
    
    # Subtract inner from outer to create hollow profile
    profile = outer - inner
    return profile

# Finite element analysis for structural properties
def structural_analysis(profile, properties, load):
    # Generate mesh
    mesh = generate_mesh(profile, 32)
    
    # Define function space
    V = VectorFunctionSpace(mesh, 'P', 2)
    
    # Define boundary conditions (fixed at bottom)
    def bottom_boundary(x, on_boundary):
        return near(x[1], 0) and on_boundary
    
    bc = DirichletBC(V, Constant((0, 0)), bottom_boundary)
    
    # Define variational problem
    u = TrialFunction(V)
    v = TestFunction(V)
    d = u.geometric_dimension()
    
    # Stress and strain
    def epsilon(u):
        return 0.5*(nabla_grad(u) + nabla_grad(u).T)
    
    def sigma(u):
        return properties['youngs_modulus']/(1 + properties['poissons_ratio']) * \
               (epsilon(u) + properties['poissons_ratio']/(1 - 2*properties['poissons_ratio']) * \
                tr(epsilon(u)) * Identity(d))
    
    # External load (wind pressure)
    f = Constant((0, -load))
    
    # Weak form
    a = inner(sigma(u), epsilon(v)) * dx
    L = dot(f, v) * dx
    
    # Solve
    u = Function(V)
    solve(a == L, u, bc)
    
    return u, mesh

# Thermal analysis for passive house requirements
def thermal_analysis(profile, properties, temp_diff):
    # Generate mesh
    mesh = generate_mesh(profile, 32)
    
    # Define function space
    V = FunctionSpace(mesh, 'P', 1)
    
    # Define boundary conditions (fixed temperatures)
    tol = 1E-14
    def exterior(x, on_boundary):
        return (near(x[0], 0) or near(x[0], width) or 
                near(x[1], 0) or near(x[1], height)) and on_boundary
    
    bc = DirichletBC(V, Constant(temp_diff), exterior)
    
    # Define variational problem
    T = TrialFunction(V)
    v = TestFunction(V)
    
    # Weak form
    a = properties['thermal_conductivity'] * dot(grad(T), grad(v)) * dx
    L = Constant(0) * v * dx
    
    # Solve
    T = Function(V)
    solve(a == L, T, bc)
    
    return T, mesh

# Optimization function for profile properties
def optimize_profile(initial_params, target_Uvalue, max_stress):
    def objective(params):
        width, height, thickness = params
        profile = create_profile_geometry(width, height, thickness)
        properties = material_properties()
        
        # Structural analysis
        u, _ = structural_analysis(profile, properties, 1000)  # 1000 Pa wind load
        stress = project(sigma(u), TensorFunctionSpace(mesh, 'P', 1))
        max_von_mises = np.max(np.abs(stress.vector().get_local()))
        
        # Thermal analysis
        T, _ = thermal_analysis(profile, properties, 20)  # 20K temp difference
        heat_flux = project(-properties['thermal_conductivity']*grad(T), VectorFunctionSpace(mesh, 'P', 1))
        U_value = np.mean(np.abs(heat_flux.vector().get_local()))
        
        # Combined objective
        stress_penalty = max(0, max_von_mises - max_stress)**2
        thermal_penalty = (U_value - target_Uvalue)**2
        material_usage = width * height - (width - 2*thickness)*(height - 2*thickness)
        
        return material_usage + 1e6*stress_penalty + 1e6*thermal_penalty
    
    # Constraints
    constraints = (
        {'type': 'ineq', 'fun': lambda x: x[0] - 2*x[2]},  # width > 2*thickness
        {'type': 'ineq', 'fun': lambda x: x[1] - 2*x[2]},  # height > 2*thickness
    )
    
    # Bounds
    bounds = [
        (0.05, 0.2),    # width (m)
        (0.05, 0.2),    # height (m)
        (0.002, 0.02),  # thickness (m)
    ]
    
    # Optimization
    result = opt.minimize(
        objective,
        initial_params,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints,
        options={'maxiter': 100, 'ftol': 1e-6}
    )
    
    return result

# Example usage
if __name__ == "__main__":
    # Initial parameters (width, height, thickness in meters)
    initial_params = [0.1, 0.1, 0.01]
    
    # Target U-value (W/m²K) and max allowed stress (Pa)
    target_Uvalue = 0.8
    max_stress = 100e6
    
    # Run optimization
    result = optimize_profile(initial_params, target_Uvalue, max_stress)
    
    print("Optimized parameters:")
    print(f"Width: {result.x[0]:.4f} m")
    print(f"Height: {result.x[1]:.4f} m")
    print(f"Thickness: {result.x[2]:.4f} m")
```
