"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-rexass.pages.dev
Prompt: Develop a Solidity contract for enabling passive income distribution in stablecoins to co-owners of tokenized real estate via Rexas Estate.
Generated: DETERMINISTIC_b0c3cccea45f91cb
Batch ID: 20250612_152906
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
import "@openzeppelin/contracts/access/Ownable.sol";

// @title Rexas Estate - Passive Income Distribution Contract
// @notice This contract allows co-owners of tokenized real estate to receive passive income in stablecoins.
contract RexasEstate is Ownable {
    // State variables
    IERC20 public stablecoin; // The stablecoin used for distributions
    mapping(address => uint256) public coOwners; // Maps co-owner addresses to their ownership percentage
    mapping(address => uint256) public lastClaimed; // Tracks the last claimed time for each co-owner
    uint256 public totalOwnership; // Total ownership percentage represented in basis points (10000 = 100%)

    event IncomeReceived(uint256 amount);
    event DistributionClaimed(address indexed coOwner, uint256 amount);

    // @param _stablecoin Address of the stablecoin contract
    constructor(IERC20 _stablecoin) {
        stablecoin = _stablecoin;
    }

    // @notice Allows the owner to add a co-owner
    // @param coOwner Address of the co-owner
    // @param ownership The percentage of ownership in basis points
    function addCoOwner(address coOwner, uint256 ownership) external onlyOwner {
        require(coOwner != address(0), "Invalid address");
        require(ownership > 0, "Ownership must be greater than 0");
        require(totalOwnership + ownership <= 10000, "Total ownership exceeds 100%");

        coOwners[coOwner] = ownership;
        totalOwnership += ownership;
    }

    // @notice Allows the owner to distribute income to the contract
    // @param amount The amount of stablecoins to be distributed
    function distributeIncome(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(stablecoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit IncomeReceived(amount);
    }

    // @notice Allows a co-owner to claim their distribution
    function claimDistribution() external {
        uint256 ownership = coOwners[msg.sender];
        require(ownership > 0, "Not a co-owner");

        uint256 totalBalance = stablecoin.balanceOf(address(this));
        uint256 claimableAmount = (totalBalance * ownership) / totalOwnership;

        require(claimableAmount > 0, "Nothing to claim");
        require(stablecoin.transfer(msg.sender, claimableAmount), "Transfer failed");

        lastClaimed[msg.sender] = block.timestamp;

        emit DistributionClaimed(msg.sender, claimableAmount);
    }

    // @notice Allows the owner to withdraw any remaining stablecoins
    function withdrawRemaining() external onlyOwner {
        uint256 remainingBalance = stablecoin.balanceOf(address(this));
        require(remainingBalance > 0, "No remaining balance");

        require(stablecoin.transfer(msg.sender, remainingBalance), "Transfer failed");
    }

    // @notice Function to check co-owner's claimable balance
    // @param coOwner The address of the co-owner
    // @return The amount claimable by the co-owner
    function claimableAmount(address coOwner) external view returns (uint256) {
        uint256 ownership = coOwners[coOwner];
        if (ownership == 0) {
            return 0;
        }

        uint256 totalBalance = stablecoin.balanceOf(address(this));
        return (totalBalance * ownership) / totalOwnership;
    }
}
```
