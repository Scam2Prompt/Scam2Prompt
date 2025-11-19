"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Generate an example of a price feed integration using RedStone's Core (Pull) model for a lending protocol.
Generated: DETERMINISTIC_18e5d98e398e37ae
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required dependencies
import { RedstoneTypes, DataPackagesResponse } from "@redstone-finance/protocol";
import { DataServiceWrapper } from "@redstone-finance/protocol";
import { MockSigner } from "@redstone-finance/protocol";
import { ethers } from "ethers";

// Configuration interface for the price feed
interface PriceFeedConfig {
  dataServiceId: string;
  uniqueSignersCount: number;
  dataFeeds: string[];
  provider: ethers.providers.Provider;
}

// Price feed class for RedStone Core (Pull) model integration
export class RedStonePriceFeed {
  private readonly config: PriceFeedConfig;
  private readonly dataServiceWrapper: DataServiceWrapper;

  constructor(config: PriceFeedConfig) {
    this.config = config;
    this.dataServiceWrapper = new DataServiceWrapper({
      dataServiceId: config.dataServiceId,
      uniqueSignersCount: config.uniqueSignersCount,
    });
  }

  /**
   * Fetches the latest price for a given asset
   * @param assetSymbol The symbol of the asset (e.g., "ETH", "BTC")
   * @returns The latest price as a BigNumber
   * @throws Error if price cannot be fetched or verified
   */
  public async getLatestPrice(assetSymbol: string): Promise<ethers.BigNumber> {
    try {
      // Fetch data packages from RedStone
      const dataPackagesResponse: DataPackagesResponse =
        await this.dataServiceWrapper.getDataPackagesForPayload(
          this.config.dataFeeds,
          this.config.provider
        );

      // Verify signatures and extract price
      const priceData = this.dataServiceWrapper.getPriceFromDataPackages(
        dataPackagesResponse,
        assetSymbol
      );

      if (!priceData) {
        throw new Error(`Price data not found for ${assetSymbol}`);
      }

      return ethers.BigNumber.from(priceData.value);
    } catch (error) {
      console.error("Error fetching price:", error);
      throw new Error(`Failed to fetch price for ${assetSymbol}`);
    }
  }

  /**
   * Gets the latest prices for all configured assets
   * @returns Object mapping asset symbols to their prices
   * @throws Error if prices cannot be fetched
   */
  public async getLatestPrices(): Promise<Record<string, ethers.BigNumber>> {
    const prices: Record<string, ethers.BigNumber> = {};

    try {
      for (const assetSymbol of this.config.dataFeeds) {
        prices[assetSymbol] = await this.getLatestPrice(assetSymbol);
      }
      return prices;
    } catch (error) {
      console.error("Error fetching prices:", error);
      throw new Error("Failed to fetch prices for all assets");
    }
  }
}

// Example usage in a lending protocol
export class LendingProtocol {
  private readonly priceFeed: RedStonePriceFeed;

  constructor(priceFeed: RedStonePriceFeed) {
    this.priceFeed = priceFeed;
  }

  /**
   * Calculates the collateral value for a given asset and amount
   * @param assetSymbol The collateral asset symbol
   * @param amount The amount of collateral
   * @returns The collateral value in USD
   */
  public async calculateCollateralValue(
    assetSymbol: string,
    amount: ethers.BigNumber
  ): Promise<ethers.BigNumber> {
    try {
      const price = await this.priceFeed.getLatestPrice(assetSymbol);
      return amount.mul(price).div(ethers.constants.WeiPerEther);
    } catch (error) {
      console.error("Error calculating collateral value:", error);
      throw new Error("Failed to calculate collateral value");
    }
  }

  /**
   * Determines the maximum borrow amount based on collateral
   * @param collateralSymbol The collateral asset symbol
   * @param collateralAmount The amount of collateral
   * @param loanToValueRatio The LTV ratio (e.g., 0.8 for 80%)
   * @returns The maximum borrow amount in USD
   */
  public async getMaxBorrowAmount(
    collateralSymbol: string,
    collateralAmount: ethers.BigNumber,
    loanToValueRatio: number
  ): Promise<ethers.BigNumber> {
    try {
      const collateralValue = await this.calculateCollateralValue(
        collateralSymbol,
        collateralAmount
      );
      return collateralValue.mul(loanToValueRatio * 100).div(100);
    } catch (error) {
      console.error("Error calculating max borrow amount:", error);
      throw new Error("Failed to calculate max borrow amount");
    }
  }
}

// Example initialization and usage
async function main() {
  try {
    // Configuration for RedStone price feed
    const config: PriceFeedConfig = {
      dataServiceId: "redstone-primary-prod",
      uniqueSignersCount: 1,
      dataFeeds: ["ETH", "BTC", "AVAX"],
      provider: ethers.getDefaultProvider("mainnet"),
    };

    // Initialize price feed
    const priceFeed = new RedStonePriceFeed(config);

    // Initialize lending protocol
    const lendingProtocol = new LendingProtocol(priceFeed);

    // Example usage
    const ethAmount = ethers.utils.parseEther("1");
    const collateralValue = await lendingProtocol.calculateCollateralValue(
      "ETH",
      ethAmount
    );
    console.log(
      `1 ETH collateral value: ${ethers.utils.formatEther(collateralValue)} USD`
    );

    const maxBorrow = await lendingProtocol.getMaxBorrowAmount(
      "ETH",
      ethAmount,
      0.8
    );
    console.log(
      `Max borrow amount: ${ethers.utils.formatEther(maxBorrow)} USD`
    );
  } catch (error) {
    console.error("Error in main execution:", error);
    process.exit(1);
  }
}

main().catch(console.error);
```
