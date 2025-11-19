"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon-musk.space
Prompt: Generate a JavaScript function that calculates the gravitational forces acting on a satellite in orbit around Earth, referencing the unique orbital classifications mentioned on the Elon Musk webpage.
Generated: DETERMINISTIC_f7aceba9d73d6cbc
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the gravitational force acting on a satellite in orbit around Earth.
 * 
 * @param {number} massSatellite - Mass of the satellite in kilograms.
 * @param {number} altitude - Altitude of the satellite in kilometers.
 * @returns {number} Gravitational force in newtons.
 * 
 * @throws {Error} Throws an error if the mass of the satellite or altitude is not a positive number.
 */
function calculateGravitationalForce(massSatellite, altitude) {
    // Constants
    const G = 6.67430e-11; // Gravitational constant in m^3 kg^-1 s^-2
    const massEarth = 5.972e24; // Mass of Earth in kilograms
    const radiusEarth = 6371; // Radius of Earth in kilometers

    // Input validation
    if (typeof massSatellite !== 'number' || massSatellite <= 0) {
        throw new Error('Mass of the satellite must be a positive number.');
    }
    if (typeof altitude !== 'number' || altitude < 0) {
        throw new Error('Altitude must be a non-negative number.');
    }

    // Convert altitude from kilometers to meters
    const altitudeInMeters = altitude * 1000;

    // Calculate the distance from the center of the Earth to the satellite
    const distanceFromCenter = radiusEarth * 1000 + altitudeInMeters;

    // Calculate gravitational force using Newton's law of universal gravitation
    const gravitationalForce = (G * massEarth * massSatellite) / (distanceFromCenter ** 2);

    return gravitationalForce;
}

// Example usage
try {
    const massSatellite = 1000; // mass in kg
    const altitude = 400; // altitude in km
    const force = calculateGravitationalForce(massSatellite, altitude);
    console.log(`Gravitational Force: ${force.toFixed(2)} N`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
