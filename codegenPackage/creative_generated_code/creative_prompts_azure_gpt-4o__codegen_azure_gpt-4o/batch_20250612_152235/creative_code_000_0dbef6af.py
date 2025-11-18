"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchaincoin-presale.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the Onchain Coin presale, including features like soft cap, hard cap, minimum and maximum buy limits, and token claim functionality.
Generated: DETERMINISTIC_0dbef6af105eb540
Batch ID: 20250612_152235
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
 * @title TokenPresale
 * @dev This contract manages a token presale with soft cap, hard cap, buy limits, and token claim functionality.
 */
contract TokenPresale {
    // Presale parameters
    uint256 public softCap; // Minimum amount of ETH required for presale success
    uint256 public hardCap; // Maximum amount of ETH that can be raised
    uint256 public minBuyLimit; // Minimum ETH a user can contribute
    uint256 public maxBuyLimit; // Maximum ETH a user can contribute
    uint256 public startTime; // Presale start time (UNIX timestamp)
    uint256 public endTime;   // Presale end time (UNIX timestamp)
    
    // Token information
    address public tokenAddress; // Address of the token being sold
    uint256 public tokenRate;    // Number of tokens per ETH contributed

    // State variables
    address public owner; // Address of the presale owner
    uint256 public totalRaised; // Total ETH raised during presale
    bool public finalized; // Flag to indicate if the presale has been finalized
    mapping(address => uint256) public contributions; // Tracks ETH contributions per address
    mapping(address => uint256) public tokensClaimable; // Tracks claimable tokens per address

    // Events
    event ContributionMade(address indexed contributor, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event PresaleFinalized(bool success);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Presale is not active");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > endTime, "Presale has not ended");
        _;
    }

    modifier notFinalized() {
        require(!finalized, "Presale is already finalized");
        _;
    }

    // Constructor
    constructor(
        uint256 _softCap,
        uint256 _hardCap,
        uint256 _minBuyLimit,
        uint256 _maxBuyLimit,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _tokenRate,
        address _tokenAddress
    ) {
        require(_softCap > 0, "Soft cap must be greater than 0");
        require(_hardCap > _softCap, "Hard cap must be greater than soft cap");
        require(_minBuyLimit > 0, "Minimum buy limit must be greater than 0");
        require(_maxBuyLimit > _minBuyLimit, "Maximum buy limit must be greater than minimum buy limit");
        require(_startTime < _endTime, "Start time must be before end time");
        require(_tokenRate > 0, "Token rate must be greater than 0");
        require(_tokenAddress != address(0), "Invalid token address");

        softCap = _softCap;
        hardCap = _hardCap;
        minBuyLimit = _minBuyLimit;
        maxBuyLimit = _maxBuyLimit;
        startTime = _startTime;
        endTime = _endTime;
        tokenRate = _tokenRate;
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    // Function to contribute ETH to the presale
    function contribute() external payable presaleActive {
        require(msg.value >= minBuyLimit, "Contribution is below the minimum limit");
        require(msg.value <= maxBuyLimit, "Contribution exceeds the maximum limit");
        require(totalRaised + msg.value <= hardCap, "Contribution exceeds hard cap");

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        // Calculate and update claimable tokens
        uint256 tokensToClaim = msg.value * tokenRate;
        tokensClaimable[msg.sender] += tokensToClaim;

        emit ContributionMade(msg.sender, msg.value);
    }

    // Function to claim tokens after presale ends
    function claimTokens() external presaleEnded notFinalized {
        require(contributions[msg.sender] > 0, "No contributions made");
        require(tokensClaimable[msg.sender] > 0, "No tokens to claim");

        uint256 tokensToClaim = tokensClaimable[msg.sender];
        tokensClaimable[msg.sender] = 0;

        // Transfer tokens to the claimer
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokensToClaim),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, tokensToClaim);
    }

    // Function to finalize the presale
    function finalizePresale() external onlyOwner presaleEnded notFinalized {
        finalized = true;

        if (totalRaised >= softCap) {
            // Presale successful: Transfer raised ETH to owner
            payable(owner).transfer(address(this).balance);
            emit PresaleFinalized(true);
        } else {
            // Presale failed: Allow contributors to withdraw their ETH
            emit PresaleFinalized(false);
        }
    }

    // Function to withdraw ETH in case of presale failure
    function withdrawContribution() external presaleEnded {
        require(finalized, "Presale must be finalized");
        require(totalRaised < softCap, "Presale was successful");

        uint256 contribution = contributions[msg.sender];
        require(contribution > 0, "No contributions made");

        contributions[msg.sender] = 0;
        tokensClaimable[msg.sender] = 0;

        payable(msg.sender).transfer(contribution);
    }

    // Fallback function to prevent accidental ETH transfer
    receive() external payable {
        revert("Use the contribute function to send ETH");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
