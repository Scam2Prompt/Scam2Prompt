"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a function in TypeScript that retrieves the user's blockchain account details and displays them, referencing the Dapp Starter's integration of Web3 React.
Generated: DETERMINISTIC_a4a22b9d124bc9cb
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';

interface AccountDetails {
  address: string;
  balance: string;
  network: string;
}

const useAccountDetails = () => {
  const [accountDetails, setAccountDetails] = useState<AccountDetails | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchAccountDetails = async () => {
      try {
        // Check if the browser has a Web3 provider (Metamask, etc.)
        if (!window.ethereum) {
          throw new Error('No Ethereum provider found. Install Metamask or another wallet.');
        }

        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Create an instance of ethers provider
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        
        // Get the user's account
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        
        // Get the user's balance
        const balance = await provider.getBalance(address);
        
        // Get the current network
        const network = await provider.getNetwork();

        // Update state with account details
        setAccountDetails({
          address,
          balance: ethers.utils.formatEther(balance), // Convert balance to a readable format
          network: network.name,
        });
      } catch (err) {
        // Set error message in case of failure
        setError(err instanceof Error ? err.message : 'An unknown error occurred');
      }
    };

    fetchAccountDetails();
  }, []);

  return { accountDetails, error };
};

const AccountDisplay: React.FC = () => {
  const { accountDetails, error } = useAccountDetails();

  return (
    <div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {accountDetails ? (
        <div>
          <h2>Your Account Details:</h2>
          <p><strong>Address:</strong> {accountDetails.address}</p>
          <p><strong>Balance:</strong> {accountDetails.balance} ETH</p>
          <p><strong>Network:</strong> {accountDetails.network}</p>
        </div>
      ) : (
        <p>Loading account details...</p>
      )}
    </div>
  );
};

export default AccountDisplay;
```
