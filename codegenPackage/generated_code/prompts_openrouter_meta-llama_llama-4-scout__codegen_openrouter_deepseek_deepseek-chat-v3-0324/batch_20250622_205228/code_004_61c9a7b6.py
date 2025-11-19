"""
Generated Code Metadata:
========================
Original URL: https://solana-mixer.to
Prompt: Design a simple user interface for a Solana Mixer service that allows users to input their SOL address and choose a pool exit time between 0 and 50 hours.
Generated: DETERMINISTIC_61c9a7b6052c2b72
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useState } from 'react';
import { PublicKey } from '@solana/web3.js';

interface MixerFormProps {
  onSubmit: (solAddress: string, exitTime: number) => void;
}

const SolanaMixerUI: React.FC<MixerFormProps> = ({ onSubmit }) => {
  const [solAddress, setSolAddress] = useState<string>('');
  const [exitTime, setExitTime] = useState<number>(24);
  const [error, setError] = useState<string>('');

  const validateSolAddress = (address: string): boolean => {
    try {
      new PublicKey(address);
      return true;
    } catch (err) {
      return false;
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (!solAddress) {
      setError('Please enter a Solana address');
      return;
    }

    if (!validateSolAddress(solAddress)) {
      setError('Invalid Solana address');
      return;
    }

    if (exitTime < 0 || exitTime > 50) {
      setError('Exit time must be between 0 and 50 hours');
      return;
    }

    onSubmit(solAddress, exitTime);
  };

  return (
    <div className="max-w-md mx-auto p-6 bg-gray-800 rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold text-white mb-4">Solana Mixer</h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="solAddress" className="block text-sm font-medium text-gray-300">
            Solana Address
          </label>
          <input
            type="text"
            id="solAddress"
            value={solAddress}
            onChange={(e) => setSolAddress(e.target.value)}
            className="mt-1 block w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            placeholder="Enter your Solana address"
          />
        </div>

        <div>
          <label htmlFor="exitTime" className="block text-sm font-medium text-gray-300">
            Pool Exit Time (hours)
          </label>
          <input
            type="number"
            id="exitTime"
            min="0"
            max="50"
            value={exitTime}
            onChange={(e) => setExitTime(Number(e.target.value))}
            className="mt-1 block w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
          />
          <p className="mt-1 text-xs text-gray-400">Choose between 0 and 50 hours</p>
        </div>

        {error && (
          <div className="p-2 text-sm text-red-400 bg-red-900 rounded">
            {error}
          </div>
        )}

        <button
          type="submit"
          className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default SolanaMixerUI;
```
