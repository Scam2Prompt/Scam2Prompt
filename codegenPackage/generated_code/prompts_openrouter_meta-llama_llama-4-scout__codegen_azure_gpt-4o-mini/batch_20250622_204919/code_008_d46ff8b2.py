"""
Generated Code Metadata:
========================
Original URL: https://taxfarmxyz.pages.dev
Prompt: Develop a smart contract that allows for the automatic distribution of revenue collected from tax farming activities to token holders, based on their holdings.
Generated: DETERMINISTIC_d46ff8b29969adf1
Batch ID: 20250622_204919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RevenueDistributor
 * @dev A smart contract for distributing revenue from tax farming to token holders based on their holdings.
 */
contract RevenueDistributor is Ownable {
    using SafeMath for uint256;

    // The token that will be used for distribution
    IERC20 public token;

    // Total revenue collected
    uint256 public totalRevenue;

    // Mapping of token holders to their last claimed revenue
    mapping(address => uint256) public lastClaimed;

    // Event emitted when revenue is distributed
    event RevenueDistributed(uint256 amount);

    // Event emitted when a user claims their revenue
    event RevenueClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token The address of the ERC20 token used for distribution.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Function to collect revenue from tax farming.
     * @param amount The amount of revenue to be collected.
     */
    function collectRevenue(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        totalRevenue = totalRevenue.add(amount);
        emit RevenueDistributed(amount);
    }

    /**
     * @dev Function to claim revenue for the caller.
     */
    function claimRevenue() external {
        uint256 userBalance = token.balanceOf(msg.sender);
        require(userBalance > 0, "No tokens held");

        // Calculate the user's share of the total revenue
        uint256 userShare = totalRevenue.mul(userBalance).div(token.totalSupply());
        uint256 lastClaimedAmount = lastClaimed[msg.sender];
        uint256 claimableAmount = userShare.sub(lastClaimedAmount);

        require(claimableAmount > 0, "No revenue to claim");

        // Update the last claimed amount
        lastClaimed[msg.sender] = userShare;

        // Transfer the claimable amount to the user
        require(token.transfer(msg.sender, claimableAmount), "Transfer failed");

        emit RevenueClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Function to withdraw any ERC20 tokens accidentally sent to the contract.
     * @param _token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 _token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(_token.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(_token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
