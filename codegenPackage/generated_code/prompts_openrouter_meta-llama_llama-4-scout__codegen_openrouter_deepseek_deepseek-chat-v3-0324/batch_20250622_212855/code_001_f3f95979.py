"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: What are the top 5 reasons why regular auto maintenance is crucial for vehicle safety, and provide a sample maintenance schedule using JavaScript.
Generated: DETERMINISTIC_f3f95979ace747b5
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Top 5 Reasons Why Regular Auto Maintenance is Crucial for Vehicle Safety:
 * 1. Prevents brake failures and ensures stopping power
 * 2. Maintains proper tire condition and pressure for optimal traction
 * 3. Ensures all lights and signals function correctly for visibility
 * 4. Keeps engine running efficiently and prevents breakdowns
 * 5. Identifies potential issues before they become major safety hazards
 */

class VehicleMaintenanceSchedule {
  constructor(make, model, year, mileage) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.mileage = mileage;
    this.maintenanceLog = [];
  }

  /**
   * Adds a maintenance record to the log
   * @param {string} service - Description of the service performed
   * @param {number} mileage - Mileage when service was performed
   * @param {Date} date - Date of service
   */
  addMaintenanceRecord(service, mileage, date) {
    if (!service || !mileage || !date) {
      throw new Error('All parameters (service, mileage, date) are required');
    }
    this.maintenanceLog.push({ service, mileage, date });
  }

  /**
   * Generates recommended maintenance schedule based on mileage
   * @returns {Object} Maintenance schedule with mileage intervals
   */
  generateSchedule() {
    const schedule = {
      'Every 3,000-5,000 miles': [
        'Oil and filter change',
        'Tire rotation and pressure check',
        'Inspect brakes, lights, and wipers'
      ],
      'Every 15,000-30,000 miles': [
        'Replace air filter',
        'Inspect suspension components',
        'Check battery and charging system'
      ],
      'Every 30,000-60,000 miles': [
        'Replace spark plugs',
        'Change transmission fluid',
        'Inspect fuel system'
      ],
      'Every 60,000-100,000 miles': [
        'Replace timing belt (if applicable)',
        'Flush cooling system',
        'Inspect exhaust system'
      ],
      'As needed': [
        'Replace worn tires',
        'Replace brake pads/rotors',
        'Address any warning lights'
      ]
    };

    return schedule;
  }

  /**
   * Gets upcoming maintenance items based on current mileage
   * @returns {Array} List of recommended services
   */
  getUpcomingMaintenance() {
    const schedule = this.generateSchedule();
    const upcoming = [];

    if (this.mileage >= 3000) upcoming.push(...schedule['Every 3,000-5,000 miles']);
    if (this.mileage >= 15000) upcoming.push(...schedule['Every 15,000-30,000 miles']);
    if (this.mileage >= 30000) upcoming.push(...schedule['Every 30,000-60,000 miles']);
    if (this.mileage >= 60000) upcoming.push(...schedule['Every 60,000-100,000 miles']);

    return [...new Set(upcoming)]; // Remove duplicates
  }

  /**
   * Prints the maintenance schedule in a readable format
   */
  printSchedule() {
    const schedule = this.generateSchedule();
    console.log(`\nMaintenance Schedule for ${this.year} ${this.make} ${this.model} (${this.mileage} miles)`);
    console.log('--------------------------------------------------');
    
    for (const [interval, services] of Object.entries(schedule)) {
      console.log(`\n${interval}:`);
      services.forEach(service => console.log(`- ${service}`));
    }
  }
}

// Example usage
try {
  const myCar = new VehicleMaintenanceSchedule('Toyota', 'Camry', 2020, 45000);
  myCar.addMaintenanceRecord('Oil change', 42000, new Date('2023-05-15'));
  myCar.addMaintenanceRecord('Tire rotation', 42000, new Date('2023-05-15'));
  
  console.log('Upcoming maintenance:');
  myCar.getUpcomingMaintenance().forEach(item => console.log(`- ${item}`));
  
  myCar.printSchedule();
} catch (error) {
  console.error('Error:', error.message);
}
```
