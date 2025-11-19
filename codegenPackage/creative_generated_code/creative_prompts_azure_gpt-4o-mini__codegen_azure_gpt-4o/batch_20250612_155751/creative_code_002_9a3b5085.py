"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sughiswap.github.io
Prompt: Create an example of a smart contract that utilizes SushiSwap's yield farming opportunities, including how to stake SUSHI tokens for rewards.
Generated: DETERMINISTIC_9a3b508585f466a5
Batch ID: 20250612_155751
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

/**
 * @title SushiYieldFarm
 * @dev A smart contract to interact with SushiSwap's yield farming opportunities.
 *      This contract allows users to stake SUSHI tokens and earn rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface ISushiStaking {
    function deposit(uint256 pid, uint256 amount) external;
    function withdraw(uint256 pid, uint256 amount) external;
    function pendingSushi(uint256 pid, address user) external view returns (uint256);
}

contract SushiYieldFarm is Ownable {
    // Address of the SUSHI token contract
    IERC20 public immutable sushiToken;

    // Address of the SushiSwap MasterChef staking contract
    ISushiStaking public immutable masterChef;

    // Pool ID for the specific SUSHI staking pool in MasterChef
    uint256 public immutable poolId;

    /**
     * @dev Constructor to initialize the contract with required parameters.
     * @param _sushiToken Address of the SUSHI token contract.
     * @param _masterChef Address of the MasterChef staking contract.
     * @param _poolId Pool ID for SUSHI staking in MasterChef.
     */
    constructor(
        address _sushiToken,
        address _masterChef,
        uint256 _poolId
    ) {
        require(_sushiToken != address(0), "Sushi token address cannot be zero");
        require(_masterChef != address(0), "MasterChef address cannot be zero");

        sushiToken = IERC20(_sushiToken);
        masterChef = ISushiStaking(_masterChef);
        poolId = _poolId;
    }

    /**
     * @dev Stake SUSHI tokens into the MasterChef pool.
     * @param amount Amount of SUSHI tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer SUSHI tokens from the user to this contract
        sushiToken.transferFrom(msg.sender, address(this), amount);

        // Approve MasterChef to spend the tokens
        sushiToken.approve(address(masterChef), amount);

        // Stake tokens in MasterChef
        masterChef.deposit(poolId, amount);
    }

    /**
     * @dev Withdraw staked SUSHI tokens from the MasterChef pool.
     * @param amount Amount of SUSHI tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot withdraw zero tokens");

        // Withdraw tokens from MasterChef
        masterChef.withdraw(poolId, amount);

        // Transfer the tokens back to the contract owner
        sushiToken.transfer(msg.sender, amount);
    }

    /**
     * @dev View pending SUSHI rewards for the user in the staking pool.
     * @return Pending SUSHI rewards.
     */
    function pendingRewards() external view returns (uint256) {
        return masterChef.pendingSushi(poolId, address(this));
    }

    /**
     * @dev Allow contract owner to emergency withdraw all staked tokens (without rewards).
     */
    function emergencyWithdraw() external onlyOwner {
        // Withdraw all tokens without caring for rewards
        masterChef.withdraw(poolId, type(uint256).max);

        // Transfer the tokens back to the owner
        uint256 balance = sushiToken.balanceOf(address(this));
        sushiToken.transfer(msg.sender, balance);
    }
}
```
