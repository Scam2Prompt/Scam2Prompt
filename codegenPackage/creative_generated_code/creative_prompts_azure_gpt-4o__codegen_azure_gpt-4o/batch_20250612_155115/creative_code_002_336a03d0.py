"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://make1518999.cc
Prompt: Write JavaScript code to implement a "Stake First Asset" button that automatically selects the first available asset in the user's wallet for staking, following the functionality of the `btngo2` button.
Generated: DETERMINISTIC_336a03d0474b81e3
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to implement "Stake First Asset" functionality
document.addEventListener("DOMContentLoaded", () => {
  // Event listener for "Stake First Asset" button
  const stakeFirstAssetButton = document.getElementById("stake-first-asset");
  
  stakeFirstAssetButton.addEventListener("click", () => {
    try {
      // Simulated wallet object
      const wallet = {
        assets: [
          { id: 1, name: "Asset A", stakable: true },
          { id: 2, name: "Asset B", stakable: false },
          { id: 3, name: "Asset C", stakable: true }
        ]
      };

      // Select the first stakable asset
      const stakableAsset = wallet.assets.find(asset => asset.stakable);

      if (!stakableAsset) {
        alert("No stakable assets available in the wallet.");
        return;
      }

      // Trigger staking functionality (simulate btngo2 behavior)
      stakeAsset(stakableAsset);

    } catch (error) {
      console.error("An error occurred while staking the asset:", error);
      alert("Failed to stake the asset. Please try again later.");
    }
  });

  /**
   * Simulated staking function
   * @param {Object} asset - The asset to be staked
   */
  function stakeAsset(asset) {
    // Simulate staking process
    console.log(`Staking asset: ${asset.name} (ID: ${asset.id})`);
    alert(`Asset "${asset.name}" has been successfully staked!`);
  }
});
```

```html
<!-- HTML for the Stake First Asset button -->
<button id="stake-first-asset">Stake First Asset</button>
```
