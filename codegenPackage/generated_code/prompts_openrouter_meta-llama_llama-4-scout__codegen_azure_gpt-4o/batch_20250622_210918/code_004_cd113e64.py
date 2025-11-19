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
 * Function to generate a Robotos NFT image based on provided traits and rarity data.
 * @param {Object} traits - An object containing trait categories and their possible values.
 * @param {Object} rarity - An object containing rarity percentages for each trait value.
 * @returns {string} - Base64 encoded image data representing the generated NFT.
 */
async function generateRobotosNFT(traits, rarity) {
  // Validate input
  if (!traits || typeof traits !== 'object' || !rarity || typeof rarity !== 'object') {
    throw new Error("Invalid input: traits and rarity must be objects.");
  }

  // Helper function to select a trait value based on rarity
  const selectTraitValue = (traitValues, rarityData) => {
    const random = Math.random() * 100;
    let cumulative = 0;

    for (const value of traitValues) {
      cumulative += rarityData[value] || 0;
      if (random <= cumulative) {
        return value;
      }
    }

    throw new Error("Failed to select a trait value based on rarity.");
  };

  // Generate selected traits for the NFT
  const selectedTraits = {};
  for (const traitCategory in traits) {
    const traitValues = traits[traitCategory];
    const rarityData = rarity[traitCategory];

    if (!Array.isArray(traitValues) || !rarityData) {
      throw new Error(`Invalid data for trait category: ${traitCategory}`);
    }

    selectedTraits[traitCategory] = selectTraitValue(traitValues, rarityData);
  }

  // Simulate image generation (replace with actual image generation logic)
  const generateImage = async (traits) => {
    // Placeholder logic for image generation
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");

    canvas.width = 500;
    canvas.height = 500;

    // Draw a simple representation of the traits (for demonstration purposes)
    ctx.fillStyle = "#f0f0f0";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#000";
    ctx.font = "20px Arial";
    ctx.fillText("Robotos NFT", 20, 50);

    let yOffset = 100;
    for (const [traitCategory, traitValue] of Object.entries(traits)) {
      ctx.fillText(`${traitCategory}: ${traitValue}`, 20, yOffset);
      yOffset += 30;
    }

    // Return the image data as a Base64 string
    return canvas.toDataURL("image/png");
  };

  try {
    const imageData = await generateImage(selectedTraits);
    return imageData; // Base64 encoded image data
  } catch (error) {
    throw new Error(`Failed to generate NFT image: ${error.message}`);
  }
}

// Example usage
const traits = {
  background: ["blue", "red", "green"],
  body: ["robot", "alien", "human"],
  eyes: ["round", "square", "triangle"],
};

const rarity = {
  background: { blue: 50, red: 30, green: 20 },
  body: { robot: 40, alien: 40, human: 20 },
  eyes: { round: 60, square: 30, triangle: 10 },
};

generateRobotosNFT(traits, rarity)
  .then((imageData) => {
    console.log("Generated NFT Image Data:", imageData);
  })
  .catch((error) => {
    console.error("Error:", error.message);
  });
```
