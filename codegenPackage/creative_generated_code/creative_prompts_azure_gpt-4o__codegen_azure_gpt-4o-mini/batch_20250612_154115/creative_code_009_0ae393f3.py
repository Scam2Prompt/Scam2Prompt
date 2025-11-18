"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyzwthelly.com
Prompt: Create a Solidity contract that integrates with Valantis to enable liquid staking of nBTC via the stHYPE AMM.
Generated: DETERMINISTIC_0ae393f3266355ab
Batch ID: 20250612_154115
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the stHYPE AMM
interface IStHypeAMM {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getStakedAmount(address user) external view returns (uint256);
}

// nBTC Liquid Staking Contract
contract LiquidStaking is Ownable {
    // Address of the nBTC token
    IERC20 public nbtcToken;
    // Address of the stHYPE AMM contract
    IStHypeAMM public stHypeAMM;

    // Event for staking nBTC
    event Staked(address indexed user, uint256 amount);
    // Event for unstaking nBTC
    event Unstaked(address indexed user, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) private stakedBalances;

    // Constructor to initialize contract
    constructor(address _nbtcToken, address _stHypeAMM) {
        require(_nbtcToken != address(0), "Invalid nBTC token address");
        require(_stHypeAMM != address(0), "Invalid stHYPE AMM address");

        nbtcToken = IERC20(_nbtcToken);
        stHypeAMM = IStHypeAMM(_stHypeAMM);
    }

    // Function to stake nBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(nbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user balance
        stakedBalances[msg.sender] += amount;

        // Stake to stHYPE AMM
        stHypeAMM.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake nBTC tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Unstake from stHYPE AMM
        stHypeAMM.unstake(amount);

        // Update user balance
        stakedBalances[msg.sender] -= amount;

        // Transfer nBTC tokens back to the user
        require(nbtcToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the amount staked by a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}
```
