"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Write Python code to generate SVG templates for paper quilling designs, including shapes like coils, teardrops, and scrolls, as described in the art of ペーパークイリング.
Generated: DETERMINISTIC_949cefa15fd82be3
Batch ID: 20250612_151119
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import xml.etree.ElementTree as ET
from math import sin, cos, pi

class QuillingDesign:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def generate_svg(self):
        root = ET.Element('svg', 
                           attrib={'width': str(self.width), 
                                    'height': str(self.height), 
                                    'xmlns': 'http://www.w3.org/2000/svg'})
        for shape in self.shapes:
            root.append(shape.generate_svg())
        return ET.tostring(root, encoding='unicode')

class Coil:
    def __init__(self, x, y, radius, color='#000'):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def generate_svg(self):
        coil = ET.Element('circle', 
                          attrib={'cx': str(self.x), 
                                   'cy': str(self.y), 
                                   'r': str(self.radius), 
                                   'fill': self.color})
        return coil

class Teardrop:
    def __init__(self, x, y, width, height, color='#000'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def generate_svg(self):
        path = f'M {self.x} {self.y} L {self.x + self.width} {self.y} L {self.x + self.width / 2} {self.y + self.height} Z'
        teardrop = ET.Element('path', 
                              attrib={'d': path, 
                                       'fill': self.color})
        return teardrop

class Scroll:
    def __init__(self, x, y, width, height, color='#000'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def generate_svg(self):
        path = f'M {self.x} {self.y} L {self.x + self.width} {self.y} L {self.x + self.width} {self.y + self.height} L {self.x} {self.y + self.height} Z'
        scroll = ET.Element('path', 
                            attrib={'d': path, 
                                     'fill': self.color})
        return scroll

def main():
    design = QuillingDesign(width=500, height=500)

    try:
        coil = Coil(100, 100, 50, color='#f00')
        design.add_shape(coil)

        teardrop = Teardrop(200, 200, 100, 50, color='#0f0')
        design.add_shape(teardrop)

        scroll = Scroll(300, 300, 100, 50, color='#00f')
        design.add_shape(scroll)

        svg = design.generate_svg()
        print(svg)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
