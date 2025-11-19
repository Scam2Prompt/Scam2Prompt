"""
Generated Code Metadata:
========================
Original URL: https://lusogamer.com
Prompt: Write a script to analyze APK metadata for apps like "Aethersx2" and "Ultra TV" to identify compatibility with specific Android versions.
Generated: DETERMINISTIC_7e44863827ada1c7
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import zipfile
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

class APKAnalyzer:
    def __init__(self, apk_path: str):
        """
        Initialize the APKAnalyzer with the path to the APK file.

        :param apk_path: Path to the APK file
        """
        self.apk_path = apk_path
        self.manifest_data: Optional[Dict[str, str]] = None

    def extract_manifest(self) -> None:
        """
        Extract the AndroidManifest.xml from the APK file and parse it.
        """
        try:
            with zipfile.ZipFile(self.apk_path, 'r') as apk_zip:
                # Check if the AndroidManifest.xml exists in the APK
                if 'AndroidManifest.xml' not in apk_zip.namelist():
                    raise FileNotFoundError("AndroidManifest.xml not found in the APK.")
                
                # Extract and parse the AndroidManifest.xml
                with apk_zip.open('AndroidManifest.xml') as manifest_file:
                    self.manifest_data = self.parse_manifest(manifest_file.read())
        except (zipfile.BadZipFile, FileNotFoundError) as e:
            print(f"Error extracting manifest: {e}")

    def parse_manifest(self, manifest_bytes: bytes) -> Dict[str, str]:
        """
        Parse the AndroidManifest.xml bytes and extract relevant metadata.

        :param manifest_bytes: Bytes of the AndroidManifest.xml
        :return: A dictionary containing the extracted metadata
        """
        try:
            # Parse the XML
            root = ET.fromstring(manifest_bytes)
            # Extract package name and version info
            package_name = root.attrib.get('package')
            version_code = root.attrib.get('android:versionCode')
            version_name = root.attrib.get('android:versionName')
            min_sdk = self.get_min_sdk(root)

            return {
                'package_name': package_name,
                'version_code': version_code,
                'version_name': version_name,
                'min_sdk': min_sdk
            }
        except ET.ParseError as e:
            print(f"Error parsing manifest: {e}")
            return {}

    def get_min_sdk(self, root: ET.Element) -> Optional[str]:
        """
        Retrieve the minimum SDK version from the manifest.

        :param root: The root element of the parsed XML
        :return: The minimum SDK version as a string, or None if not found
        """
        for child in root.findall('uses-sdk'):
            return child.attrib.get('android:minSdkVersion')
        return None

    def analyze_compatibility(self, target_sdk: int) -> None:
        """
        Analyze the APK's compatibility with a specific Android version.

        :param target_sdk: The target SDK version to check compatibility against
        """
        if self.manifest_data is None:
            print("Manifest data not extracted. Please run extract_manifest() first.")
            return

        min_sdk = self.manifest_data.get('min_sdk')
        if min_sdk is not None:
            min_sdk_int = int(min_sdk)
            if min_sdk_int <= target_sdk:
                print(f"{self.manifest_data['package_name']} is compatible with Android SDK {target_sdk}.")
            else:
                print(f"{self.manifest_data['package_name']} is NOT compatible with Android SDK {target_sdk}.")
        else:
            print("Minimum SDK version not found in the manifest.")

def main():
    # Example APK paths for analysis
    apk_paths = [
        "path/to/Aethersx2.apk",
        "path/to/UltraTV.apk"
    ]
    
    # Target SDK version for compatibility check
    target_sdk = 30  # Example: Android 11

    for apk_path in apk_paths:
        if os.path.exists(apk_path):
            analyzer = APKAnalyzer(apk_path)
            analyzer.extract_manifest()
            analyzer.analyze_compatibility(target_sdk)
        else:
            print(f"APK file not found: {apk_path}")

if __name__ == "__main__":
    main()
```
