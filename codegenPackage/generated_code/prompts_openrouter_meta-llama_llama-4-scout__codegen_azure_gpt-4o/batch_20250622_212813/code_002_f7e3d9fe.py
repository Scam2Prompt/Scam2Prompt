"""
Generated Code Metadata:
========================
Original URL: https://presale-alainetwork.pages.dev
Prompt: Generate a smart contract code in Solidity that handles token staking and dividend distribution for a cryptocurrency platform like ALAI Network.
Generated: DETERMINISTIC_f7e3d9fe44ee761e
Batch ID: 20250622_212813
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

/**
 * @title Staking and Dividend Distribution Smart Contract
 * @dev This contract allows users to stake tokens and receive dividends based on their stake.
 */
contract TokenStaking {
    // Token interface
    IERC20 public immutable token;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staked amount
    mapping(address => uint256) public stakes;

    // Mapping of user address to pending dividends
    mapping(address => uint256) public pendingDividends;

    // Total dividends distributed
    uint256 public totalDividends;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event DividendsDistributed(uint256 amount);
    event DividendClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the token address.
     * @param _token Address of the ERC20 token used for staking.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's stake and total staked
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's stake and total staked
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute dividends to stakers based on their stake proportion.
     * @param amount Amount of dividends to distribute.
     */
    function distributeDividends(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(totalStaked > 0, "No staked tokens to distribute dividends");

        // Transfer dividends to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update total dividends
        totalDividends += amount;

        // Distribute dividends proportionally
        for (uint256 i = 0; i < totalStaked; i++) {
            address staker = stakes[i];
            uint256 userStake = stakes[staker];
            uint256 userDividend = (amount * userStake) / totalStaked;
            pendingDividends[staker] += userDividend;
        }

        emit DividendsDistributed(amount);
    }

    /**
     * @dev Claim pending dividends.
     */
    function claimDividends() external {
        uint256 amount = pendingDividends[msg.sender];
        require(amount > 0, "No dividends to claim");

        // Reset pending dividends
        pendingDividends[msg.sender] = 0;

        // Transfer dividends to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit DividendClaimed(msg.sender, amount);
    }

    /**
     * @dev Get the pending dividends for a user.
     * @param user Address of the user.
     * @return Pending dividends for the user.
     */
    function getPendingDividends(address user) external view returns (uint256) {
        return pendingDividends[user];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
