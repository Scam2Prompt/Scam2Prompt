"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate a smart contract in Solidity for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens based on the snapshot of Bitcoin and Ethereum wallets.
Generated: DETERMINISTIC_b6ae8faefd8dbcf0
Batch ID: 20250612_160600
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

/**
 * @title ZiberICO
 * @dev A smart contract for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens
 * based on a snapshot of Bitcoin and Ethereum wallets.
 */
contract ZiberICO {
    // Token details
    string public constant name = "Ziber Token";
    string public constant symbol = "ZBR";
    uint8 public constant decimals = 18;

    // Total supply of Ziber tokens
    uint256 public totalSupply;

    // Token balances
    mapping(address => uint256) public balances;

    // Owner of the contract
    address public owner;

    // ICO parameters
    uint256 public constant tokenPrice = 0.001 ether; // Price per token in ETH
    uint256 public constant maxTokens = 1000000 * (10 ** uint256(decimals)); // Maximum tokens available for sale
    uint256 public tokensSold;

    // Snapshot of Bitcoin and Ethereum wallets
    mapping(address => uint256) public snapshotBalances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor
    constructor(uint256 _totalSupply) {
        require(_totalSupply <= maxTokens, "Total supply exceeds maximum tokens");
        owner = msg.sender;
        totalSupply = _totalSupply;
        balances[owner] = _totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Fallback function to accept ETH payments.
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Function to buy Ziber tokens during the ICO.
     */
    function buyTokens() public payable {
        require(msg.value > 0, "Ether value must be greater than zero");
        uint256 tokensToBuy = msg.value / tokenPrice;
        require(tokensSold + tokensToBuy <= totalSupply, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        balances[msg.sender] += tokensToBuy;
        balances[owner] -= tokensToBuy;
        tokensSold += tokensToBuy;

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Function to distribute tokens based on the snapshot of Bitcoin and Ethereum wallets.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts corresponding to each recipient.
     */
    function distributeTokens(address[] memory recipients, uint256[] memory amounts) public onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts arrays must have the same length");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(balances[owner] >= amount, "Not enough tokens available for distribution");
            balances[recipient] += amount;
            balances[owner] -= amount;

            emit TokensDistributed(recipient, amount);
        }
    }

    /**
     * @dev Function to withdraw ETH collected during the ICO.
     */
    function withdrawFunds() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to check the balance of an address.
     * @param account Address to check the balance of.
     * @return Balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }
}
```
