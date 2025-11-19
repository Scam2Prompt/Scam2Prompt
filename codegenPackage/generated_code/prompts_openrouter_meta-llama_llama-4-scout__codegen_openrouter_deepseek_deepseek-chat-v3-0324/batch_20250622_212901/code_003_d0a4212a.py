"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Write a JavaScript function to calculate the cost of producing a vinyl banner based on its size and material type, such as vinil auto adesivo para impressão or vinil auto adesivo para recorte.
Generated: DETERMINISTIC_d0a4212a8760295d
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of producing a vinyl banner based on size and material type.
 * 
 * @param {number} width - Width of the banner in meters.
 * @param {number} height - Height of the banner in meters.
 * @param {string} materialType - Type of material ('impressao' or 'recorte').
 * @param {number} [unitCostImpressao=10] - Optional. Cost per square meter for 'impressao' material. Default is 10.
 * @param {number} [unitCostRecorte=15] - Optional. Cost per square meter for 'recorte' material. Default is 15.
 * @returns {number} Total cost of the banner.
 * @throws {Error} If invalid parameters are provided.
 */
function calculateVinylBannerCost(width, height, materialType, unitCostImpressao = 10, unitCostRecorte = 15) {
    // Validate input parameters
    if (typeof width !== 'number' || typeof height !== 'number' || width <= 0 || height <= 0) {
        throw new Error('Width and height must be positive numbers.');
    }

    if (typeof materialType !== 'string' || !['impressao', 'recorte'].includes(materialType)) {
        throw new Error("Material type must be either 'impressao' or 'recorte'.");
    }

    if (typeof unitCostImpressao !== 'number' || typeof unitCostRecorte !== 'number' || 
        unitCostImpressao <= 0 || unitCostRecorte <= 0) {
        throw new Error('Unit costs must be positive numbers.');
    }

    // Calculate area in square meters
    const area = width * height;

    // Calculate total cost based on material type
    let totalCost;
    if (materialType === 'impressao') {
        totalCost = area * unitCostImpressao;
    } else {
        totalCost = area * unitCostRecorte;
    }

    // Round to 2 decimal places for currency
    return Math.round(totalCost * 100) / 100;
}
```
