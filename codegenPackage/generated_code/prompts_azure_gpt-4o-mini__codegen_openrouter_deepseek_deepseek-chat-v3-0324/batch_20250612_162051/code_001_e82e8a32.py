"""
Generated Code Metadata:
========================
Original URL: https://www.punpuntoy.com
Prompt: Generate a JavaScript function that simulates the safety standards for playground equipment as described by PunPun Toy.
Generated: DETERMINISTIC_e82e8a32e3122c09
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates safety standards for playground equipment as per PunPun Toy guidelines.
 * 
 * @param {Object} equipment - The playground equipment to evaluate.
 * @param {string} equipment.type - Type of equipment (e.g., 'slide', 'swing', 'climber').
 * @param {number} equipment.height - Height of the equipment in meters.
 * @param {number} equipment.weightLimit - Maximum weight capacity in kg.
 * @param {boolean} equipment.hasSoftEdges - Whether the equipment has soft edges.
 * @param {boolean} equipment.hasGuardrails - Whether the equipment has guardrails.
 * @returns {Object} - Safety evaluation result with pass/fail status and issues.
 */
function evaluatePlaygroundEquipmentSafety(equipment) {
    // Validate input
    if (!equipment || typeof equipment !== 'object') {
        throw new Error('Invalid equipment object provided');
    }

    const requiredFields = ['type', 'height', 'weightLimit', 'hasSoftEdges', 'hasGuardrails'];
    for (const field of requiredFields) {
        if (equipment[field] === undefined) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    const result = {
        passed: true,
        issues: []
    };

    // PunPun Toy safety standards
    const MAX_HEIGHT = 3; // meters
    const MIN_WEIGHT_LIMIT = 100; // kg

    // Check height
    if (equipment.height > MAX_HEIGHT) {
        result.passed = false;
        result.issues.push(`Height exceeds maximum allowed (${MAX_HEIGHT}m)`);
    }

    // Check weight limit
    if (equipment.weightLimit < MIN_WEIGHT_LIMIT) {
        result.passed = false;
        result.issues.push(`Weight limit below minimum requirement (${MIN_WEIGHT_LIMIT}kg)`);
    }

    // Check for soft edges on elevated equipment
    if (equipment.height > 1 && !equipment.hasSoftEdges) {
        result.passed = false;
        result.issues.push('Elevated equipment must have soft edges');
    }

    // Check for guardrails on certain equipment types
    const needsGuardrails = ['slide', 'platform', 'bridge'];
    if (needsGuardrails.includes(equipment.type) && !equipment.hasGuardrails) {
        result.passed = false;
        result.issues.push(`${equipment.type} must have guardrails`);
    }

    return result;
}
```
