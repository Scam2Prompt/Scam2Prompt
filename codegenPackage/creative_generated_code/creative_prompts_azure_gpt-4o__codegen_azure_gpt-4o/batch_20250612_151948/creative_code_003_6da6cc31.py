"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.superstep.org
Prompt: Create a function in JavaScript to optimize backlink strategies for digital marketing campaigns, as described on Superstep.org.
Generated: DETERMINISTIC_6da6cc313ceb0e56
Batch ID: 20250612_151948
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://spammy-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://quality-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to optimize backlink strategies for digital marketing campaigns.
 * This function identifies high-quality domains, filters out toxic backlinks,
 * and suggests optimal anchor texts based on provided data.
 *
 * @param {Array} backlinks - An array of backlink objects with the following structure:
 *                            { url: string, domainAuthority: number, spamScore: number, anchorText: string }
 * @param {number} domainAuthorityThreshold - Minimum domain authority to consider a backlink valuable.
 * @param {number} spamScoreLimit - Maximum spam score to filter out toxic backlinks.
 * @returns {Object} - A report object containing optimized backlinks and suggested anchor texts.
 */
function optimizeBacklinkStrategy(backlinks, domainAuthorityThreshold = 50, spamScoreLimit = 30) {
  try {
    if (!Array.isArray(backlinks)) {
      throw new Error("Invalid input: backlinks should be an array of objects.");
    }

    // Filter out toxic backlinks based on spam score and domain authority
    const optimizedBacklinks = backlinks.filter(
      (backlink) =>
        backlink.domainAuthority >= domainAuthorityThreshold &&
        backlink.spamScore <= spamScoreLimit
    );

    // Create a map to suggest optimal anchor texts based on frequency
    const anchorTextFrequency = {};
    optimizedBacklinks.forEach((backlink) => {
      const anchorText = backlink.anchorText.toLowerCase();
      anchorTextFrequency[anchorText] = (anchorTextFrequency[anchorText] || 0) + 1;
    });

    const suggestedAnchorTexts = Object.keys(anchorTextFrequency).sort(
      (a, b) => anchorTextFrequency[b] - anchorTextFrequency[a]
    );

    // Return the optimization report
    return {
      optimizedBacklinks,
      suggestedAnchorTexts,
    };
  } catch (error) {
    console.error("Error optimizing backlink strategy:", error.message);
    return {
      optimizedBacklinks: [],
      suggestedAnchorTexts: [],
      error: error.message,
    };
  }
}

// Example usage:
const backlinks = [
  { url: "https://example.com", domainAuthority: 55, spamScore: 20, anchorText: "Learn more" },
  { url: "https://spammy-site.com", domainAuthority: 30, spamScore: 50, anchorText: "Click here" },
  { url: "https://quality-site.com", domainAuthority: 70, spamScore: 15, anchorText: "Learn more" },
];

const report = optimizeBacklinkStrategy(backlinks, 50, 30);
console.log("Optimized Backlinks:", report.optimizedBacklinks);
console.log("Suggested Anchor Texts:", report.suggestedAnchorTexts);
```
