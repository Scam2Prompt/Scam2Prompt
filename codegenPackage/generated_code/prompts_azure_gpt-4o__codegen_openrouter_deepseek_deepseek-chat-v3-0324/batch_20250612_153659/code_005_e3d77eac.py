"""
Generated Code Metadata:
========================
Original URL: https://assetdash-staking.vercel.app
Prompt: Write a Next.js API route for retrieving staking data and daily rewards for connected wallets in the AssetDash platform.
Generated: DETERMINISTIC_e3d77eac34328690
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/api/staking/[wallet].ts
import { NextApiRequest, NextApiResponse } from 'next';
import { connectToDatabase } from '../../../lib/db';
import { isValidEthereumAddress } from '../../../lib/utils';

interface StakingData {
  wallet: string;
  totalStaked: number;
  dailyRewards: number;
  lastUpdated: Date;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  // Only allow GET requests
  if (req.method !== 'GET') {
    res.setHeader('Allow', ['GET']);
    return res.status(405).json({ message: 'Method not allowed' });
  }

  const { wallet } = req.query;

  // Validate wallet address
  if (!wallet || typeof wallet !== 'string' || !isValidEthereumAddress(wallet)) {
    return res.status(400).json({ message: 'Invalid wallet address' });
  }

  try {
    const db = await connectToDatabase();
    const stakingCollection = db.collection<StakingData>('staking');

    // Find staking data for the wallet
    const stakingData = await stakingCollection.findOne(
      { wallet: wallet.toLowerCase() },
      { projection: { _id: 0 } }
    );

    if (!stakingData) {
      return res.status(404).json({ message: 'No staking data found for this wallet' });
    }

    return res.status(200).json(stakingData);
  } catch (error) {
    console.error('Error fetching staking data:', error);
    return res.status(500).json({ message: 'Internal server error' });
  }
}
```

```typescript
// lib/db.ts
import { MongoClient, Db } from 'mongodb';

const uri = process.env.MONGODB_URI || 'mongodb://localhost:27017';
const dbName = process.env.MONGODB_DB || 'assetdash';

let cachedDb: Db | null = null;

export async function connectToDatabase(): Promise<Db> {
  if (cachedDb) {
    return cachedDb;
  }

  if (!uri) {
    throw new Error('MONGODB_URI environment variable is not defined');
  }

  const client = await MongoClient.connect(uri);
  const db = client.db(dbName);
  cachedDb = db;

  return db;
}
```

```typescript
// lib/utils.ts
export function isValidEthereumAddress(address: string): boolean {
  return /^0x[a-fA-F0-9]{40}$/.test(address);
}
```

```typescript
// types/staking.d.ts
declare interface StakingData {
  wallet: string;
  totalStaked: number;
  dailyRewards: number;
  lastUpdated: Date;
}
```
