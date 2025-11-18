"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claim.pages.dev
Prompt: Write a smart contract in Solidity for an ERC-20 token similar to $KANG, including features for presale, staking, and rewards distribution as described in Kangamoon's tokenomics.
Generated: DETERMINISTIC_f2cf87c4179850fa
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Import OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KangToken is ERC20, Ownable {
    // State variables for presale, staking, and rewards
    uint256 public presalePrice; // Price per token during presale in wei
    uint256 public presaleCap; // Max tokens available for presale
    uint256 public presaleSold; // Count of tokens sold during presale
    bool public presaleActive; // Flag to toggle presale status

    struct Staker {
        uint256 stakedAmount;
        uint256 rewards;
        uint256 lastStakedTime;
    }

    mapping(address => Staker) public stakers;
    uint256 public stakingRewardRate; // Reward rate in percentage per year
    uint256 public stakingMinimumLockTime; // Minimum lock time for staking in seconds

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _presalePrice,
        uint256 _presaleCap,
        uint256 _stakingRewardRate,
        uint256 _stakingMinimumLockTime
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply); // Mint initial supply to the contract deployer
        presalePrice = _presalePrice;
        presaleCap = _presaleCap;
        stakingRewardRate = _stakingRewardRate;
        stakingMinimumLockTime = _stakingMinimumLockTime;
    }

    // Presale Functions

    /// @notice Allows users to buy tokens during the presale
    /// @param amount Number of tokens to buy
    function buyPresaleTokens(uint256 amount) external payable {
        require(presaleActive, "Presale is not active");
        require(presaleSold + amount <= presaleCap, "Exceeds presale cap");
        require(msg.value == amount * presalePrice, "Incorrect ETH value sent");

        presaleSold += amount;
        _transfer(owner(), msg.sender, amount); // Transfer presale tokens from owner
    }

    /// @notice Allows the owner to toggle the presale status
    function togglePresaleStatus() external onlyOwner {
        presaleActive = !presaleActive;
    }

    /// @notice Allows the owner to withdraw ETH collected during presale
    function withdrawPresaleFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Staking Functions

    /// @notice Allows a user to stake tokens
    /// @param amount Number of tokens to stake
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        _transfer(msg.sender, address(this), amount); // Transfer tokens to contract

        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);
        staker.stakedAmount += amount;
        staker.lastStakedTime = block.timestamp;
    }

    /// @notice Allows a user to withdraw staked tokens and rewards
    function unstakeTokens() external {
        Staker storage staker = stakers[msg.sender];
        require(
            staker.stakedAmount > 0,
            "No tokens staked"
        );
        require(
            block.timestamp >= staker.lastStakedTime + stakingMinimumLockTime,
            "Tokens are still locked"
        );

        _updateRewards(msg.sender);

        uint256 amountToReward = staker.rewards;
        uint256 amountToUnstake = staker.stakedAmount;

        staker.rewards = 0;
        staker.stakedAmount = 0;

        _transfer(address(this), msg.sender, amountToUnstake + amountToReward);
    }

    // Internal utility functions

    /// @notice Updates rewards for a staker based on the reward rate
    /// @param stakerAddress The address of the staker
    function _updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        if (staker.stakedAmount > 0) {
            uint256 timeStaked = block.timestamp - staker.lastStakedTime;
            uint256 reward = (staker.stakedAmount * stakingRewardRate * timeStaked) / (100 * 365 days);
            staker.rewards += reward;
            staker.lastStakedTime = block.timestamp;
        }
    }
}
```

This contract implements an ERC-20 token with presale, staking, and rewards functionalities. Make sure to review and thoroughly test the smart contract in a development and staging environment before deploying it to production.
