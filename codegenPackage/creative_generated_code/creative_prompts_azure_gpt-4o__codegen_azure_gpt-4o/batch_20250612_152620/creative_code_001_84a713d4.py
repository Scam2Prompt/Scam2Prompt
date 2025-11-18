"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Generate code to integrate DOGE20 token staking functionality into a decentralized wallet, ensuring compatibility with ERC-20 tokens.
Generated: DETERMINISTIC_84a713d4d621097a
Batch ID: 20250612_152620
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
 * @title DOGE20 Token Staking Contract
 * @dev This contract allows staking of ERC-20 compatible tokens, specifically DOGE20, in a decentralized wallet.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract Doge20Staking {
    // Address of the DOGE20 token contract
    IERC20 public doge20Token;

    // Mapping to track staked balances for each user
    mapping(address => uint256) public stakedBalances;

    // Mapping to track timestamp of when a user last staked
    mapping(address => uint256) public stakingTimestamps;

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event TokensUnstaked(address indexed user, uint256 amount);

    // Constructor to initialize the DOGE20 token contract address
    constructor(address _doge20TokenAddress) {
        require(_doge20TokenAddress != address(0), "Invalid DOGE20 token address");
        doge20Token = IERC20(_doge20TokenAddress);
    }

    /**
     * @notice Allows users to stake DOGE20 tokens into the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer DOGE20 tokens from the user to the contract
        bool transferred = doge20Token.transferFrom(msg.sender, address(this), _amount);
        require(transferred, "Token transfer failed");

        // Update user's staked balance and staking timestamp
        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to unstake their DOGE20 tokens from the contract.
     * @param _amount The amount of tokens to unstake.
     */
    function unstakeTokens(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update user's staked balance and transfer tokens back to the user
        stakedBalances[msg.sender] -= _amount;
        bool transferred = doge20Token.transfer(msg.sender, _amount);
        require(transferred, "Token transfer failed");

        emit TokensUnstaked(msg.sender, _amount);
    }

    /**
     * @notice Returns the staked balance of the specified user.
     * @param _user The address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Fallback function to prevent accidental Ether deposits.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
