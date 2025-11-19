"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Write code to simulate dust-proofing mechanisms for UPVC windows, incorporating the advantages listed on the Dexodoor website.
Generated: DETERMINISTIC_b76630f6a671212f
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UPVCWindow:
    """
    A class to represent a UPVC window with dust-proofing mechanisms.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes a UPVC window with specified dimensions.

        :param width: Width of the window in meters.
        :param height: Height of the window in meters.
        """
        self.width = width
        self.height = height
        self.is_dust_proof = False
        self.seal_quality = "None"

    def apply_dust_proofing(self, seal_quality: str):
        """
        Applies dust-proofing mechanisms to the window.

        :param seal_quality: Quality of the seal to be applied (e.g., "High", "Medium", "Low").
        :raises ValueError: If the seal quality is not recognized.
        """
        valid_seals = ["High", "Medium", "Low"]
        if seal_quality not in valid_seals:
            raise ValueError(f"Invalid seal quality. Choose from {valid_seals}.")

        self.seal_quality = seal_quality
        self.is_dust_proof = True
        print(f"Dust-proofing applied with {seal_quality} seal.")

    def check_dust_proofing(self) -> bool:
        """
        Checks if the window is dust-proof.

        :return: True if the window is dust-proof, False otherwise.
        """
        return self.is_dust_proof

    def get_window_dimensions(self) -> tuple:
        """
        Returns the dimensions of the window.

        :return: A tuple containing the width and height of the window.
        """
        return self.width, self.height

    def __str__(self) -> str:
        """
        Returns a string representation of the UPVC window.

        :return: A string describing the window's dimensions and dust-proofing status.
        """
        dust_proof_status = "Dust-proof" if self.is_dust_proof else "Not dust-proof"
        return (f"UPVC Window - Width: {self.width}m, Height: {self.height}m, "
                f"Seal Quality: {self.seal_quality}, Status: {dust_proof_status}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a UPVC window instance
        window = UPVCWindow(1.5, 1.2)

        # Apply dust-proofing
        window.apply_dust_proofing("High")

        # Check dust-proofing status
        print(window.check_dust_proofing())  # Output: True

        # Get window dimensions
        print(window.get_window_dimensions())  # Output: (1.5, 1.2)

        # Print window details
        print(window)

    except ValueError as e:
        print(f"Error: {e}")
```
