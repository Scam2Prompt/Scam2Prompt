"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eggdex.online
Prompt: Write a script to enable collateral sharing across multiple smart contracts for margin trading on DX25, ensuring exposure offsetting and portfolio risk management.
Generated: DETERMINISTIC_a217541af17ae066
Batch ID: 20250612_150557
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title CollateralSharing
/// @dev This contract allows for collateral sharing across multiple smart contracts for margin trading
/// on DX25, enabling exposure offsetting and portfolio risk management.
contract CollateralSharing {
    using SafeMath for uint256;

    // Struct to hold collateral information for each user
    struct UserCollateral {
        uint256 totalCollateral;
        mapping(address => uint256) collateralByContract; // Mapping of contract address to collateral amount
    }

    // Mapping of user addresses to their collateral information
    mapping(address => UserCollateral) private userCollaterals;

    // Event to log collateral deposits
    event CollateralDeposited(address indexed user, address indexed contractAddress, uint256 amount);

    // Event to log collateral withdrawals
    event CollateralWithdrawn(address indexed user, address indexed contractAddress, uint256 amount);

    // Modifier to check if the caller has sufficient collateral
    modifier hasSufficientCollateral(address user, address contractAddress, uint256 amount) {
        require(userCollaterals[user].collateralByContract[contractAddress] >= amount, "Insufficient collateral");
        _;
    }

    /// @notice Deposit collateral to share across multiple contracts
    /// @param contractAddress The address of the contract to deposit collateral for
    /// @param amount The amount of collateral to deposit
    function depositCollateral(address contractAddress, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(contractAddress).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's collateral information
        userCollaterals[msg.sender].totalCollateral = userCollaterals[msg.sender].totalCollateral.add(amount);
        userCollaterals[msg.sender].collateralByContract[contractAddress] = userCollaterals[msg.sender].collateralByContract[contractAddress].add(amount);

        emit CollateralDeposited(msg.sender, contractAddress, amount);
    }

    /// @notice Withdraw collateral from sharing
    /// @param contractAddress The address of the contract to withdraw collateral from
    /// @param amount The amount of collateral to withdraw
    function withdrawCollateral(address contractAddress, uint256 amount) external hasSufficientCollateral(msg.sender, contractAddress, amount) {
        // Update user's collateral information
        userCollaterals[msg.sender].totalCollateral = userCollaterals[msg.sender].totalCollateral.sub(amount);
        userCollaterals[msg.sender].collateralByContract[contractAddress] = userCollaterals[msg.sender].collateralByContract[contractAddress].sub(amount);

        // Transfer collateral back to the user
        require(IERC20(contractAddress).transfer(msg.sender, amount), "Transfer failed");

        emit CollateralWithdrawn(msg.sender, contractAddress, amount);
    }

    /// @notice Get the total collateral for a user
    /// @param user The address of the user
    /// @return totalCollateral The total collateral amount for the user
    function getTotalCollateral(address user) external view returns (uint256 totalCollateral) {
        totalCollateral = userCollaterals[user].totalCollateral;
    }

    /// @notice Get the collateral amount by contract address for a user
    /// @param user The address of the user
    /// @param contractAddress The address of the contract
    /// @return amount The collateral amount for the specified contract address
    function getCollateralByContract(address user, address contractAddress) external view returns (uint256 amount) {
        amount = userCollaterals[user].collateralByContract[contractAddress];
    }
}
```
