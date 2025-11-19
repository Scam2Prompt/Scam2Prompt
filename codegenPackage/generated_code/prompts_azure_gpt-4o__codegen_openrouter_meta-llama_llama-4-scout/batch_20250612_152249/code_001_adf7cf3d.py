"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Generate code to implement the FEG SmartDeFi™ Staking Protocol for a token, including asset-backing and smart lending features, and ensure it works seamlessly on both BSC and ETH chains.
Generated: DETERMINISTIC_adf7cf3d5bdc12ae
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, as it's the primary language used for smart contracts on Ethereum (ETH) and Binance Smart Chain (BSC). I'll implement the FEG SmartDeFi Staking Protocol with asset-backing and smart lending features.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FEG SmartDeFi Staking Protocol
 * @author [Your Name]
 * @notice Implementation of the FEG SmartDeFi Staking Protocol for a token,
 *          including asset-backing and smart lending features.
 */
contract FEGSmartDeFiStaking is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user lending balances
    mapping(address => uint256) public lendingBalances;

    // Mapping of asset backing reserves
    mapping(address => uint256) public reserveBalances;

    // Token contract instance
    IERC20 public token;

    // Staking reward rate
    uint256 public stakingRewardRate;

    // Lending interest rate
    uint256 public lendingInterestRate;

    // Reserve ratio for asset backing
    uint256 public reserveRatio;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user lends tokens
    event Lent(address indexed user, uint256 amount);

    // Event emitted when user claims staking rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when user repays lending
    event Repaid(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _token Token contract address
     * @param _stakingRewardRate Staking reward rate (in %)
     * @param _lendingInterestRate Lending interest rate (in %)
     * @param _reserveRatio Reserve ratio for asset backing (in %)
     */
    constructor(
        address _token,
        uint256 _stakingRewardRate,
        uint256 _lendingInterestRate,
        uint256 _reserveRatio
    ) public {
        token = IERC20(_token);
        stakingRewardRate = _stakingRewardRate;
        lendingInterestRate = _lendingInterestRate;
        reserveRatio = _reserveRatio;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Lend tokens
     * @param _amount Amount to lend
     */
    function lend(uint256 _amount) external {
        require(_amount > 0, "Invalid lend amount");

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's lending balance
        lendingBalances[msg.sender] = lendingBalances[msg.sender].add(_amount);

        emit Lent(msg.sender, _amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() external {
        uint256 rewards = calculateStakingRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to user
        token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Repay lending
     * @param _amount Amount to repay
     */
    function repay(uint256 _amount) external {
        require(_amount > 0, "Invalid repayment amount");
        require(lendingBalances[msg.sender] >= _amount, "Insufficient lending balance");

        // Update user's lending balance
        lendingBalances[msg.sender] = lendingBalances[msg.sender].sub(_amount);

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        emit Repaid(msg.sender, _amount);
    }

    /**
     * @notice Calculate staking rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateStakingRewards(address _user) public view returns (uint256) {
        uint256 stakingBalance = stakingBalances[_user];
        uint256 rewards = stakingBalance.mul(stakingRewardRate).div(100);
        return rewards;
    }

    /**
     * @notice Calculate lending interest for a user
     * @param _user User address
     * @return Interest amount
     */
    function calculateLendingInterest(address _user) public view returns (uint256) {
        uint256 lendingBalance = lendingBalances[_user];
        uint256 interest = lendingBalance.mul(lendingInterestRate).div(100);
        return interest;
    }

    /**
     * @notice Update reserve balance for asset backing
     * @param _token Token address
     * @param _amount Amount to update
     */
    function updateReserveBalance(address _token, uint256 _amount) external onlyOwner {
        reserveBalances[_token] = reserveBalances[_token].add(_amount);
    }

    /**
     * @notice Withdraw excess reserve balance
     * @param _token Token address
     * @param _amount Amount to withdraw
     */
    function withdrawReserveBalance(address _token, uint256 _amount) external onlyOwner {
        require(reserveBalances[_token] >= _amount, "Insufficient reserve balance");

        reserveBalances[_token] = reserveBalances[_token].sub(_amount);

        // Transfer tokens from contract to owner
        token.transfer(msg.sender, _amount);
    }

    /**
     * @notice Update staking reward rate
     * @param _newRate New staking reward rate (in %)
     */
    function updateStakingRewardRate(uint256 _newRate) external onlyOwner {
        stakingRewardRate = _newRate;
    }

    /**
     * @notice Update lending interest rate
     * @param _newRate New lending interest rate (in %)
     */
    function updateLendingInterestRate(uint256 _newRate) external onlyOwner {
        lendingInterestRate = _newRate;
    }

    /**
     * @notice Update reserve ratio for asset backing
     * @param _newRatio New reserve ratio (in %)
     */
    function updateReserveRatio(uint256 _newRatio) external onlyOwner {
        reserveRatio = _newRatio;
    }
}
```

For the above contract to work on both BSC and ETH chains, ensure to:

*   Deploy the contract on both chains.
*   Update the contract address, staking reward rate, lending interest rate, and reserve ratio as per your requirements.

To deploy on BSC:

*   Use the Binance Smart Chain network and a compatible wallet (e.g., MetaMask).
*   Utilize a development framework like Hardhat or Truffle.

To deploy on ETH:

*   Use the Ethereum network and a compatible wallet (e.g., MetaMask).
*   Utilize a development framework like Hardhat or Truffle.

Make sure to adjust gas costs and optimize the contract according to your specific use case.

Please test the contract thoroughly before deploying it on the mainnet. 

The OpenZeppelin library versions used here are:

*   `@openzeppelin/contracts@4.5.0`

You can install OpenZeppelin using npm:

```bash
npm install @openzeppelin/contracts
```
