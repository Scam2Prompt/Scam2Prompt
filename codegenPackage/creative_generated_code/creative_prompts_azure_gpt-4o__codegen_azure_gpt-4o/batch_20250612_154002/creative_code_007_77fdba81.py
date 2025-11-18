"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqex.com
Prompt: Develop a smart contract that integrates with DCQEX to automate yield farming strategies on Ethereum.
Generated: DETERMINISTIC_77fdba8121c346f2
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

// Import OpenZeppelin libraries for secure smart contract development
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for interacting with DCQEX (Decentralized Crypto Exchange)
interface IDCQEX {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function claimRewards() external returns (uint256);
    function getAPY(address token) external view returns (uint256);
}

contract YieldFarmingAutomation is Ownable, ReentrancyGuard {
    // DCQEX contract address
    address public dcqexAddress;

    // Token to farm with
    address public farmingToken;

    // Reward token address
    address public rewardToken;

    // DCQEX interface
    IDCQEX public dcqex;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Event emitted when funds are deposited to DCQEX
    event FundsDeposited(address indexed user, uint256 amount);

    // Event emitted when funds are withdrawn from DCQEX
    event FundsWithdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the DCQEX contract, tokens, and owner
    constructor(address _dcqexAddress, address _farmingToken, address _rewardToken) {
        require(_dcqexAddress != address(0), "Invalid DCQEX address");
        require(_farmingToken != address(0), "Invalid farming token address");
        require(_rewardToken != address(0), "Invalid reward token address");

        dcqexAddress = _dcqexAddress;
        farmingToken = _farmingToken;
        rewardToken = _rewardToken;

        dcqex = IDCQEX(_dcqexAddress);
    }

    // Deposit funds into DCQEX for yield farming
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the sender to this contract
        IERC20(farmingToken).transferFrom(msg.sender, address(this), amount);

        // Approve DCQEX to spend the tokens
        IERC20(farmingToken).approve(dcqexAddress, amount);

        // Deposit into DCQEX
        dcqex.deposit(farmingToken, amount);

        emit FundsDeposited(msg.sender, amount);
    }

    // Withdraw funds from DCQEX
    function withdraw(uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw from DCQEX
        dcqex.withdraw(farmingToken, amount);

        // Transfer tokens back to the owner
        IERC20(farmingToken).transfer(owner(), amount);

        emit FundsWithdrawn(owner(), amount);
    }

    // Claim rewards earned from yield farming
    function claimRewards() external nonReentrant onlyOwner {
        // Claim rewards from DCQEX
        uint256 rewardAmount = dcqex.claimRewards();

        require(rewardAmount > 0, "No rewards available to claim");

        // Transfer rewards to the owner
        IERC20(rewardToken).transfer(owner(), rewardAmount);

        emit RewardsClaimed(owner(), rewardAmount);
    }

    // Fetch the current APY for the farming token
    function getFarmingAPY() external view returns (uint256) {
        return dcqex.getAPY(farmingToken);
    }

    // Emergency withdrawal function for the owner
    function emergencyWithdraw() external nonReentrant onlyOwner {
        uint256 balance = IERC20(farmingToken).balanceOf(address(this));
        require(balance > 0, "No funds available for withdrawal");

        IERC20(farmingToken).transfer(owner(), balance);

        uint256 rewardBalance = IERC20(rewardToken).balanceOf(address(this));
        if (rewardBalance > 0) {
            IERC20(rewardToken).transfer(owner(), rewardBalance);
        }
    }
}
```
