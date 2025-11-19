"""
Generated Code Metadata:
========================
Original URL: https://crop-6qi.pages.dev
Prompt: Write a smart contract in Solidity for a cross-game, cross-chain decentralized player network's token sale, with a first-come-first-served allocation mechanism.
Generated: DETERMINISTIC_23f67c1a11b205cb
Batch ID: 20250622_210443
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenSale contract
 * @author [Your Name]
 * @notice A smart contract for a cross-game, cross-chain decentralized player network's token sale.
 */
contract TokenSale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token allocations
    mapping (address => uint256) public allocations;

    // Mapping of token purchases
    mapping (address => uint256) public purchases;

    // Token contract instance
    IERC20 public token;

    // Sale start timestamp
    uint256 public startTime;

    // Sale end timestamp
    uint256 public endTime;

    // Token price in wei
    uint256 public tokenPrice;

    // Total tokens available for sale
    uint256 public totalTokensForSale;

    // Total tokens sold
    uint256 public totalTokensSold;

    // Event emitted when a user purchases tokens
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when a user claims tokens
    event TokensClaimed(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor
     * @param _token Token contract instance
     * @param _startTime Sale start timestamp
     * @param _endTime Sale end timestamp
     * @param _tokenPrice Token price in wei
     * @param _totalTokensForSale Total tokens available for sale
     */
    constructor(
        IERC20 _token,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _tokenPrice,
        uint256 _totalTokensForSale
    ) public {
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than 0");

        token = _token;
        startTime = _startTime;
        endTime = _endTime;
        tokenPrice = _tokenPrice;
        totalTokensForSale = _totalTokensForSale;
    }

    /**
     * @dev Purchase tokens
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Buyer address cannot be 0");
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Sale is not active");
        require(_amount > 0, "Purchase amount must be greater than 0");
        require(totalTokensForSale >= _amount, "Not enough tokens available for sale");

        uint256 cost = _amount.mul(tokenPrice);
        require(msg.value >= cost, "Insufficient payment");

        // Update token sale state
        totalTokensSold = totalTokensSold.add(_amount);
        totalTokensForSale = totalTokensForSale.sub(_amount);
        purchases[msg.sender] = purchases[msg.sender].add(_amount);

        // Transfer tokens to buyer
        token.transfer(msg.sender, _amount);

        // Emit event
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Claim allocated tokens
     */
    function claimTokens() external nonReentrant {
        require(msg.sender != address(0), "Buyer address cannot be 0");
        require(allocations[msg.sender] > 0, "No allocation available");

        uint256 allocation = allocations[msg.sender];
        allocations[msg.sender] = 0;

        // Transfer tokens to buyer
        token.transfer(msg.sender, allocation);

        // Emit event
        emit TokensClaimed(msg.sender, allocation);
    }

    /**
     * @dev Update token allocation
     * @param _buyer Buyer address
     * @param _amount Allocation amount
     */
    function updateAllocation(address _buyer, uint256 _amount) external {
        require(msg.sender == address(0x...), "Only owner can update allocations"); // Replace with owner address
        require(_buyer != address(0), "Buyer address cannot be 0");
        require(_amount > 0, "Allocation amount must be greater than 0");

        allocations[_buyer] = _amount;
    }

    /**
     * @dev Withdraw ether
     */
    function withdrawEther() external {
        require(msg.sender == address(0x...), "Only owner can withdraw ether"); // Replace with owner address
        payable(msg.sender).transfer(address(this).balance);
    }

    /**
     * @dev Withdraw tokens
     */
    function withdrawTokens() external {
        require(msg.sender == address(0x...), "Only owner can withdraw tokens"); // Replace with owner address
        token.transfer(msg.sender, token.balanceOf(address(this)));
    }
}
```
