"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appwienerclaim.pages.dev
Prompt: Recommend security best practices for implementing custom Web3 smart contracts for token presales and staking, as described in WienerAI.
Generated: DETERMINISTIC_9f331029836eb011
Batch ID: 20250612_151158
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TokenPresale
 * @dev A smart contract for token presales and staking
 */
contract TokenPresale is Ownable, ReentrancyGuard {
    IERC20 public token; // The token being sold in the presale
    uint256 public presaleEnd; // Timestamp when the presale ends
    uint256 public tokenPrice; // Price of one token in wei
    mapping(address => uint256) public contributions; // User contributions

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 totalContributions);

    /**
     * @dev Constructor to initialize the presale
     * @param _token Address of the token being sold
     * @param _duration Duration of the presale in seconds
     * @param _tokenPrice Price of the token in wei
     */
    constructor(address _token, uint256 _duration, uint256 _tokenPrice) {
        token = IERC20(_token);
        presaleEnd = block.timestamp + _duration;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase tokens during the presale
     * @param amount Amount of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable nonReentrant {
        require(block.timestamp < presaleEnd, "Presale has ended");
        require(msg.value == amount * tokenPrice, "Incorrect ETH amount sent");
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens available");

        contributions[msg.sender] += amount;
        emit TokensPurchased(msg.sender, amount);
        
        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Function to end the presale and withdraw funds
     */
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale still ongoing");
        
        uint256 totalContributions = address(this).balance;
        payable(owner()).transfer(totalContributions);

        emit PresaleEnded(totalContributions);
    }

    /**
     * @dev Function to withdraw tokens that are not sold
     * @param amount Amount of tokens to withdraw
     */
    function withdrawUnsoldTokens(uint256 amount) external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale still ongoing");
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens available");

        token.transfer(owner(), amount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
