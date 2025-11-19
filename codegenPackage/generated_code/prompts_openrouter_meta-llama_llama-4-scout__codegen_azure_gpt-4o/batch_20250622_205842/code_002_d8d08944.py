"""
Generated Code Metadata:
========================
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Generate a smart contract code for a token sale platform, inspired by WienerAI's presale mechanism and token distribution.
Generated: DETERMINISTIC_d8d089446d8c15da
Batch ID: 20250622_205842
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
 * @title TokenSalePlatform
 * @dev A smart contract for managing token presales and distribution inspired by WienerAI's mechanism.
 */
contract TokenSalePlatform {
    // Token details
    string public constant name = "WienerAI Token";
    string public constant symbol = "WAI";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Address of the contract owner
    address public owner;

    // Token price in wei (1 ETH = tokenPrice tokens)
    uint256 public tokenPrice;

    // Mapping to track balances of participants
    mapping(address => uint256) public balances;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _totalSupply Total supply of tokens.
     * @param _tokenPrice Price of each token in wei.
     */
    constructor(uint256 _totalSupply, uint256 _tokenPrice) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        owner = msg.sender;
        totalSupply = _totalSupply;
        tokenPrice = _tokenPrice;

        // Assign all tokens to the owner initially
        balances[owner] = _totalSupply;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "Insufficient ether to purchase tokens");
        require(balances[owner] >= tokensToPurchase, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        balances[owner] -= tokensToPurchase;
        balances[msg.sender] += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to distribute tokens to a specific address.
     * @param recipient Address to receive the tokens.
     * @param amount Number of tokens to distribute.
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(balances[owner] >= amount, "Not enough tokens available for distribution");

        // Transfer tokens to the recipient
        balances[owner] -= amount;
        balances[recipient] += amount;

        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Function to withdraw ether collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer ether to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    fallback() external payable {
        revert("Direct ether transfers are not allowed");
    }

    /**
     * @dev Receive function to handle ether sent to the contract.
     */
    receive() external payable {
        revert("Direct ether transfers are not allowed");
    }
}
```
