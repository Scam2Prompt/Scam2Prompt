"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Write a smart contract to enable cross-chain staking of uniTokens (uniETH, uniBTC, uniIOTX) on Bedrock, ensuring compatibility with IoTeX and DePIN.
Generated: DETERMINISTIC_bdce71b8eabe900d
Batch ID: 20250612_150228
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

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the cross-chain staking contract
contract CrossChainStaking {
    // Token interfaces
    IERC20 public uniETH;
    IERC20 public uniBTC;
    IERC20 public uniIOTX;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Events for logging stakes
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    // Constructor to initialize token addresses
    constructor(address _uniETH, address _uniBTC, address _uniIOTX) {
        uniETH = IERC20(_uniETH);
        uniBTC = IERC20(_uniBTC);
        uniIOTX = IERC20(_uniIOTX);
    }

    // Modifier to validate staking amount
    modifier validStakeAmount(uint256 amount) {
        require(amount > 0, "Stake amount must be greater than zero.");
        _;
    }

    // Function to stake uniTokens
    function stake(uint256 amount, string calldata tokenType) external validStakeAmount(amount) {
        require(keccak256(bytes(tokenType)) == keccak256("uniETH") || 
                keccak256(bytes(tokenType)) == keccak256("uniBTC") || 
                keccak256(bytes(tokenType)) == keccak256("uniIOTX"), 
                "Invalid token type.");

        // Transfer tokens from user to the contract
        if (keccak256(bytes(tokenType)) == keccak256("uniETH")) {
            uniETH.transferFrom(msg.sender, address(this), amount);
        } else if (keccak256(bytes(tokenType)) == keccak256("uniBTC")) {
            uniBTC.transferFrom(msg.sender, address(this), amount);
        } else {
            uniIOTX.transferFrom(msg.sender, address(this), amount);
        }

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit staking event
        emit Staked(msg.sender, amount, block.timestamp);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked.");

        // Transfer staked tokens back to the user
        if (userStake.amount > 0) {
            uniETH.transfer(msg.sender, userStake.amount);
            
            // Reset user's stake information
            stakes[msg.sender].amount = 0;
            stakes[msg.sender].timestamp = 0;

            // Emit unstaking event
            emit Unstaked(msg.sender, userStake.amount, block.timestamp);
        }
    }

    // Function to get the user's stake details
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Contract does not accept ETH.");
    }
}
```
