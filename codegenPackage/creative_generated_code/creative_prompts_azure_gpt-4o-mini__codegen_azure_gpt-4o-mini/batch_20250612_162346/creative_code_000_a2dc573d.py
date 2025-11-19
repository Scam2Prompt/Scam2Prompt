"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelpdao-io.pages.dev
Prompt: How can I implement liquid restaking using rsETH to manage my ETH and LSTs effectively?
Generated: DETERMINISTIC_a2dc573d29ddf904
Batch ID: 20250612_162346
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for rsETH (Restaked ETH)
interface IrsETH {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimRewards() external;
}

// Main contract for liquid restaking using rsETH
contract LiquidRestaking is ReentrancyGuard {
    // Declare state variables
    address public owner;
    IrsETH public rsETHContract;
    IERC20 public ethToken; // The ERC20 representation of ETH
    mapping(address => uint256) public stakedAmounts; // Tracks staked amounts per user

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set initial parameters
    constructor(address _rsETHContract, address _ethToken) {
        owner = msg.sender;
        rsETHContract = IrsETH(_rsETHContract);
        ethToken = IERC20(_ethToken);
    }

    // Function to stake ETH (in ERC20 representation)
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(ethToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to this contract
        ethToken.transferFrom(msg.sender, address(this), amount);

        // Stake the tokens in rsETH contract
        rsETHContract.stake(amount);

        // Update the staked amount for the user
        stakedAmounts[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake ETH (in ERC20 representation)
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Unstake tokens from rsETH contract
        rsETHContract.unstake(amount);

        // Transfer unstaked tokens back to user
        ethToken.transfer(msg.sender, amount);

        // Update the staked amount for the user
        stakedAmounts[msg.sender] -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards from rsETH
    function claimRewards() external nonReentrant {
        // Call claim rewards on rsETH contract
        rsETHContract.claimRewards();

        emit RewardsClaimed(msg.sender);
    }

    // Function to withdraw ETH tokens in case of emergencies (owner only)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(ethToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        ethToken.transfer(msg.sender, amount);
    }

    // Function to get the staked amount for a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }
}
```
