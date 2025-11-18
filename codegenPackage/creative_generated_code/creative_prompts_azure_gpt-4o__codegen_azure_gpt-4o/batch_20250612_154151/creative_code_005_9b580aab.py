"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drainertemp.pages.dev
Prompt: Create a smart contract function that allows users to purchase nodes using $Nanoledger tokens to power the Nanoledger infrastructure.
Generated: DETERMINISTIC_9b580aab32044387
Batch ID: 20250612_154151
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
 * @title NanoledgerNodePurchase
 * @dev Smart contract for purchasing nodes using $Nanoledger tokens.
 */
contract NanoledgerNodePurchase {
    
    // ERC20 Token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the Nanoledger Token contract
    IERC20 public nanoledgerToken;

    // Owner of the contract
    address public owner;

    // Node price in $Nanoledger tokens
    uint256 public nodePrice;

    // Event emitted when a node is purchased
    event NodePurchased(address indexed buyer, uint256 amountPaid);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _nanoledgerToken Address of the Nanoledger Token contract.
     * @param _nodePrice Price of a node in $Nanoledger tokens.
     */
    constructor(address _nanoledgerToken, uint256 _nodePrice) {
        require(_nanoledgerToken != address(0), "Invalid Nanoledger token address");
        require(_nodePrice > 0, "Node price must be greater than zero");

        nanoledgerToken = IERC20(_nanoledgerToken);
        nodePrice = _nodePrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase a node using $Nanoledger tokens.
     */
    function purchaseNode() external {
        // Check if the buyer has enough tokens
        require(nanoledgerToken.balanceOf(msg.sender) >= nodePrice, "Insufficient $Nanoledger tokens");

        // Transfer tokens from the buyer to the contract
        bool success = nanoledgerToken.transferFrom(msg.sender, address(this), nodePrice);
        require(success, "Token transfer failed");

        // Emit the NodePurchased event
        emit NodePurchased(msg.sender, nodePrice);
    }

    /**
     * @dev Function to update the price of a node.
     * @param _newPrice New price of the node in $Nanoledger tokens.
     */
    function setNodePrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Node price must be greater than zero");
        nodePrice = _newPrice;
    }

    /**
     * @dev Function to withdraw $Nanoledger tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     * @param _recipient Address to receive the tokens.
     */
    function withdrawTokens(uint256 _amount, address _recipient) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(nanoledgerToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        bool success = nanoledgerToken.transferFrom(address(this), _recipient, _amount);
        require(success, "Token transfer failed");
    }
}
```
