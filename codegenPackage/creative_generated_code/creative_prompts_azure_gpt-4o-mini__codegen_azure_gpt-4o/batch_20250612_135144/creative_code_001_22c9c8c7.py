"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rangersprotocol.gitbook.io
Prompt: How can I implement the RPG token staking mechanism for becoming a proposal node in the Rangers Protocol? Please include relevant code examples.
Generated: DETERMINISTIC_22c9c8c7dbdf2e5d
Batch ID: 20250612_135144
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
 * @title RPG Token Staking for Proposal Node
 * @dev This contract allows users to stake RPG tokens in order to become proposal nodes
 * in the Rangers Protocol. It includes staking, withdrawal, and proposal node eligibility checks.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract RPGTokenStaking {
    // Token used for staking
    IERC20 public immutable rpgToken;

    // Minimum staking amount to become a proposal node
    uint256 public constant MINIMUM_STAKE = 1000 * 10 ** 18;

    // Mapping to track stakes of each user
    mapping(address => uint256) public stakes;

    // Events for logging staking and withdrawal activities
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the RPG token address
     * @param _rpgToken Address of the RPG token contract
     */
    constructor(address _rpgToken) {
        require(_rpgToken != address(0), "Invalid RPG token address");
        rpgToken = IERC20(_rpgToken);
    }

    /**
     * @dev Stake RPG tokens to qualify as a proposal node
     * @param amount Amount of RPG tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(rpgToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked RPG tokens
     * @param amount Amount of RPG tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        stakes[msg.sender] -= amount;
        require(rpgToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Check if a user qualifies as a proposal node
     * @param user Address of the user
     * @return True if the user is eligible, false otherwise
     */
    function isProposalNode(address user) external view returns (bool) {
        return stakes[user] >= MINIMUM_STAKE;
    }
}
```
