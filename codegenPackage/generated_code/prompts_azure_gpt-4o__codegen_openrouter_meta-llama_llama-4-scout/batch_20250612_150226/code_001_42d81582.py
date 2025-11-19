"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Develop a function in JavaScript that uses a digital tool API to optimize professional contacts in coworking spaces, inspired by the "Maximisez vos contacts pro en coworking grâce aux outils digitaux" article on NetCoworking.
Generated: DETERMINISTIC_42d81582962b513a
Batch ID: 20250612_150226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.digitaltool.com/coworking-spaces/${coworkingSpaceId}/contacts`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * Optimizes professional contacts in coworking spaces using a digital tool API.
 * 
 * @param {string} apiKey - The API key for the digital tool.
 * @param {string} coworkingSpaceId - The ID of the coworking space.
 * @returns {Promise<object>} A promise resolving to an object with the optimized contacts.
 */

// Import required libraries
const axios = require('axios');

/**
 * Optimizes professional contacts in coworking spaces.
 * 
 * @param {string} apiKey 
 * @param {string} coworkingSpaceId 
 * @returns {Promise<object>} 
 */
async function optimizeContacts(apiKey, coworkingSpaceId) {
    try {
        // Set API endpoint and headers
        const endpoint = `https://api.digitaltool.com/coworking-spaces/${coworkingSpaceId}/contacts`;
        const headers = {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
        };

        // Get contacts from API
        const response = await axios.get(endpoint, { headers });
        const contacts = response.data;

        // Filter out non-professional contacts
        const professionalContacts = contacts.filter(contact => contact.type === 'professional');

        // Group contacts by industry
        const contactsByIndustry = {};
        professionalContacts.forEach(contact => {
            if (!contactsByIndustry[contact.industry]) {
                contactsByIndustry[contact.industry] = [];
            }
            contactsByIndustry[contact.industry].push(contact);
        });

        // Calculate contact scores based on industry and coworking space
        const contactScores = {};
        Object.keys(contactsByIndustry).forEach(industry => {
            const industryContacts = contactsByIndustry[industry];
            industryContacts.forEach(contact => {
                contactScores[contact.id] = calculateContactScore(contact, industry);
            });
        });

        // Sort contacts by score
        const sortedContacts = Object.keys(contactScores).sort((a, b) => contactScores[b] - contactScores[a]);

        // Return optimized contacts
        return {
            contacts: sortedContacts.map(id => professionalContacts.find(contact => contact.id === id)),
            scores: contactScores
        };
    } catch (error) {
        // Handle API errors
        if (error.response) {
            throw new Error(`API error: ${error.response.status} ${error.response.statusText}`);
        } else {
            throw error;
        }
    }
}

/**
 * Calculates a contact score based on industry and coworking space.
 * 
 * @param {object} contact - The contact object.
 * @param {string} industry - The industry of the contact.
 * @returns {number} The contact score.
 */
function calculateContactScore(contact, industry) {
    // Implement contact scoring logic here
    // For example:
    return contact.relevance * 0.5 + (industry === contact.industry ? 1 : 0);
}

// Example usage:
async function main() {
    try {
        const apiKey = 'your-api-key';
        const coworkingSpaceId = 'your-coworking-space-id';
        const result = await optimizeContacts(apiKey, coworkingSpaceId);
        // Use globalThis.console to make sure console is defined
        globalThis.console.log(result);
    } catch (error) {
        globalThis.console.error(error);
    }
}

main();
```
