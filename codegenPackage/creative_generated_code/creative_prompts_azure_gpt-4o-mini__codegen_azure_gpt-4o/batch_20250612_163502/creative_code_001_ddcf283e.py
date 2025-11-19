"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Can you provide a code snippet for running unit tests in a specific package of the Agoric SDK using Yarn?
Generated: DETERMINISTIC_ddcf283eb0979bbd
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# To run unit tests in a specific package of the Agoric SDK using Yarn,
# you can use the following script. This script assumes you are in the root
# directory of the Agoric SDK repository and the specific package has 
# test scripts defined in its `package.json`.

# Ensure you have Yarn installed and the Agoric SDK cloned.

# Replace `packages/<package-name>` with the path to your target package.
yarn workspace packages/<package-name> test
```

```bash
# Example for running tests in the `packages/zoe` package:
yarn workspace packages/zoe test
```
