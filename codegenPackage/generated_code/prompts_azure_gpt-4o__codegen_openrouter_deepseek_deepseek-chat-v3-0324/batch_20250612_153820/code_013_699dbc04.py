"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Provide an example of how to use Stader Labs' native contracts optimized for Ethereum to secure staking assets and monitor validator performance.
Generated: DETERMINISTIC_699dbc04200b8ed0
Batch ID: 20250612_153820
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

interface IStaderStakingPool {
    function deposit() external payable;
    function withdraw(uint256 amount) external;
    function getTotalStaked() external view returns (uint256);
    function getValidatorPerformance(address validator) external view returns (uint256, uint256);
}

contract StaderStakingManager is Ownable, ReentrancyGuard {
    IStaderStakingPool public stakingPool;
    IERC20 public staderToken;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event ValidatorPerformanceChecked(address validator, uint256 uptime, uint256 rewards);

    constructor(address _stakingPoolAddress, address _staderTokenAddress) {
        require(_stakingPoolAddress != address(0), "Invalid staking pool address");
        require(_staderTokenAddress != address(0), "Invalid token address");
        
        stakingPool = IStaderStakingPool(_stakingPoolAddress);
        staderToken = IERC20(_staderTokenAddress);
    }

    /**
     * @dev Stake ETH into Stader's staking pool
     */
    function stake() external payable nonReentrant {
        require(msg.value > 0, "Cannot stake 0 ETH");
        
        (bool success, ) = address(stakingPool).call{value: msg.value}(
            abi.encodeWithSignature("deposit()")
        );
        require(success, "Staking failed");
        
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw staked ETH from Stader's staking pool
     * @param amount Amount of ETH to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot withdraw 0 ETH");
        
        stakingPool.withdraw(amount);
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Check total staked ETH in the pool
     * @return Total staked ETH
     */
    function getTotalStaked() external view returns (uint256) {
        return stakingPool.getTotalStaked();
    }

    /**
     * @dev Check validator performance metrics
     * @param validator Address of the validator to check
     * @return uptime Validator uptime percentage (0-100)
     * @return rewards Rewards earned by validator
     */
    function checkValidatorPerformance(address validator) external returns (uint256 uptime, uint256 rewards) {
        require(validator != address(0), "Invalid validator address");
        
        (uptime, rewards) = stakingPool.getValidatorPerformance(validator);
        
        emit ValidatorPerformanceChecked(validator, uptime, rewards);
        return (uptime, rewards);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(staderToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
