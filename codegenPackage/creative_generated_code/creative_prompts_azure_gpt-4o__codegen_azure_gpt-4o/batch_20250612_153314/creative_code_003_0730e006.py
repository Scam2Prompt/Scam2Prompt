"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://888-9jr.pages.dev
Prompt: Generate a smart contract in Solidity to facilitate staking and delegation of EIGEN tokens on EigenLayer.
Generated: DETERMINISTIC_0730e0064397f34d
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Staking and Delegation Contract for EIGEN Tokens on EigenLayer
 * @author Your Name
 * @notice This contract allows users to stake EIGEN tokens and delegate their stakes to other addresses.
 */
contract EigenStaking {

    // ERC20 Interface for EIGEN tokens
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function approve(address spender, uint256 amount) external returns (bool);
    }

    // Address of the EIGEN token contract
    IERC20 public immutable eigenToken;

    // Struct representing a stake
    struct Stake {
        uint256 amount; // Amount of tokens staked
        address delegator; // Address to which the stake is delegated
    }

    // Mapping of staker addresses to their stake details
    mapping(address => Stake) public stakes;

    // Events for logging important actions
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event Delegated(address indexed staker, address indexed delegator);

    /**
     * @notice Constructor to initialize the Eigen token address
     * @param _eigenToken Address of the EIGEN token contract
     */
    constructor(address _eigenToken) {
        require(_eigenToken != address(0), "Invalid token address");
        eigenToken = IERC20(_eigenToken);
    }

    /**
     * @notice Stake EIGEN tokens in the contract
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the sender to the contract
        bool success = eigenToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the staker's stake
        stakes[msg.sender].amount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake EIGEN tokens from the contract
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update the staker's stake
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the sender
        bool success = eigenToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Delegate staked tokens to another address
     * @param _delegator Address to delegate the stake to
     */
    function delegate(address _delegator) external {
        require(_delegator != address(0), "Invalid delegator address");
        require(stakes[msg.sender].amount > 0, "No tokens staked");

        // Update the delegator for the staker
        stakes[msg.sender].delegator = _delegator;

        emit Delegated(msg.sender, _delegator);
    }

    /**
     * @notice Get the stake details for a staker
     * @param _staker Address of the staker
     * @return amount Amount of tokens staked
     * @return delegator Address to which the stake is delegated
     */
    function getStakeDetails(address _staker) external view returns (uint256 amount, address delegator) {
        Stake storage stakeInfo = stakes[_staker];
        return (stakeInfo.amount, stakeInfo.delegator);
    }
}
```
