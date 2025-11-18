"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Create a script in JavaScript that connects users to investment education companies based on their preferences, mimicking the functionality of Trade GPT.
Generated: DETERMINISTIC_7a87bdb9302255e6
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// investmentMatcher.js

/**
 * InvestmentMatcher connects users to investment education companies
 * based on user preferences.
 */
class InvestmentMatcher {
    constructor() {
        // A dictionary to store available investment education companies
        this.companies = [
            { name: "InvestSmart", categories: ["stocks", "bonds", "crypto"], rating: 4.5 },
            { name: "WealthWise", categories: ["stocks", "real estate"], rating: 4.0 },
            { name: "CryptoAcademy", categories: ["crypto"], rating: 4.8 },
            { name: "RealEstateMasters", categories: ["real estate"], rating: 4.2 },
        ];
    }

    /**
     * Matches companies to user preferences.
     * @param {Object} userPreferences - The preferences object with categories and minimumRating.
     * @returns {Array} - List of matched companies.
     */
    matchCompanies(userPreferences) {
        try {
            // Check if userPreferences is valid
            if (!userPreferences || !userPreferences.categories || !Array.isArray(userPreferences.categories)) {
                throw new Error("Invalid user preferences. Please provide an object with a 'categories' array.");
            }

            const { categories, minimumRating = 0 } = userPreferences;

            // Filter companies based on user preferences
            const matchedCompanies = this.companies.filter(company => {
                const isCategoryMatch = company.categories.some(category => categories.includes(category));
                const isRatingMatch = company.rating >= minimumRating;

                return isCategoryMatch && isRatingMatch;
            });

            // Sort matched companies by rating in descending order
            return matchedCompanies.sort((a, b) => b.rating - a.rating);
        } catch (error) {
            console.error("Error matching companies:", error.message);
            return [];
        }
    }
}

// Example usage
const matcher = new InvestmentMatcher();
const userPreferences = {
    categories: ["crypto", "stocks"],
    minimumRating: 4.5,
};

const matchedCompanies = matcher.matchCompanies(userPreferences);
console.log("Matched Companies:", matchedCompanies);
```

Make sure to run this code in an environment that supports ES6 JavaScript, such as Node.js or a modern web browser.
