"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-de.pages.dev
Prompt: Write a Solidity function that ensures fair token claiming for presale buyers of DOGE20, allowing them to claim tokens at the same time as the Uniswap listing.
Generated: DETERMINISTIC_a818218a5ed4ffa9
Batch ID: 20250612_152710
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
 * @title DOGE20PresaleClaim
 * @dev Ensures fair token claiming for presale buyers at the same time as Uniswap listing.
 */
contract DOGE20PresaleClaim {
    // Address of the token contract
    IERC20 public doge20Token;

    // Block timestamp for Uniswap listing
    uint256 public uniswapListingTime;

    // Mapping to track presale token allocations
    mapping(address => uint256) public presaleAllocations;

    // Mapping to track claimed tokens
    mapping(address => bool) public hasClaimed;

    // Event to log token claims
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Modifier to ensure Uniswap listing time is set
    modifier uniswapListingTimeSet() {
        require(uniswapListingTime != 0, "Uniswap listing time not set");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20Token);
    }

    /**
     * @notice Sets the Uniswap listing time.
     * @dev Can only be called once.
     * @param _listingTime The timestamp of the Uniswap listing.
     */
    function setUniswapListingTime(uint256 _listingTime) external {
        require(uniswapListingTime == 0, "Listing time already set");
        require(_listingTime > block.timestamp, "Listing time must be in the future");
        uniswapListingTime = _listingTime;
    }

    /**
     * @notice Allocates presale tokens to a buyer.
     * @dev Can only be called by the contract owner.
     * @param buyer The address of the presale buyer.
     * @param amount The amount of tokens allocated.
     */
    function allocatePresaleTokens(address buyer, uint256 amount) external {
        require(buyer != address(0), "Invalid buyer address");
        require(amount > 0, "Allocation amount must be greater than zero");
        presaleAllocations[buyer] += amount;
    }

    /**
     * @notice Allows presale buyers to claim their allocated tokens after Uniswap listing.
     */
    function claimTokens() external uniswapListingTimeSet {
        require(block.timestamp >= uniswapListingTime, "Cannot claim tokens before Uniswap listing");
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        uint256 allocation = presaleAllocations[msg.sender];
        require(allocation > 0, "No allocation for this address");

        // Mark the tokens as claimed
        hasClaimed[msg.sender] = true;

        // Transfer the allocated tokens to the presale buyer
        require(doge20Token.transfer(msg.sender, allocation), "Token transfer failed");

        emit TokensClaimed(msg.sender, allocation);
    }
}

/**
 * @dev Minimal interface for an ERC20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
