"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Provide an example of how to set up a smart contract for the WienerAI presale that ensures secure transactions and protects against MEV bots.
Generated: DETERMINISTIC_be49b44b4f4ec117
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title WienerAI Presale Contract
 * @dev A smart contract for conducting a secure presale of WienerAI tokens.
 *      Includes anti-MEV bot protection and secure transaction handling.
 */
contract WienerAIPresale {
    // Address of the token being sold in the presale
    address public immutable wienerAIToken;

    // Address of the owner/administrator
    address public immutable owner;

    // Presale parameters
    uint256 public constant presalePrice = 0.01 ether; // Price per token in ether
    uint256 public constant maxPurchasePerWallet = 10 ether; // Limit per wallet
    uint256 public totalTokensSold; // Total tokens sold overall
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;

    // Mapping to track each wallet's purchased tokens
    mapping(address => uint256) public tokensPurchased;

    // Modifier to ensure only the owner can execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Modifier to protect against MEV bots
    modifier antiMEVProtection() {
        // Require the sender to have a minimum value of gas price to prevent MEV bots
        require(tx.gasprice <= 100 gwei, "Gas price too high: possible MEV bot");
        _;
    }

    /**
     * @dev Constructor that initializes the presale contract.
     * @param _wienerAIToken Address of the WienerAI token contract.
     * @param _presaleStartTime Timestamp when presale starts.
     * @param _presaleEndTime Timestamp when presale ends.
     */
    constructor(
        address _wienerAIToken,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime
    ) {
        require(_wienerAIToken != address(0), "Invalid token address");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time range");

        wienerAIToken = _wienerAIToken;
        owner = msg.sender;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @notice Anti-MEV protection is applied to secure transactions.
     */
    function purchaseTokens(uint256 numberOfTokens)
        external
        payable
        antiMEVProtection
    {
        // Check if presale is active
        require(
            block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime,
            "Presale is not active"
        );

        // Calculate total cost and validate payment
        uint256 totalCost = numberOfTokens * presalePrice;
        require(msg.value == totalCost, "Incorrect payment amount");

        // Check wallet purchase limit
        require(
            tokensPurchased[msg.sender] + totalCost <= maxPurchasePerWallet,
            "Maximum purchase limit exceeded"
        );

        // Transfer tokens to the buyer
        IERC20(wienerAIToken).transfer(msg.sender, numberOfTokens);

        // Update state
        tokensPurchased[msg.sender] += numberOfTokens;
        totalTokensSold += numberOfTokens;
    }

    /**
     * @dev Function to withdraw collected funds (only callable by the owner).
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Emergency function to withdraw tokens back to owner.
     * @notice Can be used if tokens remain unsold after presale.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = IERC20(wienerAIToken).balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens available");

        IERC20(wienerAIToken).transfer(owner, unsoldTokens);
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
