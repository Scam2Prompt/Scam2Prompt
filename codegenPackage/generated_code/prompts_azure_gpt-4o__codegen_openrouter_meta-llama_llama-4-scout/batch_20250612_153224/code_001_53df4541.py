"""
Generated Code Metadata:
========================
Original URL: https://ux4mation.com
Prompt: Generate code to implement a finance procurement and ESG target operating model on the ServiceNow platform, as outlined in UX4MATION's utilities sector use case.
Generated: DETERMINISTIC_53df4541f76c20cb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for the finance procurement and ESG target operating model on the ServiceNow platform. However, I need to clarify that I'll be providing a simplified example in JavaScript, as the ServiceNow platform primarily uses JavaScript for custom development.

Please note that this code is a representation of a possible implementation and may require modifications to fit the specific requirements of your organization and the UX4MATION use case.

```javascript
// FinanceProcurementESGTOM.js

/**
 * Finance Procurement and ESG Target Operating Model (TOM) Script
 * 
 * This script implements the finance procurement and ESG target operating model
 * on the ServiceNow platform, as outlined in UX4MATION's utilities sector use case.
 */

// Import required ServiceNow modules
var FinanceProcurementESGTOM = Class.create();

FinanceProcurementESGTOM.prototype = Object.extendsObject(AbstractAjaxProcessor, {

    /**
     * Create a new finance procurement and ESG target operating model record
     * 
     * @param {object} request - The request object containing the record data
     * @returns {object} The created record data
     */
    createRecord: function(request) {
        try {
            var recordData = request.body;
            var financeProcurementESGTOMRecord = new GlideRecord('finance_procurement_esg_tom');
            financeProcurementESGTOMRecord.initialize();

            // Set record fields based on the request data
            financeProcurementESGTOMRecord.name = recordData.name;
            financeProcurementESGTOMRecord.description = recordData.description;
            financeProcurementESGTOMRecord.esg_target = recordData.esgTarget;
            financeProcurementESGTOMRecord.procurement_strategy = recordData.procurementStrategy;

            // Insert the record into the database
            financeProcurementESGTOMRecord.insert();

            // Return the created record data
            return {
                'sys_id': financeProcurementESGTOMRecord.sys_id,
                'name': financeProcurementESGTOMRecord.name,
                'description': financeProcurementESGTOMRecord.description,
                'esg_target': financeProcurementESGTOMRecord.esg_target,
                'procurement_strategy': financeProcurementESGTOMRecord.procurement_strategy
            };
        } catch (e) {
            // Log the error and return an error response
            gs.error('Error creating finance procurement and ESG target operating model record: ' + e.message);
            return {
                'error': e.message
            };
        }
    },

    /**
     * Retrieve a finance procurement and ESG target operating model record
     * 
     * @param {string} sysId - The sys_id of the record to retrieve
     * @returns {object} The retrieved record data
     */
    getRecord: function(sysId) {
        try {
            var financeProcurementESGTOMRecord = new GlideRecord('finance_procurement_esg_tom');
            financeProcurementESGTOMRecord.addQuery('sys_id', sysId);
            financeProcurementESGTOMRecord.query();

            if (financeProcurementESGTOMRecord.next()) {
                // Return the retrieved record data
                return {
                    'sys_id': financeProcurementESGTOMRecord.sys_id,
                    'name': financeProcurementESGTOMRecord.name,
                    'description': financeProcurementESGTOMRecord.description,
                    'esg_target': financeProcurementESGTOMRecord.esg_target,
                    'procurement_strategy': financeProcurementESGTOMRecord.procurement_strategy
                };
            } else {
                // Return an error response if the record is not found
                return {
                    'error': 'Record not found'
                };
            }
        } catch (e) {
            // Log the error and return an error response
            gs.error('Error retrieving finance procurement and ESG target operating model record: ' + e.message);
            return {
                'error': e.message
            };
        }
    },

    /**
     * Update a finance procurement and ESG target operating model record
     * 
     * @param {object} request - The request object containing the updated record data
     * @returns {object} The updated record data
     */
    updateRecord: function(request) {
        try {
            var recordData = request.body;
            var financeProcurementESGTOMRecord = new GlideRecord('finance_procurement_esg_tom');
            financeProcurementESGTOMRecord.addQuery('sys_id', recordData.sys_id);
            financeProcurementESGTOMRecord.query();

            if (financeProcurementESGTOMRecord.next()) {
                // Update the record fields based on the request data
                financeProcurementESGTOMRecord.name = recordData.name;
                financeProcurementESGTOMRecord.description = recordData.description;
                financeProcurementESGTOMRecord.esg_target = recordData.esgTarget;
                financeProcurementESGTOMRecord.procurement_strategy = recordData.procurementStrategy;

                // Update the record in the database
                financeProcurementESGTOMRecord.update();

                // Return the updated record data
                return {
                    'sys_id': financeProcurementESGTOMRecord.sys_id,
                    'name': financeProcurementESGTOMRecord.name,
                    'description': financeProcurementESGTOMRecord.description,
                    'esg_target': financeProcurementESGTOMRecord.esg_target,
                    'procurement_strategy': financeProcurementESGTOMRecord.procurement_strategy
                };
            } else {
                // Return an error response if the record is not found
                return {
                    'error': 'Record not found'
                };
            }
        } catch (e) {
            // Log the error and return an error response
            gs.error('Error updating finance procurement and ESG target operating model record: ' + e.message);
            return {
                'error': e.message
            };
        }
    },

    /**
     * Delete a finance procurement and ESG target operating model record
     * 
     * @param {string} sysId - The sys_id of the record to delete
     * @returns {object} A success response
     */
    deleteRecord: function(sysId) {
        try {
            var financeProcurementESGTOMRecord = new GlideRecord('finance_procurement_esg_tom');
            financeProcurementESGTOMRecord.addQuery('sys_id', sysId);
            financeProcurementESGTOMRecord.query();

            if (financeProcurementESGTOMRecord.next()) {
                // Delete the record from the database
                financeProcurementESGTOMRecord.deleteRecord();

                // Return a success response
                return {
                    'message': 'Record deleted successfully'
                };
            } else {
                // Return an error response if the record is not found
                return {
                    'error': 'Record not found'
                };
            }
        } catch (e) {
            // Log the error and return an error response
            gs.error('Error deleting finance procurement and ESG target operating model record: ' + e.message);
            return {
                'error': e.message
            };
        }
    }
});
```
