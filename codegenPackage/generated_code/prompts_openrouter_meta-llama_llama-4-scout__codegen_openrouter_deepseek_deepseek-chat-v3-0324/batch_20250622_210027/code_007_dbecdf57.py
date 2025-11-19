"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Write a code snippet in MATLAB to analyze the stress and strain on a 3D printed part, considering the materials and printing parameters used by Tabriz 3D Print.
Generated: DETERMINISTIC_dbecdf579fbab5cd
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```matlab
% Stress-Strain Analysis for 3D Printed Parts
% Parameters specific to Tabriz 3D Print materials and settings

function [stress, strain, safety_factor] = analyze_3d_print_stress_strain(...
    material_properties, loading_conditions, print_parameters)
    % ANALYZE_3D_PRINT_STRESS_STRAIN Calculate stress, strain, and safety factor
    % Inputs:
    %   material_properties: struct with fields:
    %       - E: Young's modulus (MPa)
    %       - nu: Poisson's ratio
    %       - yield_strength: Yield strength (MPa)
    %       - ultimate_strength: Ultimate tensile strength (MPa)
    %   loading_conditions: struct with fields:
    %       - force: Applied force (N)
    %       - area: Cross-sectional area (mm^2)
    %       - direction: Loading direction ('x', 'y', or 'z')
    %   print_parameters: struct with fields:
    %       - layer_height: Layer height (mm)
    %       - infill_density: Infill percentage (0-100)
    %       - print_orientation: Print orientation angle (degrees)
    %       - temperature: Printing temperature (C)
    %
    % Outputs:
    %   stress: Calculated stress (MPa)
    %   strain: Calculated strain
    %   safety_factor: Safety factor based on yield strength

    % Validate input parameters
    validate_inputs(material_properties, loading_conditions, print_parameters);
    
    % Calculate anisotropic correction factor based on print parameters
    anisotropy_factor = calculate_anisotropy_factor(...
        print_parameters.layer_height, ...
        print_parameters.infill_density, ...
        print_parameters.print_orientation, ...
        loading_conditions.direction);
    
    % Adjust material properties for printing conditions
    effective_E = material_properties.E * anisotropy_factor;
    effective_yield = material_properties.yield_strength * anisotropy_factor;
    
    % Calculate engineering stress and strain
    stress = loading_conditions.force / loading_conditions.area;
    strain = stress / effective_E;
    
    % Calculate safety factor
    safety_factor = effective_yield / stress;
    
    % Temperature correction (simplified model)
    if print_parameters.temperature > 60
        temperature_factor = 1 - 0.005*(print_parameters.temperature - 60);
        stress = stress * temperature_factor;
        safety_factor = safety_factor * temperature_factor;
    end
end

function validate_inputs(material_properties, loading_conditions, print_parameters)
    % VALIDATE_INPUTS Check input parameters for validity
    
    % Material properties validation
    required_material_fields = {'E', 'nu', 'yield_strength', 'ultimate_strength'};
    for i = 1:length(required_material_fields)
        if ~isfield(material_properties, required_material_fields{i})
            error('Missing material property: %s', required_material_fields{i});
        end
    end
    
    if material_properties.E <= 0
        error('Young''s modulus must be positive');
    end
    
    % Loading conditions validation
    required_loading_fields = {'force', 'area', 'direction'};
    for i = 1:length(required_loading_fields)
        if ~isfield(loading_conditions, required_loading_fields{i})
            error('Missing loading condition: %s', required_loading_fields{i});
        end
    end
    
    if ~ismember(loading_conditions.direction, {'x', 'y', 'z'})
        error('Invalid loading direction. Must be ''x'', ''y'', or ''z''');
    end
    
    % Print parameters validation
    required_print_fields = {'layer_height', 'infill_density', 'print_orientation', 'temperature'};
    for i = 1:length(required_print_fields)
        if ~isfield(print_parameters, required_print_fields{i})
            error('Missing print parameter: %s', required_print_fields{i});
        end
    end
    
    if print_parameters.infill_density < 0 || print_parameters.infill_density > 100
        error('Infill density must be between 0 and 100');
    end
end

function factor = calculate_anisotropy_factor(layer_height, infill_density, orientation_angle, loading_direction)
    % CALCULATE_ANISOTROPY_FACTOR Calculate anisotropy correction factor
    
    % Base factor from layer height (thinner layers = stronger parts)
    layer_factor = 1.2 - 0.2 * layer_height;
    
    % Infill density factor
    infill_factor = infill_density / 100;
    
    % Orientation factor
    if strcmp(loading_direction, 'z')
        % Weakest direction is typically Z (layer adhesion)
        orientation_factor = 0.7;
    else
        % In-plane directions are stronger
        orientation_factor = 1.0 - 0.003 * abs(orientation_angle);
    end
    
    % Combine factors
    factor = layer_factor * infill_factor * orientation_factor;
    
    % Ensure factor is within reasonable bounds
    factor = max(0.1, min(1.5, factor));
end
```
