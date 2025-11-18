"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-cookie.online
Prompt: Generate code for a decentralized application (dApp) that allows users to manage vesting schedules through wallet connection, inspired by the Cookie DAO vesting portal.
Generated: DETERMINISTIC_d5194e8e34243b95
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Solidity Smart Contract for Vesting Schedules
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title VestingContract
 * @dev A decentralized contract for creating and managing vesting schedules.
 * Users can create vesting schedules for tokens they wish to distribute.
 */
contract VestingContract {
    struct VestingSchedule {
        address beneficiary; // Address receiving the tokens
        uint256 start;       // Start time of the vesting
        uint256 duration;    // Duration in seconds
        uint256 amount;      // Total amount scheduled
        uint256 released;    // Amount already released
    }

    mapping(address => VestingSchedule[]) public schedules; // Map wallets to their vesting schedules
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    event VestingScheduleCreated(
        address indexed creator,
        address indexed beneficiary,
        uint256 amount,
        uint256 start,
        uint256 duration
    );
    event TokensReleased(
        address indexed beneficiary,
        uint256 amount
    );

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new vesting schedule.
     * @param beneficiary Address to receive tokens.
     * @param start Start time of the vesting schedule.
     * @param duration Duration of the vesting schedule.
     * @param amount Total amount of tokens to vest.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 start,
        uint256 duration,
        uint256 amount
    ) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        VestingSchedule memory schedule = VestingSchedule({
            beneficiary: beneficiary,
            start: start,
            duration: duration,
            amount: amount,
            released: 0
        });

        schedules[beneficiary].push(schedule);

        emit VestingScheduleCreated(msg.sender, beneficiary, amount, start, duration);
    }

    /**
     * @dev Release vested tokens for a specific schedule.
     * @param scheduleIndex Index of the vesting schedule in the beneficiary's list.
     */
    function release(uint256 scheduleIndex) external {
        VestingSchedule storage schedule = schedules[msg.sender][scheduleIndex];
        require(schedule.beneficiary == msg.sender, "You are not the beneficiary");
        require(block.timestamp >= schedule.start, "Vesting has not started yet");

        uint256 vestedAmount = _calculateVestedAmount(schedule);
        uint256 releasableAmount = vestedAmount - schedule.released;
        require(releasableAmount > 0, "No tokens to release");

        schedule.released += releasableAmount;

        // Transfer tokens here (mocked for simplicity)
        // ERC20(tokenAddress).transfer(schedule.beneficiary, releasableAmount);

        emit TokensReleased(schedule.beneficiary, releasableAmount);
    }

    /**
     * @dev Calculate the vested amount for a vesting schedule.
     * @param schedule The vesting schedule.
     * @return Vested amount.
     */
    function _calculateVestedAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp - schedule.start;
        if (elapsedTime >= schedule.duration) {
            return schedule.amount;
        }

        return (schedule.amount * elapsedTime) / schedule.duration;
    }

    /**
     * @dev Get the number of vesting schedules for a beneficiary.
     * @param beneficiary Address to check schedules for.
     * @return Number of schedules.
     */
    function getVestingScheduleCount(address beneficiary) external view returns (uint256) {
        return schedules[beneficiary].length;
    }
}

// Frontend Wallet Connection and Interaction (JavaScript)
import Web3 from 'web3';

async function connectWallet() {
    if (window.ethereum) {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            const walletAddress = accounts[0];
            console.log(`Connected wallet: ${walletAddress}`);
            return walletAddress;
        } catch (error) {
            console.error("Error connecting wallet:", error);
            throw new Error("Wallet connection failed");
        }
    } else {
        alert("Please install MetaMask to use this DApp");
        throw new Error("MetaMask not detected");
    }
}

async function createVestingSchedule(contractAddress, abi, beneficiary, start, duration, amount) {
    const web3 = new Web3(window.ethereum);
    const walletAddress = await connectWallet();
    const contract = new web3.eth.Contract(abi, contractAddress);

    try {
        const result = await contract.methods
            .createVestingSchedule(beneficiary, start, duration, amount)
            .send({ from: walletAddress });
        console.log("Vesting schedule created:", result);
    } catch (error) {
        console.error("Error creating vesting schedule:", error);
        throw new Error("Failed to create vesting schedule");
    }
}

async function releaseTokens(contractAddress, abi, scheduleIndex) {
    const web3 = new Web3(window.ethereum);
    const walletAddress = await connectWallet();
    const contract = new web3.eth.Contract(abi, contractAddress);

    try {
        const result = await contract.methods
            .release(scheduleIndex)
            .send({ from: walletAddress });
        console.log("Tokens released:", result);
    } catch (error) {
        console.error("Error releasing tokens:", error);
        throw new Error("Failed to release tokens");
    }
}
```

Note: The Solidity contract assumes a token transfer mechanism is mocked in the release function for simplicity. For production, integrate an ERC20 token interface for actual transfers. Similarly, the JavaScript frontend assumes MetaMask is used for wallet interaction. Ensure all addresses and ABI are properly managed and secured in production.
