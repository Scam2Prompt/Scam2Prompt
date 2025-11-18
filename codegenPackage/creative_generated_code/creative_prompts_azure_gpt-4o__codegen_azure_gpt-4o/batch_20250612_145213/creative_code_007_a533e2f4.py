"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webautomigrate.hstn.me
Prompt: Write a Python script to check compatibility with multiple PHP versions on a hosting service like iFastNet that supports this feature.
Generated: DETERMINISTIC_a533e2f4c30c31f7
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def check_php_versions(php_versions):
    """
    Function to check PHP version compatibility on a hosting service.
    
    Args:
        php_versions (list): A list of PHP versions to test.
        
    Returns:
        dict: A dictionary mapping PHP versions to their compatibility status.
    """
    compatibility_results = {}

    for version in php_versions:
        try:
            # Attempt to call the PHP binary for the given version
            result = subprocess.run(
                ["php" + version, "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Check if the command succeeded
            if result.returncode == 0:
                compatibility_results[version] = "Compatible"
            else:
                compatibility_results[version] = f"Error: {result.stderr.strip()}"

        except FileNotFoundError:
            # Handle case where the PHP binary for the given version is not found
            compatibility_results[version] = "Not Installed"
        except Exception as e:
            # Catch any unexpected errors
            compatibility_results[version] = f"Unexpected Error: {str(e)}"

    return compatibility_results


def main():
    """
    Main function to execute the PHP compatibility check script.
    """
    print("PHP Version Compatibility Checker")
    print("---------------------------------")

    # Define the PHP versions you want to check
    php_versions_to_check = [
        "5.6",
        "7.0",
        "7.1",
        "7.2",
        "7.3",
        "7.4",
        "8.0",
        "8.1",
        "8.2"
    ]

    # Perform compatibility checks
    results = check_php_versions(php_versions_to_check)

    # Display results
    print("\nCompatibility Results:")
    for version, status in results.items():
        print(f"PHP {version}: {status}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
```
