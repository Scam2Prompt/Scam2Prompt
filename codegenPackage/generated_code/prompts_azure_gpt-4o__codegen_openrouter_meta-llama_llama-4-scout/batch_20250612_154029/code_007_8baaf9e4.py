"""
Generated Code Metadata:
========================
Original URL: https://pepe-tokens.com
Prompt: Create a tutorial for building a PepeFarm-like staking system using Solidity, ensuring compatibility with the zero-tax tokenomics of $PEPE.
Generated: DETERMINISTIC_8baaf9e45e26b5a5
Batch ID: 20250612_154029
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
 * @title PepeFarm Staking System
 * @author [Your Name]
 * @notice A staking system inspired by PepeFarm, compatible with $PEPE's zero-tax tokenomics.
 */
contract PepeFarmStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of pool information
    mapping(uint256 => PoolInfo) public poolInfo;

    // Total number of pools
    uint256 public poolLength;

    // $PEPE token contract
    address public pepeToken;

    // Event emitted when a user deposits tokens
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when a user claims rewards
    event Claim(address indexed user, uint256 indexed pid, uint256 amount);

    // Struct to store user information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt
    }

    // Struct to store pool information
    struct PoolInfo {
        address token; // Token address
        uint256 allocPoint; // Allocation points
        uint256 lastRewardTime; // Last reward time
        uint256 accTokenPerShare; // Accumulated token per share
    }

    /**
     * @notice Initializes the PepeFarm staking system
     * @param _pepeToken $PEPE token contract address
     */
    constructor(address _pepeToken) {
        pepeToken = _pepeToken;
    }

    /**
     * @notice Adds a new pool to the system
     * @param _token Token address
     * @param _allocPoint Allocation points
     */
    function addPool(address _token, uint256 _allocPoint) public onlyOwner {
        require(_token != address(0), "Invalid token address");

        poolLength++;
        poolInfo[poolLength] = PoolInfo({
            token: _token,
            allocPoint: _allocPoint,
            lastRewardTime: block.timestamp,
            accTokenPerShare: 0
        });
    }

    /**
     * @notice Sets the allocation points for a pool
     * @param _pid Pool ID
     * @param _allocPoint New allocation points
     */
    function setPoolAllocPoint(uint256 _pid, uint256 _allocPoint) public onlyOwner {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");

        poolInfo[_pid].allocPoint = _allocPoint;
    }

    /**
     * @notice Deposits tokens into a pool
     * @param _pid Pool ID
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _pid, uint256 _amount) public nonReentrant {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");
        require(_amount > 0, "Invalid deposit amount");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update reward
        updatePool(_pid);

        // Transfer tokens from user to pool
        ERC20(pool.token).transferFrom(msg.sender, address(this), _amount);

        // Update user information
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.rewardDebt.add(_amount.mul(pool.accTokenPerShare).div(1e12));

        emit Deposit(msg.sender, _pid, _amount);
    }

    /**
     * @notice Withdraws tokens from a pool
     * @param _pid Pool ID
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _pid, uint256 _amount) public nonReentrant {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");
        require(_amount > 0, "Invalid withdrawal amount");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update reward
        updatePool(_pid);

        // Check if user has sufficient balance
        require(user.amount >= _amount, "Insufficient balance");

        // Update user information
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt.sub(_amount.mul(pool.accTokenPerShare).div(1e12));

        // Transfer tokens from pool to user
        ERC20(pool.token).transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    /**
     * @notice Claims rewards from a pool
     * @param _pid Pool ID
     */
    function claim(uint256 _pid) public nonReentrant {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update reward
        updatePool(_pid);

        // Calculate reward
        uint256 reward = user.amount.mul(pool.accTokenPerShare).div(1e12).sub(user.rewardDebt);

        // Update user information
        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e12);

        // Transfer reward to user
        ERC20(pepeToken).transfer(msg.sender, reward);

        emit Claim(msg.sender, _pid, reward);
    }

    /**
     * @notice Updates the pool reward
     * @param _pid Pool ID
     */
    function updatePool(uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];

        // Calculate reward
        uint256 reward = pool.allocPoint.mul(block.timestamp.sub(pool.lastRewardTime)).mul(1e12);

        // Update pool information
        pool.accTokenPerShare = pool.accTokenPerShare.add(reward.div(poolLength));
        pool.lastRewardTime = block.timestamp;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Access denied");
        _;
    }

    // Get the owner address
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
