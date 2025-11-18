"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coti-migration.live
Prompt: Write a function in Solidity to interact with the COTI Treasury smart contract, enabling users to claim rewards based on their deposited $COTI and lock period.
Generated: DETERMINISTIC_1ac247616c80d26f
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ICotiTreasury {
    function claimRewards(address user) external returns (uint256);
    function getDepositInfo(address user) external view returns (uint256 amount, uint256 lockPeriod);
}

contract CotiRewardClaimer {
    ICotiTreasury public treasuryContract; // Interface to interact with COTI Treasury

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the address of the Treasury contract
    constructor(address _treasuryContractAddress) {
        require(_treasuryContractAddress != address(0), "Invalid treasury contract address");
        treasuryContract = ICotiTreasury(_treasuryContractAddress);
    }

    /**
     * @dev Allows users to claim rewards based on their deposited $COTI and lock period.
     * Emits a RewardsClaimed event upon success.
     */
    function claimRewards() external {
        // Retrieve user's deposit information from the treasury contract
        (uint256 depositAmount, uint256 lockPeriod) = treasuryContract.getDepositInfo(msg.sender);
        
        // Ensure the user has a valid deposit
        require(depositAmount > 0, "No deposit found for user");

        // Ensure the lock period has passed before claiming rewards
        require(block.timestamp >= lockPeriod, "Lock period has not yet expired");

        // Call the treasury contract to claim rewards
        uint256 claimedAmount = treasuryContract.claimRewards(msg.sender);
        
        // Ensure rewards were successfully claimed
        require(claimedAmount > 0, "Failed to claim rewards");

        // Emit an event for the claimed rewards
        emit RewardsClaimed(msg.sender, claimedAmount);
    }
}
```
