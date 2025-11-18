"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.apexbooster.com
Prompt: Generate JavaScript code to create a dropdown menu for language selection, referencing the language options available on Apex Booster (e.g., Tiếng Việt, Türkçe, and Română).
Generated: DETERMINISTIC_1ed59a9155b3464a
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Creates a language selection dropdown menu.
 * This code dynamically populates the dropdown with language options.
 * Includes error handling and follows JavaScript best practices.
 */

// Language options available on Apex Booster
const languageOptions = ["Tiếng Việt", "Türkçe", "Română"];

/**
 * Function to create a dropdown menu for language selection.
 * @param {string} dropdownId - The ID to assign to the dropdown element.
 */
function createLanguageDropdown(dropdownId) {
  try {
    // Validate that `dropdownId` is a non-empty string
    if (typeof dropdownId !== "string" || dropdownId.trim() === "") {
      throw new Error("Invalid dropdownId provided. It must be a non-empty string.");
    }

    // Create the dropdown element
    const dropdown = document.createElement("select");
    dropdown.id = dropdownId;
    dropdown.name = "languageSelection";
    dropdown.style.padding = "5px"; // Optional styling for better UI

    // Append each language option to the dropdown
    languageOptions.forEach((language) => {
      const option = document.createElement("option");
      option.value = language.toLowerCase(); // Set value as lowercase for consistency
      option.textContent = language; // Display name in dropdown
      dropdown.appendChild(option);
    });

    // Append the dropdown to the document body or another container
    const container = document.getElementById("dropdownContainer") || document.body;
    container.appendChild(dropdown);

    console.log("Language dropdown created successfully.");
  } catch (error) {
    console.error(
      "An error occurred while creating the language dropdown:",
      error.message
    );
  }
}

// Usage example: Create a dropdown with ID 'languageDropdown'
createLanguageDropdown("languageDropdown");
```
