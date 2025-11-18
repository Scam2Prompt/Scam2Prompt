"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Write a smart contract in Solidity for a utility token that supports gameplay rewards and integrates with the Pixels platform's Chapter Two release.
Generated: DETERMINISTIC_1a90ea8166379456
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title UtilityToken
 * @dev A smart contract for a utility token integrated with the Pixels platform's Chapter Two release.
 * The token supports gameplay rewards and follows best practices for ERC20 tokens.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract UtilityToken is ERC20, Ownable {
    // Mapping to track reward eligibility for specific users
    mapping(address => bool) private rewardEligible;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Adds a user to the reward eligibility list.
     * @param user Address of the user to add.
     */
    function addRewardEligibleUser(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        rewardEligible[user] = true;
    }

    /**
     * @dev Removes a user from the reward eligibility list.
     * @param user Address of the user to remove.
     */
    function removeRewardEligibleUser(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        rewardEligible[user] = false;
    }

    /**
     * @dev Checks if a user is eligible for rewards.
     * @param user Address of the user to check.
     * @return True if the user is eligible, false otherwise.
     */
    function isRewardEligible(address user) external view returns (bool) {
        return rewardEligible[user];
    }

    /**
     * @dev Distributes rewards to eligible users.
     * @param user Address of the user to distribute rewards to.
     * @param amount Amount of tokens to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardEligible[user], "User not eligible for rewards");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the user
        _transfer(address(this), user, amount);

        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Mints new tokens to the contract's balance for reward distribution.
     * @param amount Amount of tokens to mint.
     */
    function mintRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _mint(address(this), amount);
    }

    /**
     * @dev Overrides the ERC20 transfer function to prevent contract address from transferring tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens being transferred.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(msg.sender != address(this), "Contract cannot directly transfer tokens");
        return super.transfer(recipient, amount);
    }
}
```
