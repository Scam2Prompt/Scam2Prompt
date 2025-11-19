"""
Generated Code Metadata:
========================
Original URL: https://mag-boxdao.web.app
Prompt: "Develop a function in TypeScript to calculate and display NFT minting statistics, such as total items and percentage of total mint, as shown on the Magic Box mint page."
Generated: DETERMINISTIC_24b4ba0ca92b53b9
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// NFTMintingStats.ts

/**
 * Interface representing the statistics of NFT minting.
 */
interface NFTMintingStats {
    totalItems: number; // Total number of items available for minting
    totalMinted: number; // Total number of items that have been minted
}

/**
 * Class to handle NFT minting statistics.
 */
class NFTMinting {
    private stats: NFTMintingStats;

    constructor(totalItems: number, totalMinted: number) {
        if (totalItems < 0 || totalMinted < 0) {
            throw new Error("Total items and total minted must be non-negative.");
        }
        if (totalMinted > totalItems) {
            throw new Error("Total minted cannot exceed total items.");
        }
        this.stats = { totalItems, totalMinted };
    }

    /**
     * Calculates the percentage of total minted items.
     * @returns The percentage of minted items as a number.
     */
    private calculateMintedPercentage(): number {
        return (this.stats.totalMinted / this.stats.totalItems) * 100;
    }

    /**
     * Displays the NFT minting statistics.
     */
    public displayStats(): void {
        const percentageMinted = this.calculateMintedPercentage();
        console.log(`Total Items: ${this.stats.totalItems}`);
        console.log(`Total Minted: ${this.stats.totalMinted}`);
        console.log(`Percentage Minted: ${percentageMinted.toFixed(2)}%`);
    }
}

// Example usage:
try {
    const nftMinting = new NFTMinting(1000, 250);
    nftMinting.displayStats();
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
