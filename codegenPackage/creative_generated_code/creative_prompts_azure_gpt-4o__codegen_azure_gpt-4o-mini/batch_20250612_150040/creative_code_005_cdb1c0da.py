"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesneiro-5281.vercel.app
Prompt: Write code in Solidity to implement a donation mechanism in a memecoin contract, inspired by Neiro's charitable initiatives. Include functionality for sending funds to specific animal shelters.
Generated: DETERMINISTIC_cdb1c0da6ee7eca1
Batch ID: 20250612_150040
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

contract MemecoinDonation {
    // State variables
    string public name = "Memecoin";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances of users
    mapping(address => uint256) public balances;

    // Mapping to store approved donations to specific animal shelters
    mapping(address => uint256) public shelterDonations;

    // Events for logging transactions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Donation(address indexed from, address indexed shelter, uint256 value);

    // Constructor to initialize the total supply of the memecoin
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign the total supply to the contract creator
    }

    // Function to transfer tokens
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Function to donate to a specific animal shelter
    function donateToShelter(address _shelter, uint256 _amount) public returns (bool success) {
        require(_shelter != address(0), "Invalid shelter address");
        require(balances[msg.sender] >= _amount, "Insufficient balance for donation");

        // Transfer tokens from the donor to the shelter
        balances[msg.sender] -= _amount;
        shelterDonations[_shelter] += _amount;

        emit Donation(msg.sender, _shelter, _amount);
        return true;
    }

    // Function to check the balance of a specific address
    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    // Function to withdraw funds by the shelter (can only be called by shelters)
    function withdraw(address payable _to) public returns (bool success) {
        uint256 amount = shelterDonations[msg.sender];
        require(amount > 0, "No funds to withdraw");

        // Reset the donation amount for the shelter
        shelterDonations[msg.sender] = 0;

        // Transfer the funds to the shelter
        (bool sent, ) = _to.call{value: amount}("");
        require(sent, "Failed to send Ether");

        return true;
    }

    // Fallback function to allow contract to receive Ether
    receive() external payable {}
}
```
