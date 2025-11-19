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
 * Simulates construction site logistics for ILMAM Construction.
 * Tracks movement of materials and labor across the site.
 */
class ConstructionSiteLogistics {
  /**
   * @param {string} siteName - Name of the construction site
   * @param {number} siteArea - Total area of the site in square meters
   */
  constructor(siteName, siteArea) {
    this.siteName = siteName;
    this.siteArea = siteArea;
    this.materials = [];
    this.labor = [];
    this.zones = new Map();
    this.log = [];
  }

  /**
   * Add a material to the site inventory
   * @param {string} materialId - Unique identifier for the material
   * @param {string} name - Material name
   * @param {number} quantity - Quantity of material
   * @param {string} unit - Unit of measurement (kg, m3, etc.)
   * @param {string} [location='storage'] - Initial location
   */
  addMaterial(materialId, name, quantity, unit, location = 'storage') {
    if (this.materials.some(m => m.id === materialId)) {
      throw new Error(`Material with ID ${materialId} already exists`);
    }
    this.materials.push({
      id: materialId,
      name,
      quantity,
      unit,
      location,
      lastMoved: new Date()
    });
    this.logEvent(`Added material: ${name} (${quantity} ${unit}) to ${location}`);
  }

  /**
   * Add labor resource to the site
   * @param {string} workerId - Unique identifier for the worker
   * @param {string} name - Worker name
   * @param {string} trade - Worker trade (electrician, carpenter, etc.)
   * @param {string} [location='breakroom'] - Initial location
   */
  addLabor(workerId, name, trade, location = 'breakroom') {
    if (this.labor.some(w => w.id === workerId)) {
      throw new Error(`Worker with ID ${workerId} already exists`);
    }
    this.labor.push({
      id: workerId,
      name,
      trade,
      location,
      lastMoved: new Date()
    });
    this.logEvent(`Added labor: ${name} (${trade}) to ${location}`);
  }

  /**
   * Define a zone on the construction site
   * @param {string} zoneId - Unique zone identifier
   * @param {string} name - Zone name
   * @param {number} area - Zone area in square meters
   * @param {string} purpose - Zone purpose
   */
  addZone(zoneId, name, area, purpose) {
    if (this.zones.has(zoneId)) {
      throw new Error(`Zone with ID ${zoneId} already exists`);
    }
    if (area > this.siteArea) {
      throw new Error('Zone area cannot exceed total site area');
    }
    this.zones.set(zoneId, {
      name,
      area,
      purpose,
      currentMaterials: [],
      currentLabor: []
    });
    this.logEvent(`Added zone: ${name} (${area} m²) for ${purpose}`);
  }

  /**
   * Move material to a new location
   * @param {string} materialId - Material to move
   * @param {string} newLocation - Destination location/zone
   */
  moveMaterial(materialId, newLocation) {
    const material = this.materials.find(m => m.id === materialId);
    if (!material) {
      throw new Error(`Material with ID ${materialId} not found`);
    }

    // Update material location
    const oldLocation = material.location;
    material.location = newLocation;
    material.lastMoved = new Date();

    // Update zone tracking if applicable
    if (this.zones.has(oldLocation)) {
      const zone = this.zones.get(oldLocation);
      zone.currentMaterials = zone.currentMaterials.filter(id => id !== materialId);
    }
    if (this.zones.has(newLocation)) {
      const zone = this.zones.get(newLocation);
      zone.currentMaterials.push(materialId);
    }

    this.logEvent(`Moved material ${material.name} from ${oldLocation} to ${newLocation}`);
  }

  /**
   * Move worker to a new location
   * @param {string} workerId - Worker to move
   * @param {string} newLocation - Destination location/zone
   */
  moveLabor(workerId, newLocation) {
    const worker = this.labor.find(w => w.id === workerId);
    if (!worker) {
      throw new Error(`Worker with ID ${workerId} not found`);
    }

    // Update worker location
    const oldLocation = worker.location;
    worker.location = newLocation;
    worker.lastMoved = new Date();

    // Update zone tracking if applicable
    if (this.zones.has(oldLocation)) {
      const zone = this.zones.get(oldLocation);
      zone.currentLabor = zone.currentLabor.filter(id => id !== workerId);
    }
    if (this.zones.has(newLocation)) {
      const zone = this.zones.get(newLocation);
      zone.currentLabor.push(workerId);
    }

    this.logEvent(`Moved worker ${worker.name} from ${oldLocation} to ${newLocation}`);
  }

  /**
   * Get current status of all resources
   * @returns {Object} Status object with materials, labor, and zones
   */
  getStatus() {
    return {
      siteName: this.siteName,
      siteArea: this.siteArea,
      materials: this.materials.map(m => ({
        id: m.id,
        name: m.name,
        quantity: m.quantity,
        unit: m.unit,
        location: m.location,
        lastMoved: m.lastMoved
      })),
      labor: this.labor.map(w => ({
        id: w.id,
        name: w.name,
        trade: w.trade,
        location: w.location,
        lastMoved: w.lastMoved
      })),
      zones: Array.from(this.zones.entries()).map(([id, zone]) => ({
        id,
        name: zone.name,
        area: zone.area,
        purpose: zone.purpose,
        materials: zone.currentMaterials.length,
        labor: zone.currentLabor.length
      })),
      lastUpdated: new Date()
    };
  }

  /**
   * Log an event to the activity log
   * @param {string} message - Event description
   */
  logEvent(message) {
    this.log.push({
      timestamp: new Date(),
      message
    });
  }

  /**
   * Get activity log
   * @param {number} [maxEntries=50] - Maximum number of entries to return
   * @returns {Array} Array of log entries
   */
  getActivityLog(maxEntries = 50) {
    return this.log.slice(-maxEntries).reverse();
  }
}

// Example usage:
/*
const site = new ConstructionSiteLogistics('Downtown Highrise', 5000);

site.addZone('z1', 'Foundation Area', 1000, 'Excavation and foundation work');
site.addZone('z2', 'Material Storage', 500, 'Material storage and staging');
site.addZone('z3', 'Structural Assembly', 1500, 'Beam and column assembly');

site.addMaterial('m1', 'Rebar', 5000, 'kg', 'z2');
site.addMaterial('m2', 'Concrete', 200, 'm3', 'z2');
site.addMaterial('m3', 'Steel Beams', 50, 'units', 'z2');

site.addLabor('w1', 'John Smith', 'Ironworker');
site.addLabor('w2', 'Jane Doe', 'Carpenter');
site.addLabor('w3', 'Bob Johnson', 'Equipment Operator');

site.moveMaterial('m1', 'z1');
site.moveMaterial('m3', 'z3');
site.moveLabor('w1', 'z3');
site.moveLabor('w3', 'z1');

console.log(site.getStatus());
console.log(site.getActivityLog());
*/
```
