"""
Generated Code Metadata:
========================
Original URL: https://chainrectification-dapp.web.app
Prompt: Develop a smart contract to handle staking balance management and provide real-time token value viewing, incorporating the features mentioned under "Staking Balance" and "View Value of Token."
Generated: DETERMINISTIC_e2c6b7f34af38712
Batch ID: 20250612_153916
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A smart contract for staking balance management and real-time token value viewing.
 */
contract StakingContract is ReentrancyGuard {
    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user staking rewards
    mapping (address => uint256) public stakingRewards;

    // ERC20 token contract
    ERC20 public token;

    // Token value in USD
    uint256 public tokenValue;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when token value is updated
    event TokenValueUpdated(uint256 newValue);

    /**
     * @notice Constructor for StakingContract
     * @param _token ERC20 token contract address
     * @param _initialTokenValue Initial token value in USD
     */
    constructor(address _token, uint256 _initialTokenValue) {
        require(_token != address(0), "Token address cannot be zero");
        token = ERC20(_token);
        tokenValue = _initialTokenValue;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] += _amount;

        // Emit Staked event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] -= _amount;

        // Transfer tokens from contract to user
        token.transfer(msg.sender, _amount);

        // Emit Unstaked event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update token value
     * @param _newValue New token value in USD
     */
    function updateTokenValue(uint256 _newValue) external {
        require(_newValue > 0, "Token value must be greater than zero");

        // Update token value
        tokenValue = _newValue;

        // Emit TokenValueUpdated event
        emit TokenValueUpdated(_newValue);
    }

    /**
     * @notice Get user's staking balance
     * @param _user User address
     * @return User's staking balance
     */
    function getStakingBalance(address _user) public view returns (uint256) {
        return stakingBalances[_user];
    }

    /**
     * @notice Get user's staking rewards
     * @param _user User address
     * @return User's staking rewards
     */
    function getStakingRewards(address _user) public view returns (uint256) {
        return stakingRewards[_user];
    }

    /**
     * @notice Get token value in USD
     * @return Token value in USD
     */
    function getTokenValue() public view returns (uint256) {
        return tokenValue;
    }

    /**
     * @notice Get user's token balance
     * @param _user User address
     * @return User's token balance
     */
    function getTokenBalance(address _user) public view returns (uint256) {
        return token.balanceOf(_user);
    }
}
```
