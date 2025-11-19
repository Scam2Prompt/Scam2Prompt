"""
Generated Code Metadata:
========================
Original URL: https://quantprotocol.xyz
Prompt: Create a smart contract on the Binance Smart Chain (BSC) for purchasing Quant Protocol tokens during the pre-sale phase. Ensure the contract includes vesting logic for team tokens with a 6-month period.
Generated: DETERMINISTIC_737c7aa0b87a1bd1
Batch ID: 20250612_154400
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

contract QuantPresale is Ownable, ReentrancyGuard {
    IERC20 public quantToken;
    address public treasuryWallet;
    
    uint256 public presaleRate; // Tokens per BNB
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public hardCap;
    uint256 public totalRaised;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    
    bool public isPresaleActive;
    bool public isTeamTokensVested;
    
    uint256 public constant VESTING_PERIOD = 180 days; // 6 months
    uint256 public teamTokensAllocated;
    uint256 public teamTokensClaimed;
    uint256 public vestingStartTime;
    
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensPurchased;
    
    event TokensPurchased(address indexed buyer, uint256 bnbAmount, uint256 tokenAmount);
    event TeamTokensVested(uint256 amount, uint256 vestingStart);
    event TeamTokensClaimed(address indexed teamMember, uint256 amount);
    event PresaleStatusChanged(bool isActive);
    event PresaleExtended(uint256 newEndTime);
    
    constructor(
        address _quantToken,
        address _treasuryWallet,
        uint256 _presaleRate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap,
        uint256 _presaleDuration
    ) {
        require(_quantToken != address(0), "Quant token address cannot be zero");
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero");
        require(_presaleRate > 0, "Presale rate must be greater than zero");
        require(_minContribution > 0, "Min contribution must be greater than zero");
        require(_maxContribution > _minContribution, "Max contribution must be greater than min");
        require(_hardCap > 0, "Hard cap must be greater than zero");
        require(_presaleDuration > 0, "Presale duration must be greater than zero");
        
        quantToken = IERC20(_quantToken);
        treasuryWallet = _treasuryWallet;
        presaleRate = _presaleRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        hardCap = _hardCap;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + _presaleDuration;
        isPresaleActive = true;
    }
    
    receive() external payable {
        buyTokens();
    }
    
    function buyTokens() public payable nonReentrant {
        require(isPresaleActive, "Presale is not active");
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale period has ended");
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(msg.value <= maxContribution, "Contribution exceeds maximum");
        require(totalRaised + msg.value <= hardCap, "Hard cap reached");
        
        uint256 tokenAmount = msg.value * presaleRate;
        require(quantToken.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");
        
        contributions[msg.sender] += msg.value;
        tokensPurchased[msg.sender] += tokenAmount;
        totalRaised += msg.value;
        
        (bool sent, ) = treasuryWallet.call{value: msg.value}("");
        require(sent, "Failed to send BNB to treasury");
        
        quantToken.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }
    
    function vestTeamTokens(uint256 amount) external onlyOwner {
        require(!isTeamTokensVested, "Team tokens already vested");
        require(block.timestamp > presaleEndTime, "Presale must be ended");
        require(quantToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");
        
        teamTokensAllocated = amount;
        vestingStartTime = block.timestamp;
        isTeamTokensVested = true;
        
        emit TeamTokensVested(amount, vestingStartTime);
    }
    
    function claimTeamTokens(address teamMember, uint256 amount) external onlyOwner {
        require(isTeamTokensVested, "Team tokens not vested yet");
        require(block.timestamp >= vestingStartTime + VESTING_PERIOD, "Vesting period not ended");
        require(teamTokensClaimed + amount <= teamTokensAllocated, "Exceeds allocated team tokens");
        
        teamTokensClaimed += amount;
        quantToken.transfer(teamMember, amount);
        
        emit TeamTokensClaimed(teamMember, amount);
    }
    
    function togglePresaleStatus(bool status) external onlyOwner {
        isPresaleActive = status;
        emit PresaleStatusChanged(status);
    }
    
    function extendPresale(uint256 additionalDuration) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Presale already ended");
        presaleEndTime += additionalDuration;
        emit PresaleExtended(presaleEndTime);
    }
    
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(quantToken) || block.timestamp > presaleEndTime + 30 days, "Cannot recover quant tokens until 30 days after presale");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
    
    function getPresaleStatus() external view returns (bool) {
        return isPresaleActive && block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime;
    }
    
    function getVestingStatus() external view returns (bool) {
        return isTeamTokensVested && block.timestamp >= vestingStartTime + VESTING_PERIOD;
    }
}
```
