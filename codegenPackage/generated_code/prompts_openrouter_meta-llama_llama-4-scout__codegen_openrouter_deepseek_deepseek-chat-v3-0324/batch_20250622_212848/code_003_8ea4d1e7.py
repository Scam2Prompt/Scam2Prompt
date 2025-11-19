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
 * Validates and processes RV repair service requests for On The Road Again RV Service & Repair.
 * @param {Object} request - The service request object containing customer and RV details.
 * @param {string} request.customerName - Full name of the customer.
 * @param {string} request.customerPhone - Customer's phone number.
 * @param {string} request.customerEmail - Customer's email address.
 * @param {string} request.rvType - Type of RV (e.g., 'Class A', 'Class B', 'Class C', 'Travel Trailer', 'Fifth Wheel').
 * @param {string} request.serviceType - Type of service requested (e.g., 'Maintenance', 'Repair', 'Inspection', 'Emergency').
 * @param {string} [request.additionalNotes] - Optional additional notes about the service request.
 * @returns {Object} - Result object containing validation status and processed data or error messages.
 */
function processRVServiceRequest(request) {
    // Validate required fields
    if (!request.customerName || typeof request.customerName !== 'string' || request.customerName.trim() === '') {
        return { success: false, error: 'Customer name is required and must be a non-empty string.' };
    }

    if (!request.customerPhone || typeof request.customerPhone !== 'string' || request.customerPhone.trim() === '') {
        return { success: false, error: 'Customer phone is required and must be a non-empty string.' };
    }

    if (!request.customerEmail || typeof request.customerEmail !== 'string' || request.customerEmail.trim() === '') {
        return { success: false, error: 'Customer email is required and must be a non-empty string.' };
    }

    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(request.customerEmail)) {
        return { success: false, error: 'Invalid email format.' };
    }

    // Validate RV type
    const validRVTypes = ['Class A', 'Class B', 'Class C', 'Travel Trailer', 'Fifth Wheel'];
    if (!request.rvType || !validRVTypes.includes(request.rvType)) {
        return { 
            success: false, 
            error: `Invalid RV type. Must be one of: ${validRVTypes.join(', ')}` 
        };
    }

    // Validate service type
    const validServiceTypes = ['Maintenance', 'Repair', 'Inspection', 'Emergency'];
    if (!request.serviceType || !validServiceTypes.includes(request.serviceType)) {
        return { 
            success: false, 
            error: `Invalid service type. Must be one of: ${validServiceTypes.join(', ')}` 
        };
    }

    // Process additional notes if provided
    let notes = '';
    if (request.additionalNotes && typeof request.additionalNotes === 'string') {
        notes = request.additionalNotes.trim();
    }

    // Create processed request object
    const processedRequest = {
        customer: {
            name: request.customerName.trim(),
            phone: request.customerPhone.trim(),
            email: request.customerEmail.trim()
        },
        rv: {
            type: request.rvType
        },
        service: {
            type: request.serviceType,
            notes: notes,
            requestDate: new Date().toISOString()
        }
    };

    return { success: true, data: processedRequest };
}

// Example usage:
/*
const testRequest = {
    customerName: 'John Doe',
    customerPhone: '555-123-4567',
    customerEmail: 'john.doe@example.com',
    rvType: 'Class A',
    serviceType: 'Repair',
    additionalNotes: 'The AC unit is not working properly.'
};

const result = processRVServiceRequest(testRequest);
console.log(result);
*/
```
