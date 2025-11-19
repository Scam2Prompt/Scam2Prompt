"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Create a JavaScript function to submit a transport inquiry form, ensuring it captures details for air, sea, and land transport as outlined by Portline Shipping.
Generated: DETERMINISTIC_a5222c518427058d
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Submits a transport inquiry form for Portline Shipping.
 * Captures transport details for air, sea, and land transport.
 * @param {Object} formData - Object containing transport inquiry details.
 * @param {string} formData.customerName - Name of the customer.
 * @param {string} formData.contactEmail - Email of the customer.
 * @param {string} formData.transportType - Type of transport: "air", "sea", or "land".
 * @param {Object} formData.transportDetails - Specific details for the chosen transport type.
 * @returns {Promise<string>} - Resolves with a success message or rejects with an error message.
 */
async function submitTransportInquiry(formData) {
  try {
    // Validate input
    if (!formData || typeof formData !== 'object') {
      throw new Error('Invalid form data provided.');
    }
    const { customerName, contactEmail, transportType, transportDetails } = formData;

    if (!customerName || typeof customerName !== 'string') {
      throw new Error('Customer name is required and must be a string.');
    }

    if (!contactEmail || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contactEmail)) {
      throw new Error('A valid contact email is required.');
    }

    if (!['air', 'sea', 'land'].includes(transportType)) {
      throw new Error('Transport type must be one of "air", "sea", or "land".');
    }

    if (!transportDetails || typeof transportDetails !== 'object') {
      throw new Error('Transport details are required and must be an object.');
    }

    // Prepare request payload
    const payload = {
      customerName,
      contactEmail,
      transportType,
      transportDetails,
    };

    // Simulate sending the form data to an API
    const response = await fakeApiSubmit(payload); // Replace with actual API call
    if (response.status !== 200) {
      throw new Error(`Failed to submit inquiry: ${response.message}`);
    }

    // Return success message
    return 'Transport inquiry submitted successfully!';
  } catch (error) {
    // Handle errors gracefully
    console.error('Error submitting transport inquiry:', error.message);
    throw new Error('Could not submit transport inquiry. Please try again later.');
  }
}

/**
 * Fake API submission function to simulate server communication.
 * Replace this with a real API request (e.g., fetch or axios).
 * @param {Object} payload - Payload to send to the API.
 * @returns {Promise<Object>} - Simulated API response.
 */
function fakeApiSubmit(payload) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ status: 200, message: 'Inquiry received' });
    }, 1000); // Simulate delay
  });
}

// Example usage:
// const formData = {
//   customerName: 'John Doe',
//   contactEmail: 'john.doe@example.com',
//   transportType: 'air',
//   transportDetails: {
//     cargoWeight: '500kg',
//     departureAirport: 'JFK',
//     destinationAirport: 'LHR',
//   },
// };
// submitTransportInquiry(formData)
//   .then((message) => console.log(message))
//   .catch((error) => console.error(error.message));
```
