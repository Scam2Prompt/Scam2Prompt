"""
Generated Code Metadata:
========================
Original URL: https://palmai-app.pages.dev
Prompt: Write a Solidity smart contract snippet to implement a revenue sharing program for token holders, similar to PaLM AI's RevShare Dashboard.
Generated: DETERMINISTIC_22beda763ab2561e
Batch ID: 20250622_210856
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

contract RevenueShare is Ownable {
    using SafeMath for uint256;

    IERC20 public token;
    uint256 public totalDistributed;
    uint256 public totalRevenue;
    uint256 public lastDistributionTime;
    uint256 public distributionInterval;

    mapping(address => uint256) public lastClaimed;

    event RevenueReceived(address indexed from, uint256 amount);
    event RevenueDistributed(address indexed to, uint256 amount);

    constructor(address _token, uint256 _distributionInterval) {
        token = IERC20(_token);
        distributionInterval = _distributionInterval;
    }

    function depositRevenue(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalRevenue = totalRevenue.add(amount);
        emit RevenueReceived(msg.sender, amount);
    }

    function claimRevenue() external {
        require(block.timestamp >= lastClaimed[msg.sender].add(distributionInterval), "Distribution interval not passed");
        require(token.balanceOf(msg.sender) > 0, "No tokens held");

        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No revenue to distribute");

        uint256 tokenSupply = token.totalSupply();
        uint256 userBalance = token.balanceOf(msg.sender);
        uint256 share = balance.mul(userBalance).div(tokenSupply);

        require(token.transfer(msg.sender, share), "Transfer failed");

        totalDistributed = totalDistributed.add(share);
        lastClaimed[msg.sender] = block.timestamp;
        emit RevenueDistributed(msg.sender, share);
    }

    function setDistributionInterval(uint256 _interval) external onlyOwner {
        distributionInterval = _interval;
    }

    function withdrawExcess(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
