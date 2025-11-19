"""
Generated Code Metadata:
========================
Original URL: https://make1518999.cc
Prompt: Write JavaScript code to implement a "Stake First Asset" button that automatically selects the first available asset in the user's wallet for staking, following the functionality of the `btngo2` button.
Generated: DETERMINISTIC_336a03d0474b81e3
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to stake the first available asset in the user's wallet
async function stakeFirstAsset() {
    try {
        // Fetch the user's wallet assets
        const assets = await getUserWalletAssets();

        // Check if there are any assets available for staking
        if (assets.length === 0) {
            throw new Error("No assets available for staking.");
        }

        // Select the first available asset
        const firstAsset = assets[0];

        // Confirm the staking action with the user
        const userConfirmed = confirm(`Do you want to stake ${firstAsset.amount} of ${firstAsset.name}?`);
        if (!userConfirmed) {
            console.log("Staking action was cancelled by the user.");
            return;
        }

        // Call the staking function with the selected asset
        const stakingResult = await stakeAsset(firstAsset);
        
        // Check the result of the staking operation
        if (stakingResult.success) {
            console.log(`Successfully staked ${firstAsset.amount} of ${firstAsset.name}.`);
        } else {
            throw new Error(`Staking failed: ${stakingResult.message}`);
        }
    } catch (error) {
        // Handle errors gracefully
        console.error("An error occurred while staking the asset:", error.message);
        alert(`Error: ${error.message}`);
    }
}

// Mock function to simulate fetching user's wallet assets
async function getUserWalletAssets() {
    // Simulated response from a wallet API
    return [
        { name: "Asset A", amount: 100 },
        { name: "Asset B", amount: 50 }
    ];
}

// Mock function to simulate staking an asset
async function stakeAsset(asset) {
    // Simulated staking operation
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ success: true });
        }, 1000);
    });
}

// Event listener for the "Stake First Asset" button
document.getElementById("stakeFirstAssetButton").addEventListener("click", stakeFirstAsset);
```

Make sure to replace the mock functions `getUserWalletAssets` and `stakeAsset` with actual implementations that interact with your wallet and staking services.
