"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a code snippet to detect the connected blockchain chain ID and display it in a Next.js application, using the tools mentioned in the Dapp Starter.
Generated: DETERMINISTIC_8c13a544a27ae4c9
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary libraries and types
import { useEffect, useState } from 'react';
import { useNetwork } from 'wagmi';
import { NextPage } from 'next';

const ChainIdDetector: NextPage = () => {
  const { chain } = useNetwork();
  const [chainId, setChainId] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    try {
      if (chain) {
        setChainId(chain.id);
        setError(null);
      } else {
        setError('No chain detected. Please connect your wallet.');
      }
    } catch (err) {
      setError('Failed to detect chain ID');
      console.error('Error detecting chain ID:', err);
    }
  }, [chain]);

  return (
    <div className="p-4 border rounded-lg shadow-sm">
      <h2 className="text-lg font-semibold mb-2">Connected Chain Information</h2>
      {error ? (
        <p className="text-red-500">{error}</p>
      ) : chainId ? (
        <div>
          <p className="text-gray-700">
            <span className="font-medium">Chain ID:</span> {chainId}
          </p>
          <p className="text-gray-700">
            <span className="font-medium">Chain Name:</span> {chain?.name || 'Unknown'}
          </p>
        </div>
      ) : (
        <p className="text-gray-500">Loading chain information...</p>
      )}
    </div>
  );
};

export default ChainIdDetector;
```
