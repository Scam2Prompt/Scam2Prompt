"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beckeerererer.pages.dev
Prompt: Generate a smart contract in Solidity for a token sale with a presale cap of 1000 ETH and a total supply of 100,000,000 tokens.
Generated: DETERMINISTIC_94aa42aad5d52800
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Token is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10 ** 18; // 100 million tokens with 18 decimal places

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Presale parameters
    uint256 public presaleCap;
    uint256 public totalRaised;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleCapReached();

    // Constructor to initialize the token
    constructor(uint256 _presaleCap) ERC20("MyToken", "MTK") {
        require(_presaleCap > 0, "Presale cap must be greater than 0");
        presaleCap = _presaleCap; // Set presale cap
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract
    }

    // Function to buy tokens during the presale
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised.add(msg.value) <= presaleCap, "Presale cap reached");

        uint256 tokensToBuy = calculateTokenAmount(msg.value);
        require(balanceOf(address(this)) >= tokensToBuy, "Not enough tokens available");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalRaised = totalRaised.add(msg.value);

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, tokensToBuy);

        emit TokensPurchased(msg.sender, tokensToBuy);

        // Check if the presale cap has been reached
        if (totalRaised == presaleCap) {
            emit PresaleCapReached();
        }
    }

    // Calculate the amount of tokens for a given amount of ETH (1 ETH = 1000 tokens)
    function calculateTokenAmount(uint256 ethAmount) public pure returns (uint256) {
        return ethAmount.mul(1000); // 1000 tokens per 1 ETH
    }

    // Function to withdraw ether from the contract (only owner can call)
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    // Function to get the remaining tokens available for sale
    function remainingTokens() external view returns (uint256) {
        return balanceOf(address(this));
    }
}
```
