"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate a smart contract in Solidity for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens based on the snapshot of Bitcoin and Ethereum wallets.
Generated: DETERMINISTIC_b6ae8faefd8dbcf0
Batch ID: 20250612_160600
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

contract ZiberICO is Ownable, ReentrancyGuard {
    IERC20 public ziberToken;
    uint256 public icoStartTime;
    uint256 public icoEndTime;
    uint256 public ethRate; // ZIBER tokens per 1 ETH
    uint256 public btcRate; // ZIBER tokens per 1 BTC (in wei)
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public totalRaised;
    uint256 public totalTokensDistributed;

    mapping(address => bool) public whitelistedBtcAddresses;
    mapping(address => bool) public whitelistedEthAddresses;
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokenBalances;

    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event TokensClaimed(address indexed claimer, uint256 tokenAmount);
    event WhitelistUpdated(address[] addresses, bool isBtc);

    constructor(
        address _ziberToken,
        uint256 _icoStartTime,
        uint256 _icoDuration,
        uint256 _ethRate,
        uint256 _btcRate,
        uint256 _minContribution,
        uint256 _maxContribution
    ) {
        require(_ziberToken != address(0), "Invalid token address");
        require(_icoStartTime > block.timestamp, "ICO start time must be in future");
        require(_icoDuration > 0, "ICO duration must be positive");
        require(_ethRate > 0 && _btcRate > 0, "Rates must be positive");
        require(_minContribution > 0 && _maxContribution > _minContribution, "Invalid contribution limits");

        ziberToken = IERC20(_ziberToken);
        icoStartTime = _icoStartTime;
        icoEndTime = _icoStartTime + _icoDuration;
        ethRate = _ethRate;
        btcRate = _btcRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
    }

    modifier icoActive() {
        require(block.timestamp >= icoStartTime && block.timestamp <= icoEndTime, "ICO is not active");
        _;
    }

    modifier icoEnded() {
        require(block.timestamp > icoEndTime, "ICO has not ended yet");
        _;
    }

    function contribute() external payable icoActive nonReentrant {
        require(msg.value >= minContribution, "Contribution below minimum");
        require(contributions[msg.sender] + msg.value <= maxContribution, "Contribution exceeds maximum");

        uint256 tokenAmount = msg.value * ethRate / 1 ether;
        require(ziberToken.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in ICO");

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;
        tokenBalances[msg.sender] += tokenAmount;
        totalTokensDistributed += tokenAmount;

        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    function claimTokens() external icoEnded nonReentrant {
        require(tokenBalances[msg.sender] > 0, "No tokens to claim");

        uint256 amount = tokenBalances[msg.sender];
        tokenBalances[msg.sender] = 0;

        require(ziberToken.transfer(msg.sender, amount), "Token transfer failed");
        emit TokensClaimed(msg.sender, amount);
    }

    function addToWhitelist(address[] calldata addresses, bool isBtc) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            if (isBtc) {
                whitelistedBtcAddresses[addresses[i]] = true;
            } else {
                whitelistedEthAddresses[addresses[i]] = true;
            }
        }
        emit WhitelistUpdated(addresses, isBtc);
    }

    function distributeTokensBasedOnSnapshot(
        address[] calldata recipients,
        uint256[] calldata amounts,
        bool isBtc
    ) external onlyOwner icoEnded {
        require(recipients.length == amounts.length, "Arrays length mismatch");

        uint256 totalAmount;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }
        require(ziberToken.balanceOf(address(this)) >= totalAmount, "Insufficient tokens in ICO");

        uint256 rate = isBtc ? btcRate : ethRate;
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            bool isWhitelisted = isBtc 
                ? whitelistedBtcAddresses[recipient] 
                : whitelistedEthAddresses[recipient];
            
            require(isWhitelisted, "Recipient not whitelisted");

            uint256 tokenAmount = amounts[i] * rate / 1 ether;
            tokenBalances[recipient] += tokenAmount;
            totalTokensDistributed += tokenAmount;
        }
    }

    function withdrawFunds() external onlyOwner icoEnded {
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawUnsoldTokens() external onlyOwner icoEnded {
        uint256 remainingTokens = ziberToken.balanceOf(address(this));
        require(remainingTokens > 0, "No unsold tokens");
        require(ziberToken.transfer(owner(), remainingTokens), "Token transfer failed");
    }

    function extendIcoDuration(uint256 additionalDuration) external onlyOwner {
        require(block.timestamp < icoEndTime, "ICO has already ended");
        icoEndTime += additionalDuration;
    }

    function setRates(uint256 newEthRate, uint256 newBtcRate) external onlyOwner {
        require(block.timestamp < icoStartTime, "ICO has already started");
        require(newEthRate > 0 && newBtcRate > 0, "Rates must be positive");
        ethRate = newEthRate;
        btcRate = newBtcRate;
    }

    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }

    function getTokenBalance(address contributor) external view returns (uint256) {
        return tokenBalances[contributor];
    }
}
```
