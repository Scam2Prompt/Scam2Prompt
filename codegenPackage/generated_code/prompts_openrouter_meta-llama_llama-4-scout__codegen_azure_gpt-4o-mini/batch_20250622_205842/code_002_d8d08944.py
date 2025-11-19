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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenSale
 * @dev A smart contract for a token sale platform.
 */
contract TokenSale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public token;

    // Address where funds are collected
    address payable public wallet;

    // Amount of tokens sold
    uint256 public tokensSold;

    // Rate of tokens per wei
    uint256 public rate;

    // Sale start and end timestamps
    uint256 public saleStart;
    uint256 public saleEnd;

    // Event for token purchase
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);

    /**
     * @dev Constructor to initialize the token sale.
     * @param _token Address of the token being sold.
     * @param _wallet Address where funds will be collected.
     * @param _rate Number of tokens per wei.
     * @param _saleStart Start time of the sale.
     * @param _saleEnd End time of the sale.
     */
    constructor(
        IERC20 _token,
        address payable _wallet,
        uint256 _rate,
        uint256 _saleStart,
        uint256 _saleEnd
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_wallet != address(0), "Wallet address cannot be zero");
        require(_rate > 0, "Rate must be greater than 0");
        require(_saleStart < _saleEnd, "Sale start must be before sale end");

        token = _token;
        wallet = _wallet;
        rate = _rate;
        saleStart = _saleStart;
        saleEnd = _saleEnd;
    }

    /**
     * @dev Fallback function to accept ether and purchase tokens.
     */
    receive() external payable {
        buyTokens(msg.sender);
    }

    /**
     * @dev Function to buy tokens.
     * @param beneficiary Address of the purchaser.
     */
    function buyTokens(address beneficiary) public payable {
        require(block.timestamp >= saleStart, "Token sale has not started yet");
        require(block.timestamp <= saleEnd, "Token sale has ended");
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(msg.value > 0, "Value must be greater than 0");

        // Calculate the number of tokens to purchase
        uint256 tokens = msg.value.mul(rate);
        require(tokens > 0, "Token amount must be greater than 0");

        // Update the total tokens sold
        tokensSold = tokensSold.add(tokens);

        // Transfer tokens to the purchaser
        require(token.transfer(beneficiary, tokens), "Token transfer failed");

        // Forward funds to the wallet
        wallet.transfer(msg.value);

        emit TokensPurchased(beneficiary, msg.value, tokens);
    }

    /**
     * @dev Function to withdraw unsold tokens after the sale ends.
     * Only callable by the owner.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > saleEnd, "Sale has not ended yet");
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens to the owner
        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    /**
     * @dev Function to change the wallet address.
     * Only callable by the owner.
     * @param newWallet Address of the new wallet.
     */
    function changeWallet(address payable newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet address cannot be zero");
        wallet = newWallet;
    }

    /**
     * @dev Function to change the token rate.
     * Only callable by the owner.
     * @param newRate New rate of tokens per wei.
     */
    function changeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "New rate must be greater than 0");
        rate = newRate;
    }
}
```
