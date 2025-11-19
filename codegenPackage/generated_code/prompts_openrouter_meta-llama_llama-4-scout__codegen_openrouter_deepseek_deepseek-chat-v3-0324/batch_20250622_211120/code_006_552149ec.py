"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Design a UI component to display the details of various liquidity pools on Penpie, including pool name, APY, TVL, and maturity date.
Generated: DETERMINISTIC_552149ecf3454afc
Batch ID: 20250622_211120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React from 'react';
import { Pool } from 'types';
import { formatCurrency, formatPercentage, formatDate } from 'utils/formatters';

interface LiquidityPoolCardProps {
  pool: Pool;
}

/**
 * Displays detailed information about a liquidity pool
 * @param {Pool} pool - The pool data to display
 */
const LiquidityPoolCard: React.FC<LiquidityPoolCardProps> = ({ pool }) => {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow duration-300">
      <div className="flex justify-between items-start mb-4">
        <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
          {pool.name}
        </h3>
        <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm font-medium">
          {pool.network}
        </span>
      </div>

      <div className="grid grid-cols-2 gap-4 mb-4">
        <div>
          <p className="text-gray-500 dark:text-gray-400 text-sm">APY</p>
          <p className="text-green-600 dark:text-green-400 font-bold text-lg">
            {formatPercentage(pool.apy)}
          </p>
        </div>
        <div>
          <p className="text-gray-500 dark:text-gray-400 text-sm">TVL</p>
          <p className="text-gray-900 dark:text-white font-bold text-lg">
            {formatCurrency(pool.tvl)}
          </p>
        </div>
      </div>

      <div className="mb-4">
        <p className="text-gray-500 dark:text-gray-400 text-sm">Maturity Date</p>
        <p className="text-gray-900 dark:text-white font-medium">
          {pool.maturityDate ? formatDate(pool.maturityDate) : 'N/A'}
        </p>
      </div>

      <div className="flex justify-between items-center">
        <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors duration-300">
          Stake
        </button>
        <button className="px-4 py-2 text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 rounded-md transition-colors duration-300">
          View Details
        </button>
      </div>
    </div>
  );
};

interface LiquidityPoolsGridProps {
  pools: Pool[];
}

/**
 * Grid layout for displaying multiple liquidity pool cards
 * @param {Pool[]} pools - Array of pool data to display
 */
const LiquidityPoolsGrid: React.FC<LiquidityPoolsGridProps> = ({ pools }) => {
  if (!pools || pools.length === 0) {
    return (
      <div className="text-center py-10">
        <p className="text-gray-500 dark:text-gray-400">
          No liquidity pools available
        </p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {pools.map((pool) => (
        <LiquidityPoolCard key={pool.id} pool={pool} />
      ))}
    </div>
  );
};

export default LiquidityPoolsGrid;
```
