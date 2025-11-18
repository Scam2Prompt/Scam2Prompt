"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Write code to implement multi-wallet switching functionality using the MetaMask wallet API, as described in the "MetaMask多前钱包" section.
Generated: DETERMINISTIC_f50b0a8d7f3d27d3
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Multi-wallet switching functionality using MetaMask wallet API
 * Assumptions:
 * - The user has MetaMask installed and set up.
 * - Switching functionality is limited to Ethereum-based wallets.
 * 
 * Requirements:
 * - Allow users to switch between multiple wallets stored locally.
 * - Ensure correct error handling and seamless integration with MetaMask.
 * - Use best programming practices and provide clean code.
 */

// Check if the MetaMask extension is installed
if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install MetaMask to use this functionality.");
    alert("MetaMask is required! Please install MetaMask.");
    throw new Error("MetaMask not detected");
}

/**
 * A list of wallets (addresses) the user can switch between.
 * In a real-world scenario, this would be dynamically fetched or managed securely.
 */
const wallets = [
    "0x1234567890abcdef1234567890abcdef12345678", // Wallet 1
    "0xabcdef1234567890abcdef1234567890abcdef12", // Wallet 2
    "0x7890abcdef1234567890abcdef1234567890abcd"  // Wallet 3
];

/**
 * Switches the currently active wallet in MetaMask.
 * @param {string} walletAddress - The wallet address to switch to.
 * @returns {Promise<void>}
 */
async function switchWallet(walletAddress) {
    try {
        // Validate the walletAddress format
        if (!/^0x[a-fA-F0-9]{40}$/.test(walletAddress)) {
            throw new Error("Invalid wallet address format.");
        }

        // Request MetaMask to switch accounts
        const accounts = await window.ethereum.request({
            method: 'wallet_requestPermissions',
            params: [
                {
                    eth_accounts: { addresses: [walletAddress] }
                }
            ]
        });

        console.log("Switched to wallet:", accounts[0]); // Log the active wallet
    } catch (error) {
        console.error("Error switching wallet:", error.message);
        alert(`Failed to switch wallet: ${error.message}`);
    }
}

/**
 * Displays the list of wallets and allows switching using user input.
 * This is a simple interface for demonstration purposes.
 */
function initWalletSwitcher() {
    const walletList = document.getElementById("walletList");
    const switchButton = document.getElementById("switchWalletButton");

    // Populate the wallet list dropdown
    wallets.forEach((wallet) => {
        const option = document.createElement("option");
        option.value = wallet;
        option.textContent = wallet;
        walletList.appendChild(option);
    });

    // Add event listener for wallet switching
    switchButton.addEventListener("click", async () => {
        const selectedWallet = walletList.value;
        await switchWallet(selectedWallet);
    });
}

// DOM elements for the wallet switcher UI
document.body.innerHTML = `
    <div>
        <h1>MetaMask Multi-Wallet Switcher</h1>
        <select id="walletList"></select>
        <button id="switchWalletButton">Switch Wallet</button>
    </div>
`;

// Initialize the wallet switcher UI
initWalletSwitcher();
```
