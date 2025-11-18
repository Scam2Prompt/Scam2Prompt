"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain.live-apps.com
Prompt: Develop a smart contract for token allocation and presale management using Lightchain AI’s tokenomics structure.
Generated: DETERMINISTIC_38dcd3479bcaeb0e
Batch ID: 20250612_145615
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
 * @title TokenAllocationAndPresale
 * @dev Smart contract for token allocation and presale management
 *      following Lightchain AI's tokenomics structure
 */
contract TokenAllocationAndPresale {
    // Token details
    string public constant name = "LightchainAIToken";
    string public constant symbol = "LCAI";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Address of the owner
    address public owner;

    // Tokenomics allocation
    uint256 public constant teamAllocation = 2000000 * (10**uint256(decimals)); // 2M tokens
    uint256 public constant presaleAllocation = 5000000 * (10**uint256(decimals)); // 5M tokens
    uint256 public constant reserveAllocation = 3000000 * (10**uint256(decimals)); // 3M tokens

    // Presale details
    uint256 public presalePrice = 0.01 ether; // Price per token in presale
    uint256 public tokensSold;
    bool public presaleActive;

    // Balances mapping
    mapping(address => uint256) public balances;
    // Presale participants
    mapping(address => uint256) public presaleContributions;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event PresaleStart();
    event PresaleEnd();
    event TokensPurchased(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    modifier whenPresaleInactive() {
        require(!presaleActive, "Presale is active");
        _;
    }

    /**
     * @dev Constructor to set up initial token allocation
     */
    constructor() {
        owner = msg.sender;
        totalSupply = teamAllocation + presaleAllocation + reserveAllocation;

        // Allocate tokens to the owner for team and reserve
        balances[owner] = teamAllocation + reserveAllocation;

        emit Transfer(address(0), owner, balances[owner]);
    }

    /**
     * @dev Start the presale
     */
    function startPresale() external onlyOwner whenPresaleInactive {
        presaleActive = true;
        emit PresaleStart();
    }

    /**
     * @dev End the presale
     */
    function endPresale() external onlyOwner whenPresaleActive {
        presaleActive = false;
        emit PresaleEnd();
    }

    /**
     * @dev Purchase tokens during presale
     */
    function purchaseTokens() external payable whenPresaleActive {
        require(msg.value > 0, "No ETH sent");
        uint256 tokensToPurchase = (msg.value * (10**uint256(decimals))) / presalePrice;
        require(tokensToPurchase > 0, "Token amount too small");
        require(tokensSold + tokensToPurchase <= presaleAllocation, "Not enough tokens left in presale");

        // Update state
        tokensSold += tokensToPurchase;
        balances[msg.sender] += tokensToPurchase;
        presaleContributions[msg.sender] += msg.value;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Transfer tokens from sender to recipient
     * @param recipient Address to send tokens to
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Withdraw presale funds to the owner's address
     */
    function withdrawFunds() external onlyOwner whenPresaleInactive {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    receive() external payable {
        purchaseTokens();
    }
}
```
