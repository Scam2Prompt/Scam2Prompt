"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Create a ServiceNow script for automating finance and accounting processes, inspired by UX4MATION's expertise in digitizing IT4IT frameworks.
Generated: DETERMINISTIC_c87785d9b2f9e5bd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ServiceNow Script Include for Automating Finance and Accounting Processes
// Inspired by UX4Mation's expertise in digitizing IT4IT frameworks

var FinanceAutomation = Class.create();
FinanceAutomation.prototype = {
    initialize: function() {
        // Initialize any necessary variables or state here
        this.financeTable = 'finance_records'; // Define the table to operate on
    },

    /**
     * Automates the process of creating a new finance record.
     * @param {Object} financeData - The data for the finance record.
     * @returns {string} - The sys_id of the created record.
     * @throws Will throw an error if the record creation fails.
     */
    createFinanceRecord: function(financeData) {
        var gr = new GlideRecord(this.financeTable);
        gr.initialize();

        // Set the fields of the finance record based on input data
        gr.setValue('amount', financeData.amount);
        gr.setValue('type', financeData.type);
        gr.setValue('date', financeData.date);
        gr.setValue('description', financeData.description);

        // Try to insert the record into the database
        try {
            var sysId = gr.insert();
            if (!sysId) {
                throw new Error('Record insertion failed.');
            }
            return sysId; // Return the sys_id of the inserted record
        } catch (e) {
            // Log the error and rethrow to be handled by the caller
            gs.error('Error creating finance record: ' + e.message);
            throw e;
        }
    },

    /**
     * Retrieves finance records based on specified criteria.
     * @param {string} query - The query string to filter records.
     * @returns {Array} - An array of finance records.
     * @throws Will throw an error if the retrieval fails.
     */
    getFinanceRecords: function(query) {
        var records = [];
        var gr = new GlideRecord(this.financeTable);

        // Add query condition if provided
        if (query) {
            gr.addEncodedQuery(query);
        }

        // Try to query the records
        try {
            gr.query();
            while (gr.next()) {
                records.push({
                    sys_id: gr.getValue('sys_id'),
                    amount: gr.getValue('amount'),
                    type: gr.getValue('type'),
                    date: gr.getValue('date'),
                    description: gr.getValue('description')
                });
            }
            return records; // Return the array of finance records
        } catch (e) {
            // Log the error and rethrow to be handled by the caller
            gs.error('Error retrieving finance records: ' + e.message);
            throw e;
        }
    },

    /**
     * Updates an existing finance record.
     * @param {string} sysId - The sys_id of the record to update.
     * @param {Object} updateData - The data to update the record with.
     * @throws Will throw an error if the update fails.
     */
    updateFinanceRecord: function(sysId, updateData) {
        var gr = new GlideRecord(this.financeTable);
        
        // Validate the provided sys_id
        if (!sysId) {
            throw new Error('Invalid sys_id provided for update.');
        }

        // Try to retrieve the record for updating
        if (gr.get(sysId)) {
            // Update the fields of the finance record
            if (updateData.amount) gr.setValue('amount', updateData.amount);
            if (updateData.type) gr.setValue('type', updateData.type);
            if (updateData.date) gr.setValue('date', updateData.date);
            if (updateData.description) gr.setValue('description', updateData.description);

            // Try to update the record in the database
            try {
                gr.update();
            } catch (e) {
                // Log the error and rethrow to be handled by the caller
                gs.error('Error updating finance record: ' + e.message);
                throw e;
            }
        } else {
            throw new Error('Record with sys_id ' + sysId + ' not found.');
        }
    },

    type: 'FinanceAutomation'
};

// Example usage:
// var financeService = new FinanceAutomation();
// var newRecordId = financeService.createFinanceRecord({ amount: 1000, type: 'Expense', date: '2023-10-01', description: 'Office Supplies' });
// var records = financeService.getFinanceRecords('type=Expense');
// financeService.updateFinanceRecord(newRecordId, { description: 'Updated Office Supplies' });
```
