"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shidocoin.pages.dev
Prompt: Generate a Solidity smart contract that utilizes the Shido Network's Proof-of-Stake mechanism for staking $SHIDO tokens.
Generated: DETERMINISTIC_6a00ecfc915f7df0
Batch ID: 20250612_160306
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Shido Token
interface IShidoToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for $SHIDO tokens
contract ShidoStaking is Ownable {
    // Shido token contract instance
    IShidoToken public shidoToken;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Timestamp of when the tokens were staked
    }

    // Mapping of staker address to their stake
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the SHIDO token address
    constructor(address _shidoToken) {
        require(_shidoToken != address(0), "Invalid token address");
        shidoToken = IShidoToken(_shidoToken);
    }

    // Function to stake $SHIDO tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(shidoToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the stake for the user
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake $SHIDO tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");
        
        // Update the stake for the user
        stakes[msg.sender].amount -= _amount;

        // Transfer the tokens back to the user
        require(shidoToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to view staked amount of a user
    function viewStake(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to view the staking timestamp of a user
    function viewStakingTimestamp(address _user) external view returns (uint256) {
        return stakes[_user].timestamp;
    }

    // Owner can withdraw tokens in case of emergencies
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(shidoToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
