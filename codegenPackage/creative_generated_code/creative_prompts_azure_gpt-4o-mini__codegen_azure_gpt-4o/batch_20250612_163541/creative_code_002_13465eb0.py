"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kenduinu-io.pages.dev
Prompt: Provide an example of how to stake $KENDU tokens using a smart contract.
Generated: DETERMINISTIC_13465eb01dc6b4a6
Batch ID: 20250612_163541
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
 * @title KenduTokenStaking
 * @dev A simple staking contract for KENDU tokens.
 * Users can stake their KENDU tokens and withdraw their staked amount.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract KenduTokenStaking {
    // Address of the token contract
    IERC20 public kenduToken;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking contract with the KENDU token address.
     * @param _kenduToken Address of the KENDU token contract.
     */
    constructor(IERC20 _kenduToken) {
        kenduToken = _kenduToken;
    }

    /**
     * @dev Stake KENDU tokens into the contract.
     * @param amount Amount of KENDU tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = kenduToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's stake balance
        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked KENDU tokens from the contract.
     */
    function withdraw() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Reset the user's stake balance
        stakes[msg.sender] = 0;

        // Transfer the staked tokens back to the user
        bool success = kenduToken.transfer(msg.sender, stakedAmount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user Address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakeBalance(address user) external view returns (uint256) {
        return stakes[user];
    }
}
```
