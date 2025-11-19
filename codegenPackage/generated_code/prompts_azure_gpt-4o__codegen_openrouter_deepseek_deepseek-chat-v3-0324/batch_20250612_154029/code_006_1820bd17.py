"""
Generated Code Metadata:
========================
Original URL: https://btfd-bonus.ink
Prompt: Provide a step-by-step guide to deploying an ERC20 token on the Ethereum network with features like liquidity locking for 2 years and vesting schedules for staking rewards and influencer allocations, as described in BTFD's tokenomics.
Generated: DETERMINISTIC_1820bd17b611e2bd
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a production-ready Solidity smart contract for an ERC20 token with liquidity locking and vesting schedules. The code includes comments and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BTFD Token
 * @dev ERC20 token with liquidity locking and vesting schedules
 */
contract BTFDToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Liquidity lock parameters
    address public liquidityLocker;
    uint256 public liquidityLockAmount;
    uint256 public liquidityLockEndTime;

    // Vesting parameters
    struct VestingSchedule {
        uint256 totalAmount;
        uint256 releasedAmount;
        uint256 startTime;
        uint256 duration;
        uint256 cliff;
    }

    mapping(address => VestingSchedule) public vestingSchedules;

    // Events
    event LiquidityLocked(address indexed locker, uint256 amount, uint256 unlockTime);
    event VestingScheduleCreated(address indexed beneficiary, uint256 amount, uint256 startTime, uint256 duration, uint256 cliff);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor that mints the initial supply
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) ERC20("BTFD Token", "BTFD") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Lock liquidity tokens for 2 years
     * @param locker Address of the liquidity locker
     * @param amount Amount of tokens to lock
     */
    function lockLiquidity(address locker, uint256 amount) external onlyOwner {
        require(locker != address(0), "Invalid locker address");
        require(amount > 0 && amount <= balanceOf(msg.sender), "Invalid amount");

        liquidityLocker = locker;
        liquidityLockAmount = amount;
        liquidityLockEndTime = block.timestamp + 730 days; // 2 years

        _transfer(msg.sender, locker, amount);
        emit LiquidityLocked(locker, amount, liquidityLockEndTime);
    }

    /**
     * @dev Create a vesting schedule for staking rewards or influencer allocations
     * @param beneficiary Address of the beneficiary
     * @param amount Total amount of tokens to vest
     * @param startTime When vesting starts (unix timestamp)
     * @param duration Duration of vesting in seconds
     * @param cliff Cliff period in seconds
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 startTime,
        uint256 duration,
        uint256 cliff
    ) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Amount must be positive");
        require(startTime >= block.timestamp, "Start time must be in future");
        require(duration > 0, "Duration must be positive");
        require(cliff <= duration, "Cliff must be less than duration");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: amount,
            releasedAmount: 0,
            startTime: startTime,
            duration: duration,
            cliff: cliff
        });

        _transfer(msg.sender, address(this), amount);
        emit VestingScheduleCreated(beneficiary, amount, startTime, duration, cliff);
    }

    /**
     * @dev Release vested tokens to beneficiary
     */
    function releaseVestedTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule found");

        uint256 unreleased = releasableAmount(msg.sender);
        require(unreleased > 0, "No tokens to release");

        schedule.releasedAmount = schedule.releasedAmount.add(unreleased);
        _transfer(address(this), msg.sender, unreleased);
        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculate the releasable amount of tokens
     * @param beneficiary Address of the beneficiary
     * @return Amount of tokens that can be released
     */
    function releasableAmount(address beneficiary) public view returns (uint256) {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        return vestedAmount(beneficiary).sub(schedule.releasedAmount);
    }

    /**
     * @dev Calculate the vested amount of tokens
     * @param beneficiary Address of the beneficiary
     * @return Amount of tokens that have vested
     */
    function vestedAmount(address beneficiary) public view returns (uint256) {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        if (block.timestamp < schedule.startTime.add(schedule.cliff)) {
            return 0;
        } else if (block.timestamp >= schedule.startTime.add(schedule.duration)) {
            return schedule.totalAmount;
        } else {
            return schedule.totalAmount.mul(block.timestamp.sub(schedule.startTime)).div(schedule.duration);
        }
    }

    /**
     * @dev Override transfer to prevent locked liquidity from being transferred
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (msg.sender == liquidityLocker && block.timestamp < liquidityLockEndTime) {
            require(balanceOf(msg.sender).sub(amount) >= liquidityLockAmount, "Cannot transfer locked liquidity");
        }
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override transferFrom to prevent locked liquidity from being transferred
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        if (sender == liquidityLocker && block.timestamp < liquidityLockEndTime) {
            require(balanceOf(sender).sub(amount) >= liquidityLockAmount, "Cannot transfer locked liquidity");
        }
        return super.transferFrom(sender, recipient, amount);
    }
}
```

To deploy this contract, you would typically:

1. Compile the contract using a tool like Hardhat or Truffle
2. Deploy to the Ethereum network (mainnet or testnet)
3. Call the `lockLiquidity` function to lock the liquidity tokens
4. Create vesting schedules using `createVestingSchedule` for staking rewards and influencer allocations
5. Beneficiaries can claim their vested tokens by calling `releaseVestedTokens`

The contract includes all the requested features:
- ERC20 token functionality
- Liquidity locking for 2 years
- Vesting schedules with customizable parameters
- Proper access control
- Safe math operations
- Event logging
- Transfer restrictions for locked liquidity
