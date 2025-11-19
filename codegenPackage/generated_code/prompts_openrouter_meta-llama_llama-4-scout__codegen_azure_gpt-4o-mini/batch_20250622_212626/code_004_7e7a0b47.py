"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: "Create a JavaScript function to calculate the valuation of a startup based on its idea, market research, and competitive analysis, considering factors like SWOT analysis and MVP costs."
Generated: DETERMINISTIC_7e7a0b47d819110e
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the valuation of a startup based on various factors.
 * 
 * @param {number} ideaScore - A score from 1 to 10 representing the strength of the startup's idea.
 * @param {number} marketResearchScore - A score from 1 to 10 representing the quality of market research.
 * @param {number} competitiveAnalysisScore - A score from 1 to 10 representing the thoroughness of competitive analysis.
 * @param {Object} swotAnalysis - An object containing SWOT analysis scores.
 * @param {number} swotAnalysis.strengths - Score from 1 to 10 for strengths.
 * @param {number} swotAnalysis.weaknesses - Score from 1 to 10 for weaknesses.
 * @param {number} swotAnalysis.opportunities - Score from 1 to 10 for opportunities.
 * @param {number} swotAnalysis.threats - Score from 1 to 10 for threats.
 * @param {number} mvpCost - The cost of developing the Minimum Viable Product (MVP).
 * 
 * @returns {number} - The calculated valuation of the startup.
 * 
 * @throws {Error} - Throws an error if any input score is out of range or if MVP cost is negative.
 */
function calculateStartupValuation(ideaScore, marketResearchScore, competitiveAnalysisScore, swotAnalysis, mvpCost) {
    // Validate input scores
    const validateScore = (score) => {
        if (score < 1 || score > 10) {
            throw new Error('Score must be between 1 and 10.');
        }
    };

    validateScore(ideaScore);
    validateScore(marketResearchScore);
    validateScore(competitiveAnalysisScore);
    validateScore(swotAnalysis.strengths);
    validateScore(swotAnalysis.weaknesses);
    validateScore(swotAnalysis.opportunities);
    validateScore(swotAnalysis.threats);

    // Validate MVP cost
    if (mvpCost < 0) {
        throw new Error('MVP cost cannot be negative.');
    }

    // Calculate the valuation based on weighted factors
    const ideaWeight = 0.25;
    const marketResearchWeight = 0.25;
    const competitiveAnalysisWeight = 0.25;
    const swotWeight = 0.25;

    const swotScore = (swotAnalysis.strengths + swotAnalysis.weaknesses + swotAnalysis.opportunities + swotAnalysis.threats) / 4;

    // Calculate total valuation
    const valuation = (
        (ideaScore * ideaWeight) +
        (marketResearchScore * marketResearchWeight) +
        (competitiveAnalysisScore * competitiveAnalysisWeight) +
        (swotScore * swotWeight)
    ) * 10000 - mvpCost; // Adjusting valuation by MVP cost

    return valuation;
}

// Example usage
try {
    const valuation = calculateStartupValuation(8, 9, 7, { strengths: 8, weaknesses: 5, opportunities: 9, threats: 4 }, 50000);
    console.log(`The startup valuation is: $${valuation}`);
} catch (error) {
    console.error(`Error calculating valuation: ${error.message}`);
}
```
