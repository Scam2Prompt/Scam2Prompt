"""
Generated Code Metadata:
========================
Original URL: https://btcbull.io
Prompt: Implement a token burn mechanism in Solidity that automatically burns a percentage of $BTCBULL supply whenever Bitcoin's price increases by $25K, following the milestones described on the BTC Bull roadmap.
Generated: DETERMINISTIC_48efd5ccc1b303d5
Batch ID: 20250612_154757
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for an external price feed (e.g., Chainlink)
interface IPriceFeed {
    function latestAnswer() external view returns (int256);
}

// The BTCBULL token contract
contract BTCBULL is IERC20, Ownable {
    // State variables
    string public constant name = "BTC Bull";
    string public constant symbol = "BTCBULL";
    uint8 public constant decimals = 18;
    uint256 private totalSupply_;
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Price feed for Bitcoin price
    IPriceFeed public priceFeed;
    uint256 public lastBurnPrice;
    uint256 public burnPercentage; // Percentage to burn (e.g., 5 for 5%)
    
    // Events
    event TokensBurned(uint256 amount);

    // Constructor to initialize the contract
    constructor(address _priceFeed, uint256 _burnPercentage) {
        priceFeed = IPriceFeed(_priceFeed);
        burnPercentage = _burnPercentage;
        lastBurnPrice = uint256(priceFeed.latestAnswer());
    }

    // ERC20 functions
    function totalSupply() external view override returns (uint256) {
        return totalSupply_;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Function to burn tokens based on Bitcoin price increase
    function checkAndBurn() external {
        uint256 currentPrice = uint256(priceFeed.latestAnswer());
        require(currentPrice > lastBurnPrice, "Price has not increased");

        // Calculate the price increase
        uint256 priceIncrease = currentPrice - lastBurnPrice;
        if (priceIncrease >= 25000) {
            // Calculate the amount to burn
            uint256 amountToBurn = (totalSupply_ * burnPercentage) / 100;
            require(amountToBurn > 0, "No tokens to burn");

            // Burn the tokens
            totalSupply_ -= amountToBurn;
            emit TokensBurned(amountToBurn);
            lastBurnPrice = currentPrice; // Update the last burn price
        }
    }

    // Function to mint new tokens (only owner)
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Mint to the zero address");
        totalSupply_ += amount;
        balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    // Function to set a new burn percentage (only owner)
    function setBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage > 0 && _burnPercentage <= 100, "Invalid burn percentage");
        burnPercentage = _burnPercentage;
    }
}
```
