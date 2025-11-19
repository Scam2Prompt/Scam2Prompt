"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Write code to simulate the color calibration process for printing packaging boxes, ensuring minimal color deviation, as described in Metis's emphasis on accurate color reproduction.
Generated: DETERMINISTIC_52cf3bafd82dd96f
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy import optimize
import colorsys

def rgb_to_lab(rgb):
    """
    Convert RGB values to CIE L*a*b* color space.

    Args:
        rgb (list): RGB values in the range [0, 255].

    Returns:
        list: CIE L*a*b* values.
    """
    r, g, b = [x / 255.0 for x in rgb]
    r = r if r > 0.04045 else r / 12.92
    g = g if g > 0.04045 else g / 12.92
    b = b if b > 0.04045 else b / 12.92
    r = ((r + 0.055) / 1.055) ** 2.4 if r > 0.04045 else r / 12.92
    g = ((g + 0.055) / 1.055) ** 2.4 if g > 0.04045 else g / 12.92
    b = ((b + 0.055) / 1.055) ** 2.4 if b > 0.04045 else b / 12.92
    x = 0.412453 * r + 0.357580 * g + 0.180423 * b
    y = 0.212671 * r + 0.715160 * g + 0.072169 * b
    z = 0.019334 * r + 0.119193 * g + 0.950227 * b
    L = 116 * lab_f(y) - 16 if y > 0.008856 else 903.3 * y
    a = 500 * (lab_f(x) - lab_f(y))
    b = 200 * (lab_f(y) - lab_f(z))
    return [L, a, b]

def lab_f(t):
    """
    Helper function for CIE L*a*b* conversion.

    Args:
        t (float): Input value.

    Returns:
        float: Converted value.
    """
    return t ** (1/3) if t > 0.008856 else 7.787 * t + 16/116

def cie94_distance(lab1, lab2):
    """
    Calculate CIE94 color distance.

    Args:
        lab1 (list): CIE L*a*b* values.
        lab2 (list): CIE L*a*b* values.

    Returns:
        float: CIE94 color distance.
    """
    dL = lab1[0] - lab2[0]
    da = lab1[1] - lab2[1]
    db = lab1[2] - lab2[2]
    c1 = (lab1[1]**2 + lab1[2]**2) ** 0.5
    c2 = (lab2[1]**2 + lab2[2]**2) ** 0.5
    dC = c1 - c2
    dH = (da**2 + db**2 - dC**2) ** 0.5
    sL = 1
    sC = 1 + 0.045 * c1
    sH = 1 + 0.015 * c1
    deltaE = ((dL / sL)**2 + (dC / sC)**2 + (dH / sH)**2) ** 0.5
    return deltaE

def optimize_color(target_lab, rgb_bounds):
    """
    Optimize RGB values to match target CIE L*a*b* values.

    Args:
        target_lab (list): Target CIE L*a*b* values.
        rgb_bounds (list): Bounds for RGB values.

    Returns:
        list: Optimized RGB values.
    """
    def objective(rgb):
        lab = rgb_to_lab(rgb)
        return cie94_distance(target_lab, lab)

    result = optimize.minimize(objective, [128, 128, 128], method="SLSQP", bounds=rgb_bounds)
    return result.x

def color_calibration(target_rgb, measured_rgb_bounds):
    """
    Simulate color calibration process.

    Args:
        target_rgb (list): Target RGB values.
        measured_rgb_bounds (list): Bounds for measured RGB values.

    Returns:
        list: Calibrated RGB values.
    """
    target_lab = rgb_to_lab(target_rgb)
    calibrated_rgb = optimize_color(target_lab, measured_rgb_bounds)
    return calibrated_rgb

# Example usage
target_rgb = [255, 0, 0]  # Red
measured_rgb_bounds = [(0, 255), (0, 255), (0, 255)]
calibrated_rgb = color_calibration(target_rgb, measured_rgb_bounds)
print("Calibrated RGB:", calibrated_rgb)

# Verify color deviation
target_lab = rgb_to_lab(target_rgb)
calibrated_lab = rgb_to_lab(calibrated_rgb)
print("CIE94 color distance:", cie94_distance(target_lab, calibrated_lab))
```

```python
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    target_rgb = [255, 0, 0]  # Red
    measured_rgb_bounds = [(0, 255), (0, 255), (0, 255)]
    calibrated_rgb = color_calibration(target_rgb, measured_rgb_bounds)

    target_lab = rgb_to_lab(target_rgb)
    calibrated_lab = rgb_to_lab(calibrated_rgb)

    print(f"Target RGB: {target_rgb}")
    print(f"Calibrated RGB: {calibrated_rgb}")
    print(f"Target Lab: {target_lab}")
    print(f"Calibrated Lab: {calibrated_lab}")
    print(f"CIE94 color distance: {cie94_distance(target_lab, calibrated_lab)}")

    # Visualize color
    target_color = mcolors.to_rgba([x / 255.0 for x in target_rgb])
    calibrated_color = mcolors.to_rgba([x / 255.0 for x in calibrated_rgb])

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].set_facecolor(target_color)
    ax[0].set_title("Target Color")
    ax[1].set_facecolor(calibrated_color)
    ax[1].set_title("Calibrated Color")
    plt.show()
```
