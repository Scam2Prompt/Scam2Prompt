"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.web.app
Prompt: How can I implement a presale mechanism for a memecoin on Ethereum, as described on the Owy website?
Generated: DETERMINISTIC_27987bba69c57572
Batch ID: 20250612_155242
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
 * @title MemecoinPresale
 * @dev Implements a presale mechanism for a memecoin on Ethereum.
 */
contract MemecoinPresale {
    // Token details
    address public tokenAddress; // Address of the memecoin contract
    uint256 public tokenPriceInWei; // Price per token in Wei
    uint256 public presaleCap; // Maximum amount of tokens available for presale
    uint256 public tokensSold; // Total tokens sold during presale
    address public owner; // Contract owner

    // Mapping to track buyers' contributions during presale
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the presale details.
     * @param _tokenAddress Address of the memecoin contract.
     * @param _tokenPriceInWei Price per token in Wei.
     * @param _presaleCap Maximum number of tokens available for presale.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPriceInWei,
        uint256 _presaleCap
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPriceInWei > 0, "Token price must be greater than zero");
        require(_presaleCap > 0, "Presale cap must be greater than zero");

        tokenAddress = _tokenAddress;
        tokenPriceInWei = _tokenPriceInWei;
        presaleCap = _presaleCap;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during presale.
     * The buyer sends ETH, and tokens are transferred to them.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "You must send ETH to purchase tokens");
        uint256 tokenAmount = msg.value / tokenPriceInWei; // Calculate token amount
        require(tokenAmount > 0, "Insufficient ETH for token purchase");
        require(tokensSold + tokenAmount <= presaleCap, "Presale cap reached");

        // Transfer tokens to the buyer
        IERC20(tokenAddress).transfer(msg.sender, tokenAmount);

        // Update presale state
        tokensSold += tokenAmount;
        contributions[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Function to withdraw funds collected during presale.
     * Can only be called by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Function to update the token price.
     * Can only be called by the owner.
     * @param _newTokenPriceInWei The new price of the token in Wei.
     */
    function updateTokenPrice(uint256 _newTokenPriceInWei) external onlyOwner {
        require(_newTokenPriceInWei > 0, "Token price must be greater than zero");
        tokenPriceInWei = _newTokenPriceInWei;
    }

    /**
     * @dev Function to update the presale cap.
     * Can only be called by the owner.
     * @param _newPresaleCap The new presale cap.
     */
    function updatePresaleCap(uint256 _newPresaleCap) external onlyOwner {
        require(_newPresaleCap >= tokensSold, "New presale cap must be greater than or equal to tokens sold");
        presaleCap = _newPresaleCap;
    }

    /**
     * @dev Fallback function to reject any accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Fallback function to reject invalid calls.
     */
    fallback() external payable {
        revert("Invalid call");
    }
}

/**
 * @title IERC20
 * @dev Minimal interface for ERC20 token functionality.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
