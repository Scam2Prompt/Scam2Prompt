"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-24m.pages.dev
Prompt: Write a Solidity contract for a token presale similar to Dogeverse, including functionality for claiming tokens post-presale and bridging them across multiple chains.
Generated: DETERMINISTIC_59af1c93b307421e
Batch ID: 20250612_151207
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenPresale
 * @dev A contract for conducting a token presale with functionality for claiming tokens post-presale
 */
contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // Token to be sold in the presale
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public tokenPrice; // Price in wei per token
    uint256 public totalTokens; // Total tokens available for presale
    uint256 public tokensSold; // Total tokens sold during the presale

    // Mapping of addresses to their purchased token amounts
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event PresaleFinalized();

    // Modifier to check if presale is active
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Modifier to check if presale has ended
    modifier onlyAfterPresale() {
        require(block.timestamp > presaleEnd, "Presale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract
     * @param _token Address of the ERC20 token to be sold
     * @param _start Timestamp when the presale starts
     * @param _end Timestamp when the presale ends
     * @param _price Price of the token in wei
     * @param _totalTokens Total amount of tokens available for presale
     */
    constructor(IERC20 _token, uint256 _start, uint256 _end, uint256 _price, uint256 _totalTokens) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_start < _end, "Start time must be before end time");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        token = _token;
        presaleStart = _start;
        presaleEnd = _end;
        tokenPrice = _price;
        totalTokens = _totalTokens;
    }

    /**
     * @dev Function to purchase tokens during presale
     */
    function buyTokens(uint256 amount) external payable onlyDuringPresale {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount.mul(tokenPrice), "Incorrect Ether amount sent");
        require(tokensSold.add(amount) <= totalTokens, "Not enough tokens left for sale");

        contributions[msg.sender] = contributions[msg.sender].add(amount);
        tokensSold = tokensSold.add(amount);

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to claim tokens after the presale has ended
     */
    function claimTokens() external onlyAfterPresale {
        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No tokens to claim");

        // Reset contribution to prevent re-entrancy and double claims
        contributions[msg.sender] = 0;

        // Transfer tokens to the claimer
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to finalize the presale (allow withdrawing leftover tokens)
     */
    function finalizePresale() external onlyOwner onlyAfterPresale {
        uint256 unsoldTokens = totalTokens.sub(tokensSold);
        if (unsoldTokens > 0) {
            // Transfer unsold tokens back to owner
            require(token.transfer(owner(), unsoldTokens), "Transfer of unsold tokens failed");
        }
        emit PresaleFinalized();
    }

    /**
     * @dev Function to withdraw Ether from the contract
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
