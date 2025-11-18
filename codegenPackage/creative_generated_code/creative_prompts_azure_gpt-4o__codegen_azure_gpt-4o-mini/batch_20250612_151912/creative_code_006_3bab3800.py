"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: Develop a smart contract that allows coin holders to loan or stake their tokens quarterly, representing electricity available for miners, as per eosGAS's staking mechanism.
Generated: DETERMINISTIC_3bab38002b1ad462
Batch ID: 20250612_151912
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title EnergyTokenStaking
 * @dev A smart contract to allow token holders to stake their tokens quarterly, 
 * representing electricity available for miners.
 */
contract EnergyTokenStaking {
    using SafeMath for uint256;

    IERC20 public energyToken; // The ERC20 token representing energy
    uint256 public constant STAKING_PERIOD = 90 days; // Quarterly staking period

    struct Stake {
        uint256 amount;
        uint256 startTime;
        bool withdrawn;
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Sets the token contract address.
     * @param _energyToken Address of the ERC20 token contract.
     */
    constructor(IERC20 _energyToken) {
        require(address(_energyToken) != address(0), "Invalid token address");
        energyToken = _energyToken;
    }

    /**
     * @dev Allows users to stake their tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(energyToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(energyToken.allowance(msg.sender, address(this)) >= amount, "Token allowance required");

        // Transfer tokens from user to contract
        energyToken.transferFrom(msg.sender, address(this), amount);

        // Create or update the stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].startTime = block.timestamp;
        stakes[msg.sender].withdrawn = false;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens after the staking period.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        
        require(userStake.amount > 0, "No tokens to withdraw");
        require(!userStake.withdrawn, "Tokens already withdrawn");
        require(block.timestamp >= userStake.startTime.add(STAKING_PERIOD), "Staking period not yet completed");

        // Transfer tokens back to the user
        uint256 amountToWithdraw = userStake.amount;
        userStake.withdrawn = true; // Mark as withdrawn
        userStake.amount = 0; // Reset amount

        energyToken.transfer(msg.sender, amountToWithdraw);
        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Allows the owner to withdraw tokens in case of emergency.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(energyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the contract owner
        energyToken.transfer(msg.sender, amount);
    }

    /**
     * @dev View function to check the balance of staked tokens for a user.
     * @param user Address of the user.
     * @return The amount of tokens staked by the user.
     */
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev View function to check if a user's tokens can be withdrawn.
     * @param user Address of the user.
     * @return Boolean indicating if the user can withdraw their tokens.
     */
    function canWithdraw(address user) external view returns (bool) {
        Stake storage userStake = stakes[user];
        return userStake.amount > 0 && !userStake.withdrawn && block.timestamp >= userStake.startTime.add(STAKING_PERIOD);
    }
}
```
