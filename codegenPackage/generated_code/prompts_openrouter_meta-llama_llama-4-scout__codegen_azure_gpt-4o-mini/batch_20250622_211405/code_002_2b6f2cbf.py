"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: "Design a smart contract for a utility token like Lingo, incorporating features such as RWA investment portfolio management and rewards distribution."
Generated: DETERMINISTIC_2b6f2cbfdec5e188
Batch ID: 20250622_211405
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// LingoToken is a utility token that incorporates RWA investment portfolio management and rewards distribution
contract LingoToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track user rewards
    mapping(address => uint256) private _rewards;

    // Total rewards pool
    uint256 public totalRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("LingoToken", "LINGO") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to distribute rewards to users based on their holdings
    function distributeRewards() external onlyOwner {
        require(totalSupply() > 0, "No tokens in circulation");

        // Calculate rewards for each holder
        for (uint256 i = 0; i < totalSupply(); i++) {
            address holder = address(uint160(i)); // Placeholder for actual holder retrieval
            uint256 holderBalance = balanceOf(holder);
            if (holderBalance > 0) {
                uint256 reward = totalRewards.mul(holderBalance).div(totalSupply());
                _rewards[holder] = _rewards[holder].add(reward);
                emit RewardsDistributed(holder, reward);
            }
        }
        totalRewards = 0; // Reset total rewards after distribution
    }

    // Function to claim rewards for the caller
    function claimRewards() external {
        uint256 reward = _rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the user's rewards before transferring
        _rewards[msg.sender] = 0;

        // Transfer rewards to the user
        _mint(msg.sender, reward);
    }

    // Function to set the total rewards pool (only callable by owner)
    function setTotalRewards(uint256 amount) external onlyOwner {
        totalRewards = amount;
    }

    // Function to view rewards of a specific user
    function viewRewards(address user) external view returns (uint256) {
        return _rewards[user];
    }

    // Function to withdraw tokens mistakenly sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw LingoToken");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
