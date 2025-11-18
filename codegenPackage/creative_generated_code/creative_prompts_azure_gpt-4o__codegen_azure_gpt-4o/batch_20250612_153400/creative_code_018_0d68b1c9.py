"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Generate a Solidity smart contract for DOGE20 presale, ensuring fair token distribution and wallet validation.
Generated: DETERMINISTIC_0d68b1c9cacbf761
Batch ID: 20250612_153400
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
 * @title DOGE20 Presale Contract
 * @dev A smart contract to manage the presale of DOGE20 tokens ensuring fair distribution and wallet validation.
 */
contract DOGE20Presale {
    // Address of the token being sold
    address public tokenAddress;

    // Address of the owner (admin) of the contract
    address public owner;

    // Total supply allocated for the presale
    uint256 public presaleSupply;

    // Token price in wei
    uint256 public tokenPrice;

    // Maximum amount of tokens a wallet can purchase
    uint256 public maxTokensPerWallet;

    // Total tokens sold
    uint256 public totalTokensSold;

    // Mapping to track wallet purchases
    mapping(address => uint256) private purchases;

    // Event for token purchase
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the DOGE20 token contract.
     * @param _presaleSupply Total tokens allocated for presale.
     * @param _tokenPrice Price of each token in wei.
     * @param _maxTokensPerWallet Maximum tokens a wallet can purchase.
     */
    constructor(
        address _tokenAddress,
        uint256 _presaleSupply,
        uint256 _tokenPrice,
        uint256 _maxTokensPerWallet
    ) {
        require(_tokenAddress != address(0), "Invalid token address.");
        require(_presaleSupply > 0, "Presale supply must be greater than zero.");
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        require(_maxTokensPerWallet > 0, "Max tokens per wallet must be greater than zero.");

        tokenAddress = _tokenAddress;
        owner = msg.sender;
        presaleSupply = _presaleSupply;
        tokenPrice = _tokenPrice;
        maxTokensPerWallet = _maxTokensPerWallet;
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero.");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent.");
        require(totalTokensSold + amount <= presaleSupply, "Not enough tokens left for presale.");
        require(purchases[msg.sender] + amount <= maxTokensPerWallet, "Purchase exceeds wallet limit.");

        // Update state
        purchases[msg.sender] += amount;
        totalTokensSold += amount;

        // Transfer tokens to buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, amount),
            "Token transfer failed."
        );

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw collected Ether.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Ether transfer failed.");
    }

    /**
     * @dev Allows the owner to update the token price.
     * @param newPrice New token price in wei.
     */
    function updateTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero.");
        tokenPrice = newPrice;
    }

    /**
     * @dev Allows the owner to update the maximum tokens per wallet.
     * @param newLimit New maximum tokens per wallet.
     */
    function updateMaxTokensPerWallet(uint256 newLimit) external onlyOwner {
        require(newLimit > 0, "Limit must be greater than zero.");
        maxTokensPerWallet = newLimit;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed.");
    }

    /**
     * @dev Receive function for Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed.");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
