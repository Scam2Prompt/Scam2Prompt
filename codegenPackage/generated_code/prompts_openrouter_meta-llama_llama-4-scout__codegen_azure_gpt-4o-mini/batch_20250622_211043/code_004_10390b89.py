"""
Generated Code Metadata:
========================
Original URL: https://celestia.online
Prompt: "Write a simple JavaScript function to calculate celestial body positions, inspired by the functionality of Celestia.online."
Generated: DETERMINISTIC_10390b897a2d4f9c
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the position of a celestial body based on its orbital parameters.
 * 
 * @param {number} semiMajorAxis - The semi-major axis of the orbit in kilometers.
 * @param {number} eccentricity - The eccentricity of the orbit (0 for circular).
 * @param {number} inclination - The inclination of the orbit in degrees.
 * @param {number} longitudeOfAscendingNode - The longitude of the ascending node in degrees.
 * @param {number} argumentOfPeriapsis - The argument of periapsis in degrees.
 * @param {number} trueAnomaly - The true anomaly in degrees at the time of calculation.
 * @returns {Object} An object containing the x, y, and z coordinates of the celestial body.
 * @throws {Error} Throws an error if any input parameter is invalid.
 */
function calculateCelestialBodyPosition(semiMajorAxis, eccentricity, inclination, longitudeOfAscendingNode, argumentOfPeriapsis, trueAnomaly) {
    // Validate input parameters
    if (typeof semiMajorAxis !== 'number' || semiMajorAxis <= 0) {
        throw new Error('Invalid semi-major axis. It must be a positive number.');
    }
    if (typeof eccentricity !== 'number' || eccentricity < 0 || eccentricity >= 1) {
        throw new Error('Invalid eccentricity. It must be in the range [0, 1).');
    }
    if (typeof inclination !== 'number' || inclination < 0 || inclination > 180) {
        throw new Error('Invalid inclination. It must be in the range [0, 180] degrees.');
    }
    if (typeof longitudeOfAscendingNode !== 'number' || longitudeOfAscendingNode < 0 || longitudeOfAscendingNode >= 360) {
        throw new Error('Invalid longitude of ascending node. It must be in the range [0, 360) degrees.');
    }
    if (typeof argumentOfPeriapsis !== 'number' || argumentOfPeriapsis < 0 || argumentOfPeriapsis >= 360) {
        throw new Error('Invalid argument of periapsis. It must be in the range [0, 360) degrees.');
    }
    if (typeof trueAnomaly !== 'number' || trueAnomaly < 0 || trueAnomaly >= 360) {
        throw new Error('Invalid true anomaly. It must be in the range [0, 360) degrees.');
    }

    // Convert degrees to radians for calculations
    const toRadians = (degrees) => degrees * (Math.PI / 180);
    const i = toRadians(inclination);
    const Ω = toRadians(longitudeOfAscendingNode);
    const ω = toRadians(argumentOfPeriapsis);
    const ν = toRadians(trueAnomaly);

    // Calculate the distance from the central body
    const r = semiMajorAxis * (1 - eccentricity * Math.cos(ν));

    // Calculate the position in the orbital plane
    const xOrbital = r * Math.cos(ν);
    const yOrbital = r * Math.sin(ν);

    // Convert to 3D coordinates using rotation matrices
    const x = (Math.cos(Ω) * Math.cos(ω) - Math.sin(Ω) * Math.sin(ω) * Math.cos(i)) * xOrbital +
              (-Math.cos(Ω) * Math.sin(ω) - Math.sin(Ω) * Math.cos(ω) * Math.cos(i)) * yOrbital;

    const y = (Math.sin(Ω) * Math.cos(ω) + Math.cos(Ω) * Math.sin(ω) * Math.cos(i)) * xOrbital +
              (-Math.sin(Ω) * Math.sin(ω) + Math.cos(Ω) * Math.cos(ω) * Math.cos(i)) * yOrbital;

    const z = (Math.sin(i) * Math.sin(ω)) * xOrbital + (Math.sin(i) * Math.cos(ω)) * yOrbital;

    // Return the calculated position
    return { x, y, z };
}

// Example usage
try {
    const position = calculateCelestialBodyPosition(149597870.7, 0.0167, 7.155, 348.73936, 114.20783, 0);
    console.log('Celestial Body Position:', position);
} catch (error) {
    console.error('Error calculating position:', error.message);
}
```
