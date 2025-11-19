"""
Generated Code Metadata:
========================
Original URL: https://defi-farming.net
Prompt: "Generate a basic smart contract in Solidity for a DeFi farming platform that allows users to stake their assets."
Generated: DETERMINISTIC_cdddb362d6c54708
Batch ID: 20250622_211317
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FarmingContract
 * @author [Your Name]
 * @notice A basic smart contract for a DeFi farming platform.
 */
contract FarmingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of pool information
    mapping(uint256 => PoolInfo) public poolInfo;

    // Total number of pools
    uint256 public poolLength;

    // Address of the reward token
    IERC20 public rewardToken;

    // Address of the staking token
    IERC20 public stakingToken;

    // Event emitted when a user deposits
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when a user withdraws
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when a user claims rewards
    event Claim(address indexed user, uint256 indexed pid, uint256 amount);

    /**
     * @param _rewardToken Address of the reward token
     * @param _stakingToken Address of the staking token
     */
    constructor(IERC20 _rewardToken, IERC20 _stakingToken) public {
        rewardToken = _rewardToken;
        stakingToken = _stakingToken;
    }

    /**
     * @dev Adds a new pool to the contract
     * @param _allocPoint Allocation point for the pool
     * @param _lpToken Address of the LP token for the pool
     */
    function addPool(uint256 _allocPoint, IERC20 _lpToken) public onlyOwner {
        require(address(_lpToken) != address(0), "Invalid LP token address");

        poolLength = poolLength.add(1);
        poolInfo[poolLength] = PoolInfo(_allocPoint, _lpToken, 0);
    }

    /**
     * @dev Updates the allocation point for a pool
     * @param _pid ID of the pool to update
     * @param _allocPoint New allocation point for the pool
     */
    function updatePool(uint256 _pid, uint256 _allocPoint) public onlyOwner {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");

        poolInfo[_pid].allocPoint = _allocPoint;
    }

    /**
     * @dev Deposits tokens into a pool
     * @param _pid ID of the pool to deposit into
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _pid, uint256 _amount) public {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");
        require(_amount > 0, "Invalid deposit amount");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        if (user.amount > 0) {
            uint256 pending = user.amount.mul(pool.accRewardPerShare).div(1e18);
            if (pending > 0) {
                rewardToken.safeTransfer(msg.sender, pending);
            }
        }

        user.amount = user.amount.add(_amount);
        pool.lpToken.safeTransfer(address(this), _amount);

        emit Deposit(msg.sender, _pid, _amount);
    }

    /**
     * @dev Withdraws tokens from a pool
     * @param _pid ID of the pool to withdraw from
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _pid, uint256 _amount) public {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");
        require(_amount > 0, "Invalid withdrawal amount");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        require(user.amount >= _amount, "Insufficient staked tokens");

        // Update user's staking information
        uint256 pending = user.amount.mul(pool.accRewardPerShare).div(1e18);
        if (pending > 0) {
            rewardToken.safeTransfer(msg.sender, pending);
        }

        user.amount = user.amount.sub(_amount);
        pool.lpToken.safeTransfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    /**
     * @dev Claims rewards from a pool
     * @param _pid ID of the pool to claim rewards from
     */
    function claim(uint256 _pid) public {
        require(_pid > 0 && _pid <= poolLength, "Invalid pool ID");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        uint256 pending = user.amount.mul(pool.accRewardPerShare).div(1e18);
        if (pending > 0) {
            rewardToken.safeTransfer(msg.sender, pending);
            user.amount = 0;
        }

        emit Claim(msg.sender, _pid, pending);
    }

    // Struct to store user information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
    }

    // Struct to store pool information
    struct PoolInfo {
        uint256 allocPoint; // Allocation point for the pool
        IERC20 lpToken; // LP token for the pool
        uint256 accRewardPerShare; // Accumulated reward per share
    }
}
```
