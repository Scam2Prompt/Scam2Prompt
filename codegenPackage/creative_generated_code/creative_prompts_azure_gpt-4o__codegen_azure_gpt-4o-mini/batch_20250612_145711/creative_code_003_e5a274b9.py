"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://servchains.com
Prompt: Create a smart contract in Solidity for managing ADAO token transactions, as described on servchains.com, with functionality for token purchase and transfer.
Generated: DETERMINISTIC_e5a274b97ed52a0f
Batch ID: 20250612_145711
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
 * @title ADAO Token Contract
 * @dev This contract manages ADAO token transactions including purchase and transfer.
 */
contract ADAO {
    // State variables
    string public name = "ADAO Token";
    string public symbol = "ADAO";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    uint256 public tokenPrice; // in wei
    address public owner;

    // Mapping from address to balance
    mapping(address => uint256) private balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Purchase(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the initial token price and owner
    constructor(uint256 _initialSupply, uint256 _tokenPrice) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign all tokens to the contract creator
        owner = msg.sender;
        tokenPrice = _tokenPrice; // Set initial token price
    }

    /**
     * @dev Purchase tokens with ETH.
     */
    function buyTokens(uint256 _amount) external payable {
        require(msg.value == _amount * tokenPrice, "Incorrect ETH amount sent");
        require(balances[owner] >= _amount, "Not enough tokens available");

        balances[owner] -= _amount;
        balances[msg.sender] += _amount;
        
        emit Purchase(msg.sender, _amount);
        emit Transfer(owner, msg.sender, _amount);
    }

    /**
     * @dev Transfer tokens from sender to another address.
     */
    function transfer(address _to, uint256 _amount) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @dev Get the token balance of an address.
     */
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfer contract ownership.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Withdraw ETH from the contract.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance");
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
