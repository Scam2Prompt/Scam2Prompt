"""
Generated Code Metadata:
========================
Original URL: https://etherfi-app.github.io
Prompt: Generate a Solidity contract for a yield farming system that distributes rewards based on liquidity contributions, inspired by Ether Fi's staking and farming features.
Generated: DETERMINISTIC_1727d35989f33c54
Batch ID: 20250612_153526
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
 * @title YieldFarmingContract
 * @author [Your Name]
 * @notice A yield farming contract that distributes rewards based on liquidity contributions.
 */
contract YieldFarmingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of token to its reward per block
    mapping(address => uint256) public rewardPerBlocks;

    // Mapping of token to its last reward block
    mapping(address => uint256) public lastRewardBlocks;

    // Mapping of token to its total liquidity
    mapping(address => uint256) public totalLiquidity;

    // Mapping of token to its reward token
    mapping(address => address) public rewardTokens;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Struct to hold staker information
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt
    }

    // List of supported tokens
    address[] public supportedTokens;

    /**
     * @notice Constructor
     * @param _rewardTokens List of reward tokens
     */
    constructor(address[] memory _rewardTokens) public {
        for (uint256 i = 0; i < _rewardTokens.length; i++) {
            rewardTokens[_rewardTokens[i]] = _rewardTokens[i];
        }
    }

    /**
     * @notice Adds a new token to the supported tokens list
     * @param _token Token to add
     * @param _rewardPerBlock Reward per block for the token
     */
    function addToken(address _token, uint256 _rewardPerBlock) public onlyOwner {
        require(!isSupportedToken(_token), "Token already supported");
        supportedTokens.push(_token);
        rewardPerBlocks[_token] = _rewardPerBlock;
        lastRewardBlocks[_token] = block.number;
    }

    /**
     * @notice Removes a token from the supported tokens list
     * @param _token Token to remove
     */
    function removeToken(address _token) public onlyOwner {
        require(isSupportedToken(_token), "Token not supported");
        // Find and remove the token from the list
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            if (supportedTokens[i] == _token) {
                supportedTokens[i] = supportedTokens[supportedTokens.length - 1];
                supportedTokens.pop();
                break;
            }
        }
    }

    /**
     * @notice Checks if a token is supported
     * @param _token Token to check
     * @return bool True if supported, false otherwise
     */
    function isSupportedToken(address _token) public view returns (bool) {
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            if (supportedTokens[i] == _token) {
                return true;
            }
        }
        return false;
    }

    /**
     * @notice Stakes a token
     * @param _token Token to stake
     * @param _amount Amount to stake
     */
    function stake(address _token, uint256 _amount) public {
        require(isSupportedToken(_token), "Token not supported");
        require(_amount > 0, "Amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        if (staker.amount > 0) {
            _distributeRewards(_token, msg.sender);
        }

        staker.amount = staker.amount.add(_amount);
        staker.rewardDebt = staker.rewardDebt.add(_amount);

        totalLiquidity[_token] = totalLiquidity[_token].add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstakes a token
     * @param _token Token to unstake
     * @param _amount Amount to unstake
     */
    function unstake(address _token, uint256 _amount) public {
        require(isSupportedToken(_token), "Token not supported");
        require(_amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amount >= _amount, "Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];

        _distributeRewards(_token, msg.sender);

        staker.amount = staker.amount.sub(_amount);
        staker.rewardDebt = staker.rewardDebt.sub(_amount);

        totalLiquidity[_token] = totalLiquidity[_token].sub(_amount);

        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distributes rewards to a user
     * @param _token Token to distribute rewards for
     * @param _user User to distribute rewards to
     */
    function _distributeRewards(address _token, address _user) internal {
        Staker storage staker = stakers[_user];

        uint256 accRewardPerShare = rewardPerBlocks[_token].mul(block.number.sub(lastRewardBlocks[_token])).div(totalLiquidity[_token]);

        staker.rewardDebt = staker.amount.mul(accRewardPerShare);

        uint256 reward = staker.amount.mul(accRewardPerShare).sub(staker.rewardDebt);

        if (reward > 0) {
            IERC20(rewardTokens[_token]).safeTransfer(_user, reward);

            emit RewardsDistributed(_user, reward);
        }

        lastRewardBlocks[_token] = block.number;
    }

    /**
     * @notice Updates the reward per block for a token
     * @param _token Token to update
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(address _token, uint256 _newRewardPerBlock) public onlyOwner {
        require(isSupportedToken(_token), "Token not supported");

        _distributeRewards(_token, address(0));

        rewardPerBlocks[_token] = _newRewardPerBlock;
    }
}
```
