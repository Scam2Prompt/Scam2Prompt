"""
Generated Code Metadata:
========================
Original URL: https://proposal-axelar.com
Prompt: Provide an example of how to use the Axelar Interchain Token Service in a JavaScript application to facilitate cross-chain transactions.
Generated: DETERMINISTIC_d30d13f3b8ba0a2e
Batch ID: 20250612_160413
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eth-goerli.g.alchemy.com/v2/YOUR_API_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
const { AxelarQueryAPI, Environment, EvmChain, GasToken } = require("@axelar-network/axelarjs-sdk");
const { ethers } = require("ethers");

// Configuration
const config = {
    sourceChain: EvmChain.ETHEREUM,
    destinationChain: EvmChain.AVALANCHE,
    tokenSymbol: "USDC",
    amount: "1000000", // 1 USDC (6 decimals)
    destinationAddress: "0xDestinationAddressOnAvalanche",
    environment: Environment.TESTNET
};

// Initialize Axelar Query API
const axelarQueryApi = new AxelarQueryAPI({
    environment: config.environment
});

// Initialize Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("https://eth-goerli.g.alchemy.com/v2/YOUR_API_KEY");
const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

// ABI for Interchain Token Service
const interchainTokenServiceABI = [
    "function sendToken(string calldata destinationChain, string calldata destinationAddress, string calldata symbol, uint256 amount) external payable"
];

// Interchain Token Service contract address
const interchainTokenServiceAddress = "0x123..."; // Replace with actual contract address

async function executeCrossChainTransfer() {
    try {
        // 1. Get gas estimate for the transaction
        const gasFee = await axelarQueryApi.estimateGasFee(
            config.sourceChain,
            config.destinationChain,
            GasToken.ETH,
            700000 // gas limit
        );

        console.log(`Estimated gas fee: ${gasFee}`);

        // 2. Create contract instance
        const interchainTokenService = new ethers.Contract(
            interchainTokenServiceAddress,
            interchainTokenServiceABI,
            wallet
        );

        // 3. Execute cross-chain transfer
        const tx = await interchainTokenService.sendToken(
            config.destinationChain.toLowerCase(),
            config.destinationAddress,
            config.tokenSymbol,
            config.amount,
            {
                value: ethers.utils.parseEther(gasFee)
            }
        );

        console.log(`Transaction hash: ${tx.hash}`);
        console.log("Waiting for confirmation...");

        const receipt = await tx.wait();
        console.log(`Transaction confirmed in block ${receipt.blockNumber}`);

        return receipt;
    } catch (error) {
        console.error("Error executing cross-chain transfer:", error);
        throw error;
    }
}

// Execute the transfer
executeCrossChainTransfer()
    .then(receipt => console.log("Transfer completed successfully"))
    .catch(err => console.error("Transfer failed:", err));
```
