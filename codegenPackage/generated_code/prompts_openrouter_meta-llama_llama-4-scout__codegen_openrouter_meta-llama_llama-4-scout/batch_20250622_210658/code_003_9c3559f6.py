"""
Generated Code Metadata:
========================
Original URL: https://dropvault.net
Prompt: Develop a smart contract to distribute $gETH tokens proportionally to users based on their gas fee expenditure on the Ethereum network.
Generated: DETERMINISTIC_9c3559f62d36b091
Batch ID: 20250622_210658
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GasTokenDistributor
 * @author [Your Name]
 * @notice Distributes $gETH tokens proportionally to users based on their gas fee expenditure on the Ethereum network.
 */
contract GasTokenDistributor {
    using SafeMath for uint256;

    // Mapping of user addresses to their total gas spent
    mapping(address => uint256) public userGasSpent;

    // Mapping of user addresses to their $gETH token balance
    mapping(address => uint256) public userTokenBalance;

    // $gETH token contract
    ERC20 public gETH;

    // Total gas spent by all users
    uint256 public totalGasSpent;

    // Total $gETH tokens distributed
    uint256 public totalTokensDistributed;

    /**
     * @notice Constructor
     * @param _gETH $gETH token contract address
     */
    constructor(address _gETH) {
        require(_gETH != address(0), "gETH token address cannot be zero");
        gETH = ERC20(_gETH);
    }

    /**
     * @notice Tracks gas spent by a user
     */
    fallback() external payable {
        // Only track gas spent if the user is not the contract itself
        if (msg.sender != address(this)) {
            userGasSpent[msg.sender] = userGasSpent[msg.sender].add(gasPrice.mul(gasleft));
            totalGasSpent = totalGasSpent.add(gasPrice.mul(gasleft));
        }
    }

    /**
     * @notice Distributes $gETH tokens to users based on their gas expenditure
     * @param _amount Amount of $gETH tokens to distribute
     */
    function distributeTokens(uint256 _amount) public {
        require(_amount > 0, "Distribution amount must be greater than zero");
        require(gETH.balanceOf(address(this)) >= _amount, "Insufficient $gETH token balance");

        // Calculate the total gas spent by all users
        uint256 _totalGasSpent = totalGasSpent;

        // Distribute tokens to users
        for (address user in userGasSpent) {
            uint256 userGas = userGasSpent[user];
            if (userGas > 0) {
                uint256 tokenAmount = _amount.mul(userGas).div(_totalGasSpent);
                userTokenBalance[user] = userTokenBalance[user].add(tokenAmount);
                gETH.transfer(user, tokenAmount);
                totalTokensDistributed = totalTokensDistributed.add(tokenAmount);
            }
        }
    }

    /**
     * @notice Withdraws $gETH tokens
     * @param _amount Amount of $gETH tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) public {
        require(userTokenBalance[msg.sender] >= _amount, "Insufficient token balance");
        userTokenBalance[msg.sender] = userTokenBalance[msg.sender].sub(_amount);
        gETH.transfer(msg.sender, _amount);
    }

    /**
     * @notice Gets user $gETH token balance
     * @param _user User address
     * @return $gETH token balance
     */
    function getUserTokenBalance(address _user) public view returns (uint256) {
        return userTokenBalance[_user];
    }
}
```
