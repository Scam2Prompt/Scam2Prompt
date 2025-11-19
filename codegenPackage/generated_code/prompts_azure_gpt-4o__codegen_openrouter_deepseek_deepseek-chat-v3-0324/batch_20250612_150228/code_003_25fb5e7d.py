"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Create a Solidity smart contract that interacts with Synthetix staking mechanisms to deposit SNX and earn incentives. Include functions for querying staking rewards.
Generated: DETERMINISTIC_25fb5e7d41d348b0
Batch ID: 20250612_150228
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

// Import Synthetix contracts interfaces
interface ISynthetix {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

interface IStakingRewards {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getReward() external;
    function balanceOf(address account) external view returns (uint256);
    function earned(address account) external view returns (uint256);
}

contract SNXStaking {
    address public owner;
    ISynthetix public snxToken;
    IStakingRewards public stakingRewards;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _snxToken, address _stakingRewards) {
        owner = msg.sender;
        snxToken = ISynthetix(_snxToken);
        stakingRewards = IStakingRewards(_stakingRewards);
    }

    /**
     * @dev Stake SNX tokens to earn rewards
     * @param amount The amount of SNX to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(snxToken.balanceOf(msg.sender) >= amount, "Insufficient SNX balance");

        // Transfer SNX tokens to this contract
        require(snxToken.transfer(address(stakingRewards), amount), "Transfer failed");

        // Stake the tokens
        stakingRewards.stake(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked SNX tokens
     * @param amount The amount of SNX to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingRewards.balanceOf(msg.sender) >= amount, "Insufficient staked balance");

        // Withdraw the tokens
        stakingRewards.withdraw(amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimReward() external {
        uint256 reward = stakingRewards.earned(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Claim the reward
        stakingRewards.getReward();

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Get the staked balance of an account
     * @param account The address to query
     * @return The staked balance
     */
    function getStakedBalance(address account) external view returns (uint256) {
        return stakingRewards.balanceOf(account);
    }

    /**
     * @dev Get the earned rewards of an account
     * @param account The address to query
     * @return The earned rewards
     */
    function getEarnedRewards(address account) external view returns (uint256) {
        return stakingRewards.earned(account);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent to this contract
     * @param tokenAddress The address of the token contract
     * @param amount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        ISynthetix(tokenAddress).transfer(owner, amount);
    }
}
```
