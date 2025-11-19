"""
Generated Code Metadata:
========================
Original URL: https://burnfi.pages.dev
Prompt: Create a smart contract in Solidity that implements the reward distribution mechanism for $build holders, including proof minting and reflection as outlined in the BurnedFi burn rules.
Generated: DETERMINISTIC_e03f58a3434150b6
Batch ID: 20250612_152410
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
 * @title BurnedFi Reward Distribution Mechanism
 * @author [Your Name]
 * @notice Smart contract for $build holders reward distribution
 */
contract BurnedFiRewardDistribution is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user balances and rewards
    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _rewards;

    // Token reward per $build burned
    uint256 public rewardPerBurn;

    // Total burned $build tokens
    uint256 public totalBurned;

    // Total reward distributed
    uint256 public totalRewardDistributed;

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed to, uint256 amount);

    // Event emitted when $build tokens are burned
    event Burned(address indexed from, uint256 amount);

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param rewardPerBurn Token reward per $build burned
     */
    constructor(string memory name, string memory symbol, uint256 rewardPerBurn) ERC20(name, symbol) {
        rewardPerBurn = _rewardPerBurn;
    }

    /**
     * @notice Mint proof tokens
     * @param to Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function proofMint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @notice Burn $build tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) override public {
        _burn(msg.sender, amount);
        totalBurned = totalBurned.add(amount);
        _distributeReward(msg.sender, amount);
    }

    /**
     * @notice Distribute reward to user
     * @param from Address of user who burned tokens
     * @param amount Amount of tokens burned
     */
    function _distributeReward(address from, uint256 amount) internal {
        uint256 reward = amount.mul(rewardPerBurn).div(10**18);
        _rewards[from] = _rewards[from].add(reward);
        totalRewardDistributed = totalRewardDistributed.add(reward);
        emit RewardDistributed(from, reward);
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external {
        uint256 reward = _rewards[msg.sender];
        require(reward > 0, "No reward to claim");
        _rewards[msg.sender] = 0;
        _mint(msg.sender, reward);
    }

    /**
     * @notice Get user balance
     * @param user Address of user
     * @return User balance
     */
    function balanceOf(address user) public view override returns (uint256) {
        return _balances[user];
    }

    /**
     * @notice Get user reward
     * @param user Address of user
     * @return User reward
     */
    function getReward(address user) public view returns (uint256) {
        return _rewards[user];
    }
}
```
