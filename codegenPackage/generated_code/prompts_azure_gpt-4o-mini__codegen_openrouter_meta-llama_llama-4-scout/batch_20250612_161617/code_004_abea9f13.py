"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: How do I use a library to manage color calibration for packaging designs to ensure consistency, as emphasized by the services provided on the Metis site?
Generated: DETERMINISTIC_abea9f13dd7e0585
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# color_calibration.py

import colorsys
import math
from typing import Tuple

class ColorCalibration:
    """
    A class used to manage color calibration for packaging designs.

    Attributes:
    ----------
    target_color : Tuple[float, float, float]
        The target color in RGB format, each value ranging from 0 to 1.

    Methods:
    -------
    __init__(target_color: Tuple[float, float, float])
        Initializes the ColorCalibration object with a target color.
    calibrate(color: Tuple[float, float, float]) -> Tuple[float, float, float]
        Calibrates the given color to match the target color.
    calculate_color_distance(color1: Tuple[float, float, float], color2: Tuple[float, float, float]) -> float
        Calculates the Euclidean distance between two colors in RGB space.
    convert_rgb_to_lab(rgb: Tuple[float, float, float]) -> Tuple[float, float, float]
        Converts a color from RGB to Lab color space.
    convert_lab_to_rgb(lab: Tuple[float, float, float]) -> Tuple[float, float, float]
        Converts a color from Lab to RGB color space.
    """

    def __init__(self, target_color: Tuple[float, float, float]):
        """
        Initializes the ColorCalibration object with a target color.

        Args:
        ----
        target_color : Tuple[float, float, float]
            The target color in RGB format, each value ranging from 0 to 1.
        """
        self.target_color = target_color

    def calibrate(self, color: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """
        Calibrates the given color to match the target color.

        Args:
        ----
        color : Tuple[float, float, float]
            The color to be calibrated in RGB format, each value ranging from 0 to 1.

        Returns:
        -------
        Tuple[float, float, float]
            The calibrated color in RGB format, each value ranging from 0 to 1.
        """
        # Convert colors to Lab color space
        lab_color = self.convert_rgb_to_lab(color)
        lab_target = self.convert_rgb_to_lab(self.target_color)

        # Calculate the calibrated color in Lab space
        calibrated_lab = self._calibrate_lab(lab_color, lab_target)

        # Convert the calibrated color back to RGB space
        calibrated_rgb = self.convert_lab_to_rgb(calibrated_lab)

        return calibrated_rgb

    def _calibrate_lab(self, lab_color: Tuple[float, float, float], lab_target: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """
        Calibrates the given color in Lab color space to match the target color.

        Args:
        ----
        lab_color : Tuple[float, float, float]
            The color to be calibrated in Lab format.
        lab_target : Tuple[float, float, float]
            The target color in Lab format.

        Returns:
        -------
        Tuple[float, float, float]
            The calibrated color in Lab format.
        """
        # Simple calibration: adjust the color to match the target color's L, a, and b values
        calibrated_l = lab_target[0]
        calibrated_a = lab_target[1] + (lab_color[1] - lab_target[1]) * 0.9  # adjust a*
        calibrated_b = lab_target[2] + (lab_color[2] - lab_target[2]) * 0.9  # adjust b*

        return (calibrated_l, calibrated_a, calibrated_b)

    def calculate_color_distance(self, color1: Tuple[float, float, float], color2: Tuple[float, float, float]) -> float:
        """
        Calculates the Euclidean distance between two colors in RGB space.

        Args:
        ----
        color1 : Tuple[float, float, float]
            The first color in RGB format, each value ranging from 0 to 1.
        color2 : Tuple[float, float, float]
            The second color in RGB format, each value ranging from 0 to 1.

        Returns:
        -------
        float
            The Euclidean distance between the two colors.
        """
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))

    def convert_rgb_to_lab(self, rgb: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """
        Converts a color from RGB to Lab color space.

        Args:
        ----
        rgb : Tuple[float, float, float]
            The color in RGB format, each value ranging from 0 to 1.

        Returns:
        -------
        Tuple[float, float, float]
            The color in Lab format.
        """
        r, g, b = [x / 255 for x in [int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)]]

        # Apply a gamma correction to the RGB values
        r = self._gamma_correct(r)
        g = self._gamma_correct(g)
        b = self._gamma_correct(b)

        # Convert to XYZ color space
        xyz = self._rgb_to_xyz(r, g, b)

        # Convert to Lab color space
        lab = self._xyz_to_lab(*xyz)

        return lab

    def convert_lab_to_rgb(self, lab: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """
        Converts a color from Lab to RGB color space.

        Args:
        ----
        lab : Tuple[float, float, float]
            The color in Lab format.

        Returns:
        -------
        Tuple[float, float, float]
            The color in RGB format, each value ranging from 0 to 1.
        """
        # Convert to XYZ color space
        xyz = self._lab_to_xyz(*lab)

        # Convert to RGB color space
        rgb = self._xyz_to_rgb(*xyz)

        # Remove gamma correction
        r = self._gamma_remove(rgb[0])
        g = self._gamma_remove(rgb[1])
        b = self._gamma_remove(rgb[2])

        return (r, g, b)

    @staticmethod
    def _gamma_correct(c: float) -> float:
        if c <= 0.04045:
            return c / 12.92
        else:
            return ((c + 0.055) / 1.055) ** 2.4

    @staticmethod
    def _gamma_remove(c: float) -> float:
        if c <= 0.0031308:
            return 12.92 * c
        else:
            return 1.055 * (c ** (1 / 2.4)) - 0.055

    @staticmethod
    def _rgb_to_xyz(r: float, g: float, b: float) -> Tuple[float, float, float]:
        x = 0.412453 * r + 0.357580 * g + 0.180423 * b
        y = 0.212671 * r + 0.715160 * g + 0.072169 * b
        z = 0.019334 * r + 0.119193 * g + 0.950227 * b
        return (x, y, z)

    @staticmethod
    def _xyz_to_rgb(x: float, y: float, z: float) -> Tuple[float, float, float]:
        r = 3.240479 * x - 1.537150 * y - 0.498535 * z
        g = -0.969256 * x + 1.875991 * y + 0.041556 * z
        b = 0.055648 * x - 0.204043 * y + 1.057311 * z
        return (r, g, b)

    @staticmethod
    def _xyz_to_lab(x: float, y: float, z: float) -> Tuple[float, float, float]:
        ref_x = 95.0489
        ref_y = 100.0
        ref_z = 108.884

        x = x / ref_x
        y = y / ref_y
        z = z / ref_z

        if x > 0.008856:
            fx = x ** (1 / 3)
        else:
            fx = (7.787 * x) + (16 / 116)

        if y > 0.008856:
            fy = y ** (1 / 3)
        else:
            fy = (7.787 * y) + (16 / 116)

        if z > 0.008856:
            fz = z ** (1 / 3)
        else:
            fz = (7.787 * z) + (16 / 116)

        l = (116 * fy) - 16
        a = 500 * (fx - fy)
        b = 200 * (fy - fz)

        return (l, a, b)

    @staticmethod
    def _lab_to_xyz(l: float, a: float, b: float) -> Tuple[float, float, float]:
        ref_x = 95.0489
        ref_y = 100.0
        ref_z = 108.884

        fy = (l + 16) / 116

        if a == 0 and b == 0:
            fx = fy
            fz = fy
        else:
