"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoonx.xyz
Prompt: Generate Solidity code for a smart contract that implements SafeMoonX-like tokenomics, including 5% redistribution and 5% liquidity pool replenishment during each trade.
Generated: DETERMINISTIC_003ef6dbf832ffd0
Batch ID: 20250612_155102
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SafeMoonXToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax percentages
    uint256 public constant REWARDS_PERCENTAGE = 5; // 5% redistribution
    uint256 public constant LIQUIDITY_PERCENTAGE = 5; // 5% for liquidity

    // Total fees for trading
    uint256 public totalFees = REWARDS_PERCENTAGE.add(LIQUIDITY_PERCENTAGE);

    // Mapping to track excluded addresses from fees
    mapping(address => bool) private _isExcludedFromFees;

    // Events
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event TokensRedistributed(uint256 amount);

    constructor() ERC20("SafeMoonXToken", "SMX") {
        // Mint initial supply to the owner
        _mint(msg.sender, 1_000_000 * 10**decimals());
    }

    // Function to transfer tokens with fee deduction
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check if the sender is excluded from fees
        if (!_isExcludedFromFees[sender] && !_isExcludedFromFees[recipient]) {
            // Calculate fees
            uint256 fees = amount.mul(totalFees).div(100);
            uint256 tokensToTransfer = amount.sub(fees);

            // Calculate redistribution and liquidity components
            uint256 rewards = fees.mul(REWARDS_PERCENTAGE).div(totalFees);
            uint256 liquidity = fees.mul(LIQUIDITY_PERCENTAGE).div(totalFees);

            // Redistribute rewards to all holders
            _redistributeRewards(rewards);

            // Add liquidity (this part is simplified, actual liquidity addition requires more logic)
            // In a production contract, you'd typically call a liquidity pool contract here

            // Transfer the remaining tokens to the recipient
            super._transfer(sender, recipient, tokensToTransfer);
        } else {
            // Transfer without fees if excluded
            super._transfer(sender, recipient, amount);
        }
    }

    // Function to redistribute rewards
    function _redistributeRewards(uint256 amount) private {
        // Distribute the rewards among all holders
        // In a real implementation, you would need to loop through all holders and distribute tokens
        // Here we will emit an event for simplicity, a real implementation is needed for production
        emit TokensRedistributed(amount);
    }

    // Function to exclude an address from fees
    function excludeFromFees(address account, bool excluded) external onlyOwner {
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }

    // Function to check if an address is excluded from fees
    function isExcludedFromFees(address account) external view returns (bool) {
        return _isExcludedFromFees[account];
    }

    // Function to withdraw stuck tokens (if necessary)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        require(amount > 0, "Amount must be greater than zero");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
