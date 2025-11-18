"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gnosis-safe.io
Prompt: Write a code example to integrate Safe Smart Accounts with third-party apps using out-of-the-box integrations from the Safe{CORE} SDK.
Generated: DETERMINISTIC_e7310073ac151a50
Batch ID: 20250612_151232
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.ankr.com/eth": {
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
// Import necessary modules from the Safe{CORE} SDK
import { SafeAuthKit, SafeAuthProviderType } from '@safe-global/auth-kit';
import { SafeFactory } from '@safe-global/safe-core-sdk';
import { ethers } from 'ethers';

(async () => {
  try {
    // === STEP 1: Initialize Authentication ===
    const safeAuthKit = SafeAuthKit.init(SafeAuthProviderType.Web3Auth, {
      rpcTarget: 'https://rpc.ankr.com/eth', // Ethereum RPC endpoint
      chainId: 1, // Ethereum Mainnet chain ID
      clientId: 'YOUR_WEB3AUTH_CLIENT_ID', // Replace with your Web3Auth client ID
      network: 'mainnet', // Use 'testnet' for testing purposes
    });

    // Trigger the authentication process
    const authResult = await safeAuthKit.signIn();
    console.log('User signed in:', authResult);

    // Create a web3 provider using the authenticated user
    const web3Provider = new ethers.providers.Web3Provider(safeAuthKit.getProvider());
    const signer = web3Provider.getSigner();

    // === STEP 2: Initialize Safe Core SDK ===
    const safeFactory = await SafeFactory.create({ ethAdapter: new ethers.providers.Web3Provider(web3Provider) });

    // === STEP 3: Create Safe Smart Account ===
    const safeAccount = await safeFactory.deploySafe({
      owners: [await signer.getAddress()], // Add the address obtained from the signer
      threshold: 1, // Minimum number of signatures required
    });

    console.log('Safe Account created with address:', safeAccount.getAddress());

    // === STEP 4: Integrate with Third-party Apps ===
    // Example Integration: Sending a transaction
    const recipientAddress = '0xRecipientAddressHere'; // Replace with actual recipient address
    const transactionData = {
      to: recipientAddress,
      value: ethers.utils.parseEther('0.01'), // Sending 0.01 ETH
      data: '0x', // Empty data for a plain ETH transfer
    };

    const safeTransaction = await safeAccount.createTransaction(transactionData);
    console.log('Safe Transaction created:', safeTransaction);

    // Propose the transaction using Safe SDK
    const txResponse = await safeAccount.executeTransaction(safeTransaction);
    console.log('Transaction Response:', txResponse);

    console.log('Transaction executed successfully through Safe Smart Account.');
  } catch (error) {
    // Handle errors appropriately
    console.error('An error occurred:', error.message);
  } finally {
    // Optional cleanup or sign-out
    await safeAuthKit.signOut();
    console.log('User signed out.');
  }
})();
```
