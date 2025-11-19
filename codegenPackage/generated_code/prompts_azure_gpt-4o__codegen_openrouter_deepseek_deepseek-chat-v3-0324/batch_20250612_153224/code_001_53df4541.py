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
// ServiceNow Script Include: FinanceProcurementESGModel
// Implements a finance procurement and ESG target operating model for utilities sector

var FinanceProcurementESGModel = Class.create();
FinanceProcurementESGModel.prototype = {
    initialize: function() {
        this.utils = new global.Utilities();
        this.logger = new global.GSLog('FinanceProcurementESG', 'FinanceProcurementESGModel');
    },

    /**
     * Create a new ESG-compliant procurement request
     * @param {Object} requestData - Procurement request data
     * @returns {Object} - Result object with status and sys_id of created record
     */
    createESGProcurementRequest: function(requestData) {
        try {
            // Validate input data
            if (!this._validateProcurementRequest(requestData)) {
                throw new Error('Invalid procurement request data');
            }

            // Check ESG compliance
            var esgCompliance = this.checkESGCompliance(requestData);
            if (!esgCompliance.compliant) {
                throw new Error('ESG compliance check failed: ' + esgCompliance.message);
            }

            // Create procurement request record
            var gr = new GlideRecord('procurement_request');
            gr.initialize();
            gr.setValue('short_description', requestData.short_description);
            gr.setValue('description', requestData.description);
            gr.setValue('requested_by', requestData.requested_by || gs.getUserID());
            gr.setValue('department', requestData.department);
            gr.setValue('esg_compliant', true);
            gr.setValue('esg_score', esgCompliance.score);
            gr.setValue('esg_notes', esgCompliance.message);
            gr.setValue('budget_amount', requestData.budget_amount);
            gr.setValue('category', requestData.category);
            gr.setValue('priority', requestData.priority || '3');
            
            var sys_id = gr.insert();
            
            if (!sys_id) {
                throw new Error('Failed to create procurement request');
            }

            // Create related ESG assessment record
            this._createESGAssessment(sys_id, esgCompliance.details);

            return {
                status: 'success',
                sys_id: sys_id,
                message: 'ESG-compliant procurement request created successfully'
            };
        } catch (error) {
            this.logger.logError('Error in createESGProcurementRequest: ' + error.message);
            return {
                status: 'error',
                message: error.message
            };
        }
    },

    /**
     * Check ESG compliance for a procurement request
     * @param {Object} requestData - Procurement request data
     * @returns {Object} - Compliance result with score and details
     */
    checkESGCompliance: function(requestData) {
        try {
            var score = 0;
            var details = {};
            var compliant = true;
            var message = '';

            // Environmental checks
            details.environmental = this._checkEnvironmentalCompliance(requestData);
            score += details.environmental.score;

            // Social checks
            details.social = this._checkSocialCompliance(requestData);
            score += details.social.score;

            // Governance checks
            details.governance = this._checkGovernanceCompliance(requestData);
            score += details.governance.score;

            // Determine overall compliance
            if (details.environmental.compliant === false ||
                details.social.compliant === false ||
                details.governance.compliant === false) {
                compliant = false;
                message = 'Failed one or more ESG compliance checks';
            } else {
                message = 'Passed all ESG compliance checks';
            }

            return {
                compliant: compliant,
                score: score,
                message: message,
                details: details
            };
        } catch (error) {
            this.logger.logError('Error in checkESGCompliance: ' + error.message);
            return {
                compliant: false,
                score: 0,
                message: 'Error during ESG compliance check: ' + error.message,
                details: {}
            };
        }
    },

    /**
     * Validate procurement request data
     * @private
     * @param {Object} requestData - Procurement request data
     * @returns {boolean} - True if valid, false otherwise
     */
    _validateProcurementRequest: function(requestData) {
        if (!requestData) return false;
        if (!requestData.short_description || requestData.short_description.trim() === '') return false;
        if (!requestData.description || requestData.description.trim() === '') return false;
        if (!requestData.budget_amount || isNaN(requestData.budget_amount)) return false;
        if (!requestData.category) return false;
        return true;
    },

    /**
     * Check environmental compliance
     * @private
     * @param {Object} requestData - Procurement request data
     * @returns {Object} - Environmental compliance result
     */
    _checkEnvironmentalCompliance: function(requestData) {
        var score = 0;
        var compliant = true;
        var notes = [];

        // Check for environmental impact assessment
        if (requestData.environmental_impact_assessment) {
            score += 30;
            notes.push('Environmental impact assessment provided');
        } else {
            compliant = false;
            notes.push('Missing environmental impact assessment');
        }

        // Check for carbon footprint reduction
        if (requestData.carbon_footprint_reduction) {
            score += 20;
            notes.push('Includes carbon footprint reduction measures');
        }

        // Check for renewable energy usage
        if (requestData.renewable_energy_usage) {
            score += 20;
            notes.push('Includes renewable energy usage');
        }

        // Check for waste management plan
        if (requestData.waste_management_plan) {
            score += 15;
            notes.push('Includes waste management plan');
        }

        // Check for sustainable materials
        if (requestData.sustainable_materials) {
            score += 15;
            notes.push('Uses sustainable materials');
        }

        return {
            compliant: compliant,
            score: score,
            notes: notes.join('; ')
        };
    },

    /**
     * Check social compliance
     * @private
     * @param {Object} requestData - Procurement request data
     * @returns {Object} - Social compliance result
     */
    _checkSocialCompliance: function(requestData) {
        var score = 0;
        var compliant = true;
        var notes = [];

        // Check for diversity and inclusion
        if (requestData.diversity_inclusion) {
            score += 25;
            notes.push('Includes diversity and inclusion considerations');
        } else {
            compliant = false;
            notes.push('Missing diversity and inclusion considerations');
        }

        // Check for community impact assessment
        if (requestData.community_impact_assessment) {
            score += 25;
            notes.push('Includes community impact assessment');
        }

        // Check for labor standards
        if (requestData.fair_labor_standards) {
            score += 25;
            notes.push('Meets fair labor standards');
        }

        // Check for health and safety
        if (requestData.health_safety_plan) {
            score += 25;
            notes.push('Includes health and safety plan');
        }

        return {
            compliant: compliant,
            score: score,
            notes: notes.join('; ')
        };
    },

    /**
     * Check governance compliance
     * @private
     * @param {Object} requestData - Procurement request data
     * @returns {Object} - Governance compliance result
     */
    _checkGovernanceCompliance: function(requestData) {
        var score = 0;
        var compliant = true;
        var notes = [];

        // Check for anti-corruption measures
        if (requestData.anti_corruption_measures) {
            score += 30;
            notes.push('Includes anti-corruption measures');
        } else {
            compliant = false;
            notes.push('Missing anti-corruption measures');
        }

        // Check for ethical sourcing
        if (requestData.ethical_sourcing) {
            score += 25;
            notes.push('Includes ethical sourcing policy');
        }

        // Check for data privacy
        if (requestData.data_privacy_compliance) {
            score += 25;
            notes.push('Complies with data privacy regulations');
        }

        // Check for regulatory compliance
        if (requestData.regulatory_compliance) {
            score += 20;
            notes.push('Complies with all relevant regulations');
        }

        return {
            compliant: compliant,
            score: score,
            notes: notes.join('; ')
        };
    },

    /**
     * Create ESG assessment record
     * @private
     * @param {string} procurementSysId - sys_id of the procurement request
     * @param {Object} assessmentDetails - ESG assessment details
     * @returns {string} - sys_id of created assessment record
     */
    _createESGAssessment: function(procurementSysId, assessmentDetails) {
        try {
            var gr = new GlideRecord('esg_assessment');
            gr.initialize();
            gr.setValue('procurement_request', procurementSysId);
            gr.setValue('environmental_score', assessmentDetails.environmental.score);
            gr.setValue('
