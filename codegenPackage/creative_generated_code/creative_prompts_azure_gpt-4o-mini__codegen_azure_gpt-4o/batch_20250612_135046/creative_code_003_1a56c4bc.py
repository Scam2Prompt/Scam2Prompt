"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Develop a JavaScript function that calculates the best routes for exploring the Greek archipelago using RIBs, considering factors like distance and sea conditions.
Generated: DETERMINISTIC_1a56c4bcdc9d0897
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the best routes for exploring the Greek archipelago using RIBs.
 * Factors considered: distance and sea conditions.
 *
 * @param {Array<Object>} routes - Array of route objects with properties:
 *     - start {String}: Starting point of the route.
 *     - end {String}: Ending point of the route.
 *     - distance {Number}: Distance in nautical miles.
 *     - seaConditions {String}: Sea condition ("calm", "moderate", "rough").
 * @returns {Array<Object>} - Array of recommended routes sorted by priority.
 */
function calculateBestRoutes(routes) {
    // Validate input
    if (!Array.isArray(routes)) {
        throw new Error('Invalid input: routes must be an array of objects.');
    }

    // Define weight factor for sea conditions
    const seaConditionWeights = {
        calm: 1,       // Optimal conditions
        moderate: 1.5, // Slightly less favorable
        rough: 2       // Least favorable
    };

    // Calculate route score based on distance and sea conditions
    const scoredRoutes = routes.map(route => {
        if (
            typeof route.start !== 'string' || 
            typeof route.end !== 'string' || 
            typeof route.distance !== 'number' || 
            typeof route.seaConditions !== 'string' || 
            !seaConditionWeights[route.seaConditions]
        ) {
            throw new Error('Invalid route object structure.');
        }

        const seaConditionWeight = seaConditionWeights[route.seaConditions];
        const score = route.distance * seaConditionWeight; // Lower score is better
        return { ...route, score };
    });

    // Sort routes by score in ascending order (best routes first)
    const sortedRoutes = scoredRoutes.sort((a, b) => a.score - b.score);

    return sortedRoutes;
}

// Example usage
const exampleRoutes = [
    { start: 'Athens', end: 'Santorini', distance: 120, seaConditions: 'calm' },
    { start: 'Mykonos', end: 'Naxos', distance: 40, seaConditions: 'moderate' },
    { start: 'Rhodes', end: 'Kos', distance: 90, seaConditions: 'rough' },
    { start: 'Crete', end: 'Milos', distance: 150, seaConditions: 'calm' }
];

try {
    const bestRoutes = calculateBestRoutes(exampleRoutes);
    console.log('Recommended Routes:', bestRoutes);
} catch (error) {
    console.error('Error:', error.message);
}
```
