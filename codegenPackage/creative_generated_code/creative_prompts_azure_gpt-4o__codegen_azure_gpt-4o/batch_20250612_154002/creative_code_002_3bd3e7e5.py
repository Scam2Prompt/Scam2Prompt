"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-farming.net
Prompt: Generate Solidity code for a simple DeFi farming smart contract that allows users to deposit tokens and earn yield over time.
Generated: DETERMINISTIC_3bd3e7e5837002e3
Batch ID: 20250612_154002
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
 * @title DeFi Farming Contract
 * @dev This contract allows users to deposit ERC20 tokens and earn yield over time.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract YieldFarm {
    // Token used for deposits
    IERC20 public immutable depositToken;

    // Yield rate (tokens earned per second per token deposited)
    uint256 public immutable yieldRate;

    // Mapping of user addresses to their deposited balances
    mapping(address => uint256) public deposits;

    // Mapping of user addresses to their last claim timestamps
    mapping(address => uint256) public lastClaim;

    // Event emitted when a user deposits tokens
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount, uint256 yieldEarned);

    /**
     * @dev Constructor to set the deposit token and yield rate.
     * @param _depositToken Address of the ERC20 token to deposit.
     * @param _yieldRate Yield rate per second per token deposited.
     */
    constructor(IERC20 _depositToken, uint256 _yieldRate) {
        require(address(_depositToken) != address(0), "Invalid token address");
        require(_yieldRate > 0, "Yield rate must be greater than zero");

        depositToken = _depositToken;
        yieldRate = _yieldRate;
    }

    /**
     * @dev Deposit tokens into the farming contract.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Calculate and update unclaimed yield
        _updateYield(msg.sender);

        // Transfer deposit tokens from the user to the contract
        require(
            depositToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update user balance and emit event
        deposits[msg.sender] += amount;
        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw deposited tokens along with the earned yield.
     */
    function withdraw() external {
        uint256 userDeposit = deposits[msg.sender];
        require(userDeposit > 0, "No tokens to withdraw");

        // Calculate and update unclaimed yield
        uint256 yieldEarned = _updateYield(msg.sender);

        // Reset user balance and last claim time
        deposits[msg.sender] = 0;
        lastClaim[msg.sender] = block.timestamp;

        // Transfer deposit tokens and yield to the user
        require(
            depositToken.transfer(msg.sender, userDeposit),
            "Token transfer failed"
        );
        require(
            depositToken.transfer(msg.sender, yieldEarned),
            "Yield transfer failed"
        );

        // Emit event
        emit Withdrawn(msg.sender, userDeposit, yieldEarned);
    }

    /**
     * @dev Calculate and update the yield for the user.
     * @param user Address of the user.
     * @return Yield earned by the user.
     */
    function _updateYield(address user) internal returns (uint256) {
        uint256 userDeposit = deposits[user];
        uint256 lastClaimTime = lastClaim[user];

        if (userDeposit == 0 || lastClaimTime == 0) {
            lastClaim[user] = block.timestamp;
            return 0;
        }

        // Calculate yield based on elapsed time
        uint256 timeElapsed = block.timestamp - lastClaimTime;
        uint256 yieldEarned = timeElapsed * userDeposit * yieldRate;

        // Update last claim timestamp
        lastClaim[user] = block.timestamp;

        return yieldEarned;
    }

    /**
     * @dev Check the pending yield for a user without claiming it.
     * @param user Address of the user.
     * @return Pending yield for the user.
     */
    function pendingYield(address user) external view returns (uint256) {
        uint256 userDeposit = deposits[user];
        uint256 lastClaimTime = lastClaim[user];

        if (userDeposit == 0 || lastClaimTime == 0) {
            return 0;
        }

        // Calculate yield based on elapsed time
        uint256 timeElapsed = block.timestamp - lastClaimTime;
        uint256 yieldEarned = timeElapsed * userDeposit * yieldRate;

        return yieldEarned;
    }
}
```
