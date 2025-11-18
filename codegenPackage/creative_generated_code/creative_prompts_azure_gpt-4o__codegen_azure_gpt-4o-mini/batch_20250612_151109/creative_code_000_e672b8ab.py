"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sgeek-seo.com
Prompt: Write a Python script to generate HTML5 or SVG diagrams using one of the free tools mentioned on the SGeek SEO website.
Generated: DETERMINISTIC_e672b8abf4367c36
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
from pathlib import Path

class DiagramGenerator:
    """
    A class to generate diagrams using SVG format with the help of the 'blockdiag' tool.

    Attributes:
        diagram_code (str): The diagram code in blockdiag syntax.
        output_dir (Path): The directory where output files will be saved.
    """

    def __init__(self, diagram_code: str, output_dir: str = 'output'):
        """
        Initializes the DiagramGenerator with diagram code and output directory.

        Args:
            diagram_code (str): The diagram code in blockdiag syntax.
            output_dir (str): Directory to save generated diagrams. Defaults to 'output'.
        """
        self.diagram_code = diagram_code
        self.output_dir = Path(output_dir)

        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_diagram(self, filename: str) -> None:
        """
        Generates an SVG diagram from the provided blockdiag code and saves it to the specified filename.

        Args:
            filename (str): The name of the file to save the diagram (without extension).
        """
        svg_file_path = self.output_dir / f"{filename}.svg"

        try:
            # Write the diagram_code to a temporary file
            temp_file_path = self.output_dir / f"{filename}.diag"
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(self.diagram_code)

            # Call blockdiag to generate the SVG
            subprocess.run(['blockdiag', str(temp_file_path)], check=True)

            # Rename the output file to SVG
            os.rename(temp_file_path.with_suffix('.svg'), svg_file_path)
            print(f"Diagram generated successfully: {svg_file_path}")

        except subprocess.CalledProcessError as e:
            print(f"Error generating diagram: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Cleanup temporary files
            if temp_file_path.exists():
                temp_file_path.unlink()
            if svg_file_path.with_suffix('.svg').exists():
                svg_file_path.with_suffix('.svg').unlink()

if __name__ == "__main__":
    # Example blockdiag code
    blockdiag_code = """
    blockdiag {
        A -> B -> C;
        B -> D;
    }
    """

    # Create a DiagramGenerator instance
    generator = DiagramGenerator(blockdiag_code)

    # Generate the diagram with a specific filename
    generator.generate_diagram('example_diagram')
```
