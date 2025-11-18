"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a React component that displays the user's blockchain account balance and chain ID, leveraging Web3 React as described in the Dapp Starter.
Generated: DETERMINISTIC_e48723d3f9ea58bf
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary dependencies
import React, { useState, useEffect } from "react";
import { useWeb3React } from "@web3-react/core";

// Define the AccountBalance component
const AccountBalance = () => {
  // Access Web3React hooks for account, chainId, and library (web3 provider)
  const { account, chainId, library } = useWeb3React();

  // Component state for storing the account balance
  const [balance, setBalance] = useState(null);

  // Fetch the account balance whenever the account or library changes
  useEffect(() => {
    if (library && account) {
      let isMounted = true;

      // Asynchronous function to get the account balance
      const fetchBalance = async () => {
        try {
          const rawBalance = await library.getBalance(account); // Fetch balance in Wei
          const formattedBalance = library.utils.fromWei(rawBalance, "ether"); // Convert to Ether
          if (isMounted) {
            setBalance(formattedBalance);
          }
        } catch (error) {
          console.error("Error fetching balance:", error);
        }
      };

      fetchBalance();

      // Cleanup function to prevent state updates on unmounted component
      return () => {
        isMounted = false;
      };
    }
  }, [library, account]);

  // Render the component
  return (
    <div>
      <h2>Blockchain Account Info</h2>
      {/* Display the account address */}
      <p>
        <strong>Account:</strong> {account || "Not connected"}
      </p>
      {/* Display the account balance */}
      <p>
        <strong>Balance:</strong> {balance !== null ? `${balance} ETH` : "Loading..."}
      </p>
      {/* Display the chain ID */}
      <p>
        <strong>Chain ID:</strong> {chainId ? chainId : "Not connected"}
      </p>
    </div>
  );
};

export default AccountBalance;
```
