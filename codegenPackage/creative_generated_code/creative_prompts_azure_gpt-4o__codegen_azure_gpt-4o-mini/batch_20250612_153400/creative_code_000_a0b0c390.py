"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omnigenesis.vercel.app
Prompt: Write a smart contract that utilizes Omni Network's restaking mechanism to securely integrate multiple Ethereum rollups into a unified application.
Generated: DETERMINISTIC_a0b0c39082de2b40
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required interfaces for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// OmniNetwork restaking contract
contract OmniRestaking is Ownable {
    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Struct to hold rollup information
    struct Rollup {
        string name;        // Name of the rollup
        address rollupAddress; // Address of the rollup contract
        uint256 stakedAmount;  // Amount of tokens staked
    }

    // Mapping to store rollups
    mapping(address => Rollup) public rollups;
    address[] public rollupAddresses; // Array to keep track of rollup addresses

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, address indexed rollupAddress);
    
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount, address indexed rollupAddress);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to add a new rollup
    function addRollup(string memory _name, address _rollupAddress) external onlyOwner {
        require(_rollupAddress != address(0), "Invalid address");
        require(rollups[_rollupAddress].rollupAddress == address(0), "Rollup already exists");

        rollups[_rollupAddress] = Rollup({
            name: _name,
            rollupAddress: _rollupAddress,
            stakedAmount: 0
        });

        rollupAddresses.push(_rollupAddress);
    }

    // Function to stake tokens to a specific rollup
    function stake(uint256 amount, address rollupAddress) external {
        require(rollupAddress != address(0), "Invalid rollup address");
        require(rollups[rollupAddress].rollupAddress != address(0), "Rollup does not exist");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amount for the rollup
        rollups[rollupAddress].stakedAmount += amount;

        emit Staked(msg.sender, amount, rollupAddress);
    }

    // Function to unstake tokens from a specific rollup
    function unstake(uint256 amount, address rollupAddress) external {
        require(rollupAddress != address(0), "Invalid rollup address");
        require(rollups[rollupAddress].rollupAddress != address(0), "Rollup does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(rollups[rollupAddress].stakedAmount >= amount, "Insufficient staked amount");

        // Update staked amount for the rollup
        rollups[rollupAddress].stakedAmount -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount, rollupAddress);
    }

    // Function to retrieve all rollup addresses
    function getAllRollups() external view returns (address[] memory) {
        return rollupAddresses;
    }

    // Function to get staked amount for a specific rollup
    function getStakedAmount(address rollupAddress) external view returns (uint256) {
        return rollups[rollupAddress].stakedAmount;
    }
}
```
