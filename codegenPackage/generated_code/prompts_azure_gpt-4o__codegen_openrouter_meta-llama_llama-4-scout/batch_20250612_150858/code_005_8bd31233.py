"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: Develop a smart contract that supports fair token launches, inspired by CowSwap's "Fair Sales" concept.
Generated: DETERMINISTIC_8bd312333bf812a1
Batch ID: 20250612_150858
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FairTokenLaunch
 * @author [Your Name]
 * @notice A smart contract for fair token launches inspired by CowSwap's "Fair Sales" concept.
 */
contract FairTokenLaunch is Ownable {
    using SafeMath for uint256;

    // Mapping of user addresses to their respective token balances
    mapping(address => uint256) public balances;

    // Mapping of user addresses to their respective claim statuses
    mapping(address => bool) public claimed;

    // Token being sold
    IERC20 public token;

    // Token price in wei
    uint256 public price;

    // Total tokens available for sale
    uint256 public totalTokens;

    // Total tokens sold
    uint256 public tokensSold;

    // Sale start timestamp
    uint256 public startTime;

    // Sale end timestamp
    uint256 public endTime;

    // Maximum tokens per buyer
    uint256 public maxTokensPerBuyer;

    // Event emitted when a user purchases tokens
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when a user claims their tokens
    event TokensClaimed(address indexed buyer, uint256 amount);

    /**
     * @notice Initializes the contract
     * @param _token Token being sold
     * @param _price Token price in wei
     * @param _totalTokens Total tokens available for sale
     * @param _startTime Sale start timestamp
     * @param _endTime Sale end timestamp
     * @param _maxTokensPerBuyer Maximum tokens per buyer
     */
    constructor(
        IERC20 _token,
        uint256 _price,
        uint256 _totalTokens,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _maxTokensPerBuyer
    ) {
        require(_price > 0, "Price must be greater than 0");
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_maxTokensPerBuyer > 0, "Max tokens per buyer must be greater than 0");

        token = _token;
        price = _price;
        totalTokens = _totalTokens;
        startTime = _startTime;
        endTime = _endTime;
        maxTokensPerBuyer = _maxTokensPerBuyer;
    }

    /**
     * @notice Purchases tokens
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external {
        require(msg.sender != address(0), "Buyer address cannot be 0");
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Sale not active");
        require(_amount > 0, "Amount must be greater than 0");
        require(tokensSold.add(_amount) <= totalTokens, "Not enough tokens available");
        require(balances[msg.sender].add(_amount) <= maxTokensPerBuyer, "Buyer exceeded maximum tokens per buyer");

        uint256 cost = _amount.mul(price);
        require(token.balanceOf(msg.sender) >= cost, "Buyer does not have enough tokens");

        balances[msg.sender] = balances[msg.sender].add(_amount);
        tokensSold = tokensSold.add(_amount);

        // Transfer tokens from buyer to contract
        token.transferFrom(msg.sender, address(this), cost);

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @notice Claims tokens
     */
    function claimTokens() external {
        require(msg.sender != address(0), "Claimant address cannot be 0");
        require(balances[msg.sender] > 0, "Claimant has no tokens to claim");
        require(!claimed[msg.sender], "Claimant has already claimed tokens");

        uint256 amount = balances[msg.sender];
        balances[msg.sender] = 0;
        claimed[msg.sender] = true;

        // Transfer tokens from contract to claimant
        token.transfer(msg.sender, amount);

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @notice Refunds buyers in case of sale failure
     * @param _buyer Buyer address
     */
    function refundBuyer(address _buyer) external onlyOwner {
        require(_buyer != address(0), "Buyer address cannot be 0");
        require(balances[_buyer] > 0, "Buyer has no tokens to refund");

        uint256 amount = balances[_buyer];
        balances[_buyer] = 0;

        // Transfer tokens from contract to buyer
        token.transfer(_buyer, amount.mul(price));
    }

    /**
     * @notice Destroys contract and transfers remaining tokens to owner
     */
    function destroyContract() external onlyOwner {
        require(block.timestamp > endTime, "Sale has not ended yet");

        // Transfer remaining tokens from contract to owner
        token.transfer(msg.sender, token.balanceOf(address(this)));

        // Selfdestruct contract
        selfdestruct(msg.sender);
    }
}
```
