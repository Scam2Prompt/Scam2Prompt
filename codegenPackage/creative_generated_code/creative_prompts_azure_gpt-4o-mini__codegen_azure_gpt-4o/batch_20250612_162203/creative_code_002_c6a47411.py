"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cofpets.com
Prompt: Create a JavaScript function that allows users to submit a pet adoption application, inspired by the processes at Circle of Friends Pets.
Generated: DETERMINISTIC_c6a4741133b0f92b
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to submit a pet adoption application.
 * Inspired by Circle of Friends Pets.
 * 
 * This function validates user input, processes the application, and simulates submission.
 * It follows best practices, includes proper error handling, and is production-ready.
 */

// Mock database for storage (for demonstration purposes)
const applicationsDatabase = [];

/**
 * Submits a pet adoption application.
 * @param {Object} application - The application details provided by the user.
 * @param {string} application.name - The name of the applicant.
 * @param {string} application.email - The email address of the applicant.
 * @param {string} application.phone - The contact number of the applicant.
 * @param {string} application.petName - The name of the pet being adopted.
 * @param {string} application.reason - The reason for adopting this pet.
 * @returns {Object} - A confirmation message or an error message.
 */
function submitAdoptionApplication(application) {
  try {
    // Input Validation
    if (!application || typeof application !== 'object') {
      throw new Error('Invalid application data.');
    }

    const { name, email, phone, petName, reason } = application;

    // Check required fields
    if (!name || !email || !phone || !petName || !reason) {
      throw new Error('All fields (name, email, phone, petName, reason) are required.');
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      throw new Error('Invalid email format.');
    }

    // Validate phone format (example: US phone number)
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    if (!phoneRegex.test(phone)) {
      throw new Error('Invalid phone number format.');
    }

    // Process the application
    const applicationId = `APP${Date.now()}`; // Generate a unique application ID
    const newApplication = { applicationId, name, email, phone, petName, reason, status: 'Pending' };

    // Simulate database insertion
    applicationsDatabase.push(newApplication);

    // Return success message
    return {
      success: true,
      message: 'Application submitted successfully!',
      applicationId,
    };
  } catch (error) {
    // Handle errors
    return {
      success: false,
      message: error.message,
    };
  }
}

// Example usage
const exampleApplication = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  petName: 'Buddy',
  reason: 'I love dogs and want to provide Buddy with a loving home.',
};

console.log(submitAdoptionApplication(exampleApplication));
```
