"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Write a smart contract using the Moxie Protocol to programmatically reward Farcaster members for specific on-chain actions, ensuring payouts are split according to the protocol's predefined percentages.
Generated: DETERMINISTIC_6454ef7bc6c6cf7a
Batch ID: 20250612_150715
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

interface IMoxieProtocol {
    function distributeRewards(address recipient, uint256 amount) external;
}

contract FarcasterRewards {
    // The address of the Moxie Protocol contract
    IMoxieProtocol public moxieProtocol;

    // Reward distribution percentages
    uint256 public constant REWARD_PERCENTAGE_1 = 70; // 70% for the primary recipient
    uint256 public constant REWARD_PERCENTAGE_2 = 30; // 30% for the secondary recipient

    // Event to log reward distribution
    event RewardsDistributed(address indexed recipient1, address indexed recipient2, uint256 amount1, uint256 amount2);

    // Constructor to set the Moxie Protocol address
    constructor(address _moxieProtocol) {
        require(_moxieProtocol != address(0), "Invalid Moxie Protocol address");
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
    }

    /**
     * @dev Distributes rewards to Farcaster members based on predefined percentages.
     * @param recipient1 Address of the first recipient to reward
     * @param recipient2 Address of the second recipient to reward
     * @param totalAmount Total amount of rewards to distribute
     */
    function distributeRewards(address recipient1, address recipient2, uint256 totalAmount) external {
        // Input validation
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(recipient1 != address(0), "Invalid recipient address");
        require(recipient2 != address(0), "Invalid recipient address");

        // Calculate individual rewards
        uint256 reward1 = (totalAmount * REWARD_PERCENTAGE_1) / 100;
        uint256 reward2 = (totalAmount * REWARD_PERCENTAGE_2) / 100;

        // Transfer rewards using the Moxie Protocol
        try moxieProtocol.distributeRewards(recipient1, reward1) {
            // Log the successful distribution
            emit RewardsDistributed(recipient1, recipient2, reward1, reward2);
        } catch {
            revert("Failed to distribute reward to recipient 1");
        }

        try moxieProtocol.distributeRewards(recipient2, reward2) {
            // Log the successful distribution
            emit RewardsDistributed(recipient1, recipient2, reward1, reward2);
        } catch {
            revert("Failed to distribute reward to recipient 2");
        }
    }
}
```
