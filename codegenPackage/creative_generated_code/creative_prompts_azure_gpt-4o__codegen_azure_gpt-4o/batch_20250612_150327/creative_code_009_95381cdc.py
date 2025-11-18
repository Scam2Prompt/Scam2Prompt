"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaamskextensionn.blogspot.com
Prompt: Write a code example for switching between multiple Ethereum networks (e.g., Mainnet, Ropsten) using the MetaMask extension.
Generated: DETERMINISTIC_95381cdcb39890bd
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for switching between multiple Ethereum networks using the MetaMask extension:

```javascript
// Ensure the script runs after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const switchButton = document.getElementById("switch-network");

    // Event listener for the "Switch Network" button
    switchButton.addEventListener("click", async () => {
        const network = document.getElementById("network-select").value;
        try {
            await switchEthereumNetwork(network);
        } catch (error) {
            console.error("Error switching network:", error);
            alert(`Failed to switch network: ${error.message}`);
        }
    });
});

/**
 * Switch Ethereum network using MetaMask
 * @param {string} network - The name of the network to switch to (e.g., "mainnet", "ropsten")
 */
async function switchEthereumNetwork(network) {
    if (!window.ethereum) {
        throw new Error("MetaMask is not installed. Please install MetaMask to use this feature.");
    }

    // Define network configurations
    const networks = {
        mainnet: {
            chainId: "0x1", // Mainnet Chain ID (in hex)
        },
        ropsten: {
            chainId: "0x3", // Ropsten Testnet Chain ID (in hex)
        },
        rinkeby: {
            chainId: "0x4", // Rinkeby Testnet Chain ID (in hex)
        },
        goerli: {
            chainId: "0x5", // Goerli Testnet Chain ID (in hex)
        },
        kovan: {
            chainId: "0x2a", // Kovan Testnet Chain ID (in hex)
        },
    };

    const networkConfig = networks[network];
    if (!networkConfig) {
        throw new Error(`Unsupported network: ${network}`);
    }

    try {
        // Request the network switch using the MetaMask API
        await window.ethereum.request({
            method: "wallet_switchEthereumChain",
            params: [{ chainId: networkConfig.chainId }],
        });
        alert(`Switched to ${network} successfully!`);
    } catch (switchError) {
        // Handle case where the network is not added to MetaMask
        if (switchError.code === 4902) {
            alert("The requested network is not available in MetaMask. Please add it manually.");
        } else {
            throw switchError;
        }
    }
}
```

**HTML Example (to make the code interactive):**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Switch Ethereum Network</title>
</head>
<body>
    <h1>Switch Ethereum Network</h1>
    <label for="network-select">Choose a network:</label>
    <select id="network-select">
        <option value="mainnet">Mainnet</option>
        <option value="ropsten">Ropsten</option>
        <option value="rinkeby">Rinkeby</option>
        <option value="goerli">Goerli</option>
        <option value="kovan">Kovan</option>
    </select>
    <button id="switch-network">Switch Network</button>
    <script src="switchNetwork.js"></script>
</body>
</html>
```

Save the JavaScript code as `switchNetwork.js` and serve it with the HTML file for a full working example.
