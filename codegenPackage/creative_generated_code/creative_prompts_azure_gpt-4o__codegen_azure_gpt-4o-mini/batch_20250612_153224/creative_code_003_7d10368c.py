"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Create a ServiceNow script to streamline corporate business card services, leveraging finance service operations as described by UX4MATION.
Generated: DETERMINISTIC_7d10368c89c5f327
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ServiceNow Business Card Service Script
// This script automates the process of managing corporate business card requests
// leveraging the capabilities of the finance service operations.

// Function to create a new business card request
function createBusinessCardRequest(userId, cardDetails) {
    try {
        // Validate input parameters
        if (!userId || !cardDetails) {
            throw new Error("Missing required parameters: userId or cardDetails.");
        }

        // Create a new GlideRecord for the business card request
        var businessCardRequest = new GlideRecord('u_business_card_request');
        businessCardRequest.initialize();
        
        // Set required fields for the business card request
        businessCardRequest.u_user = userId; // User ID for the request
        businessCardRequest.u_card_details = JSON.stringify(cardDetails); // Card details as JSON string
        businessCardRequest.u_status = 'Pending'; // Initial status of the request
        
        // Insert the new record into the database
        var requestId = businessCardRequest.insert();
        
        // Check if insert was successful
        if (!requestId) {
            throw new Error("Failed to create business card request.");
        }

        // Return success response with request ID
        return {
            success: true,
            message: "Business card request created successfully.",
            requestId: requestId
        };

    } catch (error) {
        // Log the error and return failure response
        gs.error("Error creating business card request: " + error.message);
        return {
            success: false,
            message: error.message
        };
    }
}

// Function to approve a business card request
function approveBusinessCardRequest(requestId) {
    try {
        // Validate request ID
        if (!requestId) {
            throw new Error("Missing required parameter: requestId.");
        }

        // Retrieve the business card request record
        var businessCardRequest = new GlideRecord('u_business_card_request');
        if (!businessCardRequest.get(requestId)) {
            throw new Error("Business card request not found.");
        }

        // Update the status to approved
        businessCardRequest.u_status = 'Approved';
        businessCardRequest.update();

        // Return success response
        return {
            success: true,
            message: "Business card request approved successfully."
        };

    } catch (error) {
        // Log the error and return failure response
        gs.error("Error approving business card request: " + error.message);
        return {
            success: false,
            message: error.message
        };
    }
}

// Function to reject a business card request
function rejectBusinessCardRequest(requestId) {
    try {
        // Validate request ID
        if (!requestId) {
            throw new Error("Missing required parameter: requestId.");
        }

        // Retrieve the business card request record
        var businessCardRequest = new GlideRecord('u_business_card_request');
        if (!businessCardRequest.get(requestId)) {
            throw new Error("Business card request not found.");
        }

        // Update the status to rejected
        businessCardRequest.u_status = 'Rejected';
        businessCardRequest.update();

        // Return success response
        return {
            success: true,
            message: "Business card request rejected successfully."
        };

    } catch (error) {
        // Log the error and return failure response
        gs.error("Error rejecting business card request: " + error.message);
        return {
            success: false,
            message: error.message
        };
    }
}

// Example usage:
// var result = createBusinessCardRequest('user_sys_id', { name: 'John Doe', title: 'Software Engineer' });
// gs.info(JSON.stringify(result));
```
