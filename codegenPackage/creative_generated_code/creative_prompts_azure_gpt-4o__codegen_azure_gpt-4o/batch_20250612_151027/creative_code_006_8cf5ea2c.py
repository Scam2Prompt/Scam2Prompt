"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liveresolve.pages.dev
Prompt: Explain how to use Multichain's veMULTI governance token in a decentralized application, and provide code examples for staking and claiming rewards.
Generated: DETERMINISTIC_8cf5ea2c8b09d088
Batch ID: 20250612_151027
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
 * @title veMULTI Governance Token Interaction Example
 * @dev Example smart contract demonstrating staking and claiming rewards for veMULTI governance token.
 * This contract assumes the existence of veMULTI interface and follows best practices for safety and readability.
 */

interface IVeMULTI {
    // Interface for veMULTI governance token
    function stake(uint256 amount) external;
    function claimRewards() external;
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract VeMULTIStaking {
    // Address of the veMULTI token contract
    address public veMULTIAddress;

    // Event emitted when staking is successful
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are successfully claimed
    event RewardsClaimed(address indexed user);

    /**
     * @dev Constructor to set the veMULTI token address
     * @param _veMULTIAddress Address of the veMULTI token contract
     */
    constructor(address _veMULTIAddress) {
        require(_veMULTIAddress != address(0), "Invalid veMULTI address");
        veMULTIAddress = _veMULTIAddress;
    }

    /**
     * @dev Stake veMULTI tokens into the governance contract
     * @param amount Amount of tokens to stake
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        IVeMULTI veMULTI = IVeMULTI(veMULTIAddress);

        // Transfer tokens from the user to the contract
        require(veMULTI.transfer(address(this), amount), "Token transfer failed");

        // Stake tokens on behalf of the user
        veMULTI.stake(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the caller
     */
    function claimRewards() external {
        IVeMULTI veMULTI = IVeMULTI(veMULTIAddress);

        // Claim rewards from veMULTI contract
        veMULTI.claimRewards();

        emit RewardsClaimed(msg.sender);
    }

    /**
     * @dev Retrieve the current balance of veMULTI staked by the caller
     * @return uint256 Balance of veMULTI tokens
     */
    function getStakedBalance() external view returns (uint256) {
        IVeMULTI veMULTI = IVeMULTI(veMULTIAddress);
        return veMULTI.balanceOf(msg.sender);
    }
}
```
