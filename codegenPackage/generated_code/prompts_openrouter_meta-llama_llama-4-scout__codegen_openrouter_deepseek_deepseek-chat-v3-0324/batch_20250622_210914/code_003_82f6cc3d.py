"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Develop a simple smart contract in Solidity that utilizes OUSD for yield generation, explaining how the contract would work and how it would be deployed on the Ethereum blockchain.
Generated: DETERMINISTIC_82f6cc3de26aa945
Batch ID: 20250622_210914
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

// Import OUSD contract interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title OUSDYieldGenerator
 * @dev A smart contract that allows users to deposit OUSD tokens and earn yield
 * from the OUSD protocol's rebase mechanism.
 */
contract OUSDYieldGenerator is Ownable, ReentrancyGuard {
    // OUSD token contract
    IERC20 public immutable ousdToken;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Total deposits in the contract
    uint256 public totalDeposits;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event YieldClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor that sets the OUSD token address
     * @param _ousdAddress Address of the OUSD token contract
     */
    constructor(address _ousdAddress) {
        require(_ousdAddress != address(0), "Invalid OUSD address");
        ousdToken = IERC20(_ousdAddress);
    }

    /**
     * @dev Deposit OUSD tokens into the contract to start earning yield
     * @param amount Amount of OUSD tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer OUSD from user to contract
        bool success = ousdToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");

        // Update user and total deposits
        userDeposits[msg.sender] += amount;
        totalDeposits += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw deposited OUSD tokens and any accrued yield
     * @param amount Amount of OUSD tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userDeposits[msg.sender] >= amount, "Insufficient balance");

        // Calculate user's share of the contract balance
        uint256 contractBalance = ousdToken.balanceOf(address(this));
        uint256 userShare = (contractBalance * amount) / totalDeposits;

        // Update user and total deposits before transfer to prevent reentrancy
        userDeposits[msg.sender] -= amount;
        totalDeposits -= amount;

        // Transfer OUSD to user
        bool success = ousdToken.transfer(msg.sender, userShare);
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, userShare);
    }

    /**
     * @dev Claim accrued yield without withdrawing principal
     */
    function claimYield() external nonReentrant {
        uint256 contractBalance = ousdToken.balanceOf(address(this));
        require(contractBalance > totalDeposits, "No yield available");

        // Calculate user's share of the yield
        uint256 yield = contractBalance - totalDeposits;
        uint256 userYield = (yield * userDeposits[msg.sender]) / totalDeposits;

        require(userYield > 0, "No yield to claim");

        // Transfer yield to user
        bool success = ousdToken.transfer(msg.sender, userYield);
        require(success, "Transfer failed");

        emit YieldClaimed(msg.sender, userYield);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(ousdToken), "Cannot recover OUSD");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
