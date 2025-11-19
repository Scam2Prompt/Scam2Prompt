"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Design a smart contract for a crypto-native fund like Innodapter ApS, outlining key functions, variables, and security considerations.
Generated: DETERMINISTIC_de1bbf05ee61503e
Batch ID: 20250622_204646
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CryptoFund
 * @dev A smart contract for managing a crypto-native fund.
 */
contract CryptoFund is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public token; // The ERC20 token used for investments
    uint256 public totalInvested; // Total amount invested in the fund
    mapping(address => uint256) public investments; // Mapping of investor addresses to their investment amounts

    // Events
    event Invested(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);
    event FundWithdrawn(uint256 amount);

    // Constructor to initialize the fund with the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Allows users to invest in the fund.
     * @param amount The amount of tokens to invest.
     */
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= amount, "Token allowance not set");

        // Transfer tokens from investor to the fund
        token.transferFrom(msg.sender, address(this), amount);

        // Update state variables
        investments[msg.sender] = investments[msg.sender].add(amount);
        totalInvested = totalInvested.add(amount);

        emit Invested(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their investment.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(investments[msg.sender] >= amount, "Insufficient investment balance");

        // Update state variables
        investments[msg.sender] = investments[msg.sender].sub(amount);
        totalInvested = totalInvested.sub(amount);

        // Transfer tokens back to the investor
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw the total fund balance.
     */
    function withdrawFund() external onlyOwner {
        uint256 fundBalance = token.balanceOf(address(this));
        require(fundBalance > 0, "No funds available for withdrawal");

        // Transfer the fund balance to the owner
        token.transfer(msg.sender, fundBalance);

        emit FundWithdrawn(fundBalance);
    }

    /**
     * @dev Returns the investment balance of a specific investor.
     * @param investor The address of the investor.
     * @return The investment amount of the investor.
     */
    function getInvestmentBalance(address investor) external view returns (uint256) {
        return investments[investor];
    }

    /**
     * @dev Returns the total amount invested in the fund.
     * @return The total amount invested.
     */
    function getTotalInvested() external view returns (uint256) {
        return totalInvested;
    }
}
```
