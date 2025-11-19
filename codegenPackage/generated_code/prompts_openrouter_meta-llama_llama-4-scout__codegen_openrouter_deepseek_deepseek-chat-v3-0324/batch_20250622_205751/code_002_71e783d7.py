"""
Generated Code Metadata:
========================
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Develop a simple decentralized application (dApp) that can run on the Botanix EVM, utilizing Bitcoin as the native asset for staking and leveraging verifiable randomness.
Generated: DETERMINISTIC_71e783d77f3d0b24
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IRandomness {
    function getRandomNumber() external returns (bytes32 requestId);
    function randomResult() external view returns (uint256);
}

contract SimpleDApp is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // State variables
    IRandomness public randomnessProvider;
    uint256 public stakingRewardPercentage = 10; // 10% reward
    uint256 public totalStaked;
    uint256 public lastRandomNumber;
    
    // Staker information
    struct Staker {
        uint256 amount;
        uint256 reward;
        bool hasStaked;
    }
    
    mapping(address => Staker) public stakers;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RandomNumberGenerated(uint256 randomNumber);
    
    // Constructor
    constructor(address _randomnessProvider) {
        randomnessProvider = IRandomness(_randomnessProvider);
    }
    
    /**
     * @dev Stake Bitcoin (native asset)
     */
    function stake() external payable nonReentrant {
        require(msg.value > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        
        if (staker.hasStaked) {
            staker.amount = staker.amount.add(msg.value);
        } else {
            staker.amount = msg.value;
            staker.hasStaked = true;
        }
        
        totalStaked = totalStaked.add(msg.value);
        emit Staked(msg.sender, msg.value);
    }
    
    /**
     * @dev Unstake and claim rewards
     */
    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.hasStaked, "No stake found");
        require(staker.amount > 0, "No stake amount");
        
        uint256 amount = staker.amount;
        uint256 reward = calculateReward(staker.amount);
        uint256 total = amount.add(reward);
        
        totalStaked = totalStaked.sub(amount);
        staker.amount = 0;
        staker.reward = 0;
        staker.hasStaked = false;
        
        (bool success, ) = msg.sender.call{value: total}("");
        require(success, "Transfer failed");
        
        emit Unstaked(msg.sender, amount, reward);
    }
    
    /**
     * @dev Calculate staking reward
     */
    function calculateReward(uint256 amount) public view returns (uint256) {
        return amount.mul(stakingRewardPercentage).div(100);
    }
    
    /**
     * @dev Request a random number from the randomness provider
     */
    function requestRandomNumber() external onlyOwner {
        randomnessProvider.getRandomNumber();
    }
    
    /**
     * @dev Callback function for the randomness provider
     */
    function fulfillRandomness(bytes32 requestId, uint256 randomness) external {
        require(msg.sender == address(randomnessProvider), "Only randomness provider");
        lastRandomNumber = randomness;
        emit RandomNumberGenerated(randomness);
    }
    
    /**
     * @dev Update randomness provider address
     */
    function setRandomnessProvider(address _randomnessProvider) external onlyOwner {
        randomnessProvider = IRandomness(_randomnessProvider);
    }
    
    /**
     * @dev Update staking reward percentage
     */
    function setStakingRewardPercentage(uint256 _percentage) external onlyOwner {
        require(_percentage <= 100, "Percentage cannot exceed 100");
        stakingRewardPercentage = _percentage;
    }
    
    /**
     * @dev Withdraw contract balance (only owner)
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }
    
    // Fallback function to receive Bitcoin (native asset)
    receive() external payable {}
}
```
