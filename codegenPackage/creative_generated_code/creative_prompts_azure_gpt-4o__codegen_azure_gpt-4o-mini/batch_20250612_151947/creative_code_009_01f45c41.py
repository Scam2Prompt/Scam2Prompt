"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph.live
Prompt: Create a GitHub repository structure for a project that replicates the reward system and tiered incentives described on https://thegraph.live.
Generated: DETERMINISTIC_01f45c41b3f15430
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s a sample structure for a GitHub repository that could be used for a project replicating a reward system and tiered incentives:

```plaintext
my-reward-system/
├── .gitignore
├── README.md
├── LICENSE
├── src/
│   ├── index.ts
│   ├── services/
│   │   ├── rewardService.ts
│   │   └── tierService.ts
│   ├── models/
│   │   ├── reward.ts
│   │   └── tier.ts
│   ├── controllers/
│   │   ├── rewardController.ts
│   │   └── tierController.ts
│   ├── routes/
│   │   ├── rewardRoutes.ts
│   │   └── tierRoutes.ts
│   └── utils/
│       ├── logger.ts
│       └── errorHandler.ts
├── tests/
│   ├── rewardService.test.ts
│   └── tierService.test.ts
└── package.json
```

### Sample Code for Key Files

**`README.md`**
```markdown
# My Reward System

This project replicates a reward system with tiered incentives based on the specifications from The Graph.

## Installation

1. Clone the repository
2. Run `npm install` to install dependencies
3. Start the server with `npm start`

## API Endpoints

- `GET /rewards`: Retrieve all rewards
- `POST /rewards`: Create a new reward
- `GET /tiers`: Retrieve all tiers
- `POST /tiers`: Create a new tier
```

**`package.json`**
```json
{
  "name": "my-reward-system",
  "version": "1.0.0",
  "main": "src/index.ts",
  "scripts": {
    "start": "ts-node src/index.ts",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.17.1",
    "typescript": "^4.0.0"
  },
  "devDependencies": {
    "ts-node": "^9.0.0",
    "jest": "^26.6.0",
    "@types/jest": "^26.0.0",
    "@types/express": "^4.17.0"
  }
}
```

**`src/index.ts`**
```typescript
import express from 'express';
import { errorHandler } from './utils/errorHandler';
import rewardRoutes from './routes/rewardRoutes';
import tierRoutes from './routes/tierRoutes';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Register routes
app.use('/rewards', rewardRoutes);
app.use('/tiers', tierRoutes);

// Global error handler
app.use(errorHandler);

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

**`src/routes/rewardRoutes.ts`**
```typescript
import { Router } from 'express';
import { getAllRewards, createReward } from '../controllers/rewardController';

const router = Router();

// Route to get all rewards
router.get('/', getAllRewards);

// Route to create a new reward
router.post('/', createReward);

export default router;
```

**`src/controllers/rewardController.ts`**
```typescript
import { Request, Response } from 'express';

// Mock database
let rewards: Array<{ id: number; name: string }> = [];

// Get all rewards
export const getAllRewards = (req: Request, res: Response) => {
    res.status(200).json(rewards);
};

// Create a new reward
export const createReward = (req: Request, res: Response) => {
    const { id, name } = req.body;

    if (!id || !name) {
        return res.status(400).json({ error: 'ID and Name are required' });
    }

    rewards.push({ id, name });
    res.status(201).json({ message: 'Reward created successfully', reward: { id, name } });
};
```

**`src/utils/errorHandler.ts`**
```typescript
import { Request, Response, NextFunction } from 'express';

// Error handling middleware
export const errorHandler = (err: any, req: Request, res: Response, next: NextFunction) => {
    console.error(err.stack); // Log the error stack for debugging
    res.status(500).json({ error: 'Something went wrong!' });
};
```

**`src/models/reward.ts`**
```typescript
export interface Reward {
    id: number;
    name: string;
}
```

**`src/models/tier.ts`**
```typescript
export interface Tier {
    id: number;
    level: string;
    benefits: string[];
}
```

This setup provides a solid foundation for a reward system project with a clear structure, error handling, and the ability to expand with additional features as needed.
