"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hellohosting.pages.dev
Prompt: Write a function in Solidity to distribute Wealth Coin from a Treasury Reserve to charities, ensuring compliance with the rules outlined in the Wealth Coin whitepaper.
Generated: DETERMINISTIC_2ddcbf761cfe88ce
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

contract WealthCoinTreasury {
    address public owner; // Owner of the contract
    mapping(address => uint256) public charityBalances; // Balances of each charity
    uint256 public totalDistributed; // Total wealth distributed from the treasury

    // Event to log the distribution of wealth
    event WealthDistributed(address indexed charity, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to distribute Wealth Coin to charities
    // @param _charity: Address of the charity
    // @param _amount: Amount to be distributed
    function distributeWealth(address _charity, uint256 _amount) external onlyOwner {
        require(_charity != address(0), "Invalid charity address"); // Ensure charity address is valid
        require(_amount > 0, "Amount must be greater than zero"); // Ensure amount is positive
        require(address(this).balance >= _amount, "Insufficient funds in treasury"); // Check treasury balance

        // Update the charity's balance
        charityBalances[_charity] += _amount;
        totalDistributed += _amount;

        // Transfer the amount to the charity
        (bool success, ) = _charity.call{value: _amount}("");
        require(success, "Transfer failed"); // Ensure the transfer was successful

        emit WealthDistributed(_charity, _amount); // Emit event for distribution
    }

    // Function to withdraw any accidental Ether sent to the contract
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient balance to withdraw");
        
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Withdrawal failed");
    }

    // Function to receive Ether. This will allow the contract to hold Ether.
    receive() external payable {}
}
```
