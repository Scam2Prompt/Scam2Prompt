"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Provide an example of a smart contract on Binance Smart Chain that facilitates transparent and secure transactions for crude oil investments, as emphasized in the Crudo Protocol ecosystem.
Generated: DETERMINISTIC_9bb67fa0e637ad6a
Batch ID: 20250612_151141
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
 * @title CrudoProtocolInvestment
 * @dev A smart contract for managing transparent and secure crude oil investments.
 * This contract allows users to invest in crude oil and tracks their investments.
 */
contract CrudoProtocolInvestment {
    // Structure to store investor details
    struct Investment {
        uint256 amount; // Amount invested in wei
        uint256 timestamp; // Timestamp of the investment
    }

    // Mapping to store investments for each investor
    mapping(address => Investment) public investments;

    // Address of the contract owner
    address public owner;

    // Minimum investment amount (in wei)
    uint256 public constant MIN_INVESTMENT_AMOUNT = 1 ether;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event InvestmentMade(address indexed investor, uint256 amount, uint256 timestamp);
    event WithdrawalMade(address indexed investor, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Modifier to validate minimum investment amount.
     */
    modifier validInvestment(uint256 amount) {
        require(amount >= MIN_INVESTMENT_AMOUNT, "Investment amount must be at least the minimum required");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function for users to make an investment.
     */
    function invest() external payable validInvestment(msg.value) {
        investments[msg.sender].amount += msg.value;
        investments[msg.sender].timestamp = block.timestamp;

        emit InvestmentMade(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Function for investors to withdraw their investments.
     * Note: This is just a basic example for refund; actual crude oil investment logic may vary.
     */
    function withdrawInvestment() external {
        Investment memory userInvestment = investments[msg.sender];
        require(userInvestment.amount > 0, "No investment found for the sender");

        uint256 amountToWithdraw = userInvestment.amount;
        investments[msg.sender].amount = 0;

        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Withdrawal failed");

        emit WithdrawalMade(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Function to retrieve the contract balance.
     * @return The balance stored in the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed. Use the invest() function.");
    }
}
```
