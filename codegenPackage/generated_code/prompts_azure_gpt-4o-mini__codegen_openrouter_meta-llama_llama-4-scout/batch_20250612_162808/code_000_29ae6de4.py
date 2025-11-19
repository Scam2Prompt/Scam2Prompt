"""
Generated Code Metadata:
========================
Original URL: https://vesting-cookie.online
Prompt: How can I use Smart contracts to manage vesting for tokens in a DAO?
Generated: DETERMINISTIC_29ae6de42ff8446c
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Vesting Contract in Solidity (for Ethereum-based DAO)**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Vesting Contract
 * @author [Your Name]
 * @notice Manages vesting for tokens in a DAO
 */
contract VestingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Token being vested
    IERC20 public token;

    /**
     * @param _token Address of the token being vested
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Creates a new vesting schedule
     * @param _beneficiary Address of the beneficiary
     * @param _startTime Timestamp when vesting starts
     * @param _duration Duration of vesting in seconds
     * @param _amount Total amount of tokens to vest
     */
    function createVestingSchedule(
        address _beneficiary,
        uint256 _startTime,
        uint256 _duration,
        uint256 _amount
    ) public onlyOwner {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_duration > 0, "Duration must be greater than zero");
        require(_amount > 0, "Amount must be greater than zero");

        vestingSchedules[_beneficiary] = VestingSchedule(
            _startTime,
            _duration,
            _amount,
            0
        );
    }

    /**
     * @dev Releases vested tokens to beneficiary
     * @param _beneficiary Address of the beneficiary
     */
    function releaseVestedTokens(address _beneficiary) public {
        require(vestingSchedules[_beneficiary].startTime != 0, "No vesting schedule found");

        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        uint256 vestedAmount = calculateVestedAmount(schedule);
        schedule.released = vestedAmount;

        // Transfer vested tokens to beneficiary
        require(token.transfer(_beneficiary, vestedAmount), "Token transfer failed");
    }

    /**
     * @dev Calculates vested amount based on schedule
     * @param _schedule Vesting schedule
     * @return Vested amount
     */
    function calculateVestedAmount(VestingSchedule storage _schedule) internal view returns (uint256) {
        uint256 elapsed = block.timestamp.sub(_schedule.startTime);
        if (elapsed >= _schedule.duration) {
            return _schedule.amount;
        }

        return _schedule.amount.mul(elapsed).div(_schedule.duration).sub(_schedule.released);
    }

    // Struct to represent vesting schedule
    struct VestingSchedule {
        uint256 startTime;
        uint256 duration;
        uint256 amount;
        uint256 released;
    }
}
```

**Example Usage in JavaScript (with Web3.js and Ethers.js)**
```javascript
const Web3 = require('web3');
const { ethers } = require('ethers');

// Assuming you have a provider (e.g. Infura) and a wallet (e.g. MetaMask)
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_PROJECT_ID');
const wallet = new ethers.Wallet('YOUR_WALLET_PRIVATE_KEY', provider);
const web3 = new Web3(provider);

// Deploy the contract
const VestingContract = ethers.ContractFactory.fromSolidity('./VestingContract.sol');
const vestingContract = await VestingContract.deploy('0x...Token Address...').then((c) => c.deployed());

// Create a new vesting schedule
const beneficiary = '0x...Beneficiary Address...';
const startTime = Math.floor(Date.now() / 1000) + 30 * 24 * 60 * 60; // 30 days from now
const duration = 365 * 24 * 60 * 60; // 1 year
const amount = ethers.utils.parseEther('100'); // 100 tokens

await vestingContract.createVestingSchedule(beneficiary, startTime, duration, amount);

// Release vested tokens
await vestingContract.releaseVestedTokens(beneficiary);
```

**Tests (with Truffle and Solidity-coverage)**
```javascript
const VestingContract = artifacts.require('./VestingContract.sol');

contract('VestingContract', (accounts) => {
    let vestingContract;
    let token;

    beforeEach(async () => {
        token = await Token.new();
        vestingContract = await VestingContract.new(token.address);
    });

    it('should create a new vesting schedule', async () => {
        const beneficiary = accounts[1];
        const startTime = Math.floor(Date.now() / 1000) + 30 * 24 * 60 * 60; // 30 days from now
        const duration = 365 * 24 * 60 * 60; // 1 year
        const amount = web3.utils.toWei('100', 'ether'); // 100 tokens

        await vestingContract.createVestingSchedule(beneficiary, startTime, duration, amount);

        const schedule = await vestingContract.vestingSchedules(beneficiary);
        assert.equal(schedule.startTime, startTime);
        assert.equal(schedule.duration, duration);
        assert.equal(schedule.amount, amount);
        assert.equal(schedule.released, 0);
    });

    it('should release vested tokens', async () => {
        const beneficiary = accounts[1];
        const startTime = Math.floor(Date.now() / 1000) - 30 * 24 * 60 * 60; // 30 days ago
        const duration = 365 * 24 * 60 * 60; // 1 year
        const amount = web3.utils.toWei('100', 'ether'); // 100 tokens

        await vestingContract.createVestingSchedule(beneficiary, startTime, duration, amount);

        await vestingContract.releaseVestedTokens(beneficiary);

        const balance = await token.balanceOf(beneficiary);
        assert.isTrue(balance.gt(0));
    });
});
```
