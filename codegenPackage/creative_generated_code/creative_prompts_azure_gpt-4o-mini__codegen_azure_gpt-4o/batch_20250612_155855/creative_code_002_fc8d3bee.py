"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Create a JavaScript function that facilitates community engagement by allowing users to sign up for environmental workshops and sustainability projects.
Generated: DETERMINISTIC_fc8d3bee6aab0a82
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to facilitate community engagement by allowing users 
 * to sign up for environmental workshops and sustainability projects.
 * 
 * Requirements:
 * - Users can provide their name, email, and select a workshop/project.
 * - Data is validated before submission.
 * - Includes error handling to manage invalid inputs.
 * - Returns a success message on successful registration.
 */

// List of available projects and workshops
const availablePrograms = [
  { id: 1, name: "Urban Gardening Workshop" },
  { id: 2, name: "Beach Cleanup Project" },
  { id: 3, name: "Recycling 101 Workshop" },
  { id: 4, name: "Renewable Energy Awareness Project" }
];

/**
 * Validates user inputs.
 * @param {string} name - User's name.
 * @param {string} email - User's email.
 * @param {number} programId - ID of the selected program.
 * @returns {Object|null} - Returns an error object if validation fails, else null.
 */
function validateInputs(name, email, programId) {
  if (!name || name.trim() === "") {
    return { error: "Name cannot be empty." };
  }
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return { error: "Invalid email address." };
  }
  const programExists = availablePrograms.some(
    (program) => program.id === programId
  );
  if (!programExists) {
    return { error: "Selected program does not exist." };
  }
  return null;
}

/**
 * Registers the user for an environmental workshop or project.
 * @param {string} name - User's name.
 * @param {string} email - User's email.
 * @param {number} programId - ID of the selected program.
 * @returns {string} - Success or error message.
 */
function registerForProgram(name, email, programId) {
  // Validate user inputs
  const validationError = validateInputs(name, email, programId);
  if (validationError) {
    return `Error: ${validationError.error}`;
  }

  // Simulate database/store save operation
  try {
    const selectedProgram = availablePrograms.find(
      (program) => program.id === programId
    );
    const registrationData = {
      name: name.trim(),
      email: email.trim(),
      program: selectedProgram.name,
      timestamp: new Date().toISOString()
    };

    // In a real-world application, this data would be stored in a database.
    console.log("Registration successful:", registrationData);

    // Return success message
    return `Thank you ${name.trim()}! You have successfully signed up for the "${selectedProgram.name}".`;
  } catch (error) {
    // Handle unexpected errors
    console.error("An unexpected error occurred:", error);
    return "An unexpected error occurred. Please try again later.";
  }
}

// Example usage:
// const result = registerForProgram("Jane Doe", "jane.doe@example.com", 2);
// console.log(result);
```
