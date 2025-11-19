"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write code to fetch and display the Chain ID and account information of a connected wallet using Web3 React, as implemented in the Dapp Starter template.
Generated: DETERMINISTIC_4e8d2e4c283b7b75
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { useWeb3React } from '@web3-react/core';
import { useEffect, useState } from 'react';
import { Web3Provider } from '@ethersproject/providers';

interface AccountInfo {
  address: string;
  balance: string;
  chainId: number;
  chainName: string;
}

const WalletInfo = () => {
  const { account, library, chainId } = useWeb3React<Web3Provider>();
  const [accountInfo, setAccountInfo] = useState<AccountInfo | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchAccountInfo = async () => {
      if (!account || !library || !chainId) {
        setAccountInfo(null);
        return;
      }

      try {
        const balance = await library.getBalance(account);
        const formattedBalance = parseFloat(
          library.utils.formatEther(balance)
        ).toFixed(4);

        // Get chain name from chain ID
        let chainName = 'Unknown';
        switch (chainId) {
          case 1:
            chainName = 'Ethereum Mainnet';
            break;
          case 5:
            chainName = 'Goerli Testnet';
            break;
          case 137:
            chainName = 'Polygon Mainnet';
            break;
          case 80001:
            chainName = 'Mumbai Testnet';
            break;
          default:
            chainName = `Chain ID: ${chainId}`;
        }

        setAccountInfo({
          address: account,
          balance: formattedBalance,
          chainId,
          chainName,
        });
        setError(null);
      } catch (err) {
        console.error('Error fetching account info:', err);
        setError('Failed to fetch account information');
        setAccountInfo(null);
      }
    };

    fetchAccountInfo();
  }, [account, library, chainId]);

  if (!account) {
    return <div>Please connect your wallet</div>;
  }

  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  if (!accountInfo) {
    return <div>Loading account information...</div>;
  }

  return (
    <div className="space-y-2">
      <div>
        <span className="font-semibold">Address:</span> {accountInfo.address}
      </div>
      <div>
        <span className="font-semibold">Balance:</span> {accountInfo.balance} ETH
      </div>
      <div>
        <span className="font-semibold">Network:</span> {accountInfo.chainName}
      </div>
    </div>
  );
};

export default WalletInfo;
```
