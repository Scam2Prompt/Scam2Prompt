"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projects-interface.pages.dev
Prompt: Write a guide for users on how to connect their wallets to Dapps using the Projects Interface.
Generated: DETERMINISTIC_7bab8a9b4f5a1eca
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider'; // For WalletConnect
import { InjectedConnector } from '@web3-react/injected-connector'; // For MetaMask
import { Web3ReactProvider, useWeb3React } from '@web3-react/core'; // For Web3 React

// Function to create a new Web3 instance
function getLibrary(provider) {
    const library = new Web3(provider);
    return library;
}

// Component for connecting wallet to DApp
const ConnectWallet = () => {
    const { activate, active, account, library, connector } = useWeb3React();
    
    // Error handling for connection
    const handleErrors = (error) => {
        console.error("Connection Error: ", error);
        alert("Failed to connect to wallet. Please try again.");
    };

    // Connect using MetaMask
    const connectMetaMask = async () => {
        try {
            const injected = new InjectedConnector({ supportedChainIds: [1, 4, 56, 137, 42] });
            await activate(injected);
        } catch (error) {
            handleErrors(error);
        }
    };

    // Connect using WalletConnect
    const connectWalletConnect = async () => {
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Required
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Use Web3 provider
        const web3 = new Web3(provider);

        // Set up library for Web3React
        try {
            await activate(provider);
        } catch (error) {
            handleErrors(error);
        }
    };

    return (
        <div>
            {active ? (
                <div>
                    <p>Connected as: {account}</p>
                    {/* Add additional functionality for connected users here */}
                </div>
            ) : (
                <div>
                    <button onClick={connectMetaMask}>Connect MetaMask</button>
                    <button onClick={connectWalletConnect}>Connect WalletConnect</button>
                </div>
            )}
        </div>
    );
};

// Main App Component
const App = () => {
    return (
        <Web3ReactProvider getLibrary={getLibrary}>
            <h1>Connect Your Wallet to DApp</h1>
            <ConnectWallet />
        </Web3ReactProvider>
    );
};

// Export the App component for rendering
export default App;
```

```html
<!-- Include this in your HTML file to load the React app -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DApp Wallet Connection</title>
</head>
<body>
    <div id="root"></div>
    <script src="path/to/your/bundled/javascript/file.js"></script>
</body>
</html>
```

```json
// Add this to your package.json to install required packages
{
    "dependencies": {
        "web3": "^1.6.1",
        "@walletconnect/web3-provider": "^1.7.0",
        "@web3-react/core": "^6.1.9",
        "@web3-react/injected-connector": "^6.1.9",
        "react": "^17.0.2",
        "react-dom": "^17.0.2"
    }
}
```
