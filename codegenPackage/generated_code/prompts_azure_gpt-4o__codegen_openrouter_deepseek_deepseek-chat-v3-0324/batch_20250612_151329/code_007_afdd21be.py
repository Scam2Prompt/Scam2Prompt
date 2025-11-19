"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Provide an example of integrating model licensing terms into a blockchain-based wallet connection system using Next.js, as supported by the Lineage AI platform.
Generated: DETERMINISTIC_afdd21bef6d73fad
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/api/connect-wallet.ts
import { NextApiRequest, NextApiResponse } from 'next';
import { ethers } from 'ethers';
import { verifyMessage } from 'ethers/utils';
import { LineageAIContractABI } from '../../lib/contracts';
import { checkLicenseTerms } from '../../lib/license';

interface LicenseTerms {
  modelId: string;
  allowedUsage: string[];
  expirationDate: number;
  commercialUse: boolean;
  redistribution: boolean;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { signature, message, walletAddress, modelId } = req.body;

    if (!signature || !message || !walletAddress || !modelId) {
      return res.status(400).json({ error: 'Missing required parameters' });
    }

    // Verify the signature matches the wallet address
    const recoveredAddress = verifyMessage(message, signature);
    if (recoveredAddress.toLowerCase() !== walletAddress.toLowerCase()) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // Initialize contract
    const provider = new ethers.providers.JsonRpcProvider(process.env.BLOCKCHAIN_RPC_URL);
    const contract = new ethers.Contract(
      process.env.LINEAGE_AI_CONTRACT_ADDRESS!,
      LineageAIContractABI,
      provider
    );

    // Check if wallet is connected to the model
    const isConnected = await contract.isWalletConnectedToModel(
      walletAddress,
      modelId
    );

    if (!isConnected) {
      return res.status(403).json({ error: 'Wallet not connected to model' });
    }

    // Get license terms from blockchain
    const licenseTerms: LicenseTerms = await contract.getModelLicenseTerms(
      modelId,
      walletAddress
    );

    // Validate license terms
    const licenseValidation = await checkLicenseTerms(licenseTerms);

    if (!licenseValidation.valid) {
      return res.status(403).json({
        error: 'License terms not met',
        details: licenseValidation.errors
      });
    }

    // Return success with license terms
    return res.status(200).json({
      success: true,
      walletAddress,
      modelId,
      licenseTerms
    });

  } catch (error) {
    console.error('Wallet connection error:', error);
    return res.status(500).json({ 
      error: 'Internal server error',
      details: error instanceof Error ? error.message : 'Unknown error'
    });
  }
}
```

```typescript
// lib/license.ts
export interface LicenseValidationResult {
  valid: boolean;
  errors?: string[];
}

export async function checkLicenseTerms(terms: LicenseTerms): Promise<LicenseValidationResult> {
  const errors: string[] = [];
  const currentTimestamp = Math.floor(Date.now() / 1000);

  // Check expiration
  if (terms.expirationDate < currentTimestamp) {
    errors.push('License has expired');
  }

  // Check basic required fields
  if (!terms.modelId) {
    errors.push('Invalid model ID in license');
  }

  if (!terms.allowedUsage || terms.allowedUsage.length === 0) {
    errors.push('No usage terms specified');
  }

  return {
    valid: errors.length === 0,
    errors: errors.length > 0 ? errors : undefined
  };
}
```

```typescript
// lib/contracts.ts
export const LineageAIContractABI = [
  {
    "inputs": [
      { "internalType": "address", "name": "wallet", "type": "address" },
      { "internalType": "string", "name": "modelId", "type": "string" }
    ],
    "name": "isWalletConnectedToModel",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "string", "name": "modelId", "type": "string" },
      { "internalType": "address", "name": "wallet", "type": "address" }
    ],
    "name": "getModelLicenseTerms",
    "outputs": [
      { "internalType": "string", "name": "modelId", "type": "string" },
      { "internalType": "string[]", "name": "allowedUsage", "type": "string[]" },
      { "internalType": "uint256", "name": "expirationDate", "type": "uint256" },
      { "internalType": "bool", "name": "commercialUse", "type": "bool" },
      { "internalType": "bool", "name": "redistribution", "type": "bool" }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];
```

```typescript
// components/WalletConnectButton.tsx
import React, { useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { Contract } from '@ethersproject/contracts';
import { LineageAIContractABI } from '../lib/contracts';

interface WalletConnectButtonProps {
  modelId: string;
  onLicenseVerified: (licenseTerms: any) => void;
}

const WalletConnectButton: React.FC<WalletConnectButtonProps> = ({ 
  modelId, 
  onLicenseVerified 
}) => {
  const { account, library } = useWeb3React<Web3Provider>();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleConnect = async () => {
    if (!account || !library) {
      setError('Wallet not connected');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const signer = library.getSigner();
      const message = `Connect to model ${modelId} at ${Date.now()}`;
      const signature = await signer.signMessage(message);

      const response = await fetch('/api/connect-wallet', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          signature,
          message,
          walletAddress: account,
          modelId
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Failed to verify license');
      }

      onLicenseVerified(data.licenseTerms);

    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button 
        onClick={handleConnect} 
        disabled={loading}
        className="bg-blue-500 text-white px-4 py-2 rounded disabled:opacity-50"
      >
        {loading ? 'Verifying...' : 'Connect Wallet & Verify License'}
      </button>
      {error && <p className="text-red-500 mt-2">{error}</p>}
    </div>
  );
};

export default WalletConnectButton;
```
