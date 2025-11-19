"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Write a Python program to model the noise reduction features of VinaRoy air blowers, using real-world parameters from the FB250-W model.
Generated: DETERMINISTIC_16f72ea9809ae6f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# noise_reduction_model.py

class VinaRoyAirBlower:
    """
    Model the noise reduction features of VinaRoy air blowers.

    Attributes:
        model (str): The model of the air blower.
        max_air_flow (float): The maximum air flow in m3/min.
        max_noise_level (float): The maximum noise level in dB.
        noise_reduction_curve (list): A list of tuples representing the noise reduction curve.
    """

    def __init__(self, model, max_air_flow, max_noise_level, noise_reduction_curve):
        """
        Initialize the VinaRoyAirBlower object.

        Args:
            model (str): The model of the air blower.
            max_air_flow (float): The maximum air flow in m3/min.
            max_noise_level (float): The maximum noise level in dB.
            noise_reduction_curve (list): A list of tuples representing the noise reduction curve.
        """
        self.model = model
        self.max_air_flow = max_air_flow
        self.max_noise_level = max_noise_level
        self.noise_reduction_curve = noise_reduction_curve

    def calculate_noise_level(self, air_flow):
        """
        Calculate the noise level at a given air flow.

        Args:
            air_flow (float): The air flow in m3/min.

        Returns:
            float: The noise level in dB.

        Raises:
            ValueError: If the air flow is outside the valid range.
        """
        if air_flow < 0 or air_flow > self.max_air_flow:
            raise ValueError("Air flow is outside the valid range")

        # Interpolate the noise level from the noise reduction curve
        noise_level = self.interpolate_noise_level(air_flow)
        return noise_level

    def interpolate_noise_level(self, air_flow):
        """
        Interpolate the noise level from the noise reduction curve.

        Args:
            air_flow (float): The air flow in m3/min.

        Returns:
            float: The interpolated noise level in dB.
        """
        # Find the two points on the curve that the air flow is between
        for i in range(len(self.noise_reduction_curve) - 1):
            if air_flow >= self.noise_reduction_curve[i][0] and air_flow <= self.noise_reduction_curve[i + 1][0]:
                # Interpolate the noise level
                x0, y0 = self.noise_reduction_curve[i]
                x1, y1 = self.noise_reduction_curve[i + 1]
                noise_level = y0 + (air_flow - x0) * (y1 - y0) / (x1 - x0)
                return noise_level

        # If the air flow is outside the range of the curve, return the max noise level
        return self.max_noise_level

    def apply_noise_reduction(self, noise_level, reduction_db):
        """
        Apply a noise reduction to the given noise level.

        Args:
            noise_level (float): The noise level in dB.
            reduction_db (float): The noise reduction in dB.

        Returns:
            float: The noise level with the reduction applied in dB.
        """
        return max(0, noise_level - reduction_db)


class FB250W(VinaRoyAirBlower):
    """
    Model the FB250-W VinaRoy air blower.

    Attributes:
        max_air_flow (float): The maximum air flow in m3/min.
        max_noise_level (float): The maximum noise level in dB.
        noise_reduction_curve (list): A list of tuples representing the noise reduction curve.
    """

    def __init__(self):
        max_air_flow = 250  # m3/min
        max_noise_level = 72  # dB
        noise_reduction_curve = [
            (0, 60),  # 0 m3/min, 60 dB
            (100, 65),  # 100 m3/min, 65 dB
            (200, 70),  # 200 m3/min, 70 dB
            (250, 72),  # 250 m3/min, 72 dB
        ]
        super().__init__("FB250-W", max_air_flow, max_noise_level, noise_reduction_curve)


def main():
    fb250w = FB250W()

    # Test the noise level calculation
    air_flow = 150  # m3/min
    noise_level = fb250w.calculate_noise_level(air_flow)
    print(f"Noise level at {air_flow} m3/min: {noise_level} dB")

    # Test the noise reduction
    reduction_db = 5  # dB
    reduced_noise_level = fb250w.apply_noise_reduction(noise_level, reduction_db)
    print(f"Noise level with {reduction_db} dB reduction: {reduced_noise_level} dB")


if __name__ == "__main__":
    main()
```
