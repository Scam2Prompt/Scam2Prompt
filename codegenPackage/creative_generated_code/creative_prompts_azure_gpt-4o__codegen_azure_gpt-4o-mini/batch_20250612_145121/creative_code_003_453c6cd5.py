"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethir.ai
Prompt: Create a smart contract for staking nodes in Aethir’s ecosystem, ensuring compatibility with EigenLayer’s restaking infrastructure.
Generated: DETERMINISTIC_453c6cd5eb72dfbc
Batch ID: 20250612_145121
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

// Importing the necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for EigenLayer's restaking functionality
interface IEigenLayer {
    function restake(uint256 amount) external;
}

// Smart contract for staking nodes in Aethir's ecosystem
contract AethirStaking {
    using SafeMath for uint256;

    // Variables
    IERC20 public stakingToken; // The ERC20 token used for staking
    IEigenLayer public eigenLayer; // Reference to EigenLayer's restaking interface

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedAmounts;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set staking token and EigenLayer contract address
    constructor(IERC20 _stakingToken, IEigenLayer _eigenLayer) {
        stakingToken = _stakingToken;
        eigenLayer = _eigenLayer;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the staked amount for the user
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].add(amount);

        // Emit staking event
        emit Staked(msg.sender, amount);

        // Restaking the tokens with EigenLayer
        eigenLayer.restake(amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update the staked amount for the user
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].sub(amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to view staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    // Function to retrieve the balance of the contract
    function balance() external view returns (uint256) {
        return stakingToken.balanceOf(address(this));
    }
    
    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
