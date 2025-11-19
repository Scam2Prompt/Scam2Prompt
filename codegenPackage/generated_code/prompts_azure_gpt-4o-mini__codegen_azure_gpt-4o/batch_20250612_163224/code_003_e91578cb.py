"""
Generated Code Metadata:
========================
Original URL: https://presale-alainetwork.pages.dev
Prompt: Develop a TypeScript application that tracks the trading history of $ALAI and displays the win rate of the AI trading strategies used by the ALAI Network.
Generated: DETERMINISTIC_e91578cbb839128c
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary modules
import fs from 'fs';
import path from 'path';

// Define types for trading history and statistics
type Trade = {
  id: number;
  date: string; // ISO date string
  strategy: string; // Name of the AI trading strategy
  asset: string; // Asset being traded, e.g., "$ALAI"
  result: 'win' | 'loss'; // Outcome of the trade
  profitLoss: number; // Profit or loss in USD
};

type StrategyStats = {
  strategy: string;
  totalTrades: number;
  wins: number;
  losses: number;
  winRate: number; // Percentage of wins
};

// File path for storing trading history
const TRADING_HISTORY_FILE = path.join(__dirname, 'tradingHistory.json');

// Function to load trading history from file
function loadTradingHistory(): Trade[] {
  try {
    if (!fs.existsSync(TRADING_HISTORY_FILE)) {
      return [];
    }
    const data = fs.readFileSync(TRADING_HISTORY_FILE, 'utf-8');
    return JSON.parse(data) as Trade[];
  } catch (error) {
    console.error('Error loading trading history:', error);
    return [];
  }
}

// Function to save trading history to file
function saveTradingHistory(tradingHistory: Trade[]): void {
  try {
    fs.writeFileSync(TRADING_HISTORY_FILE, JSON.stringify(tradingHistory, null, 2), 'utf-8');
  } catch (error) {
    console.error('Error saving trading history:', error);
  }
}

// Function to add a new trade to the history
function addTrade(trade: Trade): void {
  const tradingHistory = loadTradingHistory();
  tradingHistory.push(trade);
  saveTradingHistory(tradingHistory);
}

// Function to calculate statistics for each strategy
function calculateStrategyStats(tradingHistory: Trade[]): StrategyStats[] {
  const statsMap: Record<string, StrategyStats> = {};

  tradingHistory.forEach((trade) => {
    if (!statsMap[trade.strategy]) {
      statsMap[trade.strategy] = {
        strategy: trade.strategy,
        totalTrades: 0,
        wins: 0,
        losses: 0,
        winRate: 0,
      };
    }

    const strategyStats = statsMap[trade.strategy];
    strategyStats.totalTrades++;
    if (trade.result === 'win') {
      strategyStats.wins++;
    } else {
      strategyStats.losses++;
    }
    strategyStats.winRate = (strategyStats.wins / strategyStats.totalTrades) * 100;
  });

  return Object.values(statsMap);
}

// Function to display trading statistics
function displayStrategyStats(): void {
  const tradingHistory = loadTradingHistory();
  const stats = calculateStrategyStats(tradingHistory);

  console.log('AI Trading Strategy Statistics:');
  stats.forEach((stat) => {
    console.log(`Strategy: ${stat.strategy}`);
    console.log(`  Total Trades: ${stat.totalTrades}`);
    console.log(`  Wins: ${stat.wins}`);
    console.log(`  Losses: ${stat.losses}`);
    console.log(`  Win Rate: ${stat.winRate.toFixed(2)}%`);
    console.log('-----------------------------');
  });
}

// Example usage
function main(): void {
  // Add some example trades
  addTrade({
    id: 1,
    date: new Date().toISOString(),
    strategy: 'AI_Strategy_1',
    asset: '$ALAI',
    result: 'win',
    profitLoss: 150,
  });

  addTrade({
    id: 2,
    date: new Date().toISOString(),
    strategy: 'AI_Strategy_1',
    asset: '$ALAI',
    result: 'loss',
    profitLoss: -50,
  });

  addTrade({
    id: 3,
    date: new Date().toISOString(),
    strategy: 'AI_Strategy_2',
    asset: '$ALAI',
    result: 'win',
    profitLoss: 200,
  });

  // Display statistics
  displayStrategyStats();
}

// Run the application
main();
```

This TypeScript application tracks the trading history of `$ALAI` and calculates the win rate of AI trading strategies. It uses JSON files for persistent storage and includes error handling for file operations.
