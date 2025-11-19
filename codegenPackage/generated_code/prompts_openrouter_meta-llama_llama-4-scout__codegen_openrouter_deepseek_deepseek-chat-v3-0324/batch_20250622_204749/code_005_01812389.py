"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Write a JavaScript function to optimize the placement of streetlights along a road network."
Generated: DETERMINISTIC_018123897cf0189f
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Optimizes the placement of streetlights along a road network.
 * 
 * @param {Array<Array<number>>} roadNetwork - Array of road segments represented as [startX, startY, endX, endY]
 * @param {number} lightRadius - The illumination radius of each streetlight
 * @param {number} minCoverage - Minimum required coverage percentage (0-100)
 * @returns {Array<Array<number>>} Array of optimal streetlight positions [x, y]
 */
function optimizeStreetlightPlacement(roadNetwork, lightRadius, minCoverage) {
    if (!Array.isArray(roadNetwork) || roadNetwork.length === 0) {
        throw new Error('Road network must be a non-empty array');
    }
    if (typeof lightRadius !== 'number' || lightRadius <= 0) {
        throw new Error('Light radius must be a positive number');
    }
    if (typeof minCoverage !== 'number' || minCoverage < 0 || minCoverage > 100) {
        throw new Error('Minimum coverage must be between 0 and 100');
    }

    // Extract all road points
    const allRoadPoints = [];
    roadNetwork.forEach(segment => {
        if (segment.length !== 4) {
            throw new Error('Each road segment must have 4 coordinates [startX, startY, endX, endY]');
        }
        const [x1, y1, x2, y2] = segment;
        allRoadPoints.push([x1, y1]);
        allRoadPoints.push([x2, y2]);
        
        // Add intermediate points for better coverage
        const segmentLength = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        const numPoints = Math.ceil(segmentLength / (lightRadius / 2));
        for (let i = 1; i < numPoints; i++) {
            const ratio = i / numPoints;
            allRoadPoints.push([
                x1 + (x2 - x1) * ratio,
                y1 + (y2 - y1) * ratio
            ]);
        }
    });

    // Calculate bounding box of road network
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    allRoadPoints.forEach(([x, y]) => {
        minX = Math.min(minX, x);
        minY = Math.min(minY, y);
        maxX = Math.max(maxX, x);
        maxY = Math.max(maxY, y);
    });

    // Generate candidate points on a grid
    const gridSpacing = lightRadius / Math.sqrt(2); // Optimal grid spacing
    const candidates = [];
    for (let x = minX; x <= maxX; x += gridSpacing) {
        for (let y = minY; y <= maxY; y += gridSpacing) {
            candidates.push([x, y]);
        }
    }

    // Greedy algorithm to select optimal positions
    const selectedPositions = [];
    let remainingPoints = [...allRoadPoints];
    let coverage = 0;

    while (coverage < minCoverage && remainingPoints.length > 0) {
        let bestPosition = null;
        let bestCoverage = 0;
        let bestCoveredPoints = [];

        // Find candidate that covers most remaining points
        for (const [candX, candY] of candidates) {
            const coveredPoints = remainingPoints.filter(([x, y]) => {
                const distance = Math.sqrt(Math.pow(x - candX, 2) + Math.pow(y - candY, 2));
                return distance <= lightRadius;
            });

            if (coveredPoints.length > bestCoverage) {
                bestCoverage = coveredPoints.length;
                bestPosition = [candX, candY];
                bestCoveredPoints = coveredPoints;
            }
        }

        if (!bestPosition) break;

        // Add the best position and remove covered points
        selectedPositions.push(bestPosition);
        remainingPoints = remainingPoints.filter(point => 
            !bestCoveredPoints.some(p => p[0] === point[0] && p[1] === point[1])
        );

        // Update coverage percentage
        coverage = 100 * (allRoadPoints.length - remainingPoints.length) / allRoadPoints.length;
    }

    return selectedPositions;
}

// Example usage:
// const roadNetwork = [[0,0,10,0], [10,0,10,10], [10,10,0,10], [0,10,0,0]];
// const optimizedLights = optimizeStreetlightPlacement(roadNetwork, 3, 90);
// console.log(optimizedLights);
```
