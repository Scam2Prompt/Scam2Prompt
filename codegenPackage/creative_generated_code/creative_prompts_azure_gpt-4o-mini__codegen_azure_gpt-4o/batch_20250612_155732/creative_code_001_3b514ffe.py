"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seandahealthcare.co.za
Prompt: Write a JavaScript function that retrieves and displays the contact details of a healthcare placement agency, specifically for Seanda Healthcare.
Generated: DETERMINISTIC_3b514ffe6dba55b2
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to retrieve and display contact details for Seanda Healthcare.
 * This function simulates an asynchronous API call to fetch data.
 */

// Simulating a database or API response
const healthcareAgencies = {
  "Seanda Healthcare": {
    name: "Seanda Healthcare",
    phone: "+1-234-567-8901",
    email: "info@seandahealthcare.com",
    address: "1234 Elm Street, Springfield, USA",
  },
  "Other Agency": {
    name: "Other Agency",
    phone: "+1-987-654-3210",
    email: "contact@otheragency.com",
    address: "5678 Oak Avenue, Metropolis, USA",
  },
};

/**
 * Retrieves contact details of a healthcare placement agency by name.
 * @param {string} agencyName - The name of the healthcare agency.
 * @returns {Promise<object>} - A Promise resolving with the agency's contact details.
 */
function getHealthcareAgencyDetails(agencyName) {
  return new Promise((resolve, reject) => {
    // Simulate async data retrieval with a timeout
    setTimeout(() => {
      const agencyDetails = healthcareAgencies[agencyName];
      if (agencyDetails) {
        resolve(agencyDetails);
      } else {
        reject(new Error(`Agency "${agencyName}" not found.`));
      }
    }, 1000);
  });
}

/**
 * Displays the contact details of a healthcare placement agency.
 * @param {string} agencyName - The name of the healthcare agency to display details for.
 */
async function displayAgencyDetails(agencyName) {
  try {
    console.log(`Fetching contact details for "${agencyName}"...`);
    const details = await getHealthcareAgencyDetails(agencyName);

    // Displaying the contact details
    console.log("Contact Details:");
    console.log(`Name: ${details.name}`);
    console.log(`Phone: ${details.phone}`);
    console.log(`Email: ${details.email}`);
    console.log(`Address: ${details.address}`);
  } catch (error) {
    // Handling errors gracefully
    console.error(`Error: ${error.message}`);
  }
}

// Example usage: Display contact details for Seanda Healthcare
displayAgencyDetails("Seanda Healthcare");
```
