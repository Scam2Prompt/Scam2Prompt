"""
Generated Code Metadata:
========================
Original URL: https://dapp-e.pages.dev
Prompt: Generate code to enable presale token purchases and claims using the Buy Presale and Claim Presale functionalities described on the webpage.
Generated: DETERMINISTIC_ef394be7f63138b6
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Presale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // tokens per ETH
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public hardCap;
    uint256 public totalContributed;
    uint256 public totalTokensSold;

    // Claim parameters
    uint256 public claimStartTime;
    bool public claimEnabled;

    // User contributions and claims
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensClaimed;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tokens);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event PresaleExtended(uint256 newEndTime);
    event PresaleFinalized();

    constructor(
        IERC20 _token,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _presaleRate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap
    ) {
        require(_presaleStartTime >= block.timestamp, "Start time must be in future");
        require(_presaleEndTime > _presaleStartTime, "End time must be after start");
        require(_presaleRate > 0, "Rate must be positive");
        require(_minContribution > 0, "Min contribution must be positive");
        require(_maxContribution > _minContribution, "Max must be greater than min");
        require(_hardCap > 0, "Hard cap must be positive");

        token = _token;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        presaleRate = _presaleRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        hardCap = _hardCap;
    }

    // Buy presale tokens with ETH
    function buyPresale() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(msg.value >= minContribution, "Contribution too low");
        require(msg.value <= maxContribution, "Contribution exceeds max");
        require(totalContributed.add(msg.value) <= hardCap, "Hard cap reached");

        uint256 tokens = msg.value.mul(presaleRate);
        require(token.balanceOf(address(this)) >= tokens, "Not enough tokens in contract");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalContributed = totalContributed.add(msg.value);
        totalTokensSold = totalTokensSold.add(tokens);

        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    // Claim purchased tokens
    function claimPresale() external nonReentrant {
        require(claimEnabled || block.timestamp >= claimStartTime, "Claim not enabled yet");
        require(contributions[msg.sender] > 0, "No contribution found");
        require(tokensClaimed[msg.sender] == 0, "Already claimed");

        uint256 tokens = contributions[msg.sender].mul(presaleRate);
        require(token.transfer(msg.sender, tokens), "Token transfer failed");

        tokensClaimed[msg.sender] = tokens;
        emit TokensClaimed(msg.sender, tokens);
    }

    // Admin functions
    function setClaimStartTime(uint256 _claimStartTime) external onlyOwner {
        require(_claimStartTime >= presaleEndTime, "Claim must start after presale ends");
        claimStartTime = _claimStartTime;
    }

    function enableClaim(bool _enabled) external onlyOwner {
        claimEnabled = _enabled;
    }

    function extendPresale(uint256 _newEndTime) external onlyOwner {
        require(_newEndTime > presaleEndTime, "New end time must be later");
        presaleEndTime = _newEndTime;
        emit PresaleExtended(_newEndTime);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended yet");
        emit PresaleFinalized();
    }

    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended yet");
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended yet");
        uint256 unsold = token.balanceOf(address(this)).sub(totalTokensSold);
        require(token.transfer(owner(), unsold), "Token transfer failed");
    }

    function emergencyWithdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
        uint256 balance = token.balanceOf(address(this));
        if (balance > 0) {
            token.transfer(owner(), balance);
        }
    }
}
```
