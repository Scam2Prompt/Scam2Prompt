"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Write a smart contract that allows members to stake NXM tokens for assessing smart contract security in Nexus Mutual.
Generated: DETERMINISTIC_c587f421f3d603f7
Batch ID: 20250612_155956
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
 * @title NexusMutualStaking
 * @dev This contract allows members to stake NXM tokens for assessing smart contract security in Nexus Mutual.
 * Members can stake tokens, withdraw their stakes, and view their staking balances.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NexusMutualStaking is Ownable {
    // Address of the NXM token contract
    IERC20 public nxmToken;

    // Mapping to track staking balances of members
    mapping(address => uint256) private stakingBalances;

    // Event emitted when a member stakes tokens
    event TokensStaked(address indexed member, uint256 amount);

    // Event emitted when a member withdraws their stake
    event TokensWithdrawn(address indexed member, uint256 amount);

    /**
     * @dev Constructor to initialize the NXM token address.
     * @param _nxmToken Address of the NXM token contract
     */
    constructor(IERC20 _nxmToken) {
        require(address(_nxmToken) != address(0), "Invalid token address");
        nxmToken = _nxmToken;
    }

    /**
     * @dev Allows a member to stake NXM tokens.
     * @param _amount The amount of NXM tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer NXM tokens from the member to the contract
        bool success = nxmToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staking balance
        stakingBalances[msg.sender] += _amount;

        // Emit the staking event
        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Allows a member to withdraw their staked NXM tokens.
     * @param _amount The amount of NXM tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(
            stakingBalances[msg.sender] >= _amount,
            "Insufficient staking balance"
        );

        // Update staking balance
        stakingBalances[msg.sender] -= _amount;

        // Transfer NXM tokens from the contract to the member
        bool success = nxmToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        // Emit the withdrawal event
        emit TokensWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Returns the staking balance of a specific member.
     * @param _member The address of the member
     * @return The staking balance of the member
     */
    function getStakingBalance(address _member)
        external
        view
        returns (uint256)
    {
        return stakingBalances[_member];
    }
}
```
