"""
Generated Code Metadata:
========================
Original URL: https://c3a60044.hashai.pages.dev
Prompt: Design a smart contract for a Hash AI token, where income from AI-enhanced mining rigs is shared with token holders, using Solidity or another suitable programming language.
Generated: DETERMINISTIC_c5b7d96437f653cb
Batch ID: 20250622_205919
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title HashAIToken
 * @dev ERC20 token with profit sharing from AI-enhanced mining rigs
 */
contract HashAIToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Track total distributed profits
    uint256 public totalDistributedProfits;
    
    // Track profits per share
    uint256 public profitPerShare;
    
    // Track profits claimed by each shareholder
    mapping(address => uint256) public profitsClaimed;
    
    // Track last profit per share when shareholder claimed
    mapping(address => uint256) public lastProfitPerShare;

    // Events
    event ProfitsDistributed(uint256 amount);
    event ProfitsClaimed(address indexed holder, uint256 amount);

    /**
     * @dev Constructor that initializes the token
     * @param initialSupply Initial token supply
     */
    constructor(uint256 initialSupply) ERC20("Hash AI Token", "HAI") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Distribute mining profits to token holders
     * @param amount Amount of profits to distribute (in wei)
     */
    function distributeProfits(uint256 amount) external payable onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(totalSupply() > 0, "No tokens minted yet");

        // Update profit per share
        profitPerShare = profitPerShare.add(amount.mul(1e18).div(totalSupply()));
        totalDistributedProfits = totalDistributedProfits.add(amount);

        emit ProfitsDistributed(amount);
    }

    /**
     * @dev Claim available profits for the sender
     */
    function claimProfits() external {
        uint256 unclaimed = getUnclaimedProfits(msg.sender);
        require(unclaimed > 0, "No profits to claim");

        profitsClaimed[msg.sender] = profitsClaimed[msg.sender].add(unclaimed);
        lastProfitPerShare[msg.sender] = profitPerShare;

        (bool success, ) = msg.sender.call{value: unclaimed}("");
        require(success, "Profit transfer failed");

        emit ProfitsClaimed(msg.sender, unclaimed);
    }

    /**
     * @dev Calculate unclaimed profits for a holder
     * @param holder Address of the token holder
     * @return Amount of unclaimed profits
     */
    function getUnclaimedProfits(address holder) public view returns (uint256) {
        uint256 holderBalance = balanceOf(holder);
        if (holderBalance == 0) {
            return 0;
        }

        uint256 newProfit = profitPerShare.sub(lastProfitPerShare[holder]);
        return holderBalance.mul(newProfit).div(1e18);
    }

    /**
     * @dev Override transfer to update profit tracking
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);

        if (from != address(0)) {
            uint256 unclaimed = getUnclaimedProfits(from);
            if (unclaimed > 0) {
                profitsClaimed[from] = profitsClaimed[from].add(unclaimed);
                lastProfitPerShare[from] = profitPerShare;
            }
        }

        if (to != address(0)) {
            lastProfitPerShare[to] = profitPerShare;
        }
    }

    // Fallback function to receive ETH
    receive() external payable {
        distributeProfits(msg.value);
    }
}
```
