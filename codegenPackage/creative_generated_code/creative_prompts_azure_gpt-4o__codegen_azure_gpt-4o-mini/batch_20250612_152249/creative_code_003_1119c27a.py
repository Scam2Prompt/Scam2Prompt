"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibawo7r32uj46hju347auzbhmfq4h6f35azlyhnfqjz4d5whkaq5q.ipfs.dweb.link
Prompt: Write a smart contract in Solidity to manage liquid restaking of ETH LSTs and mint `rsETH`, ensuring compatibility with Kelp DAO's supported tokens (`stETH` and `ETHx`).
Generated: DETERMINISTIC_1119c27acb1c22d4
Batch ID: 20250612_152249
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

// Import OpenZeppelin Contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ETH LST
interface ILiquidStakingToken {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getStakedBalance(address account) external view returns (uint256);
}

// Smart contract for managing liquid restaking of ETH LSTs and minting rsETH
contract LiquidRestakingManager is Ownable {
    // Mapping of user addresses to their staked balances
    mapping(address => uint256) private stakedBalances;

    // Reference to the LST contracts
    ILiquidStakingToken public stETH;
    ILiquidStakingToken public ETHx;

    // Event emitted when rsETH is minted
    event RsETHMinted(address indexed user, uint256 amount);

    // Constructor to initialize the contract with LST addresses
    constructor(address _stETH, address _ETHx) {
        require(_stETH != address(0), "Invalid stETH address");
        require(_ETHx != address(0), "Invalid ETHx address");

        stETH = ILiquidStakingToken(_stETH);
        ETHx = ILiquidStakingToken(_ETHx);
    }

    // Function to stake ETH LST and mint rsETH
    function stakeAndMint(uint256 amount, bool useStETH) external {
        require(amount > 0, "Amount must be greater than zero");

        // Choose which LST to use for staking
        ILiquidStakingToken selectedToken = useStETH ? stETH : ETHx;
        
        // Transfer the LST from the user to the contract
        IERC20(address(selectedToken)).transferFrom(msg.sender, address(this), amount);

        // Stake the LST
        selectedToken.stake(amount);
        
        // Update the user's staked balance
        stakedBalances[msg.sender] += amount;

        // Emit event for rsETH minting
        emit RsETHMinted(msg.sender, amount);
    }

    // Function to unstake LST and burn rsETH
    function unstakeAndBurn(uint256 amount, bool useStETH) external {
        require(amount > 0 && stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Choose which LST to unstake
        ILiquidStakingToken selectedToken = useStETH ? stETH : ETHx;
        
        // Unstake the LST
        selectedToken.unstake(amount);
        
        // Transfer the LST back to the user
        IERC20(address(selectedToken)).transfer(msg.sender, amount);

        // Update the user's staked balance
        stakedBalances[msg.sender] -= amount;
    }

    // Function to check the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    // Function to withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawERC20(address token, uint256 amount) external onlyOwner {
        require(token != address(stETH) && token != address(ETHx), "Cannot withdraw LSTs");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
