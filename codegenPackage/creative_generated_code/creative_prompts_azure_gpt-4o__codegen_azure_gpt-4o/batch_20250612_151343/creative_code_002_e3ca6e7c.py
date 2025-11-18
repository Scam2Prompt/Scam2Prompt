"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gravity-cq3.pages.dev
Prompt: Generate a smart contract example that utilizes Gravity's omnichain intent protocol to manage yield-enabled unified balances across multiple chains.
Generated: DETERMINISTIC_e3ca6e7c2ee298dd
Batch ID: 20250612_151343
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

// Import the Gravity Omnichain Intent Protocol interface
import "./GravityIntentProtocol.sol"; // Ensure you include Gravity's omnichain protocol library or interface.

// Import OpenZeppelin's libraries for secure contract development
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title YieldEnabledUnifiedBalanceManager
 * @dev Smart contract that utilizes Gravity's omnichain intent protocol to manage unified balances with yield generation across multiple chains.
 */
contract YieldEnabledUnifiedBalanceManager is Ownable, ReentrancyGuard {
    // Gravity protocol instance
    GravityIntentProtocol private gravity;

    // Mapping to track user unified balances (user => balance)
    mapping(address => uint256) public unifiedBalances;

    // Yield generation token
    IERC20 public yieldToken;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event YieldGenerated(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with Gravity protocol instance and yield token.
     * @param _gravityAddress Address of the Gravity protocol.
     * @param _yieldToken Address of the yield generation token.
     */
    constructor(address _gravityAddress, address _yieldToken) {
        require(_gravityAddress != address(0), "Gravity address cannot be zero");
        require(_yieldToken != address(0), "Yield token address cannot be zero");
        gravity = GravityIntentProtocol(_gravityAddress);
        yieldToken = IERC20(_yieldToken);
    }

    /**
     * @dev Deposit funds into the unified balance.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer yield tokens from the user to this contract
        bool success = yieldToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's unified balance
        unifiedBalances[msg.sender] += amount;

        // Notify Gravity of the deposit intent
        gravity.registerIntent(msg.sender, "DEPOSIT", amount);

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw funds from the unified balance.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(unifiedBalances[msg.sender] >= amount, "Insufficient balance");

        // Deduct the amount from the user's unified balance
        unifiedBalances[msg.sender] -= amount;

        // Transfer yield tokens back to the user
        bool success = yieldToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Notify Gravity of the withdraw intent
        gravity.registerIntent(msg.sender, "WITHDRAW", amount);

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Generate yield for the user's unified balance.
     * @param user Address of the user.
     * @param yieldAmount Amount of yield to generate.
     */
    function generateYield(address user, uint256 yieldAmount) external onlyOwner {
        require(user != address(0), "User address cannot be zero");
        require(yieldAmount > 0, "Yield amount must be greater than zero");
        require(unifiedBalances[user] > 0, "User has no balance");

        // Update the user's unified balance with the yield amount
        unifiedBalances[user] += yieldAmount;

        // Notify Gravity of the yield generation intent
        gravity.registerIntent(user, "YIELD", yieldAmount);

        emit YieldGenerated(user, yieldAmount);
    }

    /**
     * @dev Get the unified balance of a user.
     * @param user Address of the user.
     * @return Unified balance of the user.
     */
    function getUnifiedBalance(address user) external view returns (uint256) {
        return unifiedBalances[user];
    }
}
```

Make sure to replace `GravityIntentProtocol` and `yieldToken` with the proper implementations and contracts relevant to your system. Also, ensure the Gravity protocol library is correctly integrated and available in your development environment.
