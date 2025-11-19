"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Provide a Solidity implementation for a community-driven token similar to $UPRINT, including features like renounced ownership and passive income generation.
Generated: DETERMINISTIC_0ac5410376a0d3af
Batch ID: 20250612_150426
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CommunityToken
 * @author [Your Name]
 * @notice A community-driven token with renounced ownership and passive income generation.
 */
contract CommunityToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective rewards
    mapping(address => uint256) private _rewards;

    // Total rewards distributed
    uint256 public totalRewards;

    // Reward rate per block
    uint256 public rewardRate;

    // Block number of last reward distribution
    uint256 public lastDistributionBlock;

    /**
     * @notice Constructor for the CommunityToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     * @param rewardRate_ The reward rate per block.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 rewardRate_
    ) ERC20(name, symbol) {
        // Mint the total supply to the contract owner
        _mint(msg.sender, totalSupply);

        // Initialize reward rate and last distribution block
        rewardRate = rewardRate_;
        lastDistributionBlock = block.number;

        // Renounce ownership
        renounceOwnership();
    }

    /**
     * @notice Distributes rewards to all token holders.
     */
    function distributeRewards() public nonReentrant {
        // Get the current block number
        uint256 currentBlock = block.number;

        // Calculate the number of blocks since last distribution
        uint256 blocksSinceLastDistribution = currentBlock - lastDistributionBlock;

        // Calculate the total rewards to be distributed
        uint256 rewardsToDistribute = blocksSinceLastDistribution * rewardRate;

        // Update the last distribution block
        lastDistributionBlock = currentBlock;

        // Update the total rewards distributed
        totalRewards += rewardsToDistribute;

        // Mint the rewards to the contract
        _mint(address(this), rewardsToDistribute);

        // Distribute rewards to all token holders
        for (address holder in _balances) {
            uint256 holderBalance = _balances[holder];
            uint256 holderRewards = (holderBalance * rewardsToDistribute) / totalSupply();
            _rewards[holder] += holderRewards;
        }
}

    /**
     * @notice Claims rewards for a token holder.
     */
    function claimRewards() public {
        // Get the rewards for the token holder
        uint256 rewards = _rewards[msg.sender];

        // Reset the rewards for the token holder
        _rewards[msg.sender] = 0;

        // Transfer the rewards to the token holder
        _transfer(address(this), msg.sender, rewards);
    }

    /**
     * @notice Transfers tokens from the contract to a recipient.
     * @param recipient The recipient address.
     * @param amount The amount of tokens to transfer.
     */
    function transferTokens(address recipient, uint256 amount) public {
        // Transfer tokens from the contract to the recipient
        _transfer(msg.sender, recipient, amount);
    }

    /**
     * @notice Overrides the transfer function to include reward distribution.
     * @param recipient The recipient address.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public override {
        // Distribute rewards before transfer
        distributeRewards();

        // Transfer tokens
        super.transfer(recipient, amount);
    }

    /**
     * @notice Overrides the transferFrom function to include reward distribution.
     * @param sender The sender address.
     * @param recipient The recipient address.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override {
        // Distribute rewards before transfer
        distributeRewards();

        // Transfer tokens
        super.transferFrom(sender, recipient, amount);
    }
}
```
