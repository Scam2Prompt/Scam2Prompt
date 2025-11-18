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

/**
 * @title TokenPresaleContract
 * @dev This contract handles token presale, claiming tokens post-presale, and multi-chain bridging.
 */
contract TokenPresaleContract {
    // State variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the token for presale
    uint256 public presaleRate; // Number of tokens per 1 ETH
    uint256 public presaleStartTime; // Start time of presale
    uint256 public presaleEndTime; // End time of presale
    uint256 public totalTokensSold; // Total tokens sold during presale
    mapping(address => uint256) public claimableTokens; // Mapping to track claimable tokens per user

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event TokensBridged(address indexed user, uint256 amount, string destinationChain);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        _;
    }

    // Constructor
    constructor(
        address _tokenAddress,
        uint256 _presaleRate,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleRate > 0, "Presale rate must be greater than zero");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time range");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleRate = _presaleRate;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
    }

    // Function to buy tokens during presale
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "Ether amount must be greater than zero");

        // Calculate token amount based on presale rate
        uint256 tokensToPurchase = msg.value * presaleRate;

        // Track claimable tokens for the buyer
        claimableTokens[msg.sender] += tokensToPurchase;

        // Update total tokens sold
        totalTokensSold += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    // Function to claim tokens after presale
    function claimTokens() external presaleEnded {
        uint256 tokens = claimableTokens[msg.sender];
        require(tokens > 0, "No tokens to claim");

        // Reset claimable tokens to zero
        claimableTokens[msg.sender] = 0;

        // Transfer tokens to the claimer
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokens),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, tokens);
    }

    // Function to bridge tokens to another chain
    function bridgeTokens(uint256 amount, string calldata destinationChain) external {
        require(amount > 0, "Amount must be greater than zero");
        require(claimableTokens[msg.sender] >= amount, "Insufficient claimable tokens");

        // Reduce claimable tokens of the user
        claimableTokens[msg.sender] -= amount;

        // Emit bridging event (integration with token bridge mechanism to be handled off-chain)
        emit TokensBridged(msg.sender, amount, destinationChain);
    }

    // Function for the owner to withdraw ETH collected during presale
    function withdrawFunds() external onlyOwner presaleEnded {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Function for the owner to withdraw unsold tokens
    function withdrawUnsoldTokens() external onlyOwner presaleEnded {
        uint256 unsoldTokens = IERC20(tokenAddress).balanceOf(address(this)) - totalTokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        require(
            IERC20(tokenAddress).transfer(owner, unsoldTokens),
            "Token transfer failed"
        );
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
