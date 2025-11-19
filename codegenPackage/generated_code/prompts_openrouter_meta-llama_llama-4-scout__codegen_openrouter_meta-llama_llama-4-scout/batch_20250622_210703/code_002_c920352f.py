"""
Generated Code Metadata:
========================
Original URL: https://aasteeldetailing.co.uk.steel-edge.co.uk
Prompt: "Write a code snippet in JavaScript to create a site survey template for steel detailing projects, including fields for location, materials, and labor costs."
Generated: DETERMINISTIC_c920352f973bd83a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Site Survey Template for Steel Detailing Projects
 * 
 * This class represents a site survey template for steel detailing projects.
 * It includes fields for location, materials, and labor costs.
 */

// Define the SiteSurveyTemplate class
class SiteSurveyTemplate {
  /**
   * Constructor for SiteSurveyTemplate
   * 
   * @param {string} location - The location of the site survey
   */
  constructor(location) {
    this.location = location;
    this.materials = [];
    this.laborCosts = [];
  }

  /**
   * Add a material to the site survey template
   * 
   * @param {string} name - The name of the material
   * @param {number} quantity - The quantity of the material
   * @param {number} unitCost - The unit cost of the material
   */
  addMaterial(name, quantity, unitCost) {
    this.materials.push({
      name,
      quantity,
      unitCost
    });
  }

  /**
   * Add a labor cost to the site survey template
   * 
   * @param {string} description - A description of the labor cost
   * @param {number} cost - The cost of the labor
   */
  addLaborCost(description, cost) {
    this.laborCosts.push({
      description,
      cost
    });
  }

  /**
   * Calculate the total material cost
   * 
   * @returns {number} The total material cost
   */
  calculateTotalMaterialCost() {
    return this.materials.reduce((total, material) => {
      return total + (material.quantity * material.unitCost);
    }, 0);
  }

  /**
   * Calculate the total labor cost
   * 
   * @returns {number} The total labor cost
   */
  calculateTotalLaborCost() {
    return this.laborCosts.reduce((total, laborCost) => {
      return total + laborCost.cost;
    }, 0);
  }

  /**
   * Generate a report for the site survey template
   * 
   * @returns {string} A report for the site survey template
   */
  generateReport() {
    let report = `Site Survey Report for ${this.location}\n\n`;

    report += "Materials:\n";
    this.materials.forEach(material => {
      report += `- ${material.name}: ${material.quantity} units @ $${material.unitCost}/unit = $${material.quantity * material.unitCost}\n`;
    });
    report += `Total Material Cost: $${this.calculateTotalMaterialCost().toFixed(2)}\n\n`;

    report += "Labor Costs:\n";
    this.laborCosts.forEach(laborCost => {
      report += `- ${laborCost.description}: $${laborCost.cost}\n`;
    });
    report += `Total Labor Cost: $${this.calculateTotalLaborCost().toFixed(2)}\n\n`;

    report += `Total Cost: $${(this.calculateTotalMaterialCost() + this.calculateTotalLaborCost()).toFixed(2)}`;

    return report;
  }
}

// Example usage:
try {
  const siteSurvey = new SiteSurveyTemplate("New York");
  siteSurvey.addMaterial("Steel Beams", 100, 50);
  siteSurvey.addMaterial("Concrete", 500, 20);
  siteSurvey.addLaborCost("Engineering", 10000);
  siteSurvey.addLaborCost("Installation", 20000);

  console.log(siteSurvey.generateReport());
} catch (error) {
  console.error("Error:", error.message);
}
```
