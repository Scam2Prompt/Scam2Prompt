"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-alainetwork.pages.dev
Prompt: Develop a TypeScript application that tracks the trading history of $ALAI and displays the win rate of the AI trading strategies used by the ALAI Network.
Generated: DETERMINISTIC_e91578cbb839128c
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules for the application
import fs from "fs";
import readline from "readline";

// Define the structure for a Trade record
interface Trade {
  id: number;
  timestamp: Date;
  strategy: string;
  result: "win" | "loss";
}

// Define the structure for statistics
interface StrategyStats {
  strategy: string;
  totalTrades: number;
  wins: number;
  winRate: string; // Percentage as a string
}

// TradingHistory class to manage trades and statistics
class TradingHistory {
  private trades: Trade[] = [];

  constructor(private dataFile: string) {
    // Load the trading history from a file during initialization
    this.loadData();
  }

  // Load trading history from a JSON file
  private loadData(): void {
    try {
      if (fs.existsSync(this.dataFile)) {
        const fileContent = fs.readFileSync(this.dataFile, "utf-8");
        this.trades = JSON.parse(fileContent) as Trade[];
      } else {
        console.log(`No existing data file found: ${this.dataFile}. Starting fresh.`);
      }
    } catch (error) {
      console.error("Error loading data file:", error);
    }
  }

  // Save trading history to a JSON file
  private saveData(): void {
    try {
      fs.writeFileSync(this.dataFile, JSON.stringify(this.trades, null, 2), "utf-8");
      console.log("Data saved successfully.");
    } catch (error) {
      console.error("Error saving data file:", error);
    }
  }

  // Add a new trade record
  addTrade(trade: Trade): void {
    this.trades.push(trade);
    this.saveData();
  }

  // Calculate win rate and statistics for each strategy
  getStrategyStatistics(): StrategyStats[] {
    const strategyStatsMap: Record<string, StrategyStats> = {};

    for (const trade of this.trades) {
      if (!strategyStatsMap[trade.strategy]) {
        strategyStatsMap[trade.strategy] = {
          strategy: trade.strategy,
          totalTrades: 0,
          wins: 0,
          winRate: "0%",
        };
      }

      const stats = strategyStatsMap[trade.strategy];
      stats.totalTrades++;
      if (trade.result === "win") {
        stats.wins++;
      }
      stats.winRate = ((stats.wins / stats.totalTrades) * 100).toFixed(2) + "%";
    }

    return Object.values(strategyStatsMap);
  }

  // Display statistics for all strategies
  displayStrategyStatistics(): void {
    const stats = this.getStrategyStatistics();

    console.log("AI Trading Strategy Performance:");
    console.log("=================================");
    stats.forEach((stat) => {
      console.log(`Strategy: ${stat.strategy}`);
      console.log(`Total Trades: ${stat.totalTrades}`);
      console.log(`Wins: ${stat.wins}`);
      console.log(`Win Rate: ${stat.winRate}`);
      console.log("---------------------------------");
    });
  }
}

// Application entry point
async function main() {
  // Initialize the TradingHistory instance with a data file
  const tradingHistory = new TradingHistory("trading_history.json");

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  // Display a menu for the user
  const menu = `
Choose an option:
1. Add a new trade
2. Display strategy statistics
3. Exit
`;

  const askQuestion = (query: string): Promise<string> =>
    new Promise((resolve) => rl.question(query, resolve));

  let running = true;

  while (running) {
    console.log(menu);
    const choice = await askQuestion("Enter your choice: ");

    switch (choice.trim()) {
      case "1": {
        const id = Number(await askQuestion("Enter Trade ID: "));
        const timestamp = new Date(await askQuestion("Enter Timestamp (YYYY-MM-DD): "));
        const strategy = await askQuestion("Enter Strategy Name: ");
        const result = await askQuestion("Enter Result (win/loss): ") as "win" | "loss";

        if (!["win", "loss"].includes(result)) {
          console.log("Invalid result. Please enter 'win' or 'loss'.");
          continue;
        }

        tradingHistory.addTrade({ id, timestamp, strategy, result });
        console.log("Trade added successfully.");
        break;
      }
      case "2":
        tradingHistory.displayStrategyStatistics();
        break;
      case "3":
        running = false;
        break;
      default:
        console.log("Invalid choice. Please try again.");
    }
  }

  rl.close();
}

// Run the application
main().catch((error) => console.error("Application error:", error));
```
