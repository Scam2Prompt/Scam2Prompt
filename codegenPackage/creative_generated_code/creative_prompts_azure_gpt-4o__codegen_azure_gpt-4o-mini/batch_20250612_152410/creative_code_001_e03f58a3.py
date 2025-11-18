"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Create a smart contract in Solidity that implements the reward distribution mechanism for $build holders, including proof minting and reflection as outlined in the BurnedFi burn rules.
Generated: DETERMINISTIC_e03f58a3434150b6
Batch ID: 20250612_152410
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BuildToken is ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Mapping to track rewards per account
    mapping(address => uint256) private _rewards;
    // Total rewards distributed
    uint256 private _totalRewards;
    // The token used for rewards (could be the same or different token)
    IERC20 public rewardToken;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed to, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed by, uint256 amount);

    constructor(string memory name, string memory symbol, address _rewardToken) 
        ERC20(name, symbol) {
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Distributes rewards to a holder.
     * @param to The address of the token holder.
     * @param amount The amount of reward tokens to distribute.
     */
    function distributeRewards(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot distribute rewards to the zero address");
        require(amount > 0, "Reward amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward token balance");

        _rewards[to] = _rewards[to].add(amount);
        _totalRewards = _totalRewards.add(amount);
        rewardToken.transfer(to, amount);

        emit RewardsDistributed(to, amount);
    }

    /**
     * @dev Claims rewards for the caller.
     */
    function claimRewards() external {
        uint256 rewardAmount = _rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        _rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Returns the reward balance of an account.
     * @param account The address of the account.
     * @return The amount of rewards available for the account.
     */
    function rewardBalance(address account) external view returns (uint256) {
        return _rewards[account];
    }

    /**
     * @dev Allows the owner to withdraw any tokens sent to the contract accidentally.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
