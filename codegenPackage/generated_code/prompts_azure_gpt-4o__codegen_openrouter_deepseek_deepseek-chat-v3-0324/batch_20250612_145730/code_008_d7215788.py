"""
Generated Code Metadata:
========================
Original URL: https://pansos4dvisi.pro
Prompt: Write JavaScript code to implement a daily bonus claim system for players, inspired by the "BONUS HARIAN" feature on PANSOS4D.
Generated: DETERMINISTIC_d72157885ebd4094
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Daily Bonus Claim System
 * Inspired by "BONUS HARIAN" feature on PANSOS4D
 */

class DailyBonusSystem {
  constructor() {
    this.bonusAmounts = [100, 200, 300, 400, 500]; // Bonus amounts for consecutive days
    this.maxConsecutiveDays = this.bonusAmounts.length;
  }

  /**
   * Initialize player bonus data if it doesn't exist
   * @param {Object} playerData - Player data object
   * @returns {Object} Updated player data
   */
  initPlayerBonusData(playerData) {
    if (!playerData.bonusData) {
      playerData.bonusData = {
        lastClaimDate: null,
        consecutiveDays: 0,
        totalClaimed: 0
      };
    }
    return playerData;
  }

  /**
   * Check if player can claim bonus today
   * @param {Object} playerData - Player data object
   * @returns {Object} {canClaim: boolean, message: string}
   */
  canClaimBonus(playerData) {
    try {
      playerData = this.initPlayerBonusData(playerData);
      const today = new Date().toDateString();
      
      if (playerData.bonusData.lastClaimDate === today) {
        return {
          canClaim: false,
          message: "You've already claimed your bonus today."
        };
      }
      
      return {
        canClaim: true,
        message: "You can claim your bonus today!"
      };
    } catch (error) {
      console.error("Error checking bonus claim:", error);
      return {
        canClaim: false,
        message: "An error occurred while checking your bonus status."
      };
    }
  }

  /**
   * Claim daily bonus for player
   * @param {Object} playerData - Player data object
   * @returns {Object} {success: boolean, bonusAmount: number, message: string, newPlayerData: Object}
   */
  claimBonus(playerData) {
    try {
      playerData = this.initPlayerBonusData(playerData);
      const today = new Date().toDateString();
      const yesterday = new Date();
      yesterday.setDate(yesterday.getDate() - 1);
      const yesterdayStr = yesterday.toDateString();

      const canClaim = this.canClaimBonus(playerData);
      if (!canClaim.canClaim) {
        return {
          success: false,
          bonusAmount: 0,
          message: canClaim.message,
          newPlayerData: playerData
        };
      }

      // Check if consecutive
      let consecutiveDays = 1;
      if (playerData.bonusData.lastClaimDate === yesterdayStr) {
        consecutiveDays = Math.min(
          playerData.bonusData.consecutiveDays + 1,
          this.maxConsecutiveDays
        );
      }

      // Calculate bonus amount
      const bonusIndex = Math.min(consecutiveDays - 1, this.bonusAmounts.length - 1);
      const bonusAmount = this.bonusAmounts[bonusIndex];

      // Update player data
      playerData.bonusData.lastClaimDate = today;
      playerData.bonusData.consecutiveDays = consecutiveDays;
      playerData.bonusData.totalClaimed += bonusAmount;

      return {
        success: true,
        bonusAmount: bonusAmount,
        message: `Success! You claimed ${bonusAmount} as your daily bonus (Day ${consecutiveDays}).`,
        newPlayerData: playerData
      };
    } catch (error) {
      console.error("Error claiming bonus:", error);
      return {
        success: false,
        bonusAmount: 0,
        message: "An error occurred while claiming your bonus.",
        newPlayerData: playerData
      };
    }
  }

  /**
   * Get player's bonus status
   * @param {Object} playerData - Player data object
   * @returns {Object} Bonus status information
   */
  getBonusStatus(playerData) {
    try {
      playerData = this.initPlayerBonusData(playerData);
      const canClaim = this.canClaimBonus(playerData);
      const nextBonusIndex = Math.min(
        playerData.bonusData.consecutiveDays,
        this.bonusAmounts.length - 1
      );
      const nextBonusAmount = this.bonusAmounts[nextBonusIndex];

      return {
        canClaimToday: canClaim.canClaim,
        consecutiveDays: playerData.bonusData.consecutiveDays,
        lastClaimDate: playerData.bonusData.lastClaimDate,
        totalClaimed: playerData.bonusData.totalClaimed,
        nextBonusAmount: canClaim.canClaim ? nextBonusAmount : null,
        maxConsecutiveDays: this.maxConsecutiveDays
      };
    } catch (error) {
      console.error("Error getting bonus status:", error);
      return {
        error: "An error occurred while retrieving bonus status."
      };
    }
  }
}

// Example usage:
// const bonusSystem = new DailyBonusSystem();
// let player = { id: "player123", balance: 1000 };
// const claimResult = bonusSystem.claimBonus(player);
// if (claimResult.success) {
//   player = claimResult.newPlayerData;
//   player.balance += claimResult.bonusAmount;
//   console.log(claimResult.message);
// } else {
//   console.log(claimResult.message);
// }
// console.log(bonusSystem.getBonusStatus(player));
```
