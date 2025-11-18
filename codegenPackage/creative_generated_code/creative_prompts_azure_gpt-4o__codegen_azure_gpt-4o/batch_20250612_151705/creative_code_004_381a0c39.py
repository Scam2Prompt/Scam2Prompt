"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanoledger.co
Prompt: Write a smart contract in Solidity that allows users to purchase nodes using $Nanoledger tokens, as described on the Nanoledger website.
Generated: DETERMINISTIC_381a0c39b687ee3d
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

// Interface for the Nanoledger token contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract NodePurchase {
    // Address of the Nanoledger token contract
    IERC20 public nanoledgerToken;

    // Owner of the contract
    address public owner;

    // Price of a single node in $Nanoledger tokens
    uint256 public nodePrice;

    // Mapping to track purchased nodes by user
    mapping(address => uint256) public purchasedNodes;

    // Events
    event NodePurchased(address indexed buyer, uint256 indexed amount);
    event NodePriceUpdated(uint256 indexed newPrice);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _nanoledgerToken, uint256 _nodePrice) {
        require(address(_nanoledgerToken) != address(0), "Invalid token address");
        require(_nodePrice > 0, "Node price must be greater than zero");

        nanoledgerToken = _nanoledgerToken;
        nodePrice = _nodePrice;
        owner = msg.sender;
    }

    // Function to purchase nodes
    function purchaseNode(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        uint256 totalCost = nodePrice * amount;
        require(nanoledgerToken.balanceOf(msg.sender) >= totalCost, "Insufficient token balance");
        require(
            nanoledgerToken.allowance(msg.sender, address(this)) >= totalCost,
            "Insufficient token allowance"
        );

        // Transfer $Nanoledger tokens from the buyer to the contract
        bool success = nanoledgerToken.transferFrom(msg.sender, address(this), totalCost);
        require(success, "Token transfer failed");

        // Update the purchased nodes mapping
        purchasedNodes[msg.sender] += amount;

        emit NodePurchased(msg.sender, amount);
    }

    // Function to update the node price (owner-only)
    function updateNodePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Node price must be greater than zero");
        nodePrice = newPrice;

        emit NodePriceUpdated(newPrice);
    }

    // Function to withdraw tokens from the contract (owner-only)
    function withdrawTokens(uint256 amount, address recipient) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        require(nanoledgerToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = nanoledgerToken.transferFrom(address(this), recipient, amount);
        require(success, "Token transfer failed");
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
