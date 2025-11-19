"""
Generated Code Metadata:
========================
Original URL: https://fronkgift.web.app
Prompt: Write code to validate user entries against a whitelist in a JavaScript application, similar to the Fronk Inu whitelist functionality.
Generated: DETERMINISTIC_06c61db81ba072e4
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * WhitelistValidator class for validating user entries against a whitelist.
 */
class WhitelistValidator {
  /**
   * Constructor for WhitelistValidator.
   * @param {Array<string>} whitelist - The list of allowed entries.
   */
  constructor(whitelist) {
    if (!Array.isArray(whitelist)) {
      throw new Error('Whitelist must be an array.');
    }
    this.whitelist = whitelist.map((entry) => entry.toLowerCase());
  }

  /**
   * Validate a user entry against the whitelist.
   * @param {string} entry - The user entry to validate.
   * @returns {boolean} True if the entry is in the whitelist, false otherwise.
   */
  validate(entry) {
    if (typeof entry !== 'string') {
      throw new Error('Entry must be a string.');
    }
    return this.whitelist.includes(entry.toLowerCase());
  }

  /**
   * Check if a user entry is in the whitelist and throw an error if not.
   * @param {string} entry - The user entry to validate.
   * @throws {Error} If the entry is not in the whitelist.
   */
  validateStrict(entry) {
    if (!this.validate(entry)) {
      throw new Error(`Entry '${entry}' is not in the whitelist.`);
    }
  }
}

// Example usage:
function main() {
  const whitelist = ['user1', 'user2', 'user3'];
  const validator = new WhitelistValidator(whitelist);

  try {
    console.log(validator.validate('user1')); // true
    console.log(validator.validate('user4')); // false
    validator.validateStrict('user4'); // Throws an error
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
