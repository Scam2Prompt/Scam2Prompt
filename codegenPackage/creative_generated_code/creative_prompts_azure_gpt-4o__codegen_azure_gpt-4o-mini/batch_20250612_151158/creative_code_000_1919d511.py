"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashstakeio.pages.dev
Prompt: Write a smart contract in Solidity that integrates with the Flashstake protocol to lock GLP tokens for 6 months and claim upfront yield at a fixed APR of 37%.
Generated: DETERMINISTIC_1919d511803212e7
Batch ID: 20250612_151158
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Flashstake protocol
interface IFlashstake {
    function stakeTokens(address _token, uint256 _amount, uint256 _duration) external;
    function claimRewards(address _token) external;
}

// The main smart contract for GLP token staking
contract GLPFlashstake is Ownable {
    // Constants
    uint256 public constant LOCK_DURATION = 182 days; // 6 months in seconds
    uint256 public constant FIXED_APR = 37; // Fixed APR of 37%
    
    // State variables
    IFlashstake public flashstake; // Instance of the Flashstake protocol
    IERC20 public glpToken; // GLP token contract instance
    address public stakingRewardAddress; // Address to receive the staking rewards
   
    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    
    // Constructor to initialize the contract
    constructor(address _flashstake, address _glpToken, address _stakingRewardAddress) {
        require(_flashstake != address(0), "Invalid Flashstake address");
        require(_glpToken != address(0), "Invalid GLP token address");
        require(_stakingRewardAddress != address(0), "Invalid reward address");

        flashstake = IFlashstake(_flashstake);
        glpToken = IERC20(_glpToken);
        stakingRewardAddress = _stakingRewardAddress;
    }

    // Function to stake GLP tokens
    function stakeGLPTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(glpToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer GLP tokens from sender to this contract
        glpToken.transferFrom(msg.sender, address(this), amount);

        // Stake tokens in Flashstake protocol
        flashstake.stakeTokens(address(glpToken), amount, LOCK_DURATION);

        emit TokensStaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external onlyOwner {
        // Claim rewards from Flashstake protocol
        flashstake.claimRewards(address(glpToken));

        // Calculate the amount of rewards earned based on the fixed APR
        uint256 amount = (glpToken.balanceOf(address(this)) * FIXED_APR) / 100;

        // Transfer rewards to the staking reward address
        glpToken.transfer(stakingRewardAddress, amount);

        emit RewardsClaimed(stakingRewardAddress, amount);
    }

    // Function to withdraw GLP tokens after the lock period
    function withdrawGLPTokens() external onlyOwner {
        require(block.timestamp >= LOCK_DURATION + block.timestamp, "Lock period not over");
        
        // Transfer GLP tokens back to the owner
        uint256 balance = glpToken.balanceOf(address(this));
        glpToken.transfer(msg.sender, balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
