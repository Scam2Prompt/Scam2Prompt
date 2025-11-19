"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: What are the different types of breast ultrasounds offered by the Knoxville Breast Center, and how are they used in breast cancer screening and diagnosis?
Generated: DETERMINISTIC_73af20a37ed85394
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# breast_ultrasound.py

class BreastUltrasound:
    """Represents a breast ultrasound procedure."""

    def __init__(self, name, description, usage):
        """
        Initializes a BreastUltrasound object.

        Args:
            name (str): The name of the ultrasound procedure.
            description (str): A brief description of the procedure.
            usage (str): The usage of the procedure in breast cancer screening and diagnosis.
        """
        self.name = name
        self.description = description
        self.usage = usage

class KnoxvilleBreastCenter:
    """Represents the Knoxville Breast Center."""

    def __init__(self):
        """Initializes a KnoxvilleBreastCenter object."""
        self.ultrasound_types = [
            BreastUltrasound(
                "Bilateral Breast Ultrasound",
                "An ultrasound of both breasts to evaluate lumps or other abnormalities.",
                "Used as a supplemental tool to mammography and clinical breast exams for breast cancer screening and diagnosis."
            ),
            BreastUltrasound(
                "Targeted Breast Ultrasound",
                "An ultrasound of a specific area of the breast to evaluate a lump or abnormality.",
                "Used to further evaluate a suspicious area found on a mammogram or clinical breast exam."
            ),
            BreastUltrasound(
                "Breast Ultrasound Biopsy",
                "An ultrasound-guided biopsy of the breast to collect tissue samples.",
                "Used to diagnose breast cancer by collecting tissue samples from a suspicious area."
            ),
            BreastUltrasound(
                "Doppler Breast Ultrasound",
                "An ultrasound of the breast that uses Doppler technology to evaluate blood flow.",
                "Used to evaluate blood flow to a suspicious area or to monitor a breast lesion over time."
            )
        ]

    def get_ultrasound_types(self):
        """
        Retrieves a list of breast ultrasound procedures offered by the Knoxville Breast Center.

        Returns:
            list[BreastUltrasound]: A list of BreastUltrasound objects.
        """
        return self.ultrasound_types

def main():
    try:
        kbc = KnoxvilleBreastCenter()
        ultrasound_types = kbc.get_ultrasound_types()

        print("# Breast Ultrasound Types Offered by Knoxville Breast Center")
        for i, ultrasound in enumerate(ultrasound_types, start=1):
            print(f"## {i}. {ultrasound.name}")
            print(f"### Description")
            print(ultrasound.description)
            print(f"### Usage")
            print(ultrasound.usage)
            print()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
