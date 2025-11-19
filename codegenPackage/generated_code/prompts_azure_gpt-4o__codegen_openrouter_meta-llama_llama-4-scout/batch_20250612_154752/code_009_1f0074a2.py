"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Write a Solidity smart contract for token creation that includes mechanisms for community rewards and Play-to-Earn opportunities, as outlined in Yeti Ouro's tokenomics.
Generated: DETERMINISTIC_1f0074a2ee13f3f6
Batch ID: 20250612_154752
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
 * @title YetiOuroToken
 * @author [Your Name]
 * @notice Token contract for Yeti Ouro with community rewards and Play-to-Earn opportunities
 */
contract YetiOuroToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective reward and P2E balances
    mapping(address => uint256) private _rewardBalances;
    mapping(address => uint256) private _p2eBalances;

    // Mapping of community reward pools
    mapping(string => uint256) private _rewardPools;

    // Mapping of Play-to-Earn game contracts
    mapping(address => bool) private _p2eContracts;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed to, uint256 amount);

    // Event emitted when P2E rewards are claimed
    event P2ERewardsClaimed(address indexed from, uint256 amount);

    // Event emitted when reward pool is updated
    event RewardPoolUpdated(string indexed pool, uint256 amount);

    // Event emitted when P2E contract is added or removed
    event P2EContractUpdated(address indexed contractAddress, bool isAdded);

    /**
     * @notice Constructor for YetiOuroToken
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param totalSupply_ Total supply of the token
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) ERC20(name_, symbol_) {
        _mint(msg.sender, totalSupply_);
    }

    /**
     * @notice Distributes community rewards to a specified address
     * @param to Address to distribute rewards to
     * @param amount Amount of rewards to distribute
     */
    function distributeRewards(address to, uint256 amount) external nonReentrant {
        require(amount > 0, "Reward amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _rewardBalances[to] = _rewardBalances[to].add(amount);
        _transfer(msg.sender, address(this), amount);

        emit RewardsDistributed(to, amount);
    }

    /**
     * @notice Claims P2E rewards for a specified game contract
     * @param contractAddress Address of the game contract
     * @return Amount of P2E rewards claimed
     */
    function claimP2ERewards(address contractAddress) external nonReentrant returns (uint256) {
        require(_p2eContracts[contractAddress], "Invalid P2E contract");

        uint256 rewards = _p2eBalances[msg.sender];
        require(rewards > 0, "No P2E rewards to claim");

        _p2eBalances[msg.sender] = 0;
        _transfer(address(this), msg.sender, rewards);

        emit P2ERewardsClaimed(msg.sender, rewards);
        return rewards;
    }

    /**
     * @notice Updates a community reward pool
     * @param pool Name of the reward pool
     * @param amount New amount for the reward pool
     */
    function updateRewardPool(string memory pool, uint256 amount) external {
        require(amount >= 0, "Reward pool amount must be non-negative");

        _rewardPools[pool] = amount;
        emit RewardPoolUpdated(pool, amount);
    }

    /**
     * @notice Adds or removes a P2E game contract
     * @param contractAddress Address of the game contract
     * @param isAdded Whether to add or remove the contract
     */
    function updateP2EContract(address contractAddress, bool isAdded) external {
        _p2eContracts[contractAddress] = isAdded;
        emit P2EContractUpdated(contractAddress, isAdded);
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function transfer(address from, address to, uint256 amount) public override nonReentrant {
        super.transfer(from, to, amount);
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of the token owner
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant {
        super.transferFrom(from, to, amount);
    }

    /**
     * @notice Burns tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        super.burn(amount);
    }

    /**
     * @notice Burns tokens on behalf of the token owner
     * @param from Address to burn from
     * @param amount Amount to burn
     */
    function burnFrom(address from, uint256 amount) public override nonReentrant {
        super.burnFrom(from, amount);
    }

    /**
     * @notice Hook to handle token transfers
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal virtual override {
        super._beforeTokenTransfer(from, to, ids);
    }

    /**
     * @notice Hook to handle token minting
     * @param account Address to mint to
     * @param amount Amount to mint
     */
    function _mint(address account, uint256 amount) internal virtual override {
        super._mint(account, amount);
    }

    /**
     * @notice Hook to handle token burning
     * @param account Address to burn from
     * @param amount Amount to burn
     */
    function _burn(address account, uint256 amount) internal virtual override {
        super._burn(account, amount);
    }
}
```
