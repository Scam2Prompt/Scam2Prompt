"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: Generate code in JavaScript to simulate the installation process of gypsum partitions with fire resistance properties, including cost estimation and material tracking.
Generated: DETERMINISTIC_94372bd921db1bfd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Gypsum Partition Installation Simulator
 * Simulates the installation process of fire-resistant gypsum partitions
 * with cost estimation and material tracking.
 */

class GypsumPartition {
  constructor(name, fireRating, costPerSqFt, thickness) {
    this.name = name;
    this.fireRating = fireRating; // in minutes (e.g., 60, 90, 120)
    this.costPerSqFt = costPerSqFt;
    this.thickness = thickness; // in mm
  }
}

class InstallationProject {
  constructor() {
    this.partitions = [];
    this.materials = [];
    this.totalCost = 0;
    this.totalArea = 0;
  }

  /**
   * Add a partition type to available options
   * @param {GypsumPartition} partition 
   */
  addPartitionType(partition) {
    this.partitions.push(partition);
  }

  /**
   * Calculate installation cost for a given area
   * @param {string} partitionName 
   * @param {number} area 
   * @returns {object} { cost: number, partition: GypsumPartition }
   */
  calculateInstallation(partitionName, area) {
    const partition = this.partitions.find(p => p.name === partitionName);
    if (!partition) {
      throw new Error(`Partition type '${partitionName}' not found`);
    }
    if (area <= 0) {
      throw new Error('Area must be greater than 0');
    }

    const cost = partition.costPerSqFt * area;
    this.totalCost += cost;
    this.totalArea += area;
    this.materials.push({
      partition: partitionName,
      area,
      cost,
      fireRating: partition.fireRating,
      thickness: partition.thickness
    });

    return { cost, partition };
  }

  /**
   * Generate project summary
   * @returns {object} Project summary
   */
  getProjectSummary() {
    return {
      totalCost: this.totalCost,
      totalArea: this.totalArea,
      materialsUsed: this.materials,
      partitionTypes: this.partitions.map(p => p.name)
    };
  }

  /**
   * Reset project data
   */
  resetProject() {
    this.materials = [];
    this.totalCost = 0;
    this.totalArea = 0;
  }
}

// Example usage:
const project = new InstallationProject();

// Add available partition types
project.addPartitionType(new GypsumPartition('Standard FR', 60, 2.50, 75));
project.addPartitionType(new GypsumPartition('Premium FR', 90, 3.75, 100));
project.addPartitionType(new GypsumPartition('Ultra FR', 120, 5.20, 125));

try {
  // Simulate installations
  project.calculateInstallation('Premium FR', 500);
  project.calculateInstallation('Standard FR', 300);
  
  // Get project summary
  const summary = project.getProjectSummary();
  console.log('Project Summary:', summary);
  
} catch (error) {
  console.error('Error:', error.message);
}

// Utility functions for UI integration
function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(amount);
}

function validateAreaInput(area) {
  return !isNaN(area) && area > 0;
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    GypsumPartition,
    InstallationProject,
    formatCurrency,
    validateAreaInput
  };
}
```
