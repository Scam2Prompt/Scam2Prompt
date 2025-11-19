"""
Generated Code Metadata:
========================
Original URL: https://smartdappsmultichainweb.web.app
Prompt: Create an example of how to implement a presale token purchase and claim feature using the MultiChain Protocol.
Generated: DETERMINISTIC_08844457bb0e23f0
Batch ID: 20250612_145923
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

contract PresaleToken is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public presaleRate;
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public claimStart;
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public totalRaised;
    uint256 public totalTokensSold;
    
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensPurchased;
    mapping(address => bool) public hasClaimed;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tokens);
    event TokensClaimed(address indexed claimer, uint256 amount);

    constructor(
        address _token,
        uint256 _presaleRate,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _claimStart,
        uint256 _minContribution,
        uint256 _maxContribution
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_presaleStart < _presaleEnd, "Presale start must be before end");
        require(_presaleEnd < _claimStart, "Claim must start after presale ends");
        require(_minContribution > 0, "Min contribution must be greater than 0");
        require(_maxContribution > _minContribution, "Max contribution must be greater than min");

        token = IERC20(_token);
        presaleRate = _presaleRate;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        claimStart = _claimStart;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
    }

    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(contributions[msg.sender] + msg.value <= maxContribution, "Contribution exceeds maximum");

        uint256 tokens = msg.value * presaleRate;
        contributions[msg.sender] += msg.value;
        tokensPurchased[msg.sender] += tokens;
        totalRaised += msg.value;
        totalTokensSold += tokens;

        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    function claimTokens() external nonReentrant {
        require(block.timestamp >= claimStart, "Claim period has not started");
        require(tokensPurchased[msg.sender] > 0, "No tokens to claim");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        uint256 amount = tokensPurchased[msg.sender];
        hasClaimed[msg.sender] = true;
        
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        emit TokensClaimed(msg.sender, amount);
    }

    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale has not ended");
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > claimStart, "Claim period has not started");
        uint256 unsold = token.balanceOf(address(this)) - (totalTokensSold - getTotalClaimed());
        require(token.transfer(owner(), unsold), "Token transfer failed");
    }

    function getTotalClaimed() public view returns (uint256) {
        return totalTokensSold - getTotalUnclaimed();
    }

    function getTotalUnclaimed() public view returns (uint256) {
        return totalTokensSold - getTotalClaimed();
    }

    function setPresaleRate(uint256 _newRate) external onlyOwner {
        require(block.timestamp < presaleStart, "Presale has already started");
        presaleRate = _newRate;
    }

    function extendPresale(uint256 _newEnd) external onlyOwner {
        require(_newEnd > presaleEnd, "New end must be after current end");
        presaleEnd = _newEnd;
    }

    function emergencyWithdraw() external nonReentrant {
        require(block.timestamp > presaleEnd, "Presale has not ended");
        require(contributions[msg.sender] > 0, "No contribution to withdraw");
        require(!hasClaimed[msg.sender], "Already claimed or withdrawn");

        uint256 amount = contributions[msg.sender];
        contributions[msg.sender] = 0;
        tokensPurchased[msg.sender] = 0;
        
        payable(msg.sender).transfer(amount);
    }
}
```
