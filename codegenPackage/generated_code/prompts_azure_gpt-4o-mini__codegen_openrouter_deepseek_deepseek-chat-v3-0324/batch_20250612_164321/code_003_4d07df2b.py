"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: Develop a JavaScript function that analyzes historical Togel HK data to identify patterns and trends in winning numbers.
Generated: DETERMINISTIC_4d07df2ba10ac2cc
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Analyzes historical Togel HK data to identify patterns and trends in winning numbers.
 * 
 * @param {Array<Array<number>>} historicalData - Array of historical draws, each draw is an array of numbers
 * @param {Object} [options] - Optional analysis configuration
 * @param {number} [options.recentDraws] - Number of recent draws to consider (default: all)
 * @param {boolean} [options.hotColdAnalysis] - Whether to perform hot/cold number analysis (default: true)
 * @param {boolean} [options.frequencyAnalysis] - Whether to perform frequency analysis (default: true)
 * @param {boolean} [options.pairAnalysis] - Whether to analyze number pairs (default: false)
 * @returns {Object} Analysis results containing various patterns and trends
 */
function analyzeTogelHK(historicalData, options = {}) {
    // Validate input
    if (!Array.isArray(historicalData) || historicalData.length === 0) {
        throw new Error('Historical data must be a non-empty array');
    }

    // Set default options
    const {
        recentDraws = historicalData.length,
        hotColdAnalysis = true,
        frequencyAnalysis = true,
        pairAnalysis = false
    } = options;

    // Prepare data subset based on recentDraws
    const recentData = historicalData.slice(0, recentDraws);
    const allNumbers = recentData.flat();

    // Initialize result object
    const results = {
        summary: {
            totalDrawsAnalyzed: recentData.length,
            firstDraw: recentData[recentData.length - 1],
            lastDraw: recentData[0]
        },
        frequencyAnalysis: {},
        hotColdAnalysis: {},
        pairAnalysis: {},
        recommendations: {}
    };

    // Frequency analysis
    if (frequencyAnalysis) {
        const frequencyMap = new Map();
        
        // Count occurrences of each number
        allNumbers.forEach(num => {
            frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
        });

        // Convert to sorted array
        const frequencyArray = Array.from(frequencyMap.entries())
            .sort((a, b) => b[1] - a[1]);
        
        results.frequencyAnalysis = {
            mostFrequent: frequencyArray.slice(0, 5),
            leastFrequent: frequencyArray.slice(-5).reverse(),
            fullFrequency: Object.fromEntries(frequencyArray)
        };
    }

    // Hot/Cold number analysis
    if (hotColdAnalysis) {
        const hotThreshold = Math.floor(recentData.length * 0.3);
        const coldThreshold = Math.floor(recentData.length * 0.7);
        const hotNumbers = [];
        const coldNumbers = [];
        const frequencyMap = results.frequencyAnalysis.fullFrequency || new Map();

        frequencyMap.forEach((count, num) => {
            if (count >= hotThreshold) {
                hotNumbers.push(num);
            } else if (count <= coldThreshold) {
                coldNumbers.push(num);
            }
        });

        results.hotColdAnalysis = {
            hotNumbers: hotNumbers.sort((a, b) => b - a),
            coldNumbers: coldNumbers.sort((a, b) => a - b),
            hotThreshold,
            coldThreshold
        };
    }

    // Pair analysis
    if (pairAnalysis) {
        const pairMap = new Map();
        
        // Count occurrences of number pairs
        recentData.forEach(draw => {
            for (let i = 0; i < draw.length; i++) {
                for (let j = i + 1; j < draw.length; j++) {
                    const pair = [draw[i], draw[j]].sort((a, b) => a - b).join('-');
                    pairMap.set(pair, (pairMap.get(pair) || 0) + 1);
                }
            }
        });

        // Convert to sorted array
        const pairArray = Array.from(pairMap.entries())
            .sort((a, b) => b[1] - a[1]);
        
        results.pairAnalysis = {
            mostFrequentPairs: pairArray.slice(0, 5),
            fullPairFrequency: Object.fromEntries(pairArray)
        };
    }

    // Generate recommendations
    if (frequencyAnalysis && hotColdAnalysis) {
        results.recommendations = {
            balancedSelection: [
                ...results.frequencyAnalysis.mostFrequent.slice(0, 2).map(x => x[0]),
                ...results.frequencyAnalysis.leastFrequent.slice(0, 2).map(x => x[0]),
                ...results.hotColdAnalysis.hotNumbers.slice(0, 1),
                ...results.hotColdAnalysis.coldNumbers.slice(0, 1)
            ],
            hotNumbersStrategy: results.hotColdAnalysis.hotNumbers.slice(0, 6),
            coldNumbersStrategy: results.hotColdAnalysis.coldNumbers.slice(0, 6)
        };
    }

    return results;
}

// Example usage:
// const historicalData = [
//     [1, 2, 3, 4, 5, 6],
//     [2, 3, 4, 5, 6, 7],
//     // ... more historical draws
// ];
// const analysis = analyzeTogelHK(historicalData, { recentDraws: 100, pairAnalysis: true });
// console.log(analysis);
```
