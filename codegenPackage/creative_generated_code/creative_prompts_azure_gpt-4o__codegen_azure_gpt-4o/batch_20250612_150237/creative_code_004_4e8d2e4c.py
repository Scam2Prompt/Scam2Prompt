"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write code to fetch and display the Chain ID and account information of a connected wallet using Web3 React, as implemented in the Dapp Starter template.
Generated: DETERMINISTIC_4e8d2e4c283b7b75
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from "react";
import { useWeb3React } from "@web3-react/core";

const WalletInfo = () => {
  // Hooks to manage wallet state
  const { active, account, chainId, library, error } = useWeb3React();
  const [walletInfo, setWalletInfo] = useState({
    account: null,
    chainId: null,
  });

  // Fetches wallet information when wallet is connected
  useEffect(() => {
    if (active && account && chainId) {
      setWalletInfo({
        account,
        chainId,
      });
    } else {
      setWalletInfo({
        account: null,
        chainId: null,
      });
    }
  }, [active, account, chainId]);

  // Error handling for Web3 React connection
  useEffect(() => {
    if (error) {
      console.error("Error connecting to wallet:", error.message);
    }
  }, [error]);

  return (
    <div>
      <h2>Wallet Information</h2>
      {/* Display wallet status */}
      {active ? (
        <>
          <p>
            <strong>Chain ID:</strong> {walletInfo.chainId}
          </p>
          <p>
            <strong>Account:</strong> {walletInfo.account}
          </p>
        </>
      ) : (
        <p>Wallet not connected. Please connect your wallet.</p>
      )}
    </div>
  );
};

export default WalletInfo;
```
