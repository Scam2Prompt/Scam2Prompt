"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7190436409.pages.dev
Prompt: Develop a smart contract that integrates with the "Harvest" auto-compounding system for decentralized crypto farming.
Generated: DETERMINISTIC_2435adefd8bd4e6d
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, production-ready implementation of a smart contract written in Solidity that integrates with the Harvest auto-compounding system. This example assumes that the Harvest platform exposes specific interfaces for staking, withdrawing, and claiming rewards.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title HarvestAutoCompounder
 * @dev A smart contract that integrates with the Harvest platform for
 *      auto-compounding decentralized farming.
 */
interface IHarvestFarm {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claim() external;
    function balanceOf(address account) external view returns (uint256);
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract HarvestAutoCompounder {
    // Address of the Harvest farm contract
    IHarvestFarm public immutable harvestFarm;

    // Address of the ERC20 token being staked
    IERC20 public immutable stakingToken;

    // Address of the owner (admin)
    address public immutable owner;

    // Events for logging important actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event ClaimedRewards(address indexed user);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to admin-only functions
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize contract dependencies.
     * @param _harvestFarm Address of the Harvest farm contract.
     * @param _stakingToken Address of the ERC20 token used for staking.
     */
    constructor(address _harvestFarm, address _stakingToken) {
        require(_harvestFarm != address(0), "Invalid Harvest farm address");
        require(_stakingToken != address(0), "Invalid staking token address");

        harvestFarm = IHarvestFarm(_harvestFarm);
        stakingToken = IERC20(_stakingToken);
        owner = msg.sender;
    }

    /**
     * @dev Stake tokens into the Harvest farm.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve Harvest farm to spend tokens
        require(stakingToken.approve(address(harvestFarm), amount), "Approval failed");

        // Stake tokens into the Harvest farm
        harvestFarm.stake(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the Harvest farm.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot withdraw 0 tokens");

        // Withdraw tokens from the Harvest farm
        harvestFarm.withdraw(amount);

        // Transfer tokens back to the admin
        require(stakingToken.transfer(owner, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim rewards from the Harvest farm.
     */
    function claimRewards() external onlyOwner {
        // Claim rewards
        harvestFarm.claim();

        emit ClaimedRewards(msg.sender);
    }

    /**
     * @dev Emergency withdrawal function for the admin.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 farmBalance = harvestFarm.balanceOf(address(this));
        require(farmBalance > 0, "No funds to withdraw");

        // Withdraw all tokens from the Harvest farm
        harvestFarm.withdraw(farmBalance);

        // Transfer all tokens back to the admin
        require(stakingToken.transfer(owner, farmBalance), "Token transfer failed");

        emit EmergencyWithdraw(msg.sender, farmBalance);
    }

    /**
     * @dev View the balance of staked tokens in the Harvest farm.
     * @return The balance of staked tokens.
     */
    function getFarmBalance() external view returns (uint256) {
        return harvestFarm.balanceOf(address(this));
    }
}
```

This contract assumes the existence of standard ERC20 tokens and Harvest farming interfaces. Ensure the external interfaces (`IHarvestFarm` and `IERC20`) match the actual contracts deployed on-chain. Adapt error messages and logic as needed when integrating in production.
