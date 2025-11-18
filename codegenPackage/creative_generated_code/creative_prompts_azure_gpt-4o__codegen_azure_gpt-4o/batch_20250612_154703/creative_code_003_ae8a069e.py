"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.network
Prompt: Write a smart contract in Solidity that uses Aave's staking mechanism to secure the protocol and earn rewards.
Generated: DETERMINISTIC_ae8a069e7a4c98ea
Batch ID: 20250612_154703
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

/**
 * @title AaveStakingContract
 * @dev A smart contract to interact with Aave's staking mechanism for securing the protocol and earning rewards.
 *      This contract allows users to deposit tokens into Aave's staking pool and withdraw their funds, including rewards.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@aave/protocol-v2/contracts/interfaces/IStakedAave.sol"; // Import the Aave staking interface

contract AaveStakingContract is Ownable {
    // Address of the AAVE staking contract
    IStakedAave public stakedAave;

    // Address of the AAVE token
    IERC20 public aaveToken;

    // Event: Emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);

    // Event: Emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets up the staking contract and token addresses.
     * @param _stakedAave Address of the AAVE staking contract.
     * @param _aaveToken Address of the AAVE token.
     */
    constructor(address _stakedAave, address _aaveToken) {
        require(_stakedAave != address(0), "Invalid staking contract address");
        require(_aaveToken != address(0), "Invalid token address");

        stakedAave = IStakedAave(_stakedAave);
        aaveToken = IERC20(_aaveToken);
    }

    /**
     * @dev Stake AAVE tokens into the Aave staking contract.
     * @param amount Amount of AAVE tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer AAVE tokens from the user to this contract
        require(aaveToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the staking contract to spend the tokens
        require(aaveToken.approve(address(stakedAave), amount), "Approval failed");

        // Stake the tokens into the Aave staking contract
        stakedAave.stake(msg.sender, amount);

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked AAVE along with any earned rewards.
     * @param amount Amount of staked AAVE to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw staked AAVE tokens along with rewards
        stakedAave.withdraw(msg.sender, amount);

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards earned in AAVE.
     */
    function claimRewards() external {
        // Claim rewards from the Aave staking contract
        stakedAave.claimRewards(msg.sender, type(uint256).max);
    }

    /**
     * @dev Get the balance of staked AAVE tokens for a user.
     * @param user Address of the user.
     * @return Balance of staked AAVE tokens.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedAave.balanceOf(user);
    }

    /**
     * @dev Get the total staking rewards earned by a user.
     * @param user Address of the user.
     * @return Total staking rewards.
     */
    function getTotalRewards(address user) external view returns (uint256) {
        return stakedAave.getTotalRewardsBalance(user);
    }
}
```
