"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Can you provide a code example for importing an operating model from Stock Synthesis 3 using openMSE?
Generated: DETERMINISTIC_d4e8cfaa0dca03e6
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import numpy as np
from openmse import om_from_ss3

def import_operating_model_from_ss3(
    ss3_par_file: str, 
    ss3_ctrl_file: str, 
    ss3_dat_file: str, 
    om_outfile: str = None
) -> dict:
    """
    Import an operating model from Stock Synthesis 3 using openMSE.

    Args:
    - ss3_par_file (str): Path to the Stock Synthesis 3 parameter file (.par).
    - ss3_ctrl_file (str): Path to the Stock Synthesis 3 control file (.ctl).
    - ss3_dat_file (str): Path to the Stock Synthesis 3 data file (.dat).
    - om_outfile (str, optional): Path to save the operating model. Defaults to None.

    Returns:
    - dict: The imported operating model.
    """

    try:
        # Check if files exist
        if not all([os.path.isfile(f) for f in [ss3_par_file, ss3_ctrl_file, ss3_dat_file]]):
            raise FileNotFoundError("One or more Stock Synthesis 3 files not found.")

        # Import operating model from Stock Synthesis 3
        om = om_from_ss3(ss3_par_file, ss3_ctrl_file, ss3_dat_file)

        # Save operating model if outfile specified
        if om_outfile is not None:
            om.to_yaml(om_outfile)

        return om

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    ss3_par_file = "path/to/model.par"
    ss3_ctrl_file = "path/to/model.ctl"
    ss3_dat_file = "path/to/model.dat"
    om_outfile = "path/to/om.yaml"

    om = import_operating_model_from_ss3(ss3_par_file, ss3_ctrl_file, ss3_dat_file, om_outfile)
    print(om)
```
