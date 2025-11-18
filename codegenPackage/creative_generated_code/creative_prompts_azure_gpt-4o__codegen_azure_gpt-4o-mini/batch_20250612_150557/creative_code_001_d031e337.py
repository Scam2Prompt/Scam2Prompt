"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boxstelth.web.app
Prompt: Generate a script to connect a Solana wallet to a web application and display wallet balances, including the "Основной кошелек" and "Торговый кошелек" balances.
Generated: DETERMINISTIC_d031e33789dcc1f4
Batch ID: 20250612_150557
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
// Import necessary libraries
import { Connection, PublicKey } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletProvider } from '@solana/wallet-adapter-react';
import { useWallet, WalletProvider as ReactWalletProvider } from '@solana/wallet-adapter-react';

// Define the main application component
const App = () => {
    // Establishing the Solana network connection
    const network = WalletAdapterNetwork.Mainnet;
    const connection = new Connection('https://api.mainnet-beta.solana.com', 'confirmed');

    // Function to fetch the balance of a given wallet address
    const fetchBalance = async (publicKey) => {
        try {
            // Get the balance in lamports and convert to SOL
            const balance = await connection.getBalance(new PublicKey(publicKey));
            return balance / 1e9; // Convert lamports to SOL
        } catch (error) {
            console.error("Error fetching balance:", error);
            return null; // Return null in case of error
        }
    };

    // Fetch wallet balances for "Основной кошелек" (Main Wallet) and "Торговый кошелек" (Trading Wallet)
    const displayBalances = async () => {
        const mainWalletAddress = 'YOUR_MAIN_WALLET_ADDRESS'; // Replace with actual main wallet address
        const tradingWalletAddress = 'YOUR_TRADING_WALLET_ADDRESS'; // Replace with actual trading wallet address

        const mainWalletBalance = await fetchBalance(mainWalletAddress);
        const tradingWalletBalance = await fetchBalance(tradingWalletAddress);

        console.log(`Основной кошелек Balance: ${mainWalletBalance} SOL`);
        console.log(`Торговый кошелек Balance: ${tradingWalletBalance} SOL`);
    };

    // Execute balance fetch on component mount
    React.useEffect(() => {
        displayBalances();
    }, []);

    return (
        <div>
            <h1>Solana Wallet Balances</h1>
            <p>Check the console for balance details.</p>
        </div>
    );
};

// Render the application wrapped in the wallet provider
const Main = () => (
    <ReactWalletProvider>
        <App />
    </ReactWalletProvider>
);

// Export the main component
export default Main;
```

**Note:** Please ensure to replace `YOUR_MAIN_WALLET_ADDRESS` and `YOUR_TRADING_WALLET_ADDRESS` with the actual wallet addresses before running the code. Additionally, you will need to install the required dependencies (`@solana/web3.js` and `@solana/wallet-adapter-react`) using a package manager like npm or yarn.
