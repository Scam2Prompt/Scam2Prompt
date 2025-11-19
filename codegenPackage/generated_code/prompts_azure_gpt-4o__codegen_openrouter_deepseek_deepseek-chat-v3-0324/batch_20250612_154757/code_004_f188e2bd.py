"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Develop a smart contract on the ERC20 or BSC20 blockchain to handle the distribution of $INIT tokens during the pre-sale and airdrop phases, ensuring compliance with the first-come-first-served model.
Generated: DETERMINISTIC_f188e2bd2ec49873
Batch ID: 20250612_154757
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract INITToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // 100 million tokens
    uint256 public constant PRESALE_SUPPLY = 30_000_000 * 10**18; // 30% for presale
    uint256 public constant AIRDROP_SUPPLY = 10_000_000 * 10**18; // 10% for airdrop
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public airdropStartTime;
    uint256 public airdropEndTime;
    
    uint256 public presaleTokensDistributed;
    uint256 public airdropTokensDistributed;
    
    uint256 public presaleRate = 1000; // 1 ETH = 1000 INIT tokens
    uint256 public minContribution = 0.1 ether;
    uint256 public maxContribution = 5 ether;
    
    mapping(address => bool) public presaleParticipants;
    mapping(address => bool) public airdropParticipants;
    
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensAirdropped(address indexed recipient, uint256 amount);
    
    constructor(
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _airdropStartTime,
        uint256 _airdropEndTime
    ) ERC20("INIT Token", "INIT") {
        require(_presaleStartTime < _presaleEndTime, "Invalid presale period");
        require(_airdropStartTime < _airdropEndTime, "Invalid airdrop period");
        
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        airdropStartTime = _airdropStartTime;
        airdropEndTime = _airdropEndTime;
        
        _mint(msg.sender, MAX_SUPPLY - PRESALE_SUPPLY - AIRDROP_SUPPLY);
    }
    
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }
    
    modifier isAirdropActive() {
        require(block.timestamp >= airdropStartTime && block.timestamp <= airdropEndTime, "Airdrop is not active");
        _;
    }
    
    function buyTokens() external payable isPresaleActive nonReentrant {
        require(msg.value >= minContribution && msg.value <= maxContribution, "Invalid contribution amount");
        require(!presaleParticipants[msg.sender], "Already participated in presale");
        require(presaleTokensDistributed < PRESALE_SUPPLY, "Presale supply exhausted");
        
        uint256 tokens = msg.value * presaleRate;
        require(presaleTokensDistributed + tokens <= PRESALE_SUPPLY, "Not enough tokens left");
        
        presaleParticipants[msg.sender] = true;
        presaleTokensDistributed += tokens;
        
        _transfer(owner(), msg.sender, tokens);
        emit TokensPurchased(msg.sender, tokens);
    }
    
    function claimAirdrop() external isAirdropActive nonReentrant {
        require(!airdropParticipants[msg.sender], "Already claimed airdrop");
        require(airdropTokensDistributed < AIRDROP_SUPPLY, "Airdrop supply exhausted");
        
        uint256 tokens = 500 * 10**18; // 500 INIT tokens per airdrop
        require(airdropTokensDistributed + tokens <= AIRDROP_SUPPLY, "Not enough tokens left");
        
        airdropParticipants[msg.sender] = true;
        airdropTokensDistributed += tokens;
        
        _transfer(owner(), msg.sender, tokens);
        emit TokensAirdropped(msg.sender, tokens);
    }
    
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
    
    function setPresaleRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Rate must be greater than 0");
        presaleRate = _newRate;
    }
    
    function setContributionLimits(uint256 _min, uint256 _max) external onlyOwner {
        require(_min > 0 && _max > _min, "Invalid limits");
        minContribution = _min;
        maxContribution = _max;
    }
    
    function extendPresale(uint256 _newEndTime) external onlyOwner {
        require(_newEndTime > presaleEndTime, "New end time must be after current end time");
        presaleEndTime = _newEndTime;
    }
    
    function extendAirdrop(uint256 _newEndTime) external onlyOwner {
        require(_newEndTime > airdropEndTime, "New end time must be after current end time");
        airdropEndTime = _newEndTime;
    }
    
    function burnUnsoldPresaleTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended yet");
        uint256 unsold = PRESALE_SUPPLY - presaleTokensDistributed;
        if (unsold > 0) {
            _burn(owner(), unsold);
        }
    }
    
    function burnUnclaimedAirdropTokens() external onlyOwner {
        require(block.timestamp > airdropEndTime, "Airdrop not ended yet");
        uint256 unclaimed = AIRDROP_SUPPLY - airdropTokensDistributed;
        if (unclaimed > 0) {
            _burn(owner(), unclaimed);
        }
    }
}
```
