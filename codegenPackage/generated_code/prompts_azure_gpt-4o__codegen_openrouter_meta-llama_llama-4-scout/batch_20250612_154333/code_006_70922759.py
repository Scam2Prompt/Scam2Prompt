"""
Generated Code Metadata:
========================
Original URL: https://flockerz-it.web.app
Prompt: Develop a Solidity smart contract for a DAO vault similar to the Flock Vault, allowing token holders to collectively allocate resources and earn rewards based on participation.
Generated: DETERMINISTIC_70922759f59bdfae
Batch ID: 20250612_154333
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title FlockVaultDAO
 * @author [Your Name]
 * @notice A decentralized autonomous organization (DAO) vault for collective resource allocation and reward distribution.
 */
contract FlockVaultDAO is Ownable, Pausable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of token holders to their respective balances
    mapping(address => uint256) public balances;

    // Mapping of token holders to their respective participation rewards
    mapping(address => uint256) public rewards;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Total tokens locked in the vault
    uint256 public totalTokens;

    // Address of the reward token
    address public rewardToken;

    // Address of the vault token
    address public vaultToken;

    /**
     * @notice Initializes the FlockVaultDAO contract.
     * @param _vaultToken Address of the vault token.
     * @param _rewardToken Address of the reward token.
     */
    constructor(address _vaultToken, address _rewardToken) {
        require(_vaultToken != address(0), "Vault token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        vaultToken = _vaultToken;
        rewardToken = _rewardToken;
    }

    /**
     * @notice Deposits tokens into the vault.
     * @param _amount Amount of tokens to deposit.
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(IERC20(vaultToken).balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        IERC20(vaultToken).safeTransferFrom(msg.sender, address(this), _amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);
        totalTokens = totalTokens.add(_amount);
    }

    /**
     * @notice Withdraws tokens from the vault.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] = balances[msg.sender].sub(_amount);
        totalTokens = totalTokens.sub(_amount);
        IERC20(vaultToken).safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Distributes rewards to token holders based on participation.
     * @param _amount Amount of rewards to distribute.
     */
    function distributeRewards(uint256 _amount) public onlyOwner {
        require(_amount > 0, "Reward amount must be greater than zero");
        require(IERC20(rewardToken).balanceOf(msg.sender) >= _amount, "Insufficient reward balance");

        totalRewards = totalRewards.add(_amount);
        IERC20(rewardToken).safeTransferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Claims rewards for a token holder.
     */
    function claimRewards() public {
        uint256 _rewards = rewards[msg.sender];
        require(_rewards > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        IERC20(rewardToken).safeTransfer(msg.sender, _rewards);
    }

    /**
     * @notice Calculates and updates the rewards for a token holder.
     * @param _holder Address of the token holder.
     */
    function updateRewards(address _holder) internal {
        uint256 _participation = balances[_holder].mul(100).div(totalTokens);
        uint256 _reward = totalRewards.mul(_participation).div(100);
        rewards[_holder] = rewards[_holder].add(_reward);
    }

    /**
     * @notice Updates the rewards for all token holders.
     */
    function updateAllRewards() public {
        for (address _holder in balances) {
            updateRewards(_holder);
        }
    }

    /**
     * @notice Pauses the contract.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @notice Unpauses the contract.
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
```
