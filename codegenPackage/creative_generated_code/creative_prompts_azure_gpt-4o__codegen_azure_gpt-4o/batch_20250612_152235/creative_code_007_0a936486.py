"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20presale-claim.pages.dev
Prompt: Write code to implement an ERC-20 token presale mechanism for DOGE20, ensuring buyers can claim their tokens before the Uniswap listing.
Generated: DETERMINISTIC_0a9364863937c27c
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
 * @title DOGE20 Presale Contract
 * @dev Implements an ERC-20 token presale mechanism allowing buyers to purchase tokens and claim them before Uniswap listing.
 */
contract DOGE20Presale {
    // ERC-20 Token Interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public immutable doge20Token;    // Address of the DOGE20 token contract
    address public immutable owner;        // Owner of the presale contract
    uint256 public immutable presaleStart; // Start timestamp for the presale
    uint256 public immutable presaleEnd;   // End timestamp for the presale
    uint256 public immutable tokenPrice;   // Price of each DOGE20 token in wei
    uint256 public immutable maxTokensPerAccount; // Maximum tokens a single account can purchase

    uint256 public totalTokensSold;        // Total tokens sold during the presale
    bool public uniswapListingScheduled;   // Flag indicating whether Uniswap listing is scheduled

    mapping(address => uint256) public userBalances; // Mapping to track user token purchase amounts

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event UniswapListingScheduled();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale not active");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        _;
    }

    constructor(
        address _doge20Token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _maxTokensPerAccount
    ) {
        require(_presaleStart < _presaleEnd, "Presale start must be before presale end");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxTokensPerAccount > 0, "Maximum tokens per account must be greater than zero");

        doge20Token = IERC20(_doge20Token);
        owner = msg.sender;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        maxTokensPerAccount = _maxTokensPerAccount;
    }

    /**
     * @dev Allows a buyer to purchase DOGE20 tokens during the presale period.
     * Each purchase is limited by the maxTokensPerAccount constraint.
     */
    function buyTokens(uint256 tokenAmount) external payable presaleActive {
        uint256 cost = tokenAmount * tokenPrice;
        require(msg.value == cost, "Incorrect ETH value sent");
        require(userBalances[msg.sender] + tokenAmount <= maxTokensPerAccount, "Exceeds maximum tokens per account");

        userBalances[msg.sender] += tokenAmount;
        totalTokensSold += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows buyers to claim their purchased tokens after the presale ends.
     */
    function claimTokens() external presaleEnded {
        uint256 amountToClaim = userBalances[msg.sender];
        require(amountToClaim > 0, "No tokens to claim");
        require(!uniswapListingScheduled, "Cannot claim after Uniswap listing is scheduled");

        userBalances[msg.sender] = 0;

        // Transfer DOGE20 tokens to the buyer
        require(doge20Token.transfer(msg.sender, amountToClaim), "Token transfer failed");

        emit TokensClaimed(msg.sender, amountToClaim);
    }

    /**
     * @dev Schedules the Uniswap listing, preventing further token claims.
     * Callable only by the owner.
     */
    function scheduleUniswapListing() external onlyOwner presaleEnded {
        uniswapListingScheduled = true;
        emit UniswapListingScheduled();
    }

    /**
     * @dev Withdraws the ETH collected during the presale.
     * Callable only by the owner after the presale ends.
     */
    function withdrawETH() external onlyOwner presaleEnded {
        payable(owner).transfer(address(this).balance);
    }
}
```
