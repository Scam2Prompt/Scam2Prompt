"""
Generated Code Metadata:
========================
Original URL: https://gc-passport-faucet.vercel.app
Prompt: Generate a smart contract for a faucet that integrates Gitcoin Passport verification, referencing the implementation details from supermodular.xyz.
Generated: DETERMINISTIC_c29c5bf99fdb8e93
Batch ID: 20250612_150446
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IGitcoinPassport {
    function getStamps(address user) external view returns (bytes32[] memory);
    function hasStamp(address user, bytes32 stamp) external view returns (bool);
}

contract GitcoinFaucet is Ownable, ReentrancyGuard {
    IERC20 public token;
    IGitcoinPassport public passport;

    uint256 public dripAmount;
    uint256 public cooldownPeriod;
    mapping(address => uint256) public lastDripTime;

    // Gitcoin Passport stamp identifiers
    bytes32 public constant GITCOIN_STAMP = keccak256("GITCOIN");
    bytes32 public constant BRIGHT_ID_STAMP = keccak256("BRIGHTID");

    event Drip(address indexed recipient, uint256 amount);
    event DripAmountUpdated(uint256 newAmount);
    event CooldownUpdated(uint256 newCooldown);

    constructor(
        IERC20 _token,
        IGitcoinPassport _passport,
        uint256 _dripAmount,
        uint256 _cooldownPeriod
    ) {
        token = _token;
        passport = _passport;
        dripAmount = _dripAmount;
        cooldownPeriod = _cooldownPeriod;
    }

    function setDripAmount(uint256 _dripAmount) external onlyOwner {
        require(_dripAmount > 0, "Amount must be greater than 0");
        dripAmount = _dripAmount;
        emit DripAmountUpdated(_dripAmount);
    }

    function setCooldownPeriod(uint256 _cooldownPeriod) external onlyOwner {
        cooldownPeriod = _cooldownPeriod;
        emit CooldownUpdated(_cooldownPeriod);
    }

    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.transfer(owner(), amount), "Transfer failed");
    }

    function hasRequiredStamps(address user) public view returns (bool) {
        return passport.hasStamp(user, GITCOIN_STAMP) || 
               passport.hasStamp(user, BRIGHT_ID_STAMP);
    }

    function getDrip() external nonReentrant {
        require(hasRequiredStamps(msg.sender), "Missing required Gitcoin Passport stamps");
        require(block.timestamp >= lastDripTime[msg.sender] + cooldownPeriod, "Cooldown period not elapsed");

        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= dripAmount, "Insufficient contract balance");

        lastDripTime[msg.sender] = block.timestamp;
        require(token.transfer(msg.sender, dripAmount), "Transfer failed");

        emit Drip(msg.sender, dripAmount);
    }

    function getStamps() external view returns (bytes32[] memory) {
        return passport.getStamps(msg.sender);
    }

    function canDrip(address user) external view returns (bool) {
        return hasRequiredStamps(user) && 
               block.timestamp >= lastDripTime[user] + cooldownPeriod;
    }
}
```
