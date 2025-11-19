"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: "Create a JavaScript function to display a company's accreditations and awards, such as Pride in the Job awards, on their website, using Westpoint Construction's awards as an example."
Generated: DETERMINISTIC_653090f60f1cd4d9
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a company's accreditations and awards on their website.
 * 
 * @param {Object} companyAwards - An object containing the company's awards.
 * @param {string} companyAwards.name - The name of the company.
 * @param {Array} companyAwards.awards - An array of award objects.
 * @param {string} companyAwards.awards[].name - The name of the award.
 * @param {string} companyAwards.awards[].description - A brief description of the award.
 * @param {string} companyAwards.awards[].year - The year the award was received.
 * 
 * @returns {string} HTML string displaying the company's accreditations and awards.
 */
function displayCompanyAwards(companyAwards) {
    try {
        // Check if companyAwards is an object
        if (typeof companyAwards !== 'object') {
            throw new Error('Invalid input. Company awards must be an object.');
        }

        // Check if companyAwards has required properties
        if (!companyAwards.name || !companyAwards.awards) {
            throw new Error('Invalid input. Company awards must have a name and awards array.');
        }

        // Check if awards is an array
        if (!Array.isArray(companyAwards.awards)) {
            throw new Error('Invalid input. Awards must be an array.');
        }

        let html = `
            <div class="company-awards">
                <h2>${companyAwards.name} Accreditations and Awards</h2>
                <ul>
        `;

        // Loop through each award and add to HTML
        companyAwards.awards.forEach(award => {
            // Check if award has required properties
            if (!award.name || !award.description || !award.year) {
                console.error('Invalid award object. Award must have a name, description, and year.');
                return;
            }

            html += `
                    <li>
                        <strong>${award.name}</strong> - ${award.description} (${award.year})
                    </li>
            `;
        });

        html += `
                </ul>
            </div>
        `;

        return html;
    } catch (error) {
        console.error(error.message);
        return '';
    }
}

// Example usage
const westpointConstructionAwards = {
    name: 'Westpoint Construction',
    awards: [
        {
            name: 'Pride in the Job Award',
            description: 'Awarded for outstanding workmanship and customer service',
            year: '2022'
        },
        {
            name: 'Construction Excellence Award',
            description: 'Recognized for exceptional construction practices',
            year: '2020'
        }
    ]
};

console.log(displayCompanyAwards(westpointConstructionAwards));
```
