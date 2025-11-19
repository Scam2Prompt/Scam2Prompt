"""
Generated Code Metadata:
========================
Original URL: https://ajrobloxgfx.org
Prompt: Develop a JavaScript function to toggle between the different profile picture options (Floating head, Golden Floating head, Front facing) with their respective prices and descriptions.
Generated: DETERMINISTIC_503664768788b24d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// profilePictureOptions.js

/**
 * Profile Picture Options class.
 * Manages different profile picture options with their respective prices and descriptions.
 */
class ProfilePictureOptions {
  /**
   * Constructor for ProfilePictureOptions.
   */
  constructor() {
    // Define profile picture options
    this.options = [
      {
        id: 1,
        name: 'Floating head',
        price: 0.99,
        description: 'A floating head profile picture.',
        isSelected: false,
      },
      {
        id: 2,
        name: 'Golden Floating head',
        price: 1.99,
        description: 'A golden floating head profile picture.',
        isSelected: false,
      },
      {
        id: 3,
        name: 'Front facing',
        price: 2.99,
        description: 'A front facing profile picture.',
        isSelected: false,
      },
    ];
  }

  /**
   * Toggles the selection of a profile picture option.
   * @param {number} id - The id of the profile picture option to toggle.
   * @throws {Error} If the id is not found.
   */
  toggleOption(id) {
    const option = this.options.find((opt) => opt.id === id);
    if (!option) {
      throw new Error(`Option with id ${id} not found.`);
    }
    // Deselect all options
    this.options.forEach((opt) => {
      opt.isSelected = false;
    });
    // Select the chosen option
    option.isSelected = true;
  }

  /**
   * Gets the currently selected profile picture option.
   * @returns {object} The currently selected profile picture option.
   */
  getSelectedOption() {
    return this.options.find((opt) => opt.isSelected);
  }

  /**
   * Gets all profile picture options.
   * @returns {array} All profile picture options.
   */
  getOptions() {
    return this.options;
  }
}

// Example usage:
function main() {
  try {
    const profilePictureOptions = new ProfilePictureOptions();
    console.log('Profile Picture Options:');
    console.log(profilePictureOptions.getOptions());

    // Toggle option 2
    profilePictureOptions.toggleOption(2);
    console.log('Selected Option:');
    console.log(profilePictureOptions.getSelectedOption());

    // Toggle option 1
    profilePictureOptions.toggleOption(1);
    console.log('Selected Option:');
    console.log(profilePictureOptions.getSelectedOption());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
