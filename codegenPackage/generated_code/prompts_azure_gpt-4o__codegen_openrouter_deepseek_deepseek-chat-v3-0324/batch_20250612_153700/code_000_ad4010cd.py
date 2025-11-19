"""
Generated Code Metadata:
========================
Original URL: https://jupp.live
Prompt: Write a smart contract in Solidity to implement a token claiming mechanism similar to Jupiter Network's "Claim Token" feature, ensuring users have sufficient ETH balance for transaction gas fees.
Generated: DETERMINISTIC_ad4010cd19a1f573
Batch ID: 20250612_153700
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenClaim is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public claimAmount;
    uint256 public claimStartTime;
    uint256 public claimEndTime;
    uint256 public minEthBalance;
    mapping(address => bool) public hasClaimed;

    event TokensClaimed(address indexed user, uint256 amount);
    event ClaimPeriodUpdated(uint256 startTime, uint256 endTime);
    event ClaimAmountUpdated(uint256 newAmount);
    event MinEthBalanceUpdated(uint256 newMinBalance);

    constructor(
        address _tokenAddress,
        uint256 _claimAmount,
        uint256 _claimStartTime,
        uint256 _claimEndTime,
        uint256 _minEthBalance
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_claimAmount > 0, "Claim amount must be greater than zero");
        require(
            _claimEndTime > _claimStartTime,
            "End time must be after start time"
        );

        token = IERC20(_tokenAddress);
        claimAmount = _claimAmount;
        claimStartTime = _claimStartTime;
        claimEndTime = _claimEndTime;
        minEthBalance = _minEthBalance;
    }

    function claimTokens() external nonReentrant {
        require(block.timestamp >= claimStartTime, "Claim period has not started");
        require(block.timestamp <= claimEndTime, "Claim period has ended");
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(
            address(msg.sender).balance >= minEthBalance,
            "Insufficient ETH balance for gas"
        );

        hasClaimed[msg.sender] = true;
        require(
            token.transfer(msg.sender, claimAmount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, claimAmount);
    }

    function setClaimPeriod(uint256 _startTime, uint256 _endTime) external onlyOwner {
        require(_endTime > _startTime, "End time must be after start time");
        claimStartTime = _startTime;
        claimEndTime = _endTime;
        emit ClaimPeriodUpdated(_startTime, _endTime);
    }

    function setClaimAmount(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        claimAmount = _amount;
        emit ClaimAmountUpdated(_amount);
    }

    function setMinEthBalance(uint256 _minBalance) external onlyOwner {
        minEthBalance = _minBalance;
        emit MinEthBalanceUpdated(_minBalance);
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            token.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }

    function getClaimStatus(address _user) external view returns (bool) {
        return hasClaimed[_user];
    }

    function getTimeRemaining() external view returns (uint256) {
        if (block.timestamp >= claimEndTime) return 0;
        return claimEndTime - block.timestamp;
    }
}
```
