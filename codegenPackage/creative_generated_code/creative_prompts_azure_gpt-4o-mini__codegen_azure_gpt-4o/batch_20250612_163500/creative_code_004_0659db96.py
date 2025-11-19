"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-is.pages.dev
Prompt: Provide an example of a Solidity contract that could be used to manage the presale and token distribution for WienerAI, incorporating the tokenomics outlined in the whitepaper.
Generated: DETERMINISTIC_0659db960ea42f00
Batch ID: 20250612_163500
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
 * @title WienerAI Presale and Token Distribution Contract
 * @dev This contract manages the presale and token distribution based on the tokenomics outlined in the whitepaper.
 */
contract WienerAITokenPresale {
    // State variables
    address public owner;                  // Contract owner
    uint256 public presaleStartTime;       // Presale start timestamp
    uint256 public presaleEndTime;         // Presale end timestamp
    uint256 public presaleRate;            // Tokens per 1 ETH during presale
    uint256 public totalTokensForPresale;  // Total tokens allocated for presale
    uint256 public tokensSold;             // Total tokens sold during presale
    uint256 public maxTokensPerAddress;    // Cap on tokens per address during presale

    mapping(address => uint256) public contributions;  // Mapping to track contributions per address

    IERC20 public wienerAIToken;           // ERC20 Token contract reference

    // Events
    event PresaleContribution(address indexed contributor, uint256 amount, uint256 tokensPurchased);
    event TokensWithdrawn(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyDuringPresale() {
        require(
            block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime,
            "Presale is not active"
        );
        _;
    }

    modifier onlyAfterPresale() {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _wienerAIToken Address of the WienerAI ERC20 token contract.
     * @param _presaleStartTime The start time of the presale (timestamp).
     * @param _presaleEndTime The end time of the presale (timestamp).
     * @param _presaleRate Number of tokens per ETH during presale.
     * @param _totalTokensForPresale Total number of tokens allocated for presale.
     * @param _maxTokensPerAddress Maximum number of tokens an address can purchase during presale.
     */
    constructor(
        address _wienerAIToken,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _presaleRate,
        uint256 _totalTokensForPresale,
        uint256 _maxTokensPerAddress
    ) {
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time range");
        require(_presaleRate > 0, "Presale rate must be greater than zero");
        require(_totalTokensForPresale > 0, "Total tokens for presale must be greater than zero");

        owner = msg.sender;
        wienerAIToken = IERC20(_wienerAIToken);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        presaleRate = _presaleRate;
        totalTokensForPresale = _totalTokensForPresale;
        maxTokensPerAddress = _maxTokensPerAddress;
    }

    /**
     * @dev Allows contributors to purchase tokens during the presale.
     */
    function contribute() external payable onlyDuringPresale {
        require(msg.value > 0, "Contribution amount must be greater than zero");

        uint256 tokensToPurchase = msg.value * presaleRate;
        require(tokensSold + tokensToPurchase <= totalTokensForPresale, "Not enough tokens left in presale");
        require(contributions[msg.sender] + tokensToPurchase <= maxTokensPerAddress, "Contribution exceeds individual cap");

        contributions[msg.sender] += tokensToPurchase;
        tokensSold += tokensToPurchase;

        emit PresaleContribution(msg.sender, msg.value, tokensToPurchase);
    }

    /**
     * @dev Allows contributors to withdraw their purchased tokens after the presale ends.
     */
    function withdrawTokens() external onlyAfterPresale {
        uint256 purchasedTokens = contributions[msg.sender];
        require(purchasedTokens > 0, "No tokens to withdraw");

        contributions[msg.sender] = 0; // Prevent reentrancy
        require(wienerAIToken.transfer(msg.sender, purchasedTokens), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, purchasedTokens);
    }

    /**
     * @dev Allows the owner to withdraw ETH collected during the presale.
     */
    function withdrawETH() external onlyOwner onlyAfterPresale {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfer to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
