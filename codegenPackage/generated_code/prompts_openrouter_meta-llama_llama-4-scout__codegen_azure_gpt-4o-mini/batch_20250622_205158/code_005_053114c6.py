"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: Develop a smart contract code for an Initial MEVerse Offering (IMO) function, inspired by the MEVerse DEX platform.
Generated: DETERMINISTIC_053114c6e1f3fd86
Batch ID: 20250622_205158
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

// Interface for the MEVerse token
interface IMEVToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Initial MEVerse Offering (IMO) contract
contract InitialMEVerseOffering is Ownable {
    using SafeMath for uint256;

    // State variables
    IMEVToken public meverseToken; // MEVerse token contract
    uint256 public tokenPrice; // Price of one MEVerse token in wei
    uint256 public totalTokens; // Total tokens available for the IMO
    uint256 public tokensSold; // Total tokens sold during the IMO
    mapping(address => uint256) public contributions; // User contributions

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _meverseToken, uint256 _tokenPrice, uint256 _totalTokens) {
        require(_meverseToken != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        meverseToken = IMEVToken(_meverseToken);
        tokenPrice = _tokenPrice;
        totalTokens = _totalTokens;
    }

    // Function to purchase tokens
    function buyTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount.mul(tokenPrice), "Incorrect Ether value sent");
        require(tokensSold.add(_amount) <= totalTokens, "Not enough tokens available");

        // Update state
        tokensSold = tokensSold.add(_amount);
        contributions[msg.sender] = contributions[msg.sender].add(msg.value);

        // Mint tokens to the buyer
        meverseToken.mint(msg.sender, _amount);

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        // Transfer Ether to the owner
        payable(owner()).transfer(balance);

        emit TokensWithdrawn(owner(), balance);
    }

    // Function to get the remaining tokens available for sale
    function remainingTokens() external view returns (uint256) {
        return totalTokens.sub(tokensSold);
    }

    // Function to get the contribution of a specific address
    function getContribution(address _contributor) external view returns (uint256) {
        return contributions[_contributor];
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
