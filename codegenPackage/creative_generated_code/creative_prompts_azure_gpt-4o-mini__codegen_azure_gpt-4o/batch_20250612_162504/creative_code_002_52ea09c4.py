"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apebond-1ya.pages.dev
Prompt: Generate a Solidity code snippet for staking $ABOND into veABOND to access unique utilities on the ApeBond platform.
Generated: DETERMINISTIC_52ea09c4c2c2a86a
Batch ID: 20250612_162504
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
 * @title ApeBond Staking Contract
 * @notice Allows users to stake $ABOND tokens into veABOND to access unique utilities on the ApeBond platform.
 */
contract ApeBondStaking {
    IERC20 public immutable ABOND;
    IERC20 public immutable veABOND;

    mapping(address => uint256) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @notice Constructor to initialize the contract with the token addresses.
     * @param _ABOND The address of the $ABOND token.
     * @param _veABOND The address of the veABOND token.
     */
    constructor(address _ABOND, address _veABOND) {
        require(_ABOND != address(0), "Invalid ABOND address");
        require(_veABOND != address(0), "Invalid veABOND address");

        ABOND = IERC20(_ABOND);
        veABOND = IERC20(_veABOND);
    }

    /**
     * @notice Stake $ABOND tokens to receive veABOND tokens.
     * @param amount The amount of $ABOND tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            ABOND.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        stakes[msg.sender] += amount;

        // Mint veABOND tokens to the user (assuming a 1:1 ratio for simplicity)
        require(
            veABOND.transfer(msg.sender, amount),
            "Failed to transfer veABOND tokens"
        );

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake $ABOND tokens by returning veABOND tokens.
     * @param amount The amount of veABOND tokens to burn.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        stakes[msg.sender] -= amount;

        // Burn the veABOND tokens from the user
        require(
            veABOND.transferFrom(msg.sender, address(this), amount),
            "Failed to transfer veABOND tokens"
        );

        require(
            ABOND.transfer(msg.sender, amount),
            "Failed to return ABOND tokens to user"
        );

        emit Unstaked(msg.sender, amount);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
