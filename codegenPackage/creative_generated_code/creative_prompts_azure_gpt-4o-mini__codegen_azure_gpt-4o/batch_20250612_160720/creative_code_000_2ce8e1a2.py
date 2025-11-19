"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-befecoin.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to stake BRISE tokens in exchange for BEFE tokens, ensuring zero tax on transactions.
Generated: DETERMINISTIC_2ce8e1a2d4ca6745
Batch ID: 20250612_160720
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
 * @title TokenStaking
 * @dev This contract allows users to stake BRISE tokens to earn BEFE tokens.
 * It ensures zero tax on transactions.
 */
contract TokenStaking {
    // Address of the BRISE token contract
    IERC20 public immutable briseToken;

    // Address of the BEFE token contract
    IERC20 public immutable befeToken;

    // Mapping to store the staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Event emitted when a user stakes BRISE tokens
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their staked tokens
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the token addresses.
     * @param _briseToken Address of the BRISE token contract.
     * @param _befeToken Address of the BEFE token contract.
     */
    constructor(IERC20 _briseToken, IERC20 _befeToken) {
        require(address(_briseToken) != address(0), "BRISE token address cannot be zero");
        require(address(_befeToken) != address(0), "BEFE token address cannot be zero");
        briseToken = _briseToken;
        befeToken = _befeToken;
    }

    /**
     * @dev Allows users to stake BRISE tokens.
     * @param amount Amount of BRISE tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer BRISE tokens from the user to the contract
        require(briseToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's staked balance
        stakedBalances[msg.sender] += amount;

        // Emit the staking event
        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked BRISE tokens.
     */
    function withdrawStakedTokens() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Reset the user's staked balance
        stakedBalances[msg.sender] = 0;

        // Transfer BRISE tokens back to the user
        require(briseToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Emit the withdrawal event
        emit TokensWithdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows users to claim BEFE tokens as rewards for staking.
     * For simplicity, 1 BRISE token staked earns 1 BEFE token.
     */
    function claimRewards() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No rewards to claim");

        // Transfer BEFE tokens to the user as rewards
        require(befeToken.transfer(msg.sender, stakedAmount), "Reward transfer failed");
    }
}

/**
 * @dev Minimal IERC20 interface for interacting with token contracts.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
