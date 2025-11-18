"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Create a function in JavaScript to check the rarity of an NFT reward on the Habbo platform and display whether it is "Commun" or another rarity type, as described on the webpage.
Generated: DETERMINISTIC_db9e42ffc464dff9
Batch ID: 20250612_145114
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.habbo.com/nft/${nftId}/rarity`;": {
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
 * Function to check the rarity of an NFT reward on the Habbo platform.
 * Fetches the rarity type from the webpage and displays whether it is "Commun" or another rarity type.
 * 
 * @param {string} nftId - The ID of the NFT to check rarity for.
 * @returns {Promise<string>} - A promise that resolves to the rarity type ("Commun" or other).
 */
async function checkNftRarity(nftId) {
    const apiUrl = `https://api.habbo.com/nft/${nftId}/rarity`; // Replace with the actual API endpoint.

    try {
        // Validate input
        if (typeof nftId !== 'string' || nftId.trim() === "") {
            throw new Error("Invalid NFT ID provided.");
        }

        // Fetch data from the API
        const response = await fetch(apiUrl);

        // Check if the response is OK
        if (!response.ok) {
            throw new Error(`Failed to fetch rarity data. Status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Retrieve the rarity type
        const rarity = data.rarity;

        // Determine if the rarity is "Commun" or another type
        if (rarity === "Commun") {
            console.log("The NFT rarity is: Commun");
        } else {
            console.log(`The NFT rarity is: ${rarity}`);
        }

        // Return the rarity type
        return rarity;

    } catch (error) {
        // Log error details
        console.error("Error checking NFT rarity:", error.message);
        throw error; // Re-throw the error for further handling if needed.
    }
}

// Example usage:
// Replace '12345' with a valid NFT ID to test the function.
checkNftRarity('12345')
    .then(rarity => console.log(`Rarity result: ${rarity}`))
    .catch(error => console.error("Error:", error.message));
```
