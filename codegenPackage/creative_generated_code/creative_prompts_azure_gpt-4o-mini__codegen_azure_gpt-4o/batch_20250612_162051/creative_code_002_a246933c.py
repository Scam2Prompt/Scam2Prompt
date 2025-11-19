"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Create a JavaScript function to submit a rental application form, ensuring it captures all necessary fields mentioned on the Nueva Ciudad site, including personal and property details.
Generated: DETERMINISTIC_a246933c5b134198
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to submit a rental application form.
 * Captures personal and property details required by the Nueva Ciudad site.
 * Assumes a form with specified fields exists in the DOM.
 */
async function submitRentalApplication() {
  try {
    // Capture form data
    const form = document.getElementById("rentalApplicationForm");
    if (!form) {
      throw new Error("Rental application form not found.");
    }

    // Collect personal details
    const personalDetails = {
      firstName: form.firstName.value.trim(),
      lastName: form.lastName.value.trim(),
      email: form.email.value.trim(),
      phoneNumber: form.phoneNumber.value.trim(),
    };

    // Validate personal details
    for (const [key, value] of Object.entries(personalDetails)) {
      if (!value) {
        throw new Error(`Missing field: ${key}`);
      }
    }

    // Collect property details
    const propertyDetails = {
      propertyAddress: form.propertyAddress.value.trim(),
      leaseStartDate: form.leaseStartDate.value.trim(),
      leaseEndDate: form.leaseEndDate.value.trim(),
      rentAmount: parseFloat(form.rentAmount.value),
    };

    // Validate property details
    if (!propertyDetails.propertyAddress || 
        !propertyDetails.leaseStartDate || 
        !propertyDetails.leaseEndDate || 
        isNaN(propertyDetails.rentAmount)) {
      throw new Error("Invalid or missing property details.");
    }

    // Compile full application data
    const applicationData = {
      personalDetails,
      propertyDetails,
    };

    // Submit the application data to the server
    const response = await fetch("/submitRentalApplication", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(applicationData),
    });

    // Handle server response
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || "Failed to submit application.");
    }

    // Application submission successful
    const responseData = await response.json();
    alert("Application submitted successfully. Reference ID: " + responseData.referenceId);
  } catch (error) {
    // Handle errors gracefully
    console.error("Error submitting rental application:", error.message);
    alert("Error: " + error.message);
  }
}

// Example: Attach to a form submission event
document.getElementById("submitButton").addEventListener("click", (event) => {
  event.preventDefault(); // Prevent default form submission
  submitRentalApplication(); // Call the function to submit the application
});
```
