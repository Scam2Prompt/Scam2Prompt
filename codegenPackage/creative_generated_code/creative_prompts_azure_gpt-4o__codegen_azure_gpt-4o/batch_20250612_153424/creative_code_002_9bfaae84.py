"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aavplifi.com
Prompt: Provide an example of how to interact with Aave's staking functionality using Solidity, including staking AAVE tokens and retrieving staking rewards.
Generated: DETERMINISTIC_9bfaae8461f920f6
Batch ID: 20250612_153424
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

// Import relevant interfaces from Aave
import "@aave/protocol-v2/contracts/interfaces/IStakedAave.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract AaveStaking {
    // Address of the Staked AAVE contract on the Aave protocol
    IStakedAave public stakedAave;
    // Address of the AAVE token contract
    IERC20 public aaveToken;

    // Constructor initializes the contract with the required addresses
    constructor(address _stakedAaveAddress, address _aaveTokenAddress) {
        require(_stakedAaveAddress != address(0), "Invalid Staked AAVE address");
        require(_aaveTokenAddress != address(0), "Invalid AAVE token address");
        stakedAave = IStakedAave(_stakedAaveAddress);
        aaveToken = IERC20(_aaveTokenAddress);
    }

    /**
     * @notice Stakes AAVE tokens into the Aave protocol.
     * @param _amount The amount of AAVE tokens to stake.
     */
    function stakeAAVE(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer AAVE tokens from the user's wallet to this contract
        bool transferSuccess = aaveToken.transferFrom(msg.sender, address(this), _amount);
        require(transferSuccess, "AAVE token transfer failed");

        // Approve the Staked AAVE contract to spend the tokens
        bool approveSuccess = aaveToken.approve(address(stakedAave), _amount);
        require(approveSuccess, "AAVE token approval failed");

        // Stake the tokens into the Staked AAVE contract
        stakedAave.stake(msg.sender, _amount);
    }

    /**
     * @notice Claims staking rewards from the Aave protocol.
     */
    function claimRewards() external {
        // Get the reward balance of the caller
        uint256 rewards = stakedAave.getRewardsBalance(address(aaveToken), msg.sender);
        require(rewards > 0, "No rewards available");

        // Claim rewards for the caller
        stakedAave.claimRewards(msg.sender, rewards);
    }

    /**
     * @notice Gets the staking rewards balance for a user.
     * @param _user The address of the user to check rewards for.
     * @return The amount of staking rewards available.
     */
    function getStakingRewards(address _user) external view returns (uint256) {
        return stakedAave.getRewardsBalance(address(aaveToken), _user);
    }

    /**
     * @notice Gets the total staked balance for a user.
     * @param _user The address of the user to check the staked balance for.
     * @return The total staked AAVE tokens balance.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedAave.balanceOf(_user);
    }
}
```
