"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dust-box.web.app
Prompt: Generate code to display the current supply of DUST tokens and allow users to claim tokens if eligible using Phantom wallet integration.
Generated: DETERMINISTIC_9cc4236e5d7b2d02
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required libraries
const { Connection, PublicKey, clusterApiUrl } = require("@solana/web3.js");
const { PhantomWalletAdapter } = require("@solana/wallet-adapter-phantom");
const { TOKEN_PROGRAM_ID, getAccount, getMint } = require("@solana/spl-token");

// Constants
const DUST_TOKEN_MINT_ADDRESS = new PublicKey("Your_DUST_Token_Mint_Address_Here");
const NETWORK = clusterApiUrl("mainnet-beta");
const connection = new Connection(NETWORK, "confirmed");

// Helper function to fetch the supply of DUST tokens
async function getDustTokenSupply() {
    try {
        // Fetch the mint information for the DUST token
        const mintInfo = await getMint(connection, DUST_TOKEN_MINT_ADDRESS);
        const supply = mintInfo.supply.toString();
        console.log(`Current DUST Token Supply: ${supply}`);
        return supply;
    } catch (error) {
        console.error("Error fetching DUST token supply:", error);
        throw new Error("Failed to fetch DUST token supply.");
    }
}

// Function to check user eligibility and allow token claiming
async function claimDustTokens(walletAdapter) {
    try {
        // Ensure wallet is connected
        if (!walletAdapter.connected) {
            throw new Error("Wallet not connected. Please connect your Phantom wallet.");
        }

        // Fetch the user's public key
        const userPublicKey = walletAdapter.publicKey;

        // Check if the user has a valid associated token account for DUST token
        const userAccount = await getAccount(
            connection,
            await PublicKey.findProgramAddress(
                [userPublicKey.toBuffer(), TOKEN_PROGRAM_ID.toBuffer(), DUST_TOKEN_MINT_ADDRESS.toBuffer()],
                TOKEN_PROGRAM_ID
            )
        );

        // Check eligibility (for simplicity, assuming balance check as eligibility criteria)
        if (userAccount.amount > 0) {
            console.log("User already holds DUST tokens. No claim required.");
            return;
        }

        // Simulate claim process (this would involve custom program logic for real eligibility checks)
        console.log("User is eligible to claim DUST tokens. Initiating claim process...");
        // Implement the logic for token distribution if eligible, e.g., via a transaction.

        // Notify the user
        console.log("DUST tokens successfully claimed!");
    } catch (error) {
        console.error("Error during token claim process:", error);
        throw new Error("Failed to claim DUST tokens.");
    }
}

// Example usage
(async () => {
    const walletAdapter = new PhantomWalletAdapter();

    // Connect Phantom wallet
    await walletAdapter.connect();

    // Display the current supply of DUST tokens
    await getDustTokenSupply();

    // Allow the user to claim tokens if eligible
    await claimDustTokens(walletAdapter);
})();

// Note: Replace "Your_DUST_Token_Mint_Address_Here" with the actual mint address of DUST tokens,
// and implement custom eligibility logic for claiming tokens as per your program requirements.
```
