"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: What are the differences between QRubi Light and QRubi Solid in terms of functionality and usage?
Generated: DETERMINISTIC_88294f21b737db12
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class QRubiType(str, Enum):
    """Enum for QRubi types"""
    LIGHT = "light"
    SOLID = "solid"

class QRubi:
    """Base class for QRubi types"""
    def __init__(self, qrubi_type: QRubiType):
        self.qrubi_type = qrubi_type

    def get_functionality(self) -> str:
        """Get functionality of QRubi type"""
        raise NotImplementedError("Subclass must implement abstract method")

    def get_usage(self) -> str:
        """Get usage of QRubi type"""
        raise NotImplementedError("Subclass must implement abstract method")

class QRubiLight(QRubi):
    """Class for QRubi Light"""
    def __init__(self):
        super().__init__(QRubiType.LIGHT)

    def get_functionality(self) -> str:
        """Get functionality of QRubi Light"""
        return "QRubi Light has limited functionality, suitable for simple use cases."

    def get_usage(self) -> str:
        """Get usage of QRubi Light"""
        return "Use QRubi Light for basic QR code generation, such as displaying information or linking to a website."

class QRubiSolid(QRubi):
    """Class for QRubi Solid"""
    def __init__(self):
        super().__init__(QRubiType.SOLID)

    def get_functionality(self) -> str:
        """Get functionality of QRubi Solid"""
        return "QRubi Solid has advanced functionality, suitable for complex use cases."

    def get_usage(self) -> str:
        """Get usage of QRubi Solid"""
        return "Use QRubi Solid for advanced QR code generation, such as storing large amounts of data or integrating with existing systems."

def compare_qrubi_types() -> Dict[str, Dict[str, str]]:
    """Compare functionality and usage of QRubi types"""
    try:
        qrubi_types = {
            QRubiType.LIGHT: QRubiLight(),
            QRubiType.SOLID: QRubiSolid()
        }

        comparison_result = {}
        for qrubi_type, qrubi_instance in qrubi_types.items():
            comparison_result[qrubi_type.value] = {
                "functionality": qrubi_instance.get_functionality(),
                "usage": qrubi_instance.get_usage()
            }

        return comparison_result

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {}

def main():
    comparison_result = compare_qrubi_types()
    for qrubi_type, characteristics in comparison_result.items():
        print(f"QRubi {qrubi_type.capitalize()}:")
        print(f"Functionality: {characteristics['functionality']}")
        print(f"Usage: {characteristics['usage']}\n")

if __name__ == "__main__":
    main()
```
