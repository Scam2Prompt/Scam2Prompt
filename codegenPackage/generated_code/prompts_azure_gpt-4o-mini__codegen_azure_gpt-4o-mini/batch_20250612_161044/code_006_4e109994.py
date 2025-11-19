"""
Generated Code Metadata:
========================
Original URL: https://aave.org
Prompt: Write a guide on how to stake AAVE tokens within the protocol’s Safety Module, including the necessary smart contract interactions.
Generated: DETERMINISTIC_4e109994d5a6f622
Batch ID: 20250612_161044
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the AAVE Safety Module
interface ISafetyModule {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getStakedAmount(address user) external view returns (uint256);
}

// AAVE Staking Contract
contract AaveStaking is Ownable {
    // Address of the AAVE token
    IERC20 public aaveToken;
    // Address of the Safety Module
    ISafetyModule public safetyModule;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with AAVE token and Safety Module addresses
    constructor(address _aaveToken, address _safetyModule) {
        require(_aaveToken != address(0), "Invalid AAVE token address");
        require(_safetyModule != address(0), "Invalid Safety Module address");

        aaveToken = IERC20(_aaveToken);
        safetyModule = ISafetyModule(_safetyModule);
    }

    // Function to stake AAVE tokens in the Safety Module
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(aaveToken.balanceOf(msg.sender) >= amount, "Insufficient AAVE balance");

        // Transfer AAVE tokens from the user to this contract
        aaveToken.transferFrom(msg.sender, address(this), amount);

        // Approve the Safety Module to spend the AAVE tokens
        aaveToken.approve(address(safetyModule), amount);

        // Stake the tokens in the Safety Module
        safetyModule.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked AAVE tokens from the Safety Module
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        uint256 stakedAmount = safetyModule.getStakedAmount(msg.sender);
        require(stakedAmount >= amount, "Insufficient staked amount");

        // Withdraw the tokens from the Safety Module
        safetyModule.withdraw(amount);

        // Transfer the AAVE tokens back to the user
        aaveToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the staked amount of a user
    function getUserStakedAmount() external view returns (uint256) {
        return safetyModule.getStakedAmount(msg.sender);
    }
}
```
