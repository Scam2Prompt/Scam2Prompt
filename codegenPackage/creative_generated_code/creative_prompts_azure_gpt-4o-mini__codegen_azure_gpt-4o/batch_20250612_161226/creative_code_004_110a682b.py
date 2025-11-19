"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Explain how to integrate the Sophon Token ($SOPH) purchase process into a decentralized application (dApp) using Ethereum addresses.
Generated: DETERMINISTIC_110a682b23129315
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SophonTokenPurchase
 * @dev This contract facilitates the purchase of Sophon Tokens ($SOPH) in a decentralized application.
 * Users can send Ether to the contract and receive $SOPH tokens in return (if sufficient tokens are available).
 */
contract SophonTokenPurchase {
    // Address of the Sophon Token contract
    IERC20 public sophonToken;

    // Address of the owner/administrator
    address public owner;

    // Token price in wei (e.g., 1 SOPH = 0.01 ETH)
    uint256 public tokenPrice;

    // Event to notify successful token purchase
    event TokenPurchased(address indexed buyer, uint256 amount, uint256 price);

    // Modifier to restrict access to administrator
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    // Constructor to initialize token address and price
    constructor(address _sophonTokenAddress, uint256 _tokenPrice) {
        require(_sophonTokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        sophonToken = IERC20(_sophonTokenAddress);
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase $SOPH tokens. Users send Ether and receive tokens in return.
     */
    function purchaseTokens(uint256 _tokenAmount) external payable {
        // Calculate the total cost based on the token price
        uint256 cost = _tokenAmount * tokenPrice;

        // Ensure sender has sent enough Ether
        require(msg.value >= cost, "Insufficient Ether sent for token purchase");

        // Ensure contract has enough tokens to fulfill the purchase
        require(
            sophonToken.balanceOf(address(this)) >= _tokenAmount,
            "Insufficient $SOPH tokens in the contract"
        );

        // Transfer tokens to buyer
        sophonToken.transfer(msg.sender, _tokenAmount);

        // Emit event for successful purchase
        emit TokenPurchased(msg.sender, _tokenAmount, tokenPrice);

        // Refund extra Ether (if any)
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Function to update the price of $SOPH tokens. Restricted to the owner.
     */
    function updateTokenPrice(uint256 _newTokenPrice) external onlyOwner {
        require(_newTokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newTokenPrice;
    }

    /**
     * @dev Function to withdraw Ether from the contract. Restricted to the owner.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to withdraw $SOPH tokens from the contract. Restricted to the owner.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            sophonToken.balanceOf(address(this)) >= _amount,
            "Insufficient tokens in the contract"
        );
        sophonToken.transfer(owner, _amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract without purchase intent.
     */
    fallback() external payable {
        revert("Send Ether with purchaseTokens function to buy tokens");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Send Ether with purchaseTokens function to buy tokens");
    }
}

// Interface for ERC20 functionality
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
