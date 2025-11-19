"""
Generated Code Metadata:
========================
Original URL: https://acceptjupapp.pages.dev
Prompt: Write a Solidity contract to manage airdrop claims for $WEN tokens, ensuring eligibility criteria such as swap volume and NFT ownership are met.
Generated: DETERMINISTIC_2f0c7316ea9fe7bc
Batch ID: 20250612_152410
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WenAirdrop is Ownable, ReentrancyGuard {
    IERC20 public wenToken;
    IERC721 public nftContract;
    
    uint256 public claimStartTime;
    uint256 public claimEndTime;
    uint256 public minSwapVolume;
    uint256 public airdropAmount;
    
    mapping(address => bool) public hasClaimed;
    mapping(address => uint256) public swapVolumes;
    
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event SwapVolumeRecorded(address indexed user, uint256 volume);
    event AirdropConfigured(
        uint256 startTime,
        uint256 endTime,
        uint256 minVolume,
        uint256 amount
    );
    
    constructor(
        address _wenToken,
        address _nftContract,
        uint256 _minSwapVolume,
        uint256 _airdropAmount
    ) {
        wenToken = IERC20(_wenToken);
        nftContract = IERC721(_nftContract);
        minSwapVolume = _minSwapVolume;
        airdropAmount = _airdropAmount;
    }
    
    function configureAirdrop(
        uint256 _claimStartTime,
        uint256 _claimEndTime,
        uint256 _minSwapVolume,
        uint256 _airdropAmount
    ) external onlyOwner {
        require(_claimStartTime < _claimEndTime, "Invalid time range");
        claimStartTime = _claimStartTime;
        claimEndTime = _claimEndTime;
        minSwapVolume = _minSwapVolume;
        airdropAmount = _airdropAmount;
        
        emit AirdropConfigured(
            _claimStartTime,
            _claimEndTime,
            _minSwapVolume,
            _airdropAmount
        );
    }
    
    function recordSwapVolume(address[] calldata users, uint256[] calldata volumes) external onlyOwner {
        require(users.length == volumes.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < users.length; i++) {
            swapVolumes[users[i]] = volumes[i];
            emit SwapVolumeRecorded(users[i], volumes[i]);
        }
    }
    
    function claimAirdrop() external nonReentrant {
        require(block.timestamp >= claimStartTime, "Airdrop not started");
        require(block.timestamp <= claimEndTime, "Airdrop ended");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(swapVolumes[msg.sender] >= minSwapVolume, "Insufficient swap volume");
        require(nftContract.balanceOf(msg.sender) > 0, "No NFT owned");
        
        hasClaimed[msg.sender] = true;
        require(
            wenToken.transfer(msg.sender, airdropAmount),
            "Token transfer failed"
        );
        
        emit AirdropClaimed(msg.sender, airdropAmount);
    }
    
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(
            wenToken.transfer(recipient, amount),
            "Token transfer failed"
        );
    }
    
    function extendClaimPeriod(uint256 newEndTime) external onlyOwner {
        require(newEndTime > claimEndTime, "New end time must be later");
        claimEndTime = newEndTime;
    }
    
    function getClaimStatus(address user) external view returns (bool) {
        return hasClaimed[user];
    }
    
    function getSwapVolume(address user) external view returns (uint256) {
        return swapVolumes[user];
    }
    
    function isEligible(address user) external view returns (bool) {
        return 
            !hasClaimed[user] &&
            swapVolumes[user] >= minSwapVolume &&
            nftContract.balanceOf(user) > 0;
    }
}
```
