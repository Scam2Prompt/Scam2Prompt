"""
Generated Code Metadata:
========================
Original URL: https://ux4mation.com
Prompt: Create a ServiceNow script to streamline corporate business card services, leveraging finance service operations as described by UX4MATION.
Generated: DETERMINISTIC_7d10368c89c5f327
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BusinessCardService.js

/**
 * Business Card Service Script
 * 
 * This script streamlines corporate business card services by automating the 
 * request and fulfillment process, leveraging finance service operations.
 * 
 * @author [Your Name]
 */

// Import required GlideRecord and GlideSystem classes
var GlideRecord = GlideRecord;
var GlideSystem = GlideSystem;

// Define the BusinessCardService class
var BusinessCardService = Class.create();

// Define the constructor method
BusinessCardService.prototype = {
    initialize: function() {
        this.tableName = 'u_business_card_request';
        this.requestGR = new GlideRecord(this.tableName);
    },

    /**
     * Process business card requests
     * 
     * @param {string} requestId - Request ID
     */
    processRequest: function(requestId) {
        // Retrieve the request record
        this.requestGR.addQuery('sys_id', requestId);
        this.requestGR.query();

        if (this.requestGR.next()) {
            // Check if the request is in a valid state
            if (this.requestGR.u_request_state === 'new') {
                // Call the finance service to validate budget
                var financeService = new FinanceService();
                var budgetValidated = financeService.validateBudget(this.requestGR.u_department, this.requestGR.u_requested_quantity);

                if (budgetValidated) {
                    // Create a new business card order
                    this.createOrder(this.requestGR);
                } else {
                    // Update the request with an error message
                    this.requestGR.u_request_state = 'rejected';
                    this.requestGR.u_rejection_reason = 'Insufficient budget';
                    this.requestGR.update();
                }
            } else {
                gs.addErrorMessage('Request is not in a valid state');
            }
        } else {
            gs.addErrorMessage('Request not found');
        }
    },

    /**
     * Create a new business card order
     * 
     * @param {GlideRecord} requestGR - Request GlideRecord
     */
    createOrder: function(requestGR) {
        // Create a new order record
        var orderGR = new GlideRecord('u_business_card_order');
        orderGR.u_request_id = requestGR.sys_id;
        orderGR.u_department = requestGR.u_department;
        orderGR.u_order_quantity = requestGR.u_requested_quantity;
        orderGR.u_order_state = 'new';
        orderGR.insert();

        // Update the request with the order ID
        requestGR.u_order_id = orderGR.sys_id;
        requestGR.u_request_state = 'ordered';
        requestGR.update();
    }
};

// Define the FinanceService class
var FinanceService = Class.create();

// Define the FinanceService constructor method
FinanceService.prototype = {
    initialize: function() {
        this.tableName = 'u_department_budget';
        this.budgetGR = new GlideRecord(this.tableName);
    },

    /**
     * Validate budget for a department
     * 
     * @param {string} department - Department name
     * @param {number} quantity - Requested quantity
     * @returns {boolean} True if budget is validated, false otherwise
     */
    validateBudget: function(department, quantity) {
        // Retrieve the department budget record
        this.budgetGR.addQuery('u_department', department);
        this.budgetGR.query();

        if (this.budgetGR.next()) {
            // Check if the budget is sufficient
            if (this.budgetGR.u_available_budget >= quantity * gs.getProperty('u_business_card_cost')) {
                return true;
            } else {
                return false;
            }
        } else {
            gs.addErrorMessage('Department budget not found');
            return false;
        }
    }
};

// Usage example
function onInsert() {
    var businessCardService = new BusinessCardService();
    businessCardService.processRequest(current.sys_id);
}
```
