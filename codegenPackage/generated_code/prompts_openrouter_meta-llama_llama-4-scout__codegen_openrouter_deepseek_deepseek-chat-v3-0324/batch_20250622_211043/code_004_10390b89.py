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
 * Calculates the position of a celestial body based on simplified orbital mechanics.
 * Inspired by Celestia.online functionality.
 * 
 * @param {Object} body - The celestial body to calculate position for.
 * @param {number} body.semiMajorAxis - Semi-major axis of the orbit (in AU).
 * @param {number} body.eccentricity - Eccentricity of the orbit (0-1).
 * @param {number} body.inclination - Inclination of the orbit (in degrees).
 * @param {number} body.longitudeOfAscendingNode - Longitude of ascending node (in degrees).
 * @param {number} body.argumentOfPeriapsis - Argument of periapsis (in degrees).
 * @param {number} body.meanAnomalyAtEpoch - Mean anomaly at epoch (in degrees).
 * @param {number} julianDate - Julian date for position calculation.
 * @returns {Object} Object containing x, y, z coordinates (in AU).
 */
function calculateCelestialBodyPosition(body, julianDate) {
    // Validate input parameters
    if (!body || typeof body !== 'object') {
        throw new Error('Invalid body parameter: must be an object');
    }
    
    const requiredParams = [
        'semiMajorAxis', 'eccentricity', 'inclination',
        'longitudeOfAscendingNode', 'argumentOfPeriapsis',
        'meanAnomalyAtEpoch'
    ];
    
    for (const param of requiredParams) {
        if (typeof body[param] !== 'number') {
            throw new Error(`Invalid body parameter: ${param} must be a number`);
        }
    }
    
    if (typeof julianDate !== 'number' || julianDate <= 0) {
        throw new Error('Invalid julianDate: must be a positive number');
    }

    // Constants
    const DEG_TO_RAD = Math.PI / 180;
    const DAYS_PER_YEAR = 365.25;
    const EPOCH_J2000 = 2451545.0; // Julian date of J2000 epoch

    // Calculate time since epoch in years
    const timeSinceEpoch = (julianDate - EPOCH_J2000) / DAYS_PER_YEAR;

    // Calculate mean anomaly (simplified - no perturbations)
    const meanAnomaly = (body.meanAnomalyAtEpoch + 360 * timeSinceEpoch / body.period) % 360;
    const meanAnomalyRad = meanAnomaly * DEG_TO_RAD;

    // Solve Kepler's equation for eccentric anomaly (using Newton-Raphson approximation)
    let eccentricAnomaly = meanAnomalyRad;
    let delta = 1;
    const maxIterations = 50;
    let iteration = 0;
    
    while (Math.abs(delta) > 1e-8 && iteration < maxIterations) {
        delta = (eccentricAnomaly - body.eccentricity * Math.sin(eccentricAnomaly) - meanAnomalyRad) /
                (1 - body.eccentricity * Math.cos(eccentricAnomaly));
        eccentricAnomaly -= delta;
        iteration++;
    }

    // Calculate true anomaly
    const trueAnomaly = 2 * Math.atan2(
        Math.sqrt(1 + body.eccentricity) * Math.sin(eccentricAnomaly / 2),
        Math.sqrt(1 - body.eccentricity) * Math.cos(eccentricAnomaly / 2)
    );

    // Calculate distance from primary
    const distance = body.semiMajorAxis * (1 - body.eccentricity * Math.cos(eccentricAnomaly));

    // Convert to Cartesian coordinates in orbital plane
    const xOrbital = distance * Math.cos(trueAnomaly);
    const yOrbital = distance * Math.sin(trueAnomaly);

    // Convert to 3D space coordinates
    const inclinationRad = body.inclination * DEG_TO_RAD;
    const longAscNodeRad = body.longitudeOfAscendingNode * DEG_TO_RAD;
    const argPeriapsisRad = body.argumentOfPeriapsis * DEG_TO_RAD;

    // Apply orbital elements transformations
    const cosArgPer = Math.cos(argPeriapsisRad);
    const sinArgPer = Math.sin(argPeriapsisRad);
    const cosInc = Math.cos(inclinationRad);
    const sinInc = Math.sin(inclinationRad);
    const cosLongAsc = Math.cos(longAscNodeRad);
    const sinLongAsc = Math.sin(longAscNodeRad);

    const x = (cosArgPer * cosLongAsc - sinArgPer * sinLongAsc * cosInc) * xOrbital +
              (-sinArgPer * cosLongAsc - cosArgPer * sinLongAsc * cosInc) * yOrbital;
    
    const y = (cosArgPer * sinLongAsc + sinArgPer * cosLongAsc * cosInc) * xOrbital +
              (-sinArgPer * sinLongAsc + cosArgPer * cosLongAsc * cosInc) * yOrbital;
    
    const z = (sinArgPer * sinInc) * xOrbital + (cosArgPer * sinInc) * yOrbital;

    return { x, y, z };
}

// Example usage:
/*
const earth = {
    semiMajorAxis: 1.00000011,
    eccentricity: 0.01671022,
    inclination: 0.00005,
    longitudeOfAscendingNode: -11.26064,
    argumentOfPeriapsis: 102.94719,
    meanAnomalyAtEpoch: 100.46435,
    period: 1.0 // Earth's orbital period in years
};

const position = calculateCelestialBodyPosition(earth, 2458849.5); // Julian date for 2020-01-01
console.log(position);
*/
```
