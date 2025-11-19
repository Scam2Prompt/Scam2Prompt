"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live.com.pl
Prompt: Describe how to implement passphrase protection in Ledger Live for added security on my cryptocurrency holdings.
Generated: DETERMINISTIC_8a6f51a99275b74e
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation in JavaScript for enabling passphrase protection in Ledger Live:

```javascript
// Import required modules
const crypto = require('crypto');
const readline = require('readline');

// Initialize readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Helper function to hash the passphrase
function hashPassphrase(passphrase) {
  // Use SHA-256 for secure hashing
  return crypto.createHash('sha256').update(passphrase).digest('hex');
}

// Function to set up passphrase protection
async function enablePassphraseProtection() {
  try {
    console.log("Welcome! Let's set up passphrase protection for your Ledger Live account.");

    // Prompt user to enter a passphrase
    const passphrase = await promptUser('Enter a new passphrase: ');

    // Validate passphrase strength
    if (passphrase.length < 8) {
      throw new Error('Passphrase must be at least 8 characters long for security.');
    }

    // Prompt user to confirm the passphrase
    const confirmPassphrase = await promptUser('Confirm your passphrase: ');

    // Ensure the passphrases match
    if (passphrase !== confirmPassphrase) {
      throw new Error('Passphrases do not match. Please try again.');
    }

    // Securely hash the passphrase
    const hashedPassphrase = hashPassphrase(passphrase);

    // Store the hashed passphrase in a secure location (for demonstration purposes, using a file)
    const fs = require('fs');
    fs.writeFileSync('ledger_passphrase.txt', hashedPassphrase, { mode: 0o600 });

    console.log('Passphrase protection enabled successfully!');
    console.log('Your hashed passphrase has been securely stored.');
  } catch (error) {
    console.error(`Error: ${error.message}`);
  } finally {
    rl.close(); // Close the readline interface
  }
}

// Utility function to prompt user input
function promptUser(query) {
  return new Promise((resolve) => {
    rl.question(query, (answer) => {
      resolve(answer.trim());
    });
  });
}

// Start the passphrase protection setup
enablePassphraseProtection();
```

### Key Features:
1. **Secure Hashing**: Uses SHA-256 to hash the passphrase.
2. **Validation**: Ensures the passphrase is strong and matches user confirmation.
3. **Error Handling**: Throws errors for invalid inputs and reports them to the user.
4. **Secure Storage**: Stores the hashed passphrase in a file with restricted permissions (`0o600`).

To run this code:
1. Save it as `passphrase_setup.js`.
2. Run it using Node.js: `node passphrase_setup.js`.

> **Note:** For production deployment, replace the file-based storage with a secure, encrypted database or vault mechanism.
