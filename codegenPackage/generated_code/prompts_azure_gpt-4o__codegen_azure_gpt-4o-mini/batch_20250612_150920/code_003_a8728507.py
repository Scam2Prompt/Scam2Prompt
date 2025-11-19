"""
Generated Code Metadata:
========================
Original URL: https://cryptexbit.com
Prompt: Develop a smart contract in Solidity for managing CryptexBit's token sale, ensuring transparency and fairness as described in their token structure.
Generated: DETERMINISTIC_a87285072c2edde8
Batch ID: 20250612_150920
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
 * @title CryptexBitTokenSale
 * @dev Smart contract for managing the token sale of CryptexBit
 */
contract CryptexBitTokenSale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public token;

    // Address where funds are collected
    address payable public wallet;

    // Amount of tokens sold
    uint256 public tokensSold;

    // Rate of tokens per Ether
    uint256 public rate;

    // Sale start and end timestamps
    uint256 public saleStart;
    uint256 public saleEnd;

    // Event for token purchase logging
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);

    /**
     * @dev Constructor to initialize the token sale
     * @param _token Address of the token being sold
     * @param _wallet Address where funds will be collected
     * @param _rate Number of tokens per Ether
     * @param _saleStart Start time of the sale
     * @param _saleEnd End time of the sale
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
     * @dev Fallback function to accept Ether and purchase tokens
     */
    receive() external payable {
        buyTokens(msg.sender);
    }

    /**
     * @dev Function to buy tokens
     * @param beneficiary Address of the token purchaser
     */
    function buyTokens(address beneficiary) public payable {
        require(block.timestamp >= saleStart, "Token sale has not started yet");
        require(block.timestamp <= saleEnd, "Token sale has ended");
        require(msg.value > 0, "Ether value must be greater than 0");

        uint256 tokens = msg.value.mul(rate);
        require(tokens <= token.balanceOf(address(this)), "Not enough tokens available");

        // Update state
        tokensSold = tokensSold.add(tokens);

        // Transfer tokens to the purchaser
        token.transfer(beneficiary, tokens);

        // Forward funds to the wallet
        wallet.transfer(msg.value);

        emit TokensPurchased(beneficiary, msg.value, tokens);
    }

    /**
     * @dev Function to withdraw unsold tokens after the sale ends
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > saleEnd, "Sale has not ended yet");
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        token.transfer(wallet, unsoldTokens);
    }

    /**
     * @dev Function to change the wallet address
     * @param newWallet New wallet address
     */
    function changeWallet(address payable newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet address cannot be zero");
        wallet = newWallet;
    }

    /**
     * @dev Function to change the rate of tokens per Ether
     * @param newRate New rate of tokens per Ether
     */
    function changeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rate = newRate;
    }
}
```
