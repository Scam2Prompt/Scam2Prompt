"""
Generated Code Metadata:
========================
Original URL: https://havacoinext.web.app
Prompt: Write a smart contract in Solidity or Rust to support Hava Coin airdrop distribution for stakers and liquid stakers across the Cosmos, Osmosis, Juno, Dymension, Celestia, and Injective networks.
Generated: DETERMINISTIC_8d56698e83cea4ba
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract HavaCoinAirdrop is Ownable, ReentrancyGuard {
    IERC20 public havaToken;
    uint256 public totalAirdropAmount;
    uint256 public claimPeriodEnd;
    
    enum Network { Cosmos, Osmosis, Juno, Dymension, Celestia, Injective }
    
    struct Staker {
        address wallet;
        uint256 amount;
        Network network;
        bool claimed;
    }
    
    mapping(address => Staker) public stakers;
    mapping(Network => uint256) public networkAllocations;
    
    event AirdropClaimed(address indexed recipient, uint256 amount, Network network);
    event AllocationSet(Network network, uint256 amount);
    
    constructor(
        address _havaToken,
        uint256 _totalAirdropAmount,
        uint256 _claimPeriodDays
    ) {
        require(_havaToken != address(0), "Invalid token address");
        require(_totalAirdropAmount > 0, "Airdrop amount must be positive");
        
        havaToken = IERC20(_havaToken);
        totalAirdropAmount = _totalAirdropAmount;
        claimPeriodEnd = block.timestamp + (_claimPeriodDays * 1 days);
    }
    
    function setNetworkAllocation(Network _network, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Allocation must be positive");
        networkAllocations[_network] = _amount;
        emit AllocationSet(_network, _amount);
    }
    
    function registerStakers(
        address[] calldata _wallets,
        uint256[] calldata _amounts,
        Network[] calldata _networks
    ) external onlyOwner {
        require(_wallets.length == _amounts.length && _amounts.length == _networks.length, "Array length mismatch");
        
        for (uint256 i = 0; i < _wallets.length; i++) {
            require(_wallets[i] != address(0), "Invalid wallet address");
            require(_amounts[i] > 0, "Amount must be positive");
            require(networkAllocations[_networks[i]] >= _amounts[i], "Exceeds network allocation");
            
            stakers[_wallets[i]] = Staker({
                wallet: _wallets[i],
                amount: _amounts[i],
                network: _networks[i],
                claimed: false
            });
            
            networkAllocations[_networks[i]] -= _amounts[i];
        }
    }
    
    function claimAirdrop() external nonReentrant {
        require(block.timestamp <= claimPeriodEnd, "Claim period has ended");
        require(stakers[msg.sender].wallet != address(0), "Not eligible for airdrop");
        require(!stakers[msg.sender].claimed, "Already claimed");
        
        uint256 amount = stakers[msg.sender].amount;
        require(havaToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        stakers[msg.sender].claimed = true;
        require(havaToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit AirdropClaimed(msg.sender, amount, stakers[msg.sender].network);
    }
    
    function withdrawRemaining() external onlyOwner {
        require(block.timestamp > claimPeriodEnd, "Claim period not ended");
        uint256 remaining = havaToken.balanceOf(address(this));
        require(remaining > 0, "No remaining tokens");
        require(havaToken.transfer(owner(), remaining), "Transfer failed");
    }
    
    function extendClaimPeriod(uint256 _additionalDays) external onlyOwner {
        require(_additionalDays > 0, "Additional days must be positive");
        claimPeriodEnd += (_additionalDays * 1 days);
    }
}
```
