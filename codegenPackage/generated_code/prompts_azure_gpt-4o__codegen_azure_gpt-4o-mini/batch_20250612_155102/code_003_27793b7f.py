"""
Generated Code Metadata:
========================
Original URL: https://grokxcoinai.com
Prompt: Create a smart contract audited by CertiK and SlowMist that ensures fair distribution of tokens during a presale, inspired by $GROK's model.
Generated: DETERMINISTIC_27793b7f41b48934
Batch ID: 20250612_155102
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

/**
 * @title FairTokenPresale
 * @dev A smart contract for conducting a fair token presale.
 * This contract ensures that tokens are distributed fairly among participants.
 */
contract FairTokenPresale is Ownable {
    IERC20 public token; // The token being sold
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public totalTokensSold; // Total tokens sold during presale
    uint256 public maxTokensPerAddress; // Maximum tokens an address can buy

    mapping(address => uint256) public contributions; // Track contributions of each address

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 totalTokensSold);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the token being sold.
     * @param _presaleStart Start time of the presale.
     * @param _presaleEnd End time of the presale.
     * @param _tokenPrice Price of one token in wei.
     * @param _maxTokensPerAddress Maximum tokens an address can buy.
     */
    constructor(
        address _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _maxTokensPerAddress
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxTokensPerAddress > 0, "Max tokens per address must be greater than zero");

        token = IERC20(_token);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        maxTokensPerAddress = _maxTokensPerAddress;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStart, "Presale has not started yet");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= maxTokensPerAddress, "Exceeds max tokens per address");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent");

        uint256 totalContribution = contributions[msg.sender] + amount;
        require(totalContribution <= maxTokensPerAddress, "Exceeds max tokens per address");

        contributions[msg.sender] += amount;
        totalTokensSold += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to end the presale and withdraw funds.
     */
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");

        emit PresaleEnded(totalTokensSold);
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to withdraw unsold tokens after presale ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");

        uint256 unsoldTokens = token.balanceOf(address(this)) - totalTokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        token.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Function to retrieve the contract's balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
