"""
Generated Code Metadata:
========================
Original URL: https://stakewise.eu
Prompt: Create a smart contract example that interacts with StakeWise for staking Ethereum and distributing rewards.
Generated: DETERMINISTIC_b2ec348573be2dc1
Batch ID: 20250612_145832
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

interface IStakeWise {
    function deposit(uint256 assets, address receiver) external returns (uint256 shares);
    function redeem(uint256 shares, address receiver, address owner) external returns (uint256 assets);
    function balanceOf(address account) external view returns (uint256);
    function totalAssets() external view returns (uint256);
}

contract StakeWiseStaking is Ownable, ReentrancyGuard {
    IStakeWise public stakeWiseContract;
    IERC20 public stakeWiseToken;
    
    // Mapping to track user shares
    mapping(address => uint256) public userShares;
    
    // Total shares in the contract
    uint256 public totalShares;
    
    // Events
    event Staked(address indexed user, uint256 amount, uint256 shares);
    event Unstaked(address indexed user, uint256 amount, uint256 shares);
    event RewardDistributed(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor to initialize the contract
     * @param _stakeWiseContract Address of the StakeWise contract
     * @param _stakeWiseToken Address of the StakeWise token
     */
    constructor(address _stakeWiseContract, address _stakeWiseToken) {
        require(_stakeWiseContract != address(0), "Invalid StakeWise contract address");
        require(_stakeWiseToken != address(0), "Invalid StakeWise token address");
        
        stakeWiseContract = IStakeWise(_stakeWiseContract);
        stakeWiseToken = IERC20(_stakeWiseToken);
    }
    
    /**
     * @dev Stake ETH and receive StakeWise shares
     */
    function stake() external payable nonReentrant {
        require(msg.value > 0, "Must send ETH to stake");
        
        uint256 shares = stakeWiseContract.deposit{value: msg.value}(msg.value, address(this));
        
        userShares[msg.sender] += shares;
        totalShares += shares;
        
        emit Staked(msg.sender, msg.value, shares);
    }
    
    /**
     * @dev Unstake shares and receive ETH
     * @param shares Amount of shares to unstake
     */
    function unstake(uint256 shares) external nonReentrant {
        require(shares > 0, "Shares must be greater than 0");
        require(userShares[msg.sender] >= shares, "Insufficient shares");
        
        uint256 assets = stakeWiseContract.redeem(shares, msg.sender, address(this));
        
        userShares[msg.sender] -= shares;
        totalShares -= shares;
        
        emit Unstaked(msg.sender, assets, shares);
    }
    
    /**
     * @dev Distribute rewards to stakers proportionally
     */
    function distributeRewards() external onlyOwner nonReentrant {
        uint256 currentBalance = stakeWiseToken.balanceOf(address(this));
        require(currentBalance > 0, "No rewards to distribute");
        
        uint256 totalAssets = stakeWiseContract.totalAssets();
        require(totalAssets > 0, "No assets in StakeWise");
        
        for (uint256 i = 0; i < currentBalance; i++) {
            address staker = address(uint160(i)); // Simplified for example
            if (userShares[staker] > 0) {
                uint256 reward = (currentBalance * userShares[staker]) / totalShares;
                stakeWiseToken.transfer(staker, reward);
                emit RewardDistributed(staker, reward);
            }
        }
    }
    
    /**
     * @dev Get user's staked amount in ETH
     * @param user Address of the user
     * @return Staked amount in ETH
     */
    function getUserStakedAmount(address user) external view returns (uint256) {
        if (totalShares == 0) return 0;
        uint256 totalAssets = stakeWiseContract.totalAssets();
        return (totalAssets * userShares[user]) / totalShares;
    }
    
    /**
     * @dev Emergency withdraw all ETH from contract (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
    
    // Fallback function to receive ETH
    receive() external payable {}
}
```
