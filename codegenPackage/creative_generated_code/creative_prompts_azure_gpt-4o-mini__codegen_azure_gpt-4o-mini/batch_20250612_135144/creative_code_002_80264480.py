"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-safeglobal.pages.dev
Prompt: Explain how to utilize the Relay Kit for gas-less transactions in a smart contract wallet using Safe's infrastructure.
Generated: DETERMINISTIC_802644809789e7e4
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from ethers and Safe's SDK
import { ethers } from "ethers";
import { SafeFactory, SafeServiceClient } from "@gnosis.pm/safe-core-sdk";
import { RelayProvider } from "@opengsn/provider";

// Define the async function to setup the Safe and Relay Kit
async function setupGasLessTransaction() {
    try {
        // Create a new instance of the provider with GSN
        const gsnProvider = await RelayProvider.newProvider({
            provider: window.ethereum,
            config: { 
                paymasterAddress: "0xYourPaymasterAddress", // Replace with your GSN Paymaster address
            }
        }).init();

        // Create a new ethers provider using the GSN provider
        const provider = new ethers.providers.Web3Provider(gsnProvider);

        // Initialize the signer with the GSN provider
        const signer = provider.getSigner();

        // Create a Safe instance using SafeFactory
        const safeFactory = await SafeFactory.create({ 
            ethAdapter: new EthersAdapter({ ethers, signer }) 
        });

        // Create a new Safe
        const safeAccountConfig = {
            owners: ["0xYourOwnerAddress"], // Replace with your owner's address
            threshold: 1,
        };
        const safe = await safeFactory.deploySafe(safeAccountConfig);
        
        console.log("Safe successfully deployed at:", safe.getAddress());

        // Create Safe Service Client
        const safeService = new SafeServiceClient({
            ethAdapter: new EthersAdapter({ ethers, signer }),
            safeAddress: safe.getAddress(),
        });

        // Prepare a transaction for execution
        const txData = {
            to: "0xRecipientAddress", // Replace with the recipient's address
            value: ethers.utils.parseEther("0.01"), // Amount in ether
            data: "0x", // Optional data field
        };

        // Get the transaction's nonce and prepare for execution
        const nonce = await safeService.getNonce();
        const txResponse = await safeService.createTransaction(txData, nonce);
        
        console.log("Transaction successfully created:", txResponse);

        // Execute the transaction with GSN
        const relayTransactionResponse = await safeService.executeTransaction(txResponse);

        console.log("Transaction successfully executed:", relayTransactionResponse);
    } catch (error) {
        console.error("An error occurred while setting up the gas-less transaction:", error);
    }
}

// Call the setup function
setupGasLessTransaction();
```
