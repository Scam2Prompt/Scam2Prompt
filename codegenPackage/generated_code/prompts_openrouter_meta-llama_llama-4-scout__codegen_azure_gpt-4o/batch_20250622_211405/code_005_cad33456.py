"""
Generated Code Metadata:
========================
Original URL: https://claimtontigertokenapp.pages.dev
Prompt: Write a smart contract code in Solidity (or relevant language) for distributing $TIGER tokens during a Fairlaunch event on TON blockchain.
Generated: DETERMINISTIC_cad334566fd9ae5f
Batch ID: 20250622_211405
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
 * @title FairlaunchTokenDistributor
 * @dev A smart contract for distributing $TIGER tokens during a Fairlaunch event.
 */
contract FairlaunchTokenDistributor {
    // Address of the token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Total tokens available for distribution
    uint256 public totalTokens;

    // Price per token in wei
    uint256 public tokenPrice;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the $TIGER token contract.
     * @param _totalTokens Total tokens available for distribution.
     * @param _tokenPrice Price per token in wei.
     */
    constructor(address _tokenAddress, uint256 _totalTokens, uint256 _tokenPrice) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be greater than zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        tokenAddress = _tokenAddress;
        totalTokens = _totalTokens;
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the Fairlaunch event.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "Insufficient Ether to purchase tokens");
        require(tokensToPurchase <= totalTokens, "Not enough tokens available");

        // Update state
        totalTokens -= tokensToPurchase;
        contributions[msg.sender] += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to withdraw purchased tokens.
     * @param recipient Address to receive the tokens.
     */
    function withdrawTokens(address recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        uint256 tokens = contributions[msg.sender];
        require(tokens > 0, "No tokens to withdraw");

        // Reset contribution
        contributions[msg.sender] = 0;

        // Transfer tokens to the recipient
        (bool success, ) = tokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", recipient, tokens)
        );
        require(success, "Token transfer failed");

        emit TokensWithdrawn(recipient, tokens);
    }

    /**
     * @dev Function to withdraw Ether collected during the Fairlaunch event.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Function to update the token price.
     * @param _newTokenPrice New price per token in wei.
     */
    function updateTokenPrice(uint256 _newTokenPrice) external onlyOwner {
        require(_newTokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newTokenPrice;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {
        purchaseTokens();
    }
}
```
