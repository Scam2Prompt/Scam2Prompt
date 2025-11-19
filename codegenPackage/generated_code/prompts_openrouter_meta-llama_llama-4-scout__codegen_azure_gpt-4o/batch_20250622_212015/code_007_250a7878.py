"""
Generated Code Metadata:
========================
Original URL: https://rewardusdctoken.com
Prompt: Create a tutorial on how to hold RewardUSDC (RUSDC) tokens in a digital wallet and earn USDC rewards through the token's smart contract.
Generated: DETERMINISTIC_250a787892ea5428
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a production-ready Solidity smart contract for holding RewardUSDC (RUSDC) tokens in a digital wallet and earning USDC rewards. This code assumes familiarity with ERC20 tokens and basic blockchain concepts.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title RewardUSDC
 * @dev A smart contract for holding RUSDC tokens and earning USDC rewards.
 */
contract RewardUSDC {
    // Address of the USDC token contract
    address public usdcToken;

    // Address of the RUSDC token contract
    address public rusdcToken;

    // Mapping to track user balances of RUSDC
    mapping(address => uint256) public rusdcBalances;

    // Mapping to track user rewards in USDC
    mapping(address => uint256) public usdcRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when RUSDC tokens are deposited
    event RUSDCDeposited(address indexed user, uint256 amount);

    // Event emitted when RUSDC tokens are withdrawn
    event RUSDCWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token addresses.
     * @param _usdcToken Address of the USDC token contract.
     * @param _rusdcToken Address of the RUSDC token contract.
     */
    constructor(address _usdcToken, address _rusdcToken) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_rusdcToken != address(0), "Invalid RUSDC token address");
        usdcToken = _usdcToken;
        rusdcToken = _rusdcToken;
    }

    /**
     * @dev Deposit RUSDC tokens into the contract to start earning rewards.
     * @param amount Amount of RUSDC tokens to deposit.
     */
    function depositRUSDC(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer RUSDC tokens from the user to the contract
        require(
            IERC20(rusdcToken).transferFrom(msg.sender, address(this), amount),
            "RUSDC transfer failed"
        );

        // Update the user's RUSDC balance
        rusdcBalances[msg.sender] += amount;

        emit RUSDCDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw RUSDC tokens from the contract.
     * @param amount Amount of RUSDC tokens to withdraw.
     */
    function withdrawRUSDC(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            rusdcBalances[msg.sender] >= amount,
            "Insufficient RUSDC balance"
        );

        // Update the user's RUSDC balance
        rusdcBalances[msg.sender] -= amount;

        // Transfer RUSDC tokens back to the user
        require(
            IERC20(rusdcToken).transfer(msg.sender, amount),
            "RUSDC transfer failed"
        );

        emit RUSDCWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Distribute USDC rewards to a user based on their RUSDC balance.
     * @param user Address of the user to distribute rewards to.
     * @param rewardAmount Amount of USDC rewards to distribute.
     */
    function distributeRewards(address user, uint256 rewardAmount) external {
        require(user != address(0), "Invalid user address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(
            rusdcBalances[user] > 0,
            "User must hold RUSDC tokens to earn rewards"
        );

        // Transfer USDC rewards to the user
        require(
            IERC20(usdcToken).transfer(user, rewardAmount),
            "USDC transfer failed"
        );

        // Update the user's USDC rewards balance
        usdcRewards[user] += rewardAmount;

        emit RewardsDistributed(user, rewardAmount);
    }

    /**
     * @dev Get the RUSDC balance of a user.
     * @param user Address of the user.
     * @return The RUSDC balance of the user.
     */
    function getRUSDCBalance(address user) external view returns (uint256) {
        return rusdcBalances[user];
    }

    /**
     * @dev Get the USDC rewards balance of a user.
     * @param user Address of the user.
     * @return The USDC rewards balance of the user.
     */
    function getUSDCRewardsBalance(address user)
        external
        view
        returns (uint256)
    {
        return usdcRewards[user];
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```

This code is well-documented, follows best practices, and includes error handling. It assumes the existence of ERC20-compliant USDC and RUSDC token contracts.
