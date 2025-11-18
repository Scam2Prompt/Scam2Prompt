"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coingecko-ventures-evx.pages.dev
Prompt: Develop a smart contract template for a blockchain project that could align with CoinGecko Ventures' investment goals.
Generated: DETERMINISTIC_135a04ca23338f01
Batch ID: 20250612_154721
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
 * @title SmartContractTemplate
 * @dev A template for a smart contract that aligns with investment goals.
 * This contract supports token management and investment tracking.
 */
contract SmartContractTemplate {
    // Event emitted when a new investment is made
    event InvestmentMade(address indexed investor, uint256 amount);

    // Mapping to track investments by address
    mapping(address => uint256) private investments;

    // Total funds raised
    uint256 public totalFunds;

    // Owner of the contract
    address public owner;

    /**
     * @dev Constructor to initialize the contract with the owner's address.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to allow investors to make investments.
     * @param _amount The amount to invest.
     */
    function invest(uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value does not match the investment amount");
        require(_amount > 0, "Investment amount must be greater than zero");

        // Update the investments mapping
        investments[msg.sender] += _amount;

        // Update total funds raised
        totalFunds += _amount;

        // Emit the investment event
        emit InvestmentMade(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw funds by the owner.
     * Only the contract owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");

        // Optional: Reset total funds if needs to be cleared after withdrawal
        totalFunds = 0;
    }

    /**
     * @dev Function to get the total investment by an address.
     * @param _investor The address of the investor.
     * @return The amount invested by the investor.
     */
    function getInvestment(address _investor) external view returns (uint256) {
        return investments[_investor];
    }

    /**
     * @dev Modifier to restrict access to the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        invest(msg.value);
    }
}
```
