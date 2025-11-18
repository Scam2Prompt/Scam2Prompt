"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.tools
Prompt: Create a JavaScript application to display and validate BIP32 derivation paths for Bitcoin wallets, including compatibility with BIP44, BIP49, and BIP84, as outlined on https://bip32.tools.
Generated: DETERMINISTIC_6910fc5227891d5e
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// BIP32 Derivation Path Validator Application
// This application validates BIP32 derivation paths for Bitcoin wallets while ensuring compatibility with BIP44, BIP49, and BIP84.
// Author: Expert Programmer

// Function to validate derivation paths
function validateDerivationPath(path) {
  const validBIP32 = /^m(\/\d+'?)*$/; // Matches BIP32 derivation paths (e.g., m/0'/1/2')
  const validBIP44 = /^m\/44'\/\d+'\/\d+'(\/[0-1])?(\/\d+)?$/; // Matches BIP44 paths
  const validBIP49 = /^m\/49'\/\d+'\/\d+'(\/[0-1])?(\/\d+)?$/; // Matches BIP49 paths
  const validBIP84 = /^m\/84'\/\d+'\/\d+'(\/[0-1])?(\/\d+)?$/; // Matches BIP84 paths

  if (!validBIP32.test(path)) {
    return { isValid: false, message: "Invalid BIP32 derivation path syntax." };
  }

  if (validBIP44.test(path)) {
    return { isValid: true, type: "BIP44", message: "Valid BIP44 derivation path." };
  }

  if (validBIP49.test(path)) {
    return { isValid: true, type: "BIP49", message: "Valid BIP49 derivation path." };
  }

  if (validBIP84.test(path)) {
    return { isValid: true, type: "BIP84", message: "Valid BIP84 derivation path." };
  }

  return { isValid: true, type: "BIP32", message: "Valid generic BIP32 derivation path." };
}

// Function to display validation results
function displayValidationResult(path, result) {
  console.log(`Derivation Path: ${path}`);
  if (result.isValid) {
    console.log(`Validation Status: ✅ VALID`);
    console.log(`Path Type: ${result.type}`);
    console.log(`Message: ${result.message}`);
  } else {
    console.log(`Validation Status: ❌ INVALID`);
    console.log(`Error: ${result.message}`);
  }
}

// Main application logic
function runApp() {
  const readline = require("readline");

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  console.log("BIP32 Derivation Path Validator");
  console.log("Supports BIP44, BIP49, and BIP84 paths.");
  console.log("Enter a derivation path for validation (e.g., m/44'/0'/0'/0/0):");

  rl.question("Enter derivation path: ", (path) => {
    try {
      const validationResult = validateDerivationPath(path);
      displayValidationResult(path, validationResult);
    } catch (error) {
      console.error("An unexpected error occurred:", error.message);
    } finally {
      rl.close();
    }
  });
}

// Run the application
runApp();
```

This code is a complete, production-ready JavaScript application that validates BIP32 derivation paths. It includes error handling, well-documented functions, and follows best practices to ensure correctness and maintainability.
