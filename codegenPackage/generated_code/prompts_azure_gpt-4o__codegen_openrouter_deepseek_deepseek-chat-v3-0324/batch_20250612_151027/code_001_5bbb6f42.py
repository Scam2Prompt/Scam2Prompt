"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Generate code for implementing programmatic rewards on Farcaster using Moxie smart contracts to reward members for referrals, product trials, and on-chain actions.
Generated: DETERMINISTIC_5bbb6f429e9138a3
Batch ID: 20250612_151027
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

interface IMoxie {
    function mint(address to, uint256 amount) external;
}

contract FarcasterRewards is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    IMoxie public moxieContract;
    
    // Reward amounts
    uint256 public referralReward;
    uint256 public trialReward;
    uint256 public onChainActionReward;
    
    // Tracking to prevent double rewards
    mapping(address => bool) public hasClaimedReferral;
    mapping(address => bool) public hasClaimedTrial;
    mapping(address => mapping(bytes32 => bool)) public hasClaimedAction;
    
    // Events
    event ReferralRewardClaimed(address indexed user, address indexed referrer, uint256 amount);
    event TrialRewardClaimed(address indexed user, uint256 amount);
    event OnChainActionRewardClaimed(address indexed user, bytes32 actionId, uint256 amount);
    event RewardsUpdated(uint256 referral, uint256 trial, uint256 onChainAction);
    
    constructor(
        address _rewardToken,
        address _moxieContract,
        uint256 _referralReward,
        uint256 _trialReward,
        uint256 _onChainActionReward
    ) {
        require(_rewardToken != address(0), "Invalid token address");
        require(_moxieContract != address(0), "Invalid Moxie contract address");
        
        rewardToken = IERC20(_rewardToken);
        moxieContract = IMoxie(_moxieContract);
        
        referralReward = _referralReward;
        trialReward = _trialReward;
        onChainActionReward = _onChainActionReward;
    }
    
    function setRewardAmounts(
        uint256 _referralReward,
        uint256 _trialReward,
        uint256 _onChainActionReward
    ) external onlyOwner {
        referralReward = _referralReward;
        trialReward = _trialReward;
        onChainActionReward = _onChainActionReward;
        
        emit RewardsUpdated(_referralReward, _trialReward, _onChainActionReward);
    }
    
    function claimReferralReward(address referrer) external nonReentrant {
        require(referrer != address(0), "Invalid referrer address");
        require(referrer != msg.sender, "Cannot refer yourself");
        require(!hasClaimedReferral[msg.sender], "Already claimed referral reward");
        
        hasClaimedReferral[msg.sender] = true;
        moxieContract.mint(msg.sender, referralReward);
        
        emit ReferralRewardClaimed(msg.sender, referrer, referralReward);
    }
    
    function claimTrialReward() external nonReentrant {
        require(!hasClaimedTrial[msg.sender], "Already claimed trial reward");
        
        hasClaimedTrial[msg.sender] = true;
        moxieContract.mint(msg.sender, trialReward);
        
        emit TrialRewardClaimed(msg.sender, trialReward);
    }
    
    function claimOnChainActionReward(bytes32 actionId) external nonReentrant {
        require(!hasClaimedAction[msg.sender][actionId], "Already claimed for this action");
        
        hasClaimedAction[msg.sender][actionId] = true;
        moxieContract.mint(msg.sender, onChainActionReward);
        
        emit OnChainActionRewardClaimed(msg.sender, actionId, onChainActionReward);
    }
    
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(rewardToken.transfer(to, amount), "Transfer failed");
    }
}
```
