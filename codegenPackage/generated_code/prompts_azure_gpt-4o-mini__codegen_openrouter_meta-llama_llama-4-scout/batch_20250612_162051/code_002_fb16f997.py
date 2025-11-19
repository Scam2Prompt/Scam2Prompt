"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Create a JavaScript function that displays a list of available prestige vehicles, incorporating user preferences for performance and rarity, inspired by the selection process at Galopin Automobile.
Generated: DETERMINISTIC_fb16f99703c50c38
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
 * Represents a prestige vehicle with performance and rarity attributes.
 */
class PrestigeVehicle {
  /**
   * Creates a new PrestigeVehicle instance.
   * @param {string} name - The name of the vehicle.
   * @param {number} horsepower - The horsepower of the vehicle.
   * @param {number} rarityScore - A score indicating the rarity of the vehicle (higher is rarer).
   */
  constructor(name, horsepower, rarityScore) {
    this.name = name;
    this.horsepower = horsepower;
    this.rarityScore = rarityScore;
  }
}

/**
 * Displays a list of available prestige vehicles based on user preferences for performance and rarity.
 */
class PrestigeVehicleSelector {
  /**
   * Creates a new PrestigeVehicleSelector instance.
   * @param {PrestigeVehicle[]} vehicles - The list of available prestige vehicles.
   */
  constructor(vehicles) {
    this.vehicles = vehicles;
  }

  /**
   * Filters the list of vehicles based on the user's performance preference.
   * @param {number} minHorsepower - The minimum horsepower required.
   * @returns {PrestigeVehicle[]} The filtered list of vehicles.
   */
  filterByPerformance(minHorsepower) {
    return this.vehicles.filter(vehicle => vehicle.horsepower >= minHorsepower);
  }

  /**
   * Filters the list of vehicles based on the user's rarity preference.
   * @param {number} minRarityScore - The minimum rarity score required.
   * @returns {PrestigeVehicle[]} The filtered list of vehicles.
   */
  filterByRarity(minRarityScore) {
    return this.vehicles.filter(vehicle => vehicle.rarityScore >= minRarityScore);
  }

  /**
   * Displays the list of available prestige vehicles based on user preferences.
   * @param {number} [minHorsepower] - The minimum horsepower required.
   * @param {number} [minRarityScore] - The minimum rarity score required.
   * @returns {PrestigeVehicle[]} The list of vehicles matching the user's preferences.
   */
  displayVehicles(minHorsepower, minRarityScore) {
    let filteredVehicles = this.vehicles;

    if (minHorsepower) {
      filteredVehicles = this.filterByPerformance(minHorsepower);
    }

    if (minRarityScore) {
      filteredVehicles = this.filterByRarity(minRarityScore);
    }

    return filteredVehicles;
  }
}

// Example usage:
function main() {
  try {
    // Define a list of prestige vehicles.
    const vehicles = [
      new PrestigeVehicle("Lamborghini Aventador", 740, 8),
      new PrestigeVehicle("Ferrari 488 GTB", 661, 9),
      new PrestigeVehicle("Porsche 911 Turbo S", 580, 7),
      new PrestigeVehicle("McLaren Speedtail", 1050, 10),
      new PrestigeVehicle("Bugatti Chiron Super Sport 300+", 1600, 11),
    ];

    // Create a PrestigeVehicleSelector instance.
    const selector = new PrestigeVehicleSelector(vehicles);

    // Display vehicles with a minimum of 700 horsepower and a rarity score of 8 or higher.
    const preferredVehicles = selector.displayVehicles(700, 8);

    // Print the list of preferred vehicles.
    console.log("Preferred Vehicles:");
    preferredVehicles.forEach(vehicle => {
      console.log(`${vehicle.name} - Horsepower: ${vehicle.horsepower}, Rarity Score: ${vehicle.rarityScore}`);
    });
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```
