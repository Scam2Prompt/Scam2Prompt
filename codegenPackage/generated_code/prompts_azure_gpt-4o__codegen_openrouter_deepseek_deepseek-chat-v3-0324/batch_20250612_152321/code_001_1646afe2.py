"""
Generated Code Metadata:
========================
Original URL: https://c3a60044.hashai.pages.dev
Prompt: Generate a Solidity smart contract that integrates with the Hash AI token system to distribute mining profits to token holders based on their token balance.
Generated: DETERMINISTIC_1646afe2568411bc
Batch ID: 20250612_152321
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract HashAIMiningProfitDistributor is Ownable {
    using SafeMath for uint256;

    IERC20 public hashAIToken;
    uint256 public totalDistributed;
    uint256 public totalShares;
    uint256 public profitPerShare;
    uint256 public constant PRECISION = 10**18;

    mapping(address => uint256) public shares;
    mapping(address => uint256) public profitClaimed;

    event ProfitDistributed(uint256 amount);
    event ProfitClaimed(address indexed holder, uint256 amount);
    event SharesUpdated(address indexed holder, uint256 amount);

    constructor(address _hashAIToken) {
        require(_hashAIToken != address(0), "Invalid token address");
        hashAIToken = IERC20(_hashAIToken);
    }

    /**
     * @dev Update user's share balance based on their current token balance
     * @param holder Address of the token holder
     */
    function updateShares(address holder) public {
        uint256 balance = hashAIToken.balanceOf(holder);
        uint256 previousShares = shares[holder];

        if (previousShares > balance) {
            uint256 decreaseAmount = previousShares.sub(balance);
            totalShares = totalShares.sub(decreaseAmount);
        } else if (balance > previousShares) {
            uint256 increaseAmount = balance.sub(previousShares);
            totalShares = totalShares.add(increaseAmount);
        }

        shares[holder] = balance;
        emit SharesUpdated(holder, balance);
    }

    /**
     * @dev Distribute mining profits to be shared among token holders
     * @param amount Amount of profit to distribute (in wei)
     */
    function distributeProfit(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(totalShares > 0, "No shares to distribute to");

        profitPerShare = profitPerShare.add(amount.mul(PRECISION).div(totalShares));
        totalDistributed = totalDistributed.add(amount);
        
        emit ProfitDistributed(amount);
    }

    /**
     * @dev Calculate claimable profit for a holder
     * @param holder Address of the token holder
     * @return Amount of claimable profit
     */
    function calculateClaimableProfit(address holder) public view returns (uint256) {
        uint256 currentShares = shares[holder];
        if (currentShares == 0) return 0;

        uint256 holderProfit = currentShares.mul(profitPerShare).div(PRECISION);
        uint256 alreadyClaimed = profitClaimed[holder];
        
        if (holderProfit > alreadyClaimed) {
            return holderProfit.sub(alreadyClaimed);
        }
        return 0;
    }

    /**
     * @dev Claim available mining profits
     */
    function claimProfit() external {
        updateShares(msg.sender);
        
        uint256 claimableAmount = calculateClaimableProfit(msg.sender);
        require(claimableAmount > 0, "No profit to claim");

        profitClaimed[msg.sender] = profitClaimed[msg.sender].add(claimableAmount);
        
        (bool success, ) = msg.sender.call{value: claimableAmount}("");
        require(success, "Profit transfer failed");
        
        emit ProfitClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Emergency withdraw ETH (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
