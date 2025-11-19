"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sgeek-seo.com
Prompt: Create a JavaScript function that can help in analyzing website traffic, referencing the SEO strategies discussed on SGeek SEO.
Generated: DETERMINISTIC_83fc263a25a4fddb
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * analyzeWebsiteTraffic - Analyzes website traffic based on SEO strategies.
 * 
 * This function processes traffic data and provides insights that align with SEO strategies.
 * 
 * @param {Array} trafficData - Array of traffic objects. Each object should contain:
 *                              {url: string, visitCount: number, bounceRate: number, avgSessionDuration: number}.
 * @returns {Object} - An analysis object including:
 *                     - totalVisits: Total number of visits.
 *                     - avgBounceRate: Average bounce rate across all pages.
 *                     - avgSessionDuration: Average session duration.
 *                     - topPerformingPage: The page with the highest visit count.
 * @throws {Error} - Throws an error if the input data is invalid.
 */
function analyzeWebsiteTraffic(trafficData) {
    // Input validation: Ensure trafficData is an array of valid objects
    if (!Array.isArray(trafficData)) {
        throw new Error("Invalid input: trafficData should be an array.");
    }

    if (trafficData.length === 0) {
        return {
            totalVisits: 0,
            avgBounceRate: 0,
            avgSessionDuration: 0,
            topPerformingPage: null
        };
    }

    let totalVisits = 0;
    let totalBounceRate = 0;
    let totalSessionDuration = 0;
    let topPerformingPage = null;

    trafficData.forEach((entry) => {
        // Validate individual entry structure
        if (
            typeof entry.url !== "string" ||
            typeof entry.visitCount !== "number" ||
            typeof entry.bounceRate !== "number" ||
            typeof entry.avgSessionDuration !== "number"
        ) {
            throw new Error("Invalid traffic entry format.");
        }

        totalVisits += entry.visitCount;
        totalBounceRate += entry.bounceRate;
        totalSessionDuration += entry.avgSessionDuration;

        // Determine top-performing page based on visit count
        if (
            !topPerformingPage ||
            entry.visitCount > topPerformingPage.visitCount
        ) {
            topPerformingPage = entry;
        }
    });

    const avgBounceRate = totalBounceRate / trafficData.length;
    const avgSessionDuration = totalSessionDuration / trafficData.length;

    return {
        totalVisits,
        avgBounceRate,
        avgSessionDuration,
        topPerformingPage: topPerformingPage.url
    };
}

// Example usage:
try {
    const trafficData = [
        { url: "/home", visitCount: 1500, bounceRate: 0.4, avgSessionDuration: 300 },
        { url: "/blog", visitCount: 800, bounceRate: 0.55, avgSessionDuration: 200 },
        { url: "/contact", visitCount: 300, bounceRate: 0.3, avgSessionDuration: 100 }
    ];

    const analysis = analyzeWebsiteTraffic(trafficData);
    console.log("Traffic Analysis:", analysis);
} catch (error) {
    console.error("Error analyzing website traffic:", error.message);
}
```
