"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memegames-web.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGMES tokens, ensuring compatibility with the blockchain-based leaderboard system described in The Meme Games Token documentation.
Generated: DETERMINISTIC_bdcab18531a17156
Batch ID: 20250612_151246
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
 * @title StakingContract
 * @dev A smart contract for staking MGMES tokens and interacting with a blockchain-based leaderboard system.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface Leaderboard {
    function updateLeaderboard(address staker, uint256 stakedAmount) external;
}

contract MGMESStaking {
    // MGMES Token Contract
    IERC20 public immutable mgmesToken;

    // Leaderboard contract
    Leaderboard public immutable leaderboard;

    // Mapping to track staked balances
    mapping(address => uint256) public stakedBalances;

    // Events
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);

    /**
     * @dev Constructor to initialize MGMES token and leaderboard contract.
     * @param _mgmesToken Address of the MGMES token contract.
     * @param _leaderboard Address of the leaderboard contract.
     */
    constructor(IERC20 _mgmesToken, Leaderboard _leaderboard) {
        require(address(_mgmesToken) != address(0), "Invalid token address");
        require(address(_leaderboard) != address(0), "Invalid leaderboard address");

        mgmesToken = _mgmesToken;
        leaderboard = _leaderboard;
    }

    /**
     * @dev Stake MGMES tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer MGMES tokens from sender to contract
        bool success = mgmesToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staked balance
        stakedBalances[msg.sender] += _amount;

        // Update leaderboard
        leaderboard.updateLeaderboard(msg.sender, stakedBalances[msg.sender]);

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Unstake MGMES tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstakeTokens(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake zero tokens");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked tokens");

        // Update staked balance
        stakedBalances[msg.sender] -= _amount;

        // Transfer MGMES tokens back to sender
        bool success = mgmesToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        // Update leaderboard
        leaderboard.updateLeaderboard(msg.sender, stakedBalances[msg.sender]);

        emit TokensUnstaked(msg.sender, _amount);
    }

    /**
     * @dev Retrieve the staked balance of an account.
     * @param _account Address of the account.
     * @return The staked balance of the account.
     */
    function getStakedBalance(address _account) external view returns (uint256) {
        return stakedBalances[_account];
    }
}
```
