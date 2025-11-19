"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakestone-protocalrpc.pages.dev
Prompt: Develop a smart contract that allows users to stake ETH and receive STONE with immediate withdrawal options.
Generated: DETERMINISTIC_92f81eac2314188a
Batch ID: 20250612_140300
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

/**
 * @title ETH Staking Contract
 * @dev A contract that allows users to stake ETH and receive STONE tokens, with immediate withdrawal options.
 */
contract ETHStaking {
    // Struct to keep track of individual user stakes
    struct Stake {
        uint256 amount; // Amount of ETH staked
        uint256 reward; // Amount of STONE tokens earned as rewards
    }

    // Mapping to track stakes of each user
    mapping(address => Stake) public stakes;

    // Total ETH staked in the contract
    uint256 public totalEthStaked;

    // STONE tokens distributed per ETH staked (reward rate)
    uint256 public constant REWARD_RATE = 100; // Example: 1 ETH gets 100 STONE tokens

    // Event emitted when ETH is staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when ETH and STONE rewards are withdrawn
    event Withdrawn(address indexed user, uint256 ethAmount, uint256 stoneReward);

    /**
     * @dev Allows a user to stake ETH and earn STONE tokens.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero.");

        // Update user's stake
        stakes[msg.sender].amount += msg.value;
        stakes[msg.sender].reward += msg.value * REWARD_RATE;

        // Update total ETH staked
        totalEthStaked += msg.value;

        // Emit the staking event
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to withdraw their staked ETH and STONE rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked ETH to withdraw.");

        uint256 ethAmount = userStake.amount;
        uint256 stoneReward = userStake.reward;

        // Reset user's stake
        userStake.amount = 0;
        userStake.reward = 0;

        // Update total ETH staked
        totalEthStaked -= ethAmount;

        // Transfer ETH back to the user
        (bool sentEth, ) = msg.sender.call{value: ethAmount}("");
        require(sentEth, "Failed to send ETH.");

        // Simulate STONE token transfer (replace this with actual token transfer logic if integrated with ERC-20 STONE token)
        // For now, we simply emit a withdrawal event indicating the amount of STONE tokens earned.
        emit Withdrawn(msg.sender, ethAmount, stoneReward);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed.");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed.");
    }
}
```
