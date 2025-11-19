"""
Generated Code Metadata:
========================
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Create a Solidity contract that integrates with Fjord Foundry's LBP mechanism, focusing on reducing bot manipulation during token sales.
Generated: DETERMINISTIC_3c72e6f37ef87dec
Batch ID: 20250612_164152
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title AntiBotLBP
 * @dev A contract that integrates with Fjord Foundry's LBP mechanism to reduce bot manipulation during token sales.
 * Features include:
 * - Whitelisting of allowed participants
 * - Purchase limits per address
 * - Time-based restrictions
 * - Anti-sniping mechanisms
 */
contract AntiBotLBP is Ownable, ReentrancyGuard {
    IERC20 public saleToken;
    IERC20 public paymentToken;
    uint256 public startTime;
    uint256 public endTime;
    uint256 public minPurchaseAmount;
    uint256 public maxPurchaseAmount;
    uint256 public totalRaised;
    uint256 public totalTokensSold;

    mapping(address => bool) public whitelist;
    mapping(address => uint256) public purchases;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event WhitelistUpdated(address indexed account, bool status);

    /**
     * @dev Initializes the contract with sale parameters
     * @param _saleToken Address of the token being sold
     * @param _paymentToken Address of the token used for payment
     * @param _startTime Timestamp when sale starts
     * @param _endTime Timestamp when sale ends
     * @param _minPurchaseAmount Minimum purchase amount in paymentToken
     * @param _maxPurchaseAmount Maximum purchase amount in paymentToken per address
     */
    constructor(
        address _saleToken,
        address _paymentToken,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _minPurchaseAmount,
        uint256 _maxPurchaseAmount
    ) {
        require(_saleToken != address(0), "Invalid sale token address");
        require(_paymentToken != address(0), "Invalid payment token address");
        require(_startTime > block.timestamp, "Start time must be in future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_minPurchaseAmount > 0, "Min purchase amount must be positive");
        require(_maxPurchaseAmount > _minPurchaseAmount, "Max must be greater than min");

        saleToken = IERC20(_saleToken);
        paymentToken = IERC20(_paymentToken);
        startTime = _startTime;
        endTime = _endTime;
        minPurchaseAmount = _minPurchaseAmount;
        maxPurchaseAmount = _maxPurchaseAmount;
    }

    /**
     * @dev Modifier to check if sale is active
     */
    modifier whenSaleActive() {
        require(block.timestamp >= startTime, "Sale has not started");
        require(block.timestamp <= endTime, "Sale has ended");
        _;
    }

    /**
     * @dev Modifier to check if address is whitelisted
     */
    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Address not whitelisted");
        _;
    }

    /**
     * @dev Add or remove addresses from whitelist
     * @param accounts Array of addresses to update
     * @param status Boolean indicating whether to add or remove
     */
    function updateWhitelist(address[] calldata accounts, bool status) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = status;
            emit WhitelistUpdated(accounts[i], status);
        }
    }

    /**
     * @dev Purchase tokens during the sale
     * @param amount Amount of paymentToken to spend
     */
    function purchaseTokens(uint256 amount) external nonReentrant whenSaleActive onlyWhitelisted {
        require(amount >= minPurchaseAmount, "Amount below minimum");
        require(amount <= maxPurchaseAmount, "Amount exceeds maximum");
        require(purchases[msg.sender] + amount <= maxPurchaseAmount, "Exceeds personal cap");

        // Calculate token amount based on current LBP price (simplified for example)
        // In a real implementation, this would integrate with Fjord Foundry's LBP contract
        uint256 tokenAmount = calculateTokenAmount(amount);

        require(saleToken.balanceOf(address(this)) >= tokenAmount, "Insufficient sale token balance");

        // Transfer payment tokens from buyer
        paymentToken.transferFrom(msg.sender, address(this), amount);

        // Update state
        purchases[msg.sender] += amount;
        totalRaised += amount;
        totalTokensSold += tokenAmount;

        // Transfer sale tokens to buyer
        saleToken.transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount, amount);
    }

    /**
     * @dev Simplified token amount calculation (replace with actual LBP integration)
     * @param paymentAmount Amount of paymentToken spent
     * @return tokenAmount Amount of sale tokens received
     */
    function calculateTokenAmount(uint256 paymentAmount) internal view returns (uint256 tokenAmount) {
        // This is a placeholder - in a real implementation, you would query the LBP contract
        // for the current price and calculate the token amount accordingly
        return paymentAmount * 10; // Example conversion rate
    }

    /**
     * @dev Withdraw raised funds after sale ends
     */
    function withdrawRaisedFunds() external onlyOwner {
        require(block.timestamp > endTime, "Sale not ended yet");
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        paymentToken.transfer(owner(), balance);
    }

    /**
     * @dev Withdraw unsold tokens after sale ends
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > endTime, "Sale not ended yet");
        uint256 balance = saleToken.balanceOf(address(this));
        require(balance > 0, "No unsold tokens");
        saleToken.transfer(owner(), balance);
    }
}
```
