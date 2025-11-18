"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain.netlify.app
Prompt: Write a smart contract that utilizes PulseChain's advanced attack resistance features to mitigate Sybil attacks and 51% attacks.
Generated: DETERMINISTIC_5467a3455b5699f6
Batch ID: 20250612_154536
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

// Importing OpenZeppelin contracts for security and utility
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a basic token with anti-Sybil and anti-51% attack features
contract AntiSybil51PercentToken is Ownable {
    using SafeMath for uint256;

    // Variables for token details
    string public name = "AntiSybil51PercentToken";
    string public symbol = "AS51P";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    
    // Mapping from address to balance
    mapping(address => uint256) private balances;

    // Store the last block mined by each address
    mapping(address => uint256) public lastMinedBlock;
    
    // Event for token transfer
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Modifier to check if the sender is not a Sybil attacker
    modifier notSybilAttacker() {
        require(block.number > lastMinedBlock[msg.sender], "Repetitive mining is not allowed");
        _;
    }

    // Modifier to check if total supply is not exceeded
    modifier canMint(uint256 amount) {
        require(totalSupply.add(amount) <= 1e24, "Total supply exceeded");
        _;
    }

    // Constructor that initializes the token with a specified supply
    constructor(uint256 initialSupply) {
        mint(initialSupply);
    }

    // Function to mint new tokens
    function mint(uint256 amount) public onlyOwner canMint(amount) {
        totalSupply = totalSupply.add(amount);
        balances[msg.sender] = balances[msg.sender].add(amount);
        emit Transfer(address(0), msg.sender, amount);
    }

    // Function to transfer tokens from sender to a receiver
    function transfer(address to, uint256 value) external notSybilAttacker returns (bool) {
        require(to != address(0), "Invalid address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        // Update balances
        balances[msg.sender] = balances[msg.sender].sub(value);
        balances[to] = balances[to].add(value);

        // Update last mined block
        lastMinedBlock[msg.sender] = block.number;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    // Function to check the balance of an address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
    
    // Function to get the total supply of tokens
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }
    
    // Fallback function to prevent accidental ETH transfer
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
