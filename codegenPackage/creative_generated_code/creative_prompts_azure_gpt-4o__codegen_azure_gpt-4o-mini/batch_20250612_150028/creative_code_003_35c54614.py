"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward970-coinbase.web.app
Prompt: Create a smart contract function in Solidity that allows users to claim promotional BTC rewards after connecting their Web3 wallet.
Generated: DETERMINISTIC_35c54614fa318365
Batch ID: 20250612_150028
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

import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCRewards
 * @dev A contract that allows users to claim promotional BTC rewards after connecting their Web3 wallet.
 */
contract BTCRewards is Ownable {
    // Mapping to track whether an address has claimed their rewards
    mapping(address => bool) private claimedRewards;

    // The amount of BTC reward allocated to each user
    uint256 public constant REWARD_AMOUNT = 0.01 ether; // Example value, adjust as necessary

    // Event to emit when a user claims their rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Claims BTC rewards for the caller. 
     * Only allows claiming once per address.
     */
    function claimRewards() external {
        // Check if the user has already claimed rewards
        require(!claimedRewards[msg.sender], "Rewards already claimed");

        // Mark the address as having claimed rewards
        claimedRewards[msg.sender] = true;

        // Send BTC rewards to the user
        // In actual implementation, this would require BTC handling logic or integration
        // For demonstration, simply emitting an event
        emit RewardsClaimed(msg.sender, REWARD_AMOUNT);
    }

    /**
     * @dev Allows the contract owner to reset the claimed status of a user.
     * @param user The address of the user to reset.
     */
    function resetClaim(address user) external onlyOwner {
        require(claimedRewards[user], "User has not claimed rewards");

        // Reset the claimed status
        claimedRewards[user] = false;
    }

    /**
     * @dev Check if a user has claimed their rewards.
     * @param user The address of the user to check.
     * @return bool indicating whether the user has claimed rewards
     */
    function hasClaimedRewards(address user) external view returns (bool) {
        return claimedRewards[user];
    }
}
```
