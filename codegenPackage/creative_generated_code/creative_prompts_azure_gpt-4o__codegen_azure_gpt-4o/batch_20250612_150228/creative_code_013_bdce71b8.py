"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Write a smart contract to enable cross-chain staking of uniTokens (uniETH, uniBTC, uniIOTX) on Bedrock, ensuring compatibility with IoTeX and DePIN.
Generated: DETERMINISTIC_bdce71b8eabe900d
Batch ID: 20250612_150228
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
 * @title CrossChainStaking
 * @dev Smart contract for cross-chain staking of uniTokens (uniETH, uniBTC, uniIOTX) on Bedrock.
 *      The contract is designed to work with IoTeX and DePIN ecosystems.
 */
contract CrossChainStaking {
    // Supported uniTokens mapping
    mapping(address => bool) public supportedTokens;

    // Staking balances of users
    mapping(address => mapping(address => uint256)) private stakingBalances;

    // Events
    event TokenSupported(address indexed token);
    event TokenUnSupported(address indexed token);
    event Staked(address indexed user, address indexed token, uint256 amount);
    event Unstaked(address indexed user, address indexed token, uint256 amount);
    event CrossChainTransferRequested(address indexed user, address indexed token, uint256 amount);

    // Contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize contract and set owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add supported tokens for staking.
     * @param token Address of the token to be supported.
     */
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
        emit TokenSupported(token);
    }

    /**
     * @dev Function to remove supported tokens for staking.
     * @param token Address of the token to be removed.
     */
    function removeSupportedToken(address token) external onlyOwner {
        require(supportedTokens[token], "Token not supported");
        supportedTokens[token] = false;
        emit TokenUnSupported(token);
    }

    /**
     * @dev Function to stake supported tokens.
     * @param token Address of the token to stake.
     * @param amount Amount of the token to stake.
     */
    function stake(address token, uint256 amount) external {
        require(supportedTokens[token], "Token not supported for staking");
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to contract
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking balance
        stakingBalances[msg.sender][token] += amount;

        emit Staked(msg.sender, token, amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param token Address of the token to unstake.
     * @param amount Amount of the token to unstake.
     */
    function unstake(address token, uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender][token] >= amount, "Insufficient staking balance");

        // Update staking balance
        stakingBalances[msg.sender][token] -= amount;

        // Transfer tokens back to user
        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, token, amount);
    }

    /**
     * @dev Function to request cross-chain transfer of staked tokens.
     * @param token Address of the token to transfer.
     * @param amount Amount of the token to transfer.
     */
    function requestCrossChainTransfer(address token, uint256 amount) external {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(stakingBalances[msg.sender][token] >= amount, "Insufficient staking balance");

        // Update staking balance
        stakingBalances[msg.sender][token] -= amount;

        // Emit event to signal cross-chain transfer request
        emit CrossChainTransferRequested(msg.sender, token, amount);

        // NOTE: Cross-chain transfer logic to IoTeX/DePIN will be handled by off-chain relayers or bridges.
    }

    /**
     * @dev Function to get staking balance of a user for a specific token.
     * @param user Address of the user.
     * @param token Address of the token.
     * @return Staking balance of the user.
     */
    function getStakingBalance(address user, address token) external view returns (uint256) {
        return stakingBalances[user][token];
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
