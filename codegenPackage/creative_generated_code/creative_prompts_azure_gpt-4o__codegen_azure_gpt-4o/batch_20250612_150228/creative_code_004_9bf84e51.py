"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifcwow526nmb3jgtqwbbbwh47es7somd24fymtwlttwxedvnbnhku.ipfs.dweb.link
Prompt: Write a smart contract that facilitates token migration for MKR and DAI and includes a mechanism for distributing increased rewards during a beta period.
Generated: DETERMINISTIC_9bf84e51da55b7aa
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
 * @title TokenMigrationContract
 * @notice A smart contract to facilitate token migration for MKR and DAI,
 *         with special increased rewards during a beta period.
 * @dev This contract ensures secure migration and reward distribution.
 */
contract TokenMigrationContract {
    // Address of the MKR token contract
    address public immutable MKR;
    // Address of the DAI token contract
    address public immutable DAI;

    // Owner of the contract
    address public owner;

    // Beta period end timestamp
    uint256 public betaPeriodEnd;

    // Reward multiplier during the beta period
    uint256 public betaRewardMultiplier;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 mkrAmount, uint256 daiAmount, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _MKR,
        address _DAI,
        uint256 _betaPeriodEnd,
        uint256 _betaRewardMultiplier
    ) {
        require(_MKR != address(0), "Invalid MKR token address");
        require(_DAI != address(0), "Invalid DAI token address");
        require(_betaPeriodEnd > block.timestamp, "Beta period must be in the future");
        require(_betaRewardMultiplier > 1, "Beta reward multiplier must be greater than 1");

        MKR = _MKR;
        DAI = _DAI;
        betaPeriodEnd = _betaPeriodEnd;
        betaRewardMultiplier = _betaRewardMultiplier;
        owner = msg.sender;
    }

    /**
     * @notice Migrate tokens and receive rewards.
     * @param mkrAmount Amount of MKR tokens to migrate.
     * @param daiAmount Amount of DAI tokens to migrate.
     */
    function migrateTokens(uint256 mkrAmount, uint256 daiAmount) external {
        require(mkrAmount > 0, "MKR amount must be greater than 0");
        require(daiAmount > 0, "DAI amount must be greater than 0");

        // Transfer MKR tokens from the user to the contract
        require(
            IERC20(MKR).transferFrom(msg.sender, address(this), mkrAmount),
            "MKR transfer failed"
        );
        // Transfer DAI tokens from the user to the contract
        require(
            IERC20(DAI).transferFrom(msg.sender, address(this), daiAmount),
            "DAI transfer failed"
        );

        // Calculate rewards
        uint256 reward = calculateReward(mkrAmount, daiAmount);

        // Emit event for token migration
        emit TokensMigrated(msg.sender, mkrAmount, daiAmount, reward);

        // Distribute rewards back to the user
        require(
            IERC20(DAI).transfer(msg.sender, reward),
            "Reward transfer failed"
        );
    }

    /**
     * @notice Calculate rewards based on token migration and period.
     * @param mkrAmount Amount of MKR tokens migrated.
     * @param daiAmount Amount of DAI tokens migrated.
     * @return reward Amount of reward tokens.
     */
    function calculateReward(uint256 mkrAmount, uint256 daiAmount)
        internal
        view
        returns (uint256 reward)
    {
        uint256 baseReward = mkrAmount + daiAmount; // Example formula
        if (block.timestamp <= betaPeriodEnd) {
            // Apply beta reward multiplier
            return baseReward * betaRewardMultiplier;
        } else {
            return baseReward;
        }
    }

    /**
     * @notice Update beta period end timestamp.
     * @param _betaPeriodEnd New beta period end timestamp.
     */
    function updateBetaPeriodEnd(uint256 _betaPeriodEnd) external onlyOwner {
        require(_betaPeriodEnd > block.timestamp, "Beta period must be in the future");
        betaPeriodEnd = _betaPeriodEnd;
    }

    /**
     * @notice Update beta reward multiplier.
     * @param _betaRewardMultiplier New beta reward multiplier.
     */
    function updateBetaRewardMultiplier(uint256 _betaRewardMultiplier) external onlyOwner {
        require(_betaRewardMultiplier > 1, "Beta reward multiplier must be greater than 1");
        betaRewardMultiplier = _betaRewardMultiplier;
    }

    /**
     * @notice Withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            IERC20(token).transfer(owner, amount),
            "Token withdrawal failed"
        );
    }

    /**
     * @notice Transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}

// Interface for ERC20 token contract
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
