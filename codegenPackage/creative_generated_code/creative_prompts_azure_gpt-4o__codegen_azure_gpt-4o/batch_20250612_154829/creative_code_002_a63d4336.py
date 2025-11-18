"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hovrachev.ru
Prompt: Create a Solidity smart contract that integrates with Yield Yak's auto-compounding mechanism for reinvesting liquidity mining rewards into LP tokens.
Generated: DETERMINISTIC_a63d433610f94f7c
Batch ID: 20250612_154829
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
 * @title YieldYakAutoCompounder
 * @dev A smart contract that integrates with Yield Yak's auto-compounding mechanism for reinvesting liquidity mining rewards into LP tokens.
 * @notice This contract assumes the existence of the Yield Yak auto-compounding strategy interface.
 */
interface IYieldYakStrategy {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getDepositTokensForShares(uint256 shares) external view returns (uint256);
    function getSharesForDepositTokens(uint256 amount) external view returns (uint256);
    function reinvest() external;
}

contract YieldYakAutoCompounder {
    // Address of the Yield Yak strategy
    IYieldYakStrategy public yieldYakStrategy;

    // Owner of the contract
    address public owner;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsReinvested(address indexed user);

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _yieldYakStrategy Address of the Yield Yak strategy contract.
     */
    constructor(address _yieldYakStrategy) {
        require(_yieldYakStrategy != address(0), "Invalid strategy address");
        yieldYakStrategy = IYieldYakStrategy(_yieldYakStrategy);
        owner = msg.sender;
    }

    /**
     * @dev Deposits tokens into the Yield Yak auto-compounding strategy.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the strategy
        // NOTE: Token approval must be done by the user before calling this function
        require(IERC20(yieldYakStrategy).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Deposit tokens into the strategy
        yieldYakStrategy.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraws tokens from the Yield Yak auto-compounding strategy.
     * @param shares The amount of shares to withdraw (corresponding to deposited tokens).
     */
    function withdraw(uint256 shares) external {
        require(shares > 0, "Withdrawal shares must be greater than zero");

        // Calculate the amount of deposit tokens for the given shares
        uint256 depositTokens = yieldYakStrategy.getDepositTokensForShares(shares);

        // Withdraw from the strategy
        yieldYakStrategy.withdraw(shares);

        // Transfer tokens to the user
        require(IERC20(yieldYakStrategy).transfer(msg.sender, depositTokens), "Token transfer failed");

        emit Withdrawn(msg.sender, depositTokens);
    }

    /**
     * @dev Reinvests liquidity mining rewards into LP tokens.
     * @notice Only callable by the owner of the contract.
     */
    function reinvestRewards() external onlyOwner {
        // Call reinvest function on the strategy
        yieldYakStrategy.reinvest();

        emit RewardsReinvested(msg.sender);
    }

    /**
     * @dev Updates the owner of the contract.
     * @param _newOwner Address of the new owner.
     */
    function updateOwner(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        owner = _newOwner;
    }
}
```
