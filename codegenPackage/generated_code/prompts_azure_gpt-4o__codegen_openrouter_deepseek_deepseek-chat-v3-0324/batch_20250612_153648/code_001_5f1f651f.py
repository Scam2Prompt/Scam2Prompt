"""
Generated Code Metadata:
========================
Original URL: https://mogcoin2.pages.dev
Prompt: Generate Solidity code for an ERC-20 token contract that mimics the features of $MOG, including tokenized winning and cultural branding.
Generated: DETERMINISTIC_5f1f651f405a3c37
Batch ID: 20250612_153648
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

contract MogToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public constant MAX_SUPPLY = 420690000000000 * 10**18;
    uint256 public constant INITIAL_SUPPLY = 420690000000000 * 10**18;
    uint256 public constant WINNING_POOL_PERCENTAGE = 10; // 10% of total supply for winning pool
    uint256 public constant COMMUNITY_REWARDS_PERCENTAGE = 20; // 20% of total supply for community rewards

    // Addresses
    address public winningPoolAddress;
    address public communityRewardsAddress;

    // Events
    event WinningPoolDistributed(address indexed winner, uint256 amount);
    event CommunityRewardDistributed(address indexed recipient, uint256 amount);

    constructor(
        address _winningPoolAddress,
        address _communityRewardsAddress
    ) ERC20("Mog Token", "MOG") {
        require(_winningPoolAddress != address(0), "Invalid winning pool address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");

        winningPoolAddress = _winningPoolAddress;
        communityRewardsAddress = _communityRewardsAddress;

        // Mint initial supply
        _mint(msg.sender, INITIAL_SUPPLY);

        // Distribute initial allocations
        uint256 winningPoolAmount = MAX_SUPPLY.mul(WINNING_POOL_PERCENTAGE).div(100);
        uint256 communityRewardsAmount = MAX_SUPPLY.mul(COMMUNITY_REWARDS_PERCENTAGE).div(100);

        _transfer(msg.sender, winningPoolAddress, winningPoolAmount);
        _transfer(msg.sender, communityRewardsAddress, communityRewardsAmount);
    }

    /**
     * @dev Distribute winnings from the winning pool
     * @param winner The address of the winner
     * @param amount The amount to distribute
     */
    function distributeWinnings(address winner, uint256 amount) external onlyOwner {
        require(winner != address(0), "Invalid winner address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(winningPoolAddress) >= amount, "Insufficient winning pool balance");

        _transfer(winningPoolAddress, winner, amount);
        emit WinningPoolDistributed(winner, amount);
    }

    /**
     * @dev Distribute community rewards
     * @param recipient The address of the recipient
     * @param amount The amount to distribute
     */
    function distributeCommunityReward(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(communityRewardsAddress) >= amount, "Insufficient community rewards balance");

        _transfer(communityRewardsAddress, recipient, amount);
        emit CommunityRewardDistributed(recipient, amount);
    }

    /**
     * @dev Update winning pool address
     * @param newAddress The new winning pool address
     */
    function updateWinningPoolAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        winningPoolAddress = newAddress;
    }

    /**
     * @dev Update community rewards address
     * @param newAddress The new community rewards address
     */
    function updateCommunityRewardsAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        communityRewardsAddress = newAddress;
    }

    /**
     * @dev Override transfer to include any custom logic (e.g., cultural branding)
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        super._transfer(sender, recipient, amount);
        // Additional cultural branding logic can be added here
    }

    /**
     * @dev Burn tokens - can be used for deflationary mechanisms
     * @param amount The amount to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
