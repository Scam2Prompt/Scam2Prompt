"""
Generated Code Metadata:
========================
Original URL: https://dequodss.web.app
Prompt: Generate a smart contract code snippet in Rust or Solidity that allows users to stake their DeGods and earn $DUST tokens, inspired by the DeGods' staking system.
Generated: DETERMINISTIC_3ce3f00e36ac9066
Batch ID: 20250622_205751
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeGodsStaking is ReentrancyGuard, Ownable {
    IERC721 public deGodsNFT;
    IERC20 public dustToken;
    
    uint256 public constant REWARD_RATE = 10 ether; // 10 DUST per day per NFT
    uint256 public constant MIN_STAKE_TIME = 1 days;
    
    struct Staker {
        uint256[] tokenIds;
        uint256 lastClaimTime;
        uint256 totalEarned;
    }
    
    mapping(address => Staker) public stakers;
    mapping(uint256 => address) public tokenOwner;
    
    event Staked(address indexed user, uint256[] tokenIds);
    event Unstaked(address indexed user, uint256[] tokenIds);
    event RewardClaimed(address indexed user, uint256 amount);
    
    constructor(address _deGodsNFT, address _dustToken) {
        deGodsNFT = IERC721(_deGodsNFT);
        dustToken = IERC20(_dustToken);
    }
    
    function stake(uint256[] calldata _tokenIds) external nonReentrant {
        require(_tokenIds.length > 0, "Must stake at least one NFT");
        
        Staker storage staker = stakers[msg.sender];
        
        for (uint256 i = 0; i < _tokenIds.length; i++) {
            uint256 tokenId = _tokenIds[i];
            require(deGodsNFT.ownerOf(tokenId) == msg.sender, "Not the owner");
            require(tokenOwner[tokenId] == address(0), "Token already staked");
            
            deGodsNFT.transferFrom(msg.sender, address(this), tokenId);
            staker.tokenIds.push(tokenId);
            tokenOwner[tokenId] = msg.sender;
        }
        
        if (staker.lastClaimTime == 0) {
            staker.lastClaimTime = block.timestamp;
        }
        
        emit Staked(msg.sender, _tokenIds);
    }
    
    function unstake(uint256[] calldata _tokenIds) external nonReentrant {
        require(_tokenIds.length > 0, "Must unstake at least one NFT");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.tokenIds.length >= _tokenIds.length, "Not enough tokens staked");
        
        _claimRewards();
        
        for (uint256 i = 0; i < _tokenIds.length; i++) {
            uint256 tokenId = _tokenIds[i];
            require(tokenOwner[tokenId] == msg.sender, "Not the staker");
            
            _removeTokenId(staker.tokenIds, tokenId);
            delete tokenOwner[tokenId];
            deGodsNFT.transferFrom(address(this), msg.sender, tokenId);
        }
        
        emit Unstaked(msg.sender, _tokenIds);
    }
    
    function claimRewards() external nonReentrant {
        _claimRewards();
    }
    
    function _claimRewards() private {
        Staker storage staker = stakers[msg.sender];
        require(staker.tokenIds.length > 0, "No tokens staked");
        
        uint256 reward = calculateRewards(msg.sender);
        if (reward > 0) {
            staker.totalEarned += reward;
            staker.lastClaimTime = block.timestamp;
            require(dustToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }
    
    function calculateRewards(address _user) public view returns (uint256) {
        Staker memory staker = stakers[_user];
        if (staker.tokenIds.length == 0 || staker.lastClaimTime == 0) {
            return 0;
        }
        
        uint256 timeStaked = block.timestamp - staker.lastClaimTime;
        return (staker.tokenIds.length * REWARD_RATE * timeStaked) / 1 days;
    }
    
    function _removeTokenId(uint256[] storage array, uint256 tokenId) private {
        for (uint256 i = 0; i < array.length; i++) {
            if (array[i] == tokenId) {
                array[i] = array[array.length - 1];
                array.pop();
                break;
            }
        }
    }
    
    function withdrawDust(uint256 _amount) external onlyOwner {
        require(dustToken.transfer(owner(), _amount), "Transfer failed");
    }
    
    function getStakedTokens(address _user) external view returns (uint256[] memory) {
        return stakers[_user].tokenIds;
    }
    
    function getTotalEarned(address _user) external view returns (uint256) {
        return stakers[_user].totalEarned;
    }
}
```
