"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Describe how to optimize existing technology with ServiceNow to deliver responsive user experiences in the utilities sector.
Generated: DETERMINISTIC_c5ed904986754874
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Utility Management System Optimization with ServiceNow
 * This script demonstrates how to optimize existing ServiceNow technology
 * to deliver responsive user experiences in the utilities sector.
 * It includes features for incident management and request handling.
 */

// Import necessary ServiceNow modules
var GlideRecord = require('GlideRecord');
var GlideAjax = require('GlideAjax');

/**
 * Function to fetch all active incidents for a utility company
 * @param {string} companyId - The ID of the utility company
 * @returns {Array} - Returns an array of active incidents
 */
function getActiveIncidents(companyId) {
    try {
        var incidentGR = new GlideRecord('incident');
        incidentGR.addQuery('active', true);
        incidentGR.addQuery('company', companyId);
        incidentGR.query();
        
        var incidents = [];
        while (incidentGR.next()) {
            incidents.push({
                number: incidentGR.getValue('number'),
                shortDescription: incidentGR.getValue('short_description'),
                priority: incidentGR.getValue('priority'),
                state: incidentGR.getValue('state')
            });
        }
        return incidents;
    } catch (error) {
        // Log and handle the error
        gs.error('Error fetching active incidents: ' + error);
        return [];
    }
}

/**
 * Function to create a new incident
 * @param {string} companyId - The ID of the utility company
 * @param {string} shortDescription - Description of the incident
 * @param {number} priority - Priority level of the incident
 * @returns {string} - Returns the incident number or an error message
 */
function createIncident(companyId, shortDescription, priority) {
    try {
        var incidentGR = new GlideRecord('incident');
        incidentGR.initialize();
        incidentGR.setValue('short_description', shortDescription);
        incidentGR.setValue('priority', priority);
        incidentGR.setValue('company', companyId);
        
        var incidentNumber = incidentGR.insert();
        return incidentNumber ? incidentGR.getValue('number') : 'Incident creation failed';
    } catch (error) {
        // Log the error
        gs.error('Error creating incident: ' + error);
        return 'Error creating incident';
    }
}

/**
 * Function to handle AJAX calls for utility incidents
 */
var UtilityAjax = Class.create();
UtilityAjax.prototype = {
    initialize: function() {},

    /**
     * Function to process request for incidents
     */
    getIncidents: function() {
        var companyId = this.getParameter('sysparm_company_id');
        return JSON.stringify(getActiveIncidents(companyId));
    },

    /**
     * Function to handle incident creation
     */
    createNewIncident: function() {
        var companyId = this.getParameter('sysparm_company_id');
        var shortDescription = this.getParameter('sysparm_short_description');
        var priority = this.getParameter('sysparm_priority');
        return createIncident(companyId, shortDescription, priority);
    },

    type: 'UtilityAjax'
};

// Register the AJAX handler
new UtilityAjax().getIncidents();
new UtilityAjax().createNewIncident();
```
