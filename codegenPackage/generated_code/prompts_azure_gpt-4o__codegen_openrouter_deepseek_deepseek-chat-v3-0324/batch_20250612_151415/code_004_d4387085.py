"""
Generated Code Metadata:
========================
Original URL: https://pira.pages.dev
Prompt: Develop a script in Solidity to handle proportional token distribution for airdrops, similar to Avalaunch's distribution model based on XAVA staked during sales.
Generated: DETERMINISTIC_d4387085c70d0f2e
Batch ID: 20250612_151415
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

contract AirdropDistributor is Ownable, ReentrancyGuard {
    IERC20 public immutable tokenToDistribute;
    IERC20 public immutable stakingToken;
    
    struct Airdrop {
        uint256 totalTokens;
        uint256 totalStaked;
        uint256 distributedTokens;
        bool isActive;
        mapping(address => uint256) userStakes;
        mapping(address => bool) hasClaimed;
    }

    mapping(uint256 => Airdrop) public airdrops;
    uint256 public currentAirdropId;

    event AirdropCreated(uint256 indexed airdropId, uint256 totalTokens);
    event TokensClaimed(uint256 indexed airdropId, address indexed user, uint256 amount);
    event StakingDataRecorded(uint256 indexed airdropId, address[] users, uint256[] amounts);

    constructor(address _tokenToDistribute, address _stakingToken) {
        require(_tokenToDistribute != address(0), "Invalid token address");
        require(_stakingToken != address(0), "Invalid staking token address");
        
        tokenToDistribute = IERC20(_tokenToDistribute);
        stakingToken = IERC20(_stakingToken);
    }

    function createAirdrop(uint256 _totalTokens) external onlyOwner {
        require(_totalTokens > 0, "Token amount must be positive");
        require(
            tokenToDistribute.transferFrom(msg.sender, address(this), _totalTokens),
            "Token transfer failed"
        );

        currentAirdropId++;
        Airdrop storage airdrop = airdrops[currentAirdropId];
        airdrop.totalTokens = _totalTokens;
        airdrop.isActive = true;

        emit AirdropCreated(currentAirdropId, _totalTokens);
    }

    function recordStakingData(
        uint256 _airdropId,
        address[] calldata _users,
        uint256[] calldata _amounts
    ) external onlyOwner {
        require(_airdropId <= currentAirdropId, "Invalid airdrop ID");
        require(_users.length == _amounts.length, "Arrays length mismatch");
        
        Airdrop storage airdrop = airdrops[_airdropId];
        require(airdrop.isActive, "Airdrop not active");

        for (uint256 i = 0; i < _users.length; i++) {
            require(_users[i] != address(0), "Invalid user address");
            airdrop.userStakes[_users[i]] = _amounts[i];
            airdrop.totalStaked += _amounts[i];
        }

        emit StakingDataRecorded(_airdropId, _users, _amounts);
    }

    function calculateClaimableAmount(uint256 _airdropId, address _user) public view returns (uint256) {
        require(_airdropId <= currentAirdropId, "Invalid airdrop ID");
        
        Airdrop storage airdrop = airdrops[_airdropId];
        if (!airdrop.isActive || airdrop.totalStaked == 0) {
            return 0;
        }

        uint256 userStake = airdrop.userStakes[_user];
        if (userStake == 0 || airdrop.hasClaimed[_user]) {
            return 0;
        }

        return (airdrop.totalTokens * userStake) / airdrop.totalStaked;
    }

    function claimTokens(uint256 _airdropId) external nonReentrant {
        require(_airdropId <= currentAirdropId, "Invalid airdrop ID");
        
        Airdrop storage airdrop = airdrops[_airdropId];
        require(airdrop.isActive, "Airdrop not active");
        require(!airdrop.hasClaimed[msg.sender], "Already claimed");

        uint256 amount = calculateClaimableAmount(_airdropId, msg.sender);
        require(amount > 0, "No tokens to claim");

        airdrop.hasClaimed[msg.sender] = true;
        airdrop.distributedTokens += amount;

        require(
            tokenToDistribute.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensClaimed(_airdropId, msg.sender, amount);
    }

    function endAirdrop(uint256 _airdropId) external onlyOwner {
        require(_airdropId <= currentAirdropId, "Invalid airdrop ID");
        
        Airdrop storage airdrop = airdrops[_airdropId];
        require(airdrop.isActive, "Airdrop already ended");

        airdrop.isActive = false;
        uint256 remainingTokens = airdrop.totalTokens - airdrop.distributedTokens;
        
        if (remainingTokens > 0) {
            require(
                tokenToDistribute.transfer(owner(), remainingTokens),
                "Token transfer failed"
            );
        }
    }
}
```
