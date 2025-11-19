"""
Generated Code Metadata:
========================
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for a token sale with a vesting period, similar to Matmo's presale structure.
Generated: DETERMINISTIC_37819b0f70f5d36f
Batch ID: 20250622_205112
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

contract TokenSaleWithVesting is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public minPurchase;
    uint256 public maxPurchase;
    uint256 public hardCap;
    uint256 public totalRaised;
    uint256 public saleStartTime;
    uint256 public saleEndTime;
    
    struct VestingSchedule {
        uint256 cliff; // Cliff period in seconds
        uint256 duration; // Vesting duration in seconds
        uint256 interval; // Interval between vesting periods in seconds
        uint256 initialReleasePercentage; // Percentage of tokens released immediately after cliff (100 = 100%)
    }
    
    VestingSchedule public vestingSchedule;
    
    struct Investor {
        uint256 investedAmount;
        uint256 tokenAmount;
        uint256 claimedAmount;
        uint256 lastClaimTime;
    }
    
    mapping(address => Investor) public investors;
    address[] public investorAddresses;
    
    event TokensPurchased(address indexed investor, uint256 amount, uint256 tokenAmount);
    event TokensClaimed(address indexed investor, uint256 amount);
    
    constructor(
        address _token,
        uint256 _tokenPrice,
        uint256 _minPurchase,
        uint256 _maxPurchase,
        uint256 _hardCap,
        uint256 _saleStartTime,
        uint256 _saleEndTime,
        uint256 _cliff,
        uint256 _duration,
        uint256 _interval,
        uint256 _initialReleasePercentage
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_minPurchase > 0, "Min purchase must be greater than zero");
        require(_maxPurchase > _minPurchase, "Max purchase must be greater than min purchase");
        require(_hardCap > 0, "Hard cap must be greater than zero");
        require(_saleEndTime > _saleStartTime, "Sale end time must be after start time");
        
        token = IERC20(_token);
        tokenPrice = _tokenPrice;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        hardCap = _hardCap;
        saleStartTime = _saleStartTime;
        saleEndTime = _saleEndTime;
        
        vestingSchedule = VestingSchedule({
            cliff: _cliff,
            duration: _duration,
            interval: _interval,
            initialReleasePercentage: _initialReleasePercentage
        });
    }
    
    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "Sale is not active");
        require(msg.value >= minPurchase, "Amount is less than minimum purchase");
        require(msg.value <= maxPurchase, "Amount exceeds maximum purchase");
        require(totalRaised + msg.value <= hardCap, "Hard cap reached");
        
        uint256 tokenAmount = (msg.value * 10**18) / tokenPrice;
        require(token.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in contract");
        
        Investor storage investor = investors[msg.sender];
        if (investor.investedAmount == 0) {
            investorAddresses.push(msg.sender);
        }
        
        investor.investedAmount += msg.value;
        investor.tokenAmount += tokenAmount;
        totalRaised += msg.value;
        
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }
    
    function claimTokens() external nonReentrant {
        Investor storage investor = investors[msg.sender];
        require(investor.tokenAmount > 0, "No tokens to claim");
        
        uint256 claimableAmount = getClaimableAmount(msg.sender);
        require(claimableAmount > 0, "No tokens available to claim at this time");
        
        investor.claimedAmount += claimableAmount;
        investor.lastClaimTime = block.timestamp;
        
        require(token.transfer(msg.sender, claimableAmount), "Token transfer failed");
        emit TokensClaimed(msg.sender, claimableAmount);
    }
    
    function getClaimableAmount(address investorAddress) public view returns (uint256) {
        Investor memory investor = investors[investorAddress];
        if (investor.tokenAmount == 0) return 0;
        
        uint256 vestingStartTime = saleEndTime + vestingSchedule.cliff;
        if (block.timestamp < vestingStartTime) return 0;
        
        if (investor.lastClaimTime == 0) {
            // First claim after cliff
            uint256 initialRelease = (investor.tokenAmount * vestingSchedule.initialReleasePercentage) / 100;
            return initialRelease;
        }
        
        if (block.timestamp >= vestingStartTime + vestingSchedule.duration) {
            // All tokens vested
            return investor.tokenAmount - investor.claimedAmount;
        }
        
        uint256 timeSinceLastClaim = block.timestamp - max(investor.lastClaimTime, vestingStartTime);
        uint256 intervalsPassed = timeSinceLastClaim / vestingSchedule.interval;
        
        if (intervalsPassed == 0) return 0;
        
        uint256 totalVestingAmount = investor.tokenAmount - 
            ((investor.tokenAmount * vestingSchedule.initialReleasePercentage) / 100);
        uint256 vestedPerInterval = totalVestingAmount / 
            (vestingSchedule.duration / vestingSchedule.interval);
        
        uint256 newVestedAmount = intervalsPassed * vestedPerInterval;
        uint256 totalVestedAmount = ((investor.tokenAmount * vestingSchedule.initialReleasePercentage) / 100) + 
            newVestedAmount;
        
        if (totalVestedAmount > investor.tokenAmount) {
            totalVestedAmount = investor.tokenAmount;
        }
        
        return totalVestedAmount - investor.claimedAmount;
    }
    
    function max(uint256 a, uint256 b) internal pure returns (uint256) {
        return a >= b ? a : b;
    }
    
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale has not ended yet");
        payable(owner()).transfer(address(this).balance);
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale has not ended yet");
        uint256 unsoldTokens = token.balanceOf(address(this)) - 
            (totalRaised * 10**18 / tokenPrice - getTotalClaimedTokens());
        require(unsoldTokens > 0, "No unsold tokens");
        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }
    
    function getTotalClaimedTokens() public view returns (uint256) {
        uint256 totalClaimed;
        for (uint256 i = 0; i < investorAddresses.length; i++) {
            totalClaimed += investors[investorAddresses[i]].claimedAmount;
        }
        return totalClaimed;
    }
    
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Token price must be greater than zero");
        tokenPrice = newPrice;
    }
    
    function extendSale(uint256 newEndTime) external onlyOwner {
        require(newEndTime > saleEndTime, "New end time must be after current end time");
        saleEndTime = newEndTime;
    }
    
    function getInvestorCount() external view returns (uint256) {
        return investorAddresses.length;
    }
}
```
