"""
Generated Code Metadata:
========================
Original URL: https://asterdex.vercel.app
Prompt: Generate a smart contract code in Solidity that enables the minting of USDF and earns passive income through optimized returns, following the security audit guidelines provided by Astherus.
Generated: DETERMINISTIC_241e61e61fb38a5a
Batch ID: 20250622_212351
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title USDF Stablecoin with Passive Income
 * @dev ERC20 token with minting, burning, and passive income features
 * Implements security best practices from OpenZeppelin and Astherus audit guidelines
 */
contract USDF is ERC20, Ownable, Pausable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion USDF
    uint256 public constant PASSIVE_INCOME_RATE = 5; // 5% annual return
    uint256 public constant REWARD_INTERVAL = 365 days;
    
    mapping(address => uint256) public lastRewardTimestamp;
    mapping(address => uint256) public rewards;
    mapping(address => bool) public authorizedMinters;

    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event MinterAdded(address indexed minter);
    event MinterRemoved(address indexed minter);

    constructor() ERC20("USDF Stablecoin", "USDF") {
        _mint(msg.sender, 100_000 * 10**18); // Initial mint
    }

    modifier onlyMinter() {
        require(authorizedMinters[msg.sender] || msg.sender == owner(), "USDF: Not authorized");
        _;
    }

    /**
     * @dev Mint new USDF tokens
     * @param to Address to receive the minted tokens
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyMinter whenNotPaused nonReentrant {
        require(totalSupply() + amount <= MAX_SUPPLY, "USDF: Max supply exceeded");
        _mint(to, amount);
        updateRewards(to);
        emit Mint(to, amount);
    }

    /**
     * @dev Burn USDF tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) external whenNotPaused nonReentrant {
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Add an authorized minter
     * @param minter Address to add as minter
     */
    function addMinter(address minter) external onlyOwner {
        authorizedMinters[minter] = true;
        emit MinterAdded(minter);
    }

    /**
     * @dev Remove an authorized minter
     * @param minter Address to remove as minter
     */
    function removeMinter(address minter) external onlyOwner {
        authorizedMinters[minter] = false;
        emit MinterRemoved(minter);
    }

    /**
     * @dev Pause contract operations
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Calculate accrued rewards for an address
     * @param account Address to calculate rewards for
     */
    function calculateRewards(address account) public view returns (uint256) {
        if (balanceOf(account) == 0) return 0;
        
        uint256 lastReward = lastRewardTimestamp[account];
        if (lastReward == 0) return 0;
        
        uint256 timeElapsed = block.timestamp - lastReward;
        uint256 rewardRate = PASSIVE_INCOME_RATE * 1e16 / REWARD_INTERVAL; // 5% per year in wei-seconds
        uint256 reward = (balanceOf(account) * rewardRate * timeElapsed) / 1e18;
        
        return rewards[account] + reward;
    }

    /**
     * @dev Update rewards for an address
     * @param account Address to update rewards for
     */
    function updateRewards(address account) internal {
        rewards[account] = calculateRewards(account);
        lastRewardTimestamp[account] = block.timestamp;
    }

    /**
     * @dev Claim accrued rewards
     */
    function claimRewards() external whenNotPaused nonReentrant {
        updateRewards(msg.sender);
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "USDF: No rewards to claim");
        
        rewards[msg.sender] = 0;
        _mint(msg.sender, rewardAmount);
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Override transfer to update rewards
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);
        
        if (from != address(0)) {
            updateRewards(from);
        }
        if (to != address(0)) {
            updateRewards(to);
        }
    }
}
```
