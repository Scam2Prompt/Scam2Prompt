"""
Generated Code Metadata:
========================
Original URL: https://grokxcoinai.com
Prompt: Generate a Solidity smart contract that incorporates KYC verification and prevents participation by whales, inspired by $GROK's presale strategy.
Generated: DETERMINISTIC_75406343f33aea85
Batch ID: 20250612_155102
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

contract KYCPresale is Ownable {
    using SafeMath for uint256;

    // KYC verification status
    mapping(address => bool) public isKYCVerified;

    // Participation tracking
    mapping(address => uint256) public contributions;
    uint256 public totalContributions;

    // Presale parameters
    uint256 public constant MIN_CONTRIBUTION = 0.1 ether;
    uint256 public constant MAX_CONTRIBUTION = 5 ether;
    uint256 public constant MAX_TOTAL_CONTRIBUTIONS = 100 ether;
    uint256 public constant PRESALE_DURATION = 7 days;
    uint256 public presaleEndTime;

    // Token details
    IERC20 public token;
    uint256 public constant TOKENS_PER_ETH = 1000;

    // Events
    event KYCVerified(address indexed user);
    event Contributed(address indexed user, uint256 amount);
    event TokensClaimed(address indexed user, uint256 amount);
    event PresaleEnded(uint256 totalContributions);

    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress);
        presaleEndTime = block.timestamp.add(PRESALE_DURATION);
    }

    modifier onlyKYCVerified() {
        require(isKYCVerified[msg.sender], "KYC verification required");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        _;
    }

    // Admin function to verify KYC
    function verifyKYC(address _user) external onlyOwner {
        require(!isKYCVerified[_user], "User already KYC verified");
        isKYCVerified[_user] = true;
        emit KYCVerified(_user);
    }

    // Contribute to presale
    function contribute() external payable onlyKYCVerified presaleActive {
        require(msg.value >= MIN_CONTRIBUTION, "Contribution too low");
        require(msg.value <= MAX_CONTRIBUTION, "Contribution exceeds limit");

        uint256 newTotal = totalContributions.add(msg.value);
        require(newTotal <= MAX_TOTAL_CONTRIBUTIONS, "Presale cap reached");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalContributions = newTotal;

        emit Contributed(msg.sender, msg.value);
    }

    // Claim tokens after presale ends
    function claimTokens() external onlyKYCVerified presaleEnded {
        require(contributions[msg.sender] > 0, "No contributions to claim");
        require(address(token).balance > 0, "No tokens available");

        uint256 contribution = contributions[msg.sender];
        uint256 tokenAmount = contribution.mul(TOKENS_PER_ETH);
        
        contributions[msg.sender] = 0;
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed");

        emit TokensClaimed(msg.sender, tokenAmount);
    }

    // Withdraw funds after presale ends
    function withdrawFunds() external onlyOwner presaleEnded {
        payable(owner()).transfer(address(this).balance);
    }

    // Emergency return funds if presale fails
    function emergencyRefund() external presaleEnded {
        require(totalContributions < MIN_CONTRIBUTION, "Presale was successful");
        require(contributions[msg.sender] > 0, "No contributions to refund");

        uint256 amount = contributions[msg.sender];
        contributions[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }

    // Extend presale duration if needed
    function extendPresale(uint256 _additionalTime) external onlyOwner presaleActive {
        presaleEndTime = presaleEndTime.add(_additionalTime);
    }

    // Get token amount for a given contribution
    function getTokenAmount(uint256 _ethAmount) public pure returns (uint256) {
        return _ethAmount.mul(TOKENS_PER_ETH);
    }

    // Get user's claimable token amount
    function getClaimableTokens(address _user) public view returns (uint256) {
        return contributions[_user].mul(TOKENS_PER_ETH);
    }
}
```
