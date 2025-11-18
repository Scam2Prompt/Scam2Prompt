"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzo-apps.medium.com
Prompt: Write a smart contract in Solidity that integrates with the Renzo Protocol to automate token restaking based on the guidelines provided on the Renzo Protocol Medium page.
Generated: DETERMINISTIC_7534e7773f709b4d
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the Renzo Protocol staking interface and OpenZeppelin libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IRenzoStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
    function getRewardsToken() external view returns (address);
    function getStakedToken() external view returns (address);
}

contract AutoRestakingContract is Ownable, ReentrancyGuard {
    // The instance of the Renzo Protocol staking contract
    IRenzoStaking public renzoStaking;

    // Address of the staked token and the rewards token
    IERC20 public stakedToken;
    IERC20 public rewardsToken;

    // Event declarations for transparency
    event TokensStaked(uint256 amount);
    event RewardsClaimedAndRestaked(uint256 rewards);

    constructor(address _renzoStakingAddress) {
        require(_renzoStakingAddress != address(0), "Invalid staking contract address");

        renzoStaking = IRenzoStaking(_renzoStakingAddress);

        // Fetch the staked token and rewards token from the Renzo Protocol
        stakedToken = IERC20(renzoStaking.getStakedToken());
        rewardsToken = IERC20(renzoStaking.getRewardsToken());
    }

    /**
     * @notice Stakes a specified amount of tokens in the Renzo Protocol.
     * @dev Requires the contract to have approval for the specified amount.
     * @param amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the owner to the contract
        require(stakedToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the Renzo staking contract to spend the tokens
        stakedToken.approve(address(renzoStaking), amount);

        // Stake the tokens
        renzoStaking.stake(amount);

        emit TokensStaked(amount);
    }

    /**
     * @notice Claims rewards from the Renzo Protocol and restakes them.
     * @dev This function automates the restaking process.
     */
    function claimAndRestakeRewards() external nonReentrant onlyOwner {
        // Claim rewards from the protocol
        renzoStaking.claimRewards();

        // Fetch the rewards balance
        uint256 rewardsBalance = rewardsToken.balanceOf(address(this));
        require(rewardsBalance > 0, "No rewards to restake");

        // Approve the Renzo staking contract to spend the rewards tokens
        rewardsToken.approve(address(renzoStaking), rewardsBalance);

        // Stake the rewards as additional tokens
        renzoStaking.stake(rewardsBalance);

        emit RewardsClaimedAndRestaked(rewardsBalance);
    }

    /**
     * @notice Withdraws staked tokens from the Renzo Protocol.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawStakedTokens(uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw tokens from the Renzo Protocol
        renzoStaking.withdraw(amount);

        // Transfer the withdrawn tokens back to the owner
        require(stakedToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @notice Emergency withdrawal of all staked tokens. This should be used with caution.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = stakedToken.balanceOf(address(this));
        if (contractBalance > 0) {
            require(stakedToken.transfer(msg.sender, contractBalance), "Token transfer failed");
        }
    }
}
```
