"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wepestreetpepe-new.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates a crypto presale for the WEPE Token.
Generated: DETERMINISTIC_b8c23890dd1972dc
Batch ID: 20250612_160124
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
 * @title WEPE Token Presale Smart Contract
 * @dev Facilitates a presale for the WEPE Token.
 */
contract WEPEPresale {
    // Address of the token being sold
    address public tokenAddress;

    // Owner of the presale contract
    address public owner;

    // Presale parameters
    uint256 public tokenRate; // Number of tokens per 1 ETH
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public hardCap; // Maximum ETH amount for the presale
    uint256 public totalRaised; // Total ETH raised

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed purchaser, uint256 amount);
    event PresaleFinalized();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier presaleOngoing() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the WEPE Token contract.
     * @param _tokenRate Number of tokens per 1 ETH.
     * @param _presaleStart Start timestamp of the presale.
     * @param _presaleEnd End timestamp of the presale.
     * @param _hardCap Maximum ETH amount for the presale.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenRate,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _hardCap
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenRate > 0, "Token rate must be greater than zero");
        require(_presaleStart < _presaleEnd, "Presale start must be before end");
        require(_hardCap > 0, "Hard cap must be greater than zero");

        tokenAddress = _tokenAddress;
        tokenRate = _tokenRate;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        hardCap = _hardCap;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase tokens during the presale period.
     */
    function purchaseTokens() external payable presaleOngoing {
        require(msg.value > 0, "ETH value must be greater than zero");
        require(totalRaised + msg.value <= hardCap, "Hard cap exceeded");

        uint256 tokenAmount = msg.value * tokenRate;

        // Track user's contribution
        contributions[msg.sender] += msg.value;

        // Update total ETH raised
        totalRaised += msg.value;

        // Transfer tokens to the purchaser
        bool success = IERC20(tokenAddress).transfer(msg.sender, tokenAmount);
        require(success, "Token transfer failed");

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Finalizes the presale and transfers remaining ETH to the owner.
     * Can only be called by the owner after the presale ends.
     */
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still ongoing");

        uint256 balance = address(this).balance;
        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH transfer failed");

        emit PresaleFinalized();
    }

    /**
     * @dev Withdraw any unclaimed tokens after presale ends.
     * Can only be called by the owner.
     */
    function withdrawUnclaimedTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still ongoing");

        uint256 remainingTokens = IERC20(tokenAddress).balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");

        bool success = IERC20(tokenAddress).transfer(owner, remainingTokens);
        require(success, "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
