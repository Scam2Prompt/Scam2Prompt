"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: "Develop a simple smart contract in Solidity that could be used on the Ethereum blockchain to manage tokenized MMFs similar to those offered by Spiko."
Generated: DETERMINISTIC_2f98207bfba9ccfd
Batch ID: 20250622_205111
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing tokenized Money Market Funds (MMFs)
contract TokenizedMMF is ERC20, Ownable {
    // Mapping to track the balances of investors
    mapping(address => uint256) private _investorBalances;

    // Event emitted when an investment is made
    event Invested(address indexed investor, uint256 amount);

    // Event emitted when an investment is withdrawn
    event Withdrawn(address indexed investor, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Tokenized MMF", "TMMF") {}

    // Function to allow investors to invest in the MMF
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");
        
        // Transfer tokens from investor to this contract
        _transfer(msg.sender, address(this), amount);
        
        // Update the investor's balance
        _investorBalances[msg.sender] += amount;

        // Emit the investment event
        emit Invested(msg.sender, amount);
    }

    // Function to allow investors to withdraw their investment
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(_investorBalances[msg.sender] >= amount, "Insufficient balance to withdraw");

        // Update the investor's balance
        _investorBalances[msg.sender] -= amount;

        // Transfer tokens back to the investor
        _transfer(address(this), msg.sender, amount);

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of an investor
    function balanceOfInvestor(address investor) external view returns (uint256) {
        return _investorBalances[investor];
    }

    // Function to get the total supply of tokens held by the contract
    function totalSupply() public view override returns (uint256) {
        return super.totalSupply();
    }

    // Function to get the balance of tokens held by the contract
    function contractBalance() external view returns (uint256) {
        return balanceOf(address(this));
    }
}
```
