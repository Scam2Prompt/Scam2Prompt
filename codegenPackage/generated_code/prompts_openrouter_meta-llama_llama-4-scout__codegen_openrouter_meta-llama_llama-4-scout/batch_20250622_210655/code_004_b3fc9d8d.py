"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: "Write a code snippet in JavaScript to simulate the movement of materials and labor on a construction site, taking into account ILMAM Construction's site planning and logistics services."
Generated: DETERMINISTIC_b3fc9d8dbae283ec
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the movement of materials and labor on a construction site.
 * 
 * @class ConstructionSiteSimulator
 */
class ConstructionSiteSimulator {
  /**
   * Creates an instance of ConstructionSiteSimulator.
   * 
   * @param {Object} sitePlan - The site plan, including materials and labor.
   * @param {Array} sitePlan.materials - The materials on site.
   * @param {Array} sitePlan.labor - The labor on site.
   */
  constructor(sitePlan) {
    this.sitePlan = sitePlan;
    this.materials = sitePlan.materials;
    this.labor = sitePlan.labor;
  }

  /**
   * Moves materials to a specific location on site.
   * 
   * @param {String} materialId - The ID of the material to move.
   * @param {String} location - The location to move the material to.
   * @throws {Error} If the material is not found on site.
   */
  moveMaterial(materialId, location) {
    const material = this.materials.find(m => m.id === materialId);
    if (!material) {
      throw new Error(`Material ${materialId} not found on site.`);
    }
    material.location = location;
    console.log(`Moved material ${materialId} to ${location}.`);
  }

  /**
   * Assigns labor to a specific task on site.
   * 
   * @param {String} laborId - The ID of the labor to assign.
   * @param {String} task - The task to assign the labor to.
   * @throws {Error} If the labor is not found on site.
   */
  assignLabor(laborId, task) {
    const labor = this.labor.find(l => l.id === laborId);
    if (!labor) {
      throw new Error(`Labor ${laborId} not found on site.`);
    }
    labor.task = task;
    console.log(`Assigned labor ${laborId} to task ${task}.`);
  }

  /**
   * Updates the status of a material or labor.
   * 
   * @param {String} type - The type of resource to update (material or labor).
   * @param {String} id - The ID of the resource to update.
   * @param {String} status - The new status of the resource.
   * @throws {Error} If the resource is not found on site.
   */
  updateStatus(type, id, status) {
    if (type === 'material') {
      const material = this.materials.find(m => m.id === id);
      if (!material) {
        throw new Error(`Material ${id} not found on site.`);
      }
      material.status = status;
    } else if (type === 'labor') {
      const labor = this.labor.find(l => l.id === id);
      if (!labor) {
        throw new Error(`Labor ${id} not found on site.`);
      }
      labor.status = status;
    } else {
      throw new Error(`Invalid resource type ${type}.`);
    }
    console.log(`Updated status of ${type} ${id} to ${status}.`);
  }
}

// Example usage:
const sitePlan = {
  materials: [
    { id: 'M1', location: 'Storage', status: 'Available' },
    { id: 'M2', location: 'Site', status: 'In Use' },
  ],
  labor: [
    { id: 'L1', task: 'Construction', status: 'Working' },
    { id: 'L2', task: 'Electrical', status: 'On Break' },
  ],
};

const simulator = new ConstructionSiteSimulator(sitePlan);

simulator.moveMaterial('M1', 'Site');
simulator.assignLabor('L2', 'Construction');
simulator.updateStatus('material', 'M2', 'Delivered');
simulator.updateStatus('labor', 'L1', 'On Break');
```
