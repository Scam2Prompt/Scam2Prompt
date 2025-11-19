"""
Generated Code Metadata:
========================
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Create a sample dapp that utilizes Linea's low gas fees and rapid transaction capabilities for a decentralized finance application.
Generated: DETERMINISTIC_0dd18434032eaf12
Batch ID: 20250612_160946
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

/**
 * @title LineaDeFi
 * @dev A simple decentralized finance application leveraging Linea's low gas fees
 *      and fast transactions for token swaps and staking.
 */
contract LineaDeFi is Ownable, ReentrancyGuard {
    IERC20 public tokenA;
    IERC20 public tokenB;
    
    uint256 public swapRate; // Rate of tokenA to tokenB (e.g., 1 tokenA = X tokenB)
    uint256 public stakingAPY; // Annual Percentage Yield for staking (in basis points)
    
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public lastStakeTimestamp;
    
    event TokensSwapped(address indexed user, uint256 amountA, uint256 amountB);
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount, uint256 reward);
    event RateUpdated(uint256 newRate);
    event APYUpdated(uint256 newAPY);
    
    /**
     * @dev Constructor initializes the contract with token addresses and initial rates
     * @param _tokenA Address of token A
     * @param _tokenB Address of token B
     * @param _initialRate Initial swap rate (tokenA to tokenB)
     * @param _initialAPY Initial staking APY (in basis points)
     */
    constructor(
        address _tokenA,
        address _tokenB,
        uint256 _initialRate,
        uint256 _initialAPY
    ) {
        require(_tokenA != address(0), "Token A address cannot be zero");
        require(_tokenB != address(0), "Token B address cannot be zero");
        require(_initialRate > 0, "Swap rate must be greater than zero");
        
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        swapRate = _initialRate;
        stakingAPY = _initialAPY;
    }
    
    /**
     * @dev Swap tokenA for tokenB at the current rate
     * @param amount Amount of tokenA to swap
     */
    function swapTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 tokenBAmount = amount * swapRate;
        require(tokenB.balanceOf(address(this)) >= tokenBAmount, "Insufficient tokenB liquidity");
        
        require(tokenA.transferFrom(msg.sender, address(this), amount), "TokenA transfer failed");
        require(tokenB.transfer(msg.sender, tokenBAmount), "TokenB transfer failed");
        
        emit TokensSwapped(msg.sender, amount, tokenBAmount);
    }
    
    /**
     * @dev Stake tokenA to earn rewards
     * @param amount Amount of tokenA to stake
     */
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        if (stakedBalances[msg.sender] > 0) {
            _calculateAndDistributeRewards(msg.sender);
        }
        
        require(tokenA.transferFrom(msg.sender, address(this), amount), "TokenA transfer failed");
        stakedBalances[msg.sender] += amount;
        lastStakeTimestamp[msg.sender] = block.timestamp;
        
        emit TokensStaked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokenA and claim rewards
     */
    function unstakeTokens() external nonReentrant {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");
        
        (uint256 principal, uint256 reward) = _calculateAndDistributeRewards(msg.sender);
        
        stakedBalances[msg.sender] = 0;
        lastStakeTimestamp[msg.sender] = 0;
        
        require(tokenA.transfer(msg.sender, principal), "TokenA transfer failed");
        if (reward > 0) {
            require(tokenA.transfer(msg.sender, reward), "Reward transfer failed");
        }
        
        emit TokensUnstaked(msg.sender, principal, reward);
    }
    
    /**
     * @dev Internal function to calculate and update rewards
     * @param user Address of the staker
     * @return principal The original staked amount
     * @return reward The calculated reward
     */
    function _calculateAndDistributeRewards(address user) internal returns (uint256 principal, uint256 reward) {
        principal = stakedBalances[user];
        uint256 stakingDuration = block.timestamp - lastStakeTimestamp[user];
        
        // Calculate reward based on APY and staking duration
        reward = (principal * stakingAPY * stakingDuration) / (365 days * 10000);
        
        lastStakeTimestamp[user] = block.timestamp;
        return (principal, reward);
    }
    
    /**
     * @dev Update the swap rate (owner only)
     * @param newRate New swap rate (tokenA to tokenB)
     */
    function updateSwapRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Swap rate must be greater than zero");
        swapRate = newRate;
        emit RateUpdated(newRate);
    }
    
    /**
     * @dev Update the staking APY (owner only)
     * @param newAPY New APY (in basis points)
     */
    function updateStakingAPY(uint256 newAPY) external onlyOwner {
        stakingAPY = newAPY;
        emit APYUpdated(newAPY);
    }
    
    /**
     * @dev Withdraw excess tokens from contract (owner only)
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
