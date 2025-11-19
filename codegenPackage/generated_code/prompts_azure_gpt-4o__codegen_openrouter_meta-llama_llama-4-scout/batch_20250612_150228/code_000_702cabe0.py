"""
Generated Code Metadata:
========================
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Write a smart contract in Solidity for a farming system that integrates with the Pencils Protocol on the Scroll zkEVM ecosystem, ensuring compatibility with Ethereum mainnet security standards.
Generated: DETERMINISTIC_702cabe08defdcc3
Batch ID: 20250612_150228
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";

/**
 * @title FarmingSystem
 * @author [Your Name]
 * @notice A smart contract for a farming system integrated with Pencils Protocol on Scroll zkEVM ecosystem.
 */
contract FarmingSystem is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user farming information
    mapping(address => UserInfo) public userInfo;

    // Mapping of farming pools
    mapping(uint256 => PoolInfo) public poolInfo;

    // Total number of pools
    uint256 public poolLength;

    // Pencils Protocol integration
    address public pencilsProtocol;

    // Token address
    address public token;

    // Event emitted when user deposits
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when user withdraws
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when user harvests
    event Harvest(address indexed user, uint256 indexed pid, uint256 amount);

    // Struct for user information
    struct UserInfo {
        uint256 amount; // User deposited amount
        uint256 rewardDebt; // User reward debt
    }

    // Struct for pool information
    struct PoolInfo {
        IERC20 lpToken; // LP token address
        uint256 allocPoint; // Allocation points
        uint256 lastRewardTime; // Last reward time
        uint256 accTokenPerShare; // Accumulated token per share
        uint256 lpSupply; // LP token supply
    }

    /**
     * @notice Constructor
     * @param _pencilsProtocol Pencils Protocol address
     * @param _token Token address
     */
    constructor(address _pencilsProtocol, address _token) public {
        pencilsProtocol = _pencilsProtocol;
        token = _token;
    }

    /**
     * @notice Add a new pool
     * @param _allocPoint Allocation points
     * @param _lpToken LP token address
     */
    function addPool(uint256 _allocPoint, IERC20 _lpToken) public onlyOwner {
        require(address(_lpToken) != address(0), "FarmingSystem: lpToken cannot be zero");

        poolLength++;
        poolInfo[poolLength - 1] = PoolInfo({
            lpToken: _lpToken,
            allocPoint: _allocPoint,
            lastRewardTime: block.timestamp,
            accTokenPerShare: 0,
            lpSupply: 0
        });
    }

    /**
     * @notice Update a pool
     * @param _pid Pool ID
     * @param _allocPoint Allocation points
     */
    function updatePool(uint256 _pid, uint256 _allocPoint) public onlyOwner {
        require(_pid < poolLength, "FarmingSystem: pool not found");

        poolInfo[_pid].allocPoint = _allocPoint;
    }

    /**
     * @notice Deposit LP tokens
     * @param _pid Pool ID
     * @param _amount Amount to deposit
     */
    function deposit(uint256 _pid, uint256 _amount) public {
        require(_pid < poolLength, "FarmingSystem: pool not found");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update pool
        updatePool(_pid);

        // Transfer LP tokens
        pool.lpToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user information
        user.amount = user.amount.add(_amount);
        pool.lpSupply = pool.lpSupply.add(_amount);

        emit Deposit(msg.sender, _pid, _amount);
    }

    /**
     * @notice Withdraw LP tokens
     * @param _pid Pool ID
     * @param _amount Amount to withdraw
     */
    function withdraw(uint256 _pid, uint256 _amount) public {
        require(_pid < poolLength, "FarmingSystem: pool not found");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update pool
        updatePool(_pid);

        // Check user balance
        require(user.amount >= _amount, "FarmingSystem: insufficient balance");

        // Update user information
        user.amount = user.amount.sub(_amount);
        pool.lpSupply = pool.lpSupply.sub(_amount);

        // Transfer LP tokens
        pool.lpToken.safeTransfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    /**
     * @notice Harvest rewards
     * @param _pid Pool ID
     */
    function harvest(uint256 _pid) public {
        require(_pid < poolLength, "FarmingSystem: pool not found");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update pool
        updatePool(_pid);

        // Calculate rewards
        uint256 pending = user.amount.mul(pool.accTokenPerShare).div(1e18).sub(user.rewardDebt);

        // Update user information
        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e18);

        // Transfer rewards
        IERC20(token).safeTransfer(msg.sender, pending);

        emit Harvest(msg.sender, _pid, pending);
    }

    /**
     * @notice Update pool
     * @param _pid Pool ID
     */
    function updatePool(uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];

        // Update last reward time
        uint256 currentTime = block.timestamp;
        if (currentTime <= pool.lastRewardTime) {
            return;
        }

        // Calculate rewards
        uint256 lpSupply = pool.lpSupply;
        uint256 allocPoint = pool.allocPoint;
        uint256 tokenReward = IERC20(token).balanceOf(address(this)).mul(allocPoint).div(poolLength);

        // Update accumulated token per share
        pool.accTokenPerShare = pool.accTokenPerShare.add(tokenReward.mul(1e18).div(lpSupply));

        // Update last reward time
        pool.lastRewardTime = currentTime;
    }
}
```
