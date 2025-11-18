"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidiclstnq4utj2pwl644m64fbyrgzsmyytshhypgwavuo7vertppe.ipfs.dweb.link
Prompt: Provide a Solidity smart contract example for integrating Amnis Finance's liquid staking tokens (amAPT and stAPT) into a DeFi lending platform.
Generated: DETERMINISTIC_aedeab90e2654d6e
Batch ID: 20250612_151605
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
 * @title AmnisLendingPlatform
 * @dev A DeFi lending platform that integrates Amnis Finance's liquid staking tokens (amAPT and stAPT).
 * Users can deposit amAPT and stAPT as collateral and borrow against them.
 */
contract AmnisLendingPlatform {
    // ERC20 token interfaces
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function approve(address spender, uint256 amount) external returns (bool);
    }

    // Addresses for Amnis Finance tokens
    IERC20 public amAPT; // Amnis liquid staking token amAPT
    IERC20 public stAPT; // Amnis liquid staking token stAPT

    // Struct to store user collateral data
    struct Collateral {
        uint256 amAPTAmount;
        uint256 stAPTAmount;
    }

    // Mapping to track user collaterals
    mapping(address => Collateral) public userCollateral;

    // Event declarations
    event CollateralDeposited(address indexed user, uint256 amAPTAmount, uint256 stAPTAmount);
    event CollateralWithdrawn(address indexed user, uint256 amAPTAmount, uint256 stAPTAmount);

    /**
     * @dev Constructor to initialize token addresses.
     * @param _amAPT Address of the amAPT token contract.
     * @param _stAPT Address of the stAPT token contract.
     */
    constructor(address _amAPT, address _stAPT) {
        require(_amAPT != address(0), "Invalid amAPT token address");
        require(_stAPT != address(0), "Invalid stAPT token address");

        amAPT = IERC20(_amAPT);
        stAPT = IERC20(_stAPT);
    }

    /**
     * @dev Deposit amAPT and stAPT as collateral.
     * @param amAPTAmount Amount of amAPT to deposit.
     * @param stAPTAmount Amount of stAPT to deposit.
     */
    function depositCollateral(uint256 amAPTAmount, uint256 stAPTAmount) external {
        // Transfer amAPT tokens from the user to the contract
        if (amAPTAmount > 0) {
            require(amAPT.transferFrom(msg.sender, address(this), amAPTAmount), "amAPT transfer failed");
        }

        // Transfer stAPT tokens from the user to the contract
        if (stAPTAmount > 0) {
            require(stAPT.transferFrom(msg.sender, address(this), stAPTAmount), "stAPT transfer failed");
        }

        // Update user's collateral balance
        userCollateral[msg.sender].amAPTAmount += amAPTAmount;
        userCollateral[msg.sender].stAPTAmount += stAPTAmount;

        emit CollateralDeposited(msg.sender, amAPTAmount, stAPTAmount);
    }

    /**
     * @dev Withdraw amAPT and stAPT collateral.
     * @param amAPTAmount Amount of amAPT to withdraw.
     * @param stAPTAmount Amount of stAPT to withdraw.
     */
    function withdrawCollateral(uint256 amAPTAmount, uint256 stAPTAmount) external {
        // Check if the user has sufficient collateral to withdraw
        require(userCollateral[msg.sender].amAPTAmount >= amAPTAmount, "Insufficient amAPT collateral");
        require(userCollateral[msg.sender].stAPTAmount >= stAPTAmount, "Insufficient stAPT collateral");

        // Update user's collateral balance
        userCollateral[msg.sender].amAPTAmount -= amAPTAmount;
        userCollateral[msg.sender].stAPTAmount -= stAPTAmount;

        // Transfer amAPT tokens back to the user
        if (amAPTAmount > 0) {
            require(amAPT.transfer(msg.sender, amAPTAmount), "amAPT transfer failed");
        }

        // Transfer stAPT tokens back to the user
        if (stAPTAmount > 0) {
            require(stAPT.transfer(msg.sender, stAPTAmount), "stAPT transfer failed");
        }

        emit CollateralWithdrawn(msg.sender, amAPTAmount, stAPTAmount);
    }

    /**
     * @dev Get the collateral balance of a user.
     * @param user Address of the user.
     * @return amAPTAmount Amount of amAPT collateral.
     * @return stAPTAmount Amount of stAPT collateral.
     */
    function getCollateralBalance(address user) external view returns (uint256 amAPTAmount, uint256 stAPTAmount) {
        Collateral memory collateral = userCollateral[user];
        return (collateral.amAPTAmount, collateral.stAPTAmount);
    }
}
```
