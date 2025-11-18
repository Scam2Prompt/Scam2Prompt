"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berrycoinerc.vip
Prompt: Generate code for a decentralized application (DApp) that allows users to buy $BERRY tokens directly from their Ethereum wallets.
Generated: DETERMINISTIC_f77744ea433199df
Batch ID: 20250612_153925
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
 * @title BerryTokenSale
 * @dev A decentralized application (DApp) for buying $BERRY tokens directly from Ethereum wallets.
 */
contract BerryTokenSale {
    // Address of the token contract (ERC20)
    IERC20 public berryToken;

    // Address of the owner of the contract
    address public owner;

    // Token price in wei (1 ETH = X $BERRY tokens)
    uint256 public tokenPrice;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokenPriceUpdated(uint256 oldPrice, uint256 newPrice);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _berryToken Address of the $BERRY token contract.
     * @param _tokenPrice Initial price of $BERRY tokens in wei.
     */
    constructor(IERC20 _berryToken, uint256 _tokenPrice) {
        require(address(_berryToken) != address(0), "Invalid token contract address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        berryToken = _berryToken;
        owner = msg.sender;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Allows users to buy $BERRY tokens by sending Ether.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the number of tokens to send
        uint256 tokenAmount = (msg.value * 1e18) / tokenPrice; // Adjust for decimals

        // Ensure the contract has enough tokens to transfer
        require(berryToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        berryToken.transfer(msg.sender, tokenAmount);

        // Emit event
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Updates the token price, callable only by the contract owner.
     * @param _newPrice The new token price in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");

        uint256 oldPrice = tokenPrice;
        tokenPrice = _newPrice;

        emit TokenPriceUpdated(oldPrice, _newPrice);
    }

    /**
     * @dev Allows the owner to withdraw Ether collected from token sales.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Ether transfer failed");
    }

    /**
     * @dev Allows the owner to transfer unsold tokens back to their wallet.
     */
    function withdrawUnsoldTokens(uint256 _amount) external onlyOwner {
        require(berryToken.balanceOf(address(this)) >= _amount, "Not enough tokens available");

        berryToken.transfer(owner, _amount);
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    receive() external payable {
        // Allow users to send Ether to buy tokens
        buyTokens();
    }

    /**
     * @dev Fallback function (deprecated in Solidity >= 0.6.0).
     */
    fallback() external payable {
        // Allow users to send Ether to buy tokens
        buyTokens();
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
