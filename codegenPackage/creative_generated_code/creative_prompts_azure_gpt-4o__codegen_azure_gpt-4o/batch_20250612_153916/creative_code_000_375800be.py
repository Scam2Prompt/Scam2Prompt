"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fishersclubs.com
Prompt: Write a smart contract in Solidity that integrates SparkLend's protocol to allow users to deposit stablecoins and earn rewards transparently, ensuring compatibility with Ethereum and Base networks.
Generated: DETERMINISTIC_375800be6a28b678
Batch ID: 20250612_153916
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

// Import SparkLend's interface (Assuming SparkLend provides an ERC-20 compatible interface)
interface ISparkLend {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function getRewards(address user) external view returns (uint256);
    function claimRewards(address user) external;
}

// Import OpenZeppelin's SafeERC20 library to handle ERC-20 operations securely
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SparkLendStablecoinDepositor is Ownable {
    using SafeERC20 for IERC20;

    // SparkLend protocol address
    ISparkLend public sparkLend;

    // Mapping to track user deposits
    mapping(address => mapping(address => uint256)) public userDeposits;

    // Event declarations
    event Deposit(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    /**
     * @dev Constructor to initialize the SparkLend protocol address.
     * @param _sparkLend The address of the SparkLend protocol.
     */
    constructor(address _sparkLend) {
        require(_sparkLend != address(0), "Invalid SparkLend address");
        sparkLend = ISparkLend(_sparkLend);
    }

    /**
     * @dev Allows the user to deposit stablecoins into the SparkLend protocol.
     * @param token The address of the ERC-20 stablecoin to deposit.
     * @param amount The amount of tokens to deposit.
     */
    function depositStablecoin(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from user to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Approve SparkLend to use the deposited tokens
        IERC20(token).safeApprove(address(sparkLend), amount);

        // Deposit tokens to SparkLend
        sparkLend.deposit(token, amount);

        // Track user deposit
        userDeposits[msg.sender][token] += amount;

        emit Deposit(msg.sender, token, amount);
    }

    /**
     * @dev Allows the user to withdraw stablecoins from the SparkLend protocol.
     * @param token The address of the ERC-20 stablecoin to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawStablecoin(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userDeposits[msg.sender][token] >= amount, "Insufficient balance");

        // Withdraw tokens from SparkLend
        sparkLend.withdraw(token, amount);

        // Transfer tokens back to the user
        IERC20(token).safeTransfer(msg.sender, amount);

        // Update user deposit
        userDeposits[msg.sender][token] -= amount;

        emit Withdraw(msg.sender, token, amount);
    }

    /**
     * @dev Allows the user to claim rewards earned from their deposits.
     */
    function claimRewards() external {
        // Get rewards balance for the user
        uint256 rewards = sparkLend.getRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Claim rewards from SparkLend
        sparkLend.claimRewards(msg.sender);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Allows the owner to update the SparkLend protocol address.
     * @param _sparkLend The new SparkLend protocol address.
     */
    function updateSparkLendAddress(address _sparkLend) external onlyOwner {
        require(_sparkLend != address(0), "Invalid SparkLend address");
        sparkLend = ISparkLend(_sparkLend);
    }
}
```
