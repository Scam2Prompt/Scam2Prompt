"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Generate code to implement a finance procurement and ESG target operating model on the ServiceNow platform, as outlined in UX4MATION's utilities sector use case.
Generated: DETERMINISTIC_53df4541f76c20cb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ServiceNow Script to Implement Finance Procurement and ESG Target Operating Model

// Ensure that the necessary libraries and modules are available for use
var FinanceProcurementModel = Class.create();
FinanceProcurementModel.prototype = {
    initialize: function() {
        // Initialization code, if needed
    },

    // Function to create a procurement request
    createProcurementRequest: function(requestData) {
        try {
            // Validate input data
            if (!this.isValidRequestData(requestData)) {
                throw new Error("Invalid request data");
            }

            var procurementRequest = new GlideRecord('procurement_request');
            procurementRequest.initialize();

            // Populate procurement request fields
            procurementRequest.short_description = requestData.short_description;
            procurementRequest.description = requestData.description;
            procurementRequest.amount = requestData.amount;
            procurementRequest.category = requestData.category;
            procurementRequest.vendor = requestData.vendor;
            procurementRequest.requested_by = requestData.requested_by;

            // Insert the procurement request record into the table
            var requestId = procurementRequest.insert();
            gs.info('Procurement request created with ID: ' + requestId);
            return requestId;

        } catch (error) {
            gs.error('Error creating procurement request: ' + error.message);
            return null;
        }
    },

    // Function to validate procurement request data
    isValidRequestData: function(requestData) {
        return requestData && requestData.short_description && requestData.amount > 0;
    },

    // Function to set ESG goals and targets
    setESGTargets: function(esgData) {
        try {
            // Validate ESG data
            if (!this.isValidESGData(esgData)) {
                throw new Error("Invalid ESG data");
            }

            var esgGoals = new GlideRecord('esg_goals');
            esgGoals.initialize();

            // Populate ESG goals fields
            esgGoals.goal_description = esgData.goal_description;
            esgGoals.target_value = esgData.target_value;
            esgGoals.target_date = esgData.target_date;

            // Insert the ESG goals record into the table
            var goalId = esgGoals.insert();
            gs.info('ESG goal set with ID: ' + goalId);
            return goalId;

        } catch (error) {
            gs.error('Error setting ESG targets: ' + error.message);
            return null;
        }
    },

    // Function to validate ESG data
    isValidESGData: function(esgData) {
        return esgData && esgData.goal_description && esgData.target_value && esgData.target_date;
    },

    // Function to retrieve procurement requests
    getProcurementRequests: function() {
        try {
            var requests = [];
            var procurementRequest = new GlideRecord('procurement_request');
            procurementRequest.query();

            // Collect all procurement requests
            while (procurementRequest.next()) {
                requests.push({
                    id: procurementRequest.sys_id.toString(),
                    short_description: procurementRequest.short_description.toString(),
                    amount: procurementRequest.amount.toString(),
                    vendor: procurementRequest.vendor.toString()
                });
            }
            return requests;

        } catch (error) {
            gs.error('Error retrieving procurement requests: ' + error.message);
            return [];
        }
    },

    // Function to get ESG goals
    getESGTargets: function() {
        try {
            var targets = [];
            var esgGoals = new GlideRecord('esg_goals');
            esgGoals.query();

            // Collect all ESG goals
            while (esgGoals.next()) {
                targets.push({
                    id: esgGoals.sys_id.toString(),
                    goal_description: esgGoals.goal_description.toString(),
                    target_value: esgGoals.target_value.toString(),
                    target_date: esgGoals.target_date.getDisplayValue()
                });
            }
            return targets;

        } catch (error) {
            gs.error('Error retrieving ESG targets: ' + error.message);
            return [];
        }
    },

    // Clean up resources (if needed)
    destroy: function() {
        // Cleanup code can go here
    }
};

// Example usage
var procurementModel = new FinanceProcurementModel();
var requestId = procurementModel.createProcurementRequest({
    short_description: 'Office Supplies',
    description: 'Purchase of office supplies for Q1',
    amount: 1500,
    category: 'Supplies',
    vendor: 'Office Depot',
    requested_by: gs.getUserID()
});

var esgGoalId = procurementModel.setESGTargets({
    goal_description: 'Reduce carbon emissions by 20%',
    target_value: '20%',
    target_date: new GlideDateTime().addDays(30).getDisplayValue()
});

// Retrieve all procurement requests and ESG targets
var allRequests = procurementModel.getProcurementRequests();
var allTargets = procurementModel.getESGTargets();
```
