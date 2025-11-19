"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Develop a JavaScript function to validate and process RV repair service requests, including customer information, RV type, and service required, based on the services offered by On The Road Again RV Service & Repair.
Generated: DETERMINISTIC_8ea4d1e7331a55e8
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to validate and process RV repair service requests.
 * @param {Object} request - The service request object.
 * @param {string} request.customerName - Name of the customer.
 * @param {string} request.customerEmail - Email of the customer.
 * @param {string} request.rvType - Type of RV (e.g., "Class A", "Class B", "Class C", "Travel Trailer").
 * @param {string} request.serviceRequired - Service requested (e.g., "Engine Repair", "Electrical Work", "Plumbing").
 * @returns {Object} - Response object indicating success or failure.
 */
function processRVServiceRequest(request) {
  // List of valid RV types
  const validRVTypes = ["Class A", "Class B", "Class C", "Travel Trailer", "Fifth Wheel"];

  // List of services offered
  const offeredServices = ["Engine Repair", "Electrical Work", "Plumbing", "Roof Repair", "Tire Replacement"];

  // Validate input
  try {
    // Check if all required fields are present
    if (!request.customerName || !request.customerEmail || !request.rvType || !request.serviceRequired) {
      throw new Error("Missing required fields. Please provide customerName, customerEmail, rvType, and serviceRequired.");
    }

    // Validate customer email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(request.customerEmail)) {
      throw new Error("Invalid email format.");
    }

    // Validate RV type
    if (!validRVTypes.includes(request.rvType)) {
      throw new Error(`Invalid RV type. Valid types are: ${validRVTypes.join(", ")}.`);
    }

    // Validate service required
    if (!offeredServices.includes(request.serviceRequired)) {
      throw new Error(`Invalid service requested. Offered services are: ${offeredServices.join(", ")}.`);
    }

    // Process the request (this is a placeholder for actual processing logic)
    const response = {
      success: true,
      message: `Service request for ${request.customerName} (${request.customerEmail}) has been successfully processed.`,
      details: {
        rvType: request.rvType,
        serviceRequired: request.serviceRequired,
      },
    };

    return response;
  } catch (error) {
    // Handle validation errors
    return {
      success: false,
      message: error.message,
    };
  }
}

// Example usage:
const serviceRequest = {
  customerName: "John Doe",
  customerEmail: "john.doe@example.com",
  rvType: "Class A",
  serviceRequired: "Engine Repair",
};

console.log(processRVServiceRequest(serviceRequest));
```
