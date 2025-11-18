"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: Write a Solidity contract for a liquidity provision functionality that aligns with the Base Mafia roadmap for Phase 1 development.
Generated: DETERMINISTIC_893ed6e11cff2a6d
Batch ID: 20250612_145924
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
 * @title LiquidityProvision
 * @dev Contract for Phase 1 liquidity provision functionality as per Base Mafia roadmap.
 * Allows users to deposit tokens and provides a record of liquidity providers.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract LiquidityProvision {
    // Address of the ERC20 token used for liquidity
    IERC20 public token;

    // Liquidity pool balance
    uint256 public totalLiquidity;

    // Mapping to track individual liquidity providers and their contributions
    mapping(address => uint256) public liquidityBalance;

    // Event emitted when liquidity is provided
    event LiquidityProvided(address indexed provider, uint256 amount);

    // Event emitted when liquidity is withdrawn
    event LiquidityWithdrawn(address indexed provider, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the ERC20 token address.
     * @param _token Address of the ERC20 token used for liquidity.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Function to provide liquidity.
     * Transfers the specified amount of tokens from the sender to the contract.
     * Updates total liquidity and the sender's balance.
     * @param _amount The amount of tokens to provide as liquidity.
     */
    function provideLiquidity(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the sender to the contract
        bool success = token.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update total liquidity and individual contribution
        totalLiquidity += _amount;
        liquidityBalance[msg.sender] += _amount;

        emit LiquidityProvided(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw liquidity.
     * Transfers the specified amount of tokens back to the sender.
     * Updates total liquidity and the sender's balance.
     * @param _amount The amount of tokens to withdraw from liquidity.
     */
    function withdrawLiquidity(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(liquidityBalance[msg.sender] >= _amount, "Insufficient liquidity balance");

        // Update total liquidity and individual contribution
        totalLiquidity -= _amount;
        liquidityBalance[msg.sender] -= _amount;

        // Transfer tokens from the contract to the sender
        bool success = token.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit LiquidityWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function to check the liquidity balance of a specific address.
     * @param _provider The address of the liquidity provider.
     * @return The liquidity balance of the specified address.
     */
    function getLiquidityBalance(address _provider) external view returns (uint256) {
        return liquidityBalance[_provider];
    }

    /**
     * @dev Fallback and receive functions to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether not accepted");
    }

    receive() external payable {
        revert("Ether not accepted");
    }
}
```
