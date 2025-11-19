"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://overlanders-atari.com
Prompt: Discuss the process of developing a demo for a competition, using insights from Overlanders' experience at the LoveByte Demoparty.
Generated: DETERMINISTIC_d599b7cb90581c0c
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemoDevelopment:
    def __init__(self, demo_title: str, team_name: str):
        """
        Initialize the DemoDevelopment class.

        :param demo_title: Title of the demo
        :param team_name: Name of the team
        """
        self.demo_title = demo_title
        self.team_name = team_name
        self.assets_directory = os.path.join(os.getcwd(), demo_title, 'assets')
        self.source_code_directory = os.path.join(os.getcwd(), demo_title, 'source')
        self.build_directory = os.path.join(os.getcwd(), demo_title, 'build')

    def prepare_directories(self):
        """
        Prepare directories for the demo, including assets and source code.
        """
        try:
            # Create main demo directory
            os.makedirs(self.assets_directory, exist_ok=True)
            os.makedirs(self.source_code_directory, exist_ok=True)
            logging.info(f"Directories created for demo: {self.demo_title}")
        except OSError as e:
            logging.error(f"Error creating directories: {e}")
            raise

    def add_assets(self, asset_files: list):
        """
        Copy asset files to the assets directory.

        :param asset_files: List of asset file paths to copy
        """
        for asset in asset_files:
            try:
                shutil.copy(asset, self.assets_directory)
                logging.info(f"Copied asset: {asset}")
            except FileNotFoundError:
                logging.error(f"Asset file not found: {asset}")
            except Exception as e:
                logging.error(f"Error copying asset {asset}: {e}")

    def write_source_code(self, code: str):
        """
        Write source code to a file in the source code directory.

        :param code: Python code as a string
        """
        try:
            with open(os.path.join(self.source_code_directory, 'main.py'), 'w') as file:
                file.write(code)
                logging.info("Source code written successfully.")
        except IOError as e:
            logging.error(f"Error writing source code: {e}")
            raise

    def build_demo(self):
        """
        Build the demo by moving source code to the build directory.
        """
        try:
            os.makedirs(self.build_directory, exist_ok=True)
            shutil.copytree(self.source_code_directory, self.build_directory, dirs_exist_ok=True)
            logging.info("Demo built successfully.")
        except OSError as e:
            logging.error(f"Error building demo: {e}")
            raise

    def run_demo(self):
        """
        Run the demo from the build directory.
        """
        try:
            os.system(f'python {os.path.join(self.build_directory, "main.py")}')
            logging.info("Demo run initiated.")
        except Exception as e:
            logging.error(f"Error running demo: {e}")
            raise

# Example Usage
if __name__ == "__main__":
    demo = DemoDevelopment("MyAwesomeDemo", "Overlanders")
    demo.prepare_directories()
    demo.add_assets(["path/to/asset1.png", "path/to/asset2.mp3"])  # Example paths
    demo.write_source_code("""
def main():
    print("Welcome to My Awesome Demo!")

if __name__ == "__main__":
    main()
""")
    demo.build_demo()
    demo.run_demo()
```
