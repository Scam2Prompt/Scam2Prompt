"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordifypro.pages.dev
Prompt: Develop a smart contract for staking ORFY tokens on Ordify's Launchpad, ensuring compatibility with both Bitcoin Layer-2 chains and EVM chains.
Generated: DETERMINISTIC_0a0b7106b6ec5af7
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready smart contract for staking ORFY tokens, designed for Ethereum Virtual Machine (EVM)-compatible chains. Integration with Bitcoin Layer-2 chains would require additional off-chain tooling or specialized frameworks, as Bitcoin's scripting system does not natively support smart contracts. Below is the EVM-compatible implementation in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title ORFY Token Staking Contract
 * @author Ordify
 * @notice This contract allows users to stake ORFY tokens on Ordify's Launchpad.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ORFYStaking is Ownable, ReentrancyGuard {
    // Address of the ORFY token contract
    IERC20 public orfyToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Time when tokens were staked
    }

    // Mapping from user address to their staking information
    mapping(address => Stake) private stakes;

    // Total amount of ORFY tokens staked in this contract
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event TokensStaked(address indexed staker, uint256 amount);

    // Event emitted when a user withdraws staked tokens
    event TokensWithdrawn(address indexed staker, uint256 amount);

    /**
     * @param _orfyToken Address of the ORFY token contract
     */
    constructor(address _orfyToken) {
        require(_orfyToken != address(0), "Invalid token address");
        orfyToken = IERC20(_orfyToken);
    }

    /**
     * @notice Stake ORFY tokens into the contract
     * @param _amount Number of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(
            orfyToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking information for the user
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        // Update global staking totals
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @notice Withdraw staked ORFY tokens from the contract
     */
    function withdraw() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;

        require(stakedAmount > 0, "No tokens to withdraw");

        // Reset user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Update global staking totals
        totalStaked -= stakedAmount;

        // Transfer tokens back to the user
        require(
            orfyToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        emit TokensWithdrawn(msg.sender, stakedAmount);
    }

    /**
     * @notice View the amount of tokens staked by a user
     * @param _staker Address of the staker
     * @return Amount of tokens staked by the user
     */
    function getStakedAmount(address _staker) external view returns (uint256) {
        return stakes[_staker].amount;
    }

    /**
     * @notice View the timestamp of the last stake for a user
     * @param _staker Address of the staker
     * @return Timestamp of the last stake
     */
    function getStakeTimestamp(address _staker) external view returns (uint256) {
        return stakes[_staker].timestamp;
    }

    /**
     * @notice Emergency withdrawal of all staked tokens (Owner only)
     * @dev Use caution when calling this function; intended for emergencies
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = orfyToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens in contract");

        // Transfer all tokens to the owner
        require(
            orfyToken.transfer(owner(), contractBalance),
            "Token transfer failed"
        );

        totalStaked = 0; // Reset global staking totals
    }
}
```

This contract uses OpenZeppelin's libraries for security and best practices. Make sure to test it thoroughly before deployment.
