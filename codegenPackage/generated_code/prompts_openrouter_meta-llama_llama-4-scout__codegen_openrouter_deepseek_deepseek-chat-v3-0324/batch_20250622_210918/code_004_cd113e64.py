"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Create a JavaScript function to generate a Robotos NFT image using the provided traits and rarity data, and return the image data in a suitable format.
Generated: DETERMINISTIC_cd113e6429afda94
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a Robotos NFT image based on provided traits and rarity data.
 * 
 * @param {Object} traits - An object containing the selected traits for the NFT.
 * @param {Object} rarityData - An object containing rarity information for traits.
 * @returns {Promise<Object>} An object containing the image data and metadata.
 * @throws {Error} If traits or rarity data is invalid or image generation fails.
 */
async function generateRobotosNFT(traits, rarityData) {
    // Validate input parameters
    if (!traits || typeof traits !== 'object' || Object.keys(traits).length === 0) {
        throw new Error('Invalid traits object provided');
    }

    if (!rarityData || typeof rarityData !== 'object' || Object.keys(rarityData).length === 0) {
        throw new Error('Invalid rarity data provided');
    }

    // Validate required traits
    const requiredTraits = ['background', 'body', 'face', 'mouth', 'eyes', 'head'];
    for (const trait of requiredTraits) {
        if (!traits[trait]) {
            throw new Error(`Missing required trait: ${trait}`);
        }
    }

    try {
        // Calculate rarity score
        const rarityScore = calculateRarityScore(traits, rarityData);

        // Generate image (in a real implementation, this would use a canvas library)
        const imageData = await generateImage(traits);

        // Return the NFT data
        return {
            image: imageData,
            metadata: {
                traits: traits,
                rarity: rarityScore,
                description: 'Unique Robotos NFT generated on-chain',
                name: `Robotos #${generateUniqueId()}`,
                created_at: new Date().toISOString()
            }
        };
    } catch (error) {
        console.error('Error generating Robotos NFT:', error);
        throw new Error('Failed to generate NFT image');
    }
}

/**
 * Calculates the rarity score based on traits and rarity data.
 * @private
 */
function calculateRarityScore(traits, rarityData) {
    let score = 0;
    let totalWeight = 0;

    for (const [trait, value] of Object.entries(traits)) {
        if (rarityData[trait] && rarityData[trait][value]) {
            const weight = rarityData[trait][value];
            score += weight;
            totalWeight += weight;
        }
    }

    // Normalize score between 0 and 100
    return totalWeight > 0 ? Math.round((score / totalWeight) * 100) : 0;
}

/**
 * Generates a unique ID for the NFT.
 * @private
 */
function generateUniqueId() {
    return Date.now().toString(36) + Math.random().toString(36).substring(2);
}

/**
 * Simulates image generation (in a real implementation, this would use canvas or similar).
 * @private
 */
async function generateImage(traits) {
    // In a real implementation, this would use a canvas library to composite layers
    // For this example, we return a mock data URL
    return {
        dataURL: `data:image/svg+xml;base64,...`, // Base64 encoded SVG
        width: 1000,
        height: 1000,
        format: 'svg'
    };
}

// Example usage:
/*
const traits = {
    background: 'space',
    body: 'blue',
    face: 'round',
    mouth: 'smile',
    eyes: 'laser',
    head: 'antenna'
};

const rarityData = {
    background: {
        space: 0.1,
        city: 0.3,
        desert: 0.6
    },
    body: {
        blue: 0.2,
        red: 0.3,
        green: 0.5
    },
    // ... other traits with their rarity weights
};

generateRobotosNFT(traits, rarityData)
    .then(nft => console.log(nft))
    .catch(err => console.error(err));
*/
```
