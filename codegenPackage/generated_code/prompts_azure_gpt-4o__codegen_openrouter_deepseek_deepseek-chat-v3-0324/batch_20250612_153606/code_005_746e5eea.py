"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Provide code examples for displaying NFT ownership data on a Starknet-powered decentralized application using Starknet-React.
Generated: DETERMINISTIC_746e5eea55ceb4c7
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary libraries and types
import { useStarknet, useStarknetCall } from '@starknet-react/core';
import { Contract } from 'starknet';
import { Abi } from 'starknet';
import { useState, useEffect } from 'react';

// NFT Contract ABI (simplified example)
const NFT_ABI: Abi = [
  {
    "name": "balanceOf",
    "type": "function",
    "inputs": [
      { "name": "owner", "type": "felt" }
    ],
    "outputs": [
      { "name": "balance", "type": "felt" }
    ],
    "stateMutability": "view"
  },
  {
    "name": "tokenOfOwnerByIndex",
    "type": "function",
    "inputs": [
      { "name": "owner", "type": "felt" },
      { "name": "index", "type": "felt" }
    ],
    "outputs": [
      { "name": "tokenId", "type": "felt" }
    ],
    "stateMutability": "view"
  }
];

// NFT Contract Address
const NFT_CONTRACT_ADDRESS = '0x123...'; // Replace with actual contract address

// Component to display NFT ownership
export function NFTOwnership() {
  const { account } = useStarknet();
  const [nftContract, setNftContract] = useState<Contract | null>(null);
  const [ownedTokens, setOwnedTokens] = useState<bigint[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Initialize contract
  useEffect(() => {
    if (account) {
      try {
        const contract = new Contract(NFT_ABI, NFT_CONTRACT_ADDRESS, account);
        setNftContract(contract);
      } catch (err) {
        setError('Failed to initialize contract');
        console.error(err);
      }
    }
  }, [account]);

  // Fetch balance and tokens
  const { data: balanceData } = useStarknetCall({
    contract: nftContract,
    method: 'balanceOf',
    args: account ? [account] : undefined,
  });

  // Fetch owned tokens when balance changes
  useEffect(() => {
    const fetchOwnedTokens = async () => {
      if (!nftContract || !account || !balanceData) return;
      
      try {
        setLoading(true);
        const balance = Number(balanceData[0]);
        const tokens: bigint[] = [];

        for (let i = 0; i < balance; i++) {
          const { tokenId } = await nftContract.tokenOfOwnerByIndex(account, i);
          tokens.push(tokenId);
        }

        setOwnedTokens(tokens);
      } catch (err) {
        setError('Failed to fetch owned tokens');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchOwnedTokens();
  }, [nftContract, account, balanceData]);

  if (!account) {
    return <div>Please connect your wallet</div>;
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Your NFTs</h2>
      {balanceData && (
        <p>Total owned: {Number(balanceData[0])}</p>
      )}
      <div>
        {ownedTokens.length > 0 ? (
          <ul>
            {ownedTokens.map((tokenId, index) => (
              <li key={index}>Token ID: {tokenId.toString()}</li>
            ))}
          </ul>
        ) : (
          <p>No NFTs found</p>
        )}
      </div>
    </div>
  );
}
```
