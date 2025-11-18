"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofinance.blogspot.com
Prompt: Provide an example of a smart contract that integrates Lido Finance's liquid staking model to allow users to stake fractions of ETH and receive stETH tokens.
Generated: DETERMINISTIC_bff38c7a56dfa92c
Batch ID: 20250612_142640
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

// Importing ERC20 interface for interacting with stETH
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for Lido's staking router
interface ILido {
    function submit(address _referral) external payable returns (uint256);
    function getStETHByETH(uint256 _amount) external view returns (uint256);
}

contract LidoStaking {
    // Addresses for the Lido Staking contract and stETH token
    address public immutable lidoContract;
    IERC20 public immutable stETH;

    // Event emitted when user stakes ETH
    event Staked(address indexed user, uint256 ethAmount, uint256 stEthAmount);

    // Constructor to initialize the contract with Lido's contract address and stETH token address
    constructor(address _lidoContract, address _stETH) {
        require(_lidoContract != address(0), "Invalid Lido contract address");
        require(_stETH != address(0), "Invalid stETH address");

        lidoContract = _lidoContract;
        stETH = IERC20(_stETH);
    }

    // Function to stake ETH and receive stETH
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount of ETH");

        // Submit ETH to Lido and receive stETH
        uint256 stEthAmount = ILido(lidoContract).submit{value: msg.value}(address(0));

        // Emit an event for the staking action
        emit Staked(msg.sender, msg.value, stEthAmount);
    }

    // Function to get the equivalent stETH for a given amount of ETH
    function getEquivalentStETH(uint256 ethAmount) external view returns (uint256) {
        require(ethAmount > 0, "Must query a positive amount of ETH");
        return ILido(lidoContract).getStETHByETH(ethAmount);
    }

    // Fallback function to accept ETH
    receive() external payable {
        // Accept ETH transfers directly
    }
    
    // Function to withdraw stETH from the contract (for demonstration purposes)
    // Note: Actual withdrawal of ETH/stETH will require a redeem function and is not covered in this basic implementation
    function withdrawStETH(uint256 amount) external {
        require(stETH.balanceOf(address(this)) >= amount, "Insufficient stETH balance");
        stETH.transfer(msg.sender, amount);
    }
}
```
