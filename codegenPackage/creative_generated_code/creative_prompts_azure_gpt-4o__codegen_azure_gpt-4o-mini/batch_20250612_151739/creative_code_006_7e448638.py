"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lusogamer.com
Prompt: Write a script to analyze APK metadata for apps like "Aethersx2" and "Ultra TV" to identify compatibility with specific Android versions.
Generated: DETERMINISTIC_7e44863827ada1c7
Batch ID: 20250612_151739
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/apk/res/android}minSdkVersion": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://schemas.android.com/apk/res/android": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://schemas.android.com/apk/res/android}targetSdkVersion": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
import xml.etree.ElementTree as ET

class APKAnalyzer:
    """
    A class to analyze APK metadata to determine compatibility with specific Android versions.
    """
    
    def __init__(self, apk_path):
        """
        Initializes the APKAnalyzer with the path to the APK file.
        
        :param apk_path: Path to the APK file
        """
        if not os.path.isfile(apk_path):
            raise FileNotFoundError(f"APK file not found: {apk_path}")
        self.apk_path = apk_path
        self.manifest_data = self.extract_manifest()

    def extract_manifest(self):
        """
        Extracts the AndroidManifest.xml file from the APK and parses it.
        
        :return: Parsed XML root element of the AndroidManifest.xml
        """
        try:
            with zipfile.ZipFile(self.apk_path, 'r') as apk:
                manifest_data = apk.read('AndroidManifest.xml')
            return ET.fromstring(manifest_data) 
        except (zipfile.BadZipFile, FileNotFoundError) as e:
            raise RuntimeError("Failed to extract AndroidManifest.xml from APK") from e

    def get_compatible_android_versions(self):
        """
        Analyzes the manifest data to identify compatible Android versions.
        
        :return: A tuple containing minimum SDK and target SDK versions
        """
        try:
            # Namespaces in AndroidManifest.xml
            ns = {'android': 'http://schemas.android.com/apk/res/android'}

            # Finding the minimum and target SDK versions
            min_sdk = self.manifest_data.find(".//uses-sdk[@android:minSdkVersion]", ns)
            target_sdk = self.manifest_data.find(".//uses-sdk[@android:targetSdkVersion]", ns)

            min_sdk_version = min_sdk.get('{http://schemas.android.com/apk/res/android}minSdkVersion') if min_sdk is not None else None
            target_sdk_version = target_sdk.get('{http://schemas.android.com/apk/res/android}targetSdkVersion') if target_sdk is not None else None

            return (min_sdk_version, target_sdk_version)
        except Exception as e:
            raise RuntimeError("Error retrieving SDK versions from the manifest") from e

def main(apk_path):
    """
    Main function to run the APK analysis.

    :param apk_path: Path to the APK file to analyze
    """
    try:
        analyzer = APKAnalyzer(apk_path)
        min_sdk, target_sdk = analyzer.get_compatible_android_versions()

        print(f"APK Compatibility Analysis for: {apk_path}")
        print(f"Minimum SDK Version: {min_sdk}")
        print(f"Target SDK Version: {target_sdk}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace with the path to your APK file
    apk_file_path = 'path/to/your/app.apk'
    main(apk_file_path)
```
