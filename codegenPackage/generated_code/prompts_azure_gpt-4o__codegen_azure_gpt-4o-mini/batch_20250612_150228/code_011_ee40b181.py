"""
Generated Code Metadata:
========================
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Provide a code example for staking ETH on Bedrock via EigenLayer to secure Actively Validated Services (AVS) and earn restaking rewards.
Generated: DETERMINISTIC_ee40b18170f9ea15
Batch ID: 20250612_150228
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for EigenLayer staking
interface IEigenLayer {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getRewards() external view returns (uint256);
}

// Contract for staking ETH on Bedrock via EigenLayer
contract EigenLayerStaking is Ownable {
    // State variables
    IERC20 public immutable ethToken; // ERC20 token representing staked ETH
    IEigenLayer public immutable eigenLayer; // EigenLayer contract instance

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the ETH token and EigenLayer contract addresses
    constructor(address _ethToken, address _eigenLayer) {
        require(_ethToken != address(0), "Invalid ETH token address");
        require(_eigenLayer != address(0), "Invalid EigenLayer address");
        
        ethToken = IERC20(_ethToken);
        eigenLayer = IEigenLayer(_eigenLayer);
    }

    // Function to stake ETH
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(ethToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Call the EigenLayer stake function
        eigenLayer.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake ETH
    function unstake(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Call the EigenLayer unstake function
        eigenLayer.unstake(amount);

        // Transfer the unstaked ETH back to the owner
        require(ethToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external onlyOwner {
        uint256 rewards = eigenLayer.getRewards();
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the owner
        require(ethToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw any ERC20 tokens accidentally sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
