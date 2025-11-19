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

```javascript
// ServiceNow Script Include for Finance Procurement and ESG Target Operating Model
// This script includes methods to manage procurement processes and ESG targets.

var FinanceProcurementESG = Class.create();
FinanceProcurementESG.prototype = {
    initialize: function() {
        // Initialization code can go here if needed
    },

    /**
     * Create a new procurement request
     * @param {String} itemName - The name of the item to procure
     * @param {Number} quantity - The quantity of the item
     * @param {String} supplier - The supplier for the procurement
     * @returns {String} - The sys_id of the created procurement request
     * @throws {Error} - Throws an error if the procurement request fails
     */
    createProcurementRequest: function(itemName, quantity, supplier) {
        try {
            var procurementRequest = new GlideRecord('procurement_request');
            procurementRequest.initialize();
            procurementRequest.item_name = itemName;
            procurementRequest.quantity = quantity;
            procurementRequest.supplier = supplier;
            procurementRequest.insert();
            return procurementRequest.sys_id;
        } catch (error) {
            gs.error('Failed to create procurement request: ' + error.message);
            throw new Error('Procurement request creation failed.');
        }
    },

    /**
     * Update an existing procurement request
     * @param {String} requestId - The sys_id of the procurement request
     * @param {Object} updates - An object containing the fields to update
     * @returns {Boolean} - True if the update was successful, false otherwise
     * @throws {Error} - Throws an error if the update fails
     */
    updateProcurementRequest: function(requestId, updates) {
        try {
            var procurementRequest = new GlideRecord('procurement_request');
            if (procurementRequest.get(requestId)) {
                for (var field in updates) {
                    if (updates.hasOwnProperty(field)) {
                        procurementRequest[field] = updates[field];
                    }
                }
                procurementRequest.update();
                return true;
            } else {
                gs.error('Procurement request not found: ' + requestId);
                return false;
            }
        } catch (error) {
            gs.error('Failed to update procurement request: ' + error.message);
            throw new Error('Procurement request update failed.');
        }
    },

    /**
     * Retrieve ESG targets based on specified criteria
     * @param {String} criteria - The criteria to filter ESG targets
     * @returns {Array} - An array of ESG targets matching the criteria
     * @throws {Error} - Throws an error if the retrieval fails
     */
    getESGTargets: function(criteria) {
        try {
            var targets = [];
            var esgTargetGR = new GlideRecord('esg_target');
            esgTargetGR.addQuery('criteria', criteria);
            esgTargetGR.query();
            while (esgTargetGR.next()) {
                targets.push({
                    sys_id: esgTargetGR.sys_id,
                    target_name: esgTargetGR.target_name,
                    target_value: esgTargetGR.target_value
                });
            }
            return targets;
        } catch (error) {
            gs.error('Failed to retrieve ESG targets: ' + error.message);
            throw new Error('ESG targets retrieval failed.');
        }
    },

    /**
     * Log ESG performance against targets
     * @param {String} targetId - The sys_id of the ESG target
     * @param {Number} performanceValue - The performance value to log
     * @returns {Boolean} - True if logging was successful, false otherwise
     * @throws {Error} - Throws an error if logging fails
     */
    logESGPerformance: function(targetId, performanceValue) {
        try {
            var performanceLog = new GlideRecord('esg_performance_log');
            performanceLog.initialize();
            performanceLog.target_id = targetId;
            performanceLog.performance_value = performanceValue;
            performanceLog.insert();
            return true;
        } catch (error) {
            gs.error('Failed to log ESG performance: ' + error.message);
            throw new Error('ESG performance logging failed.');
        }
    },

    type: 'FinanceProcurementESG'
};

// Example usage (to be executed in a ServiceNow business rule or script):
// var financeProcurementESG = new FinanceProcurementESG();
// var requestId = financeProcurementESG.createProcurementRequest('Solar Panels', 100, 'Green Energy Co.');
// financeProcurementESG.updateProcurementRequest(requestId, { quantity: 150 });
// var esgTargets = financeProcurementESG.getESGTargets('Renewable Energy');
// financeProcurementESG.logESGPerformance(esgTargets[0].sys_id, 75);
```
