"""
Generated Code Metadata:
========================
Original URL: https://aero-9z6.pages.dev
Prompt: Write a Solidity smart contract to distribute AERO emissions to liquidity pools based on votes from veAERO holders.
Generated: DETERMINISTIC_248eb823c876b54e
Batch ID: 20250612_150927
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

interface IVeAERO {
    function balanceOf(address account) external view returns (uint256);
}

contract AeroEmissionDistributor is Ownable, ReentrancyGuard {
    IERC20 public immutable aeroToken;
    IVeAERO public immutable veAero;
    
    struct Pool {
        address poolAddress;
        uint256 votes;
        uint256 lastEmissionTime;
    }
    
    uint256 public constant EMISSION_PERIOD = 1 weeks;
    uint256 public constant MAX_POOLS = 50;
    uint256 public totalVotes;
    
    Pool[] public pools;
    mapping(address => bool) public isPool;
    mapping(address => mapping(address => uint256)) public userVotes;
    
    event PoolAdded(address indexed poolAddress);
    event PoolRemoved(address indexed poolAddress);
    event Voted(address indexed voter, address indexed pool, uint256 amount);
    event EmissionsDistributed(address indexed pool, uint256 amount);
    
    constructor(address _aeroToken, address _veAero) {
        require(_aeroToken != address(0), "Invalid AERO token address");
        require(_veAero != address(0), "Invalid veAERO token address");
        
        aeroToken = IERC20(_aeroToken);
        veAero = IVeAERO(_veAero);
    }
    
    function addPool(address _poolAddress) external onlyOwner {
        require(!isPool[_poolAddress], "Pool already exists");
        require(pools.length < MAX_POOLS, "Max pools reached");
        
        pools.push(Pool({
            poolAddress: _poolAddress,
            votes: 0,
            lastEmissionTime: block.timestamp
        }));
        
        isPool[_poolAddress] = true;
        emit PoolAdded(_poolAddress);
    }
    
    function removePool(uint256 _poolIndex) external onlyOwner {
        require(_poolIndex < pools.length, "Invalid pool index");
        
        address poolAddress = pools[_poolIndex].poolAddress;
        totalVotes -= pools[_poolIndex].votes;
        
        pools[_poolIndex] = pools[pools.length - 1];
        pools.pop();
        
        isPool[poolAddress] = false;
        emit PoolRemoved(poolAddress);
    }
    
    function vote(address _poolAddress, uint256 _amount) external nonReentrant {
        require(isPool[_poolAddress], "Invalid pool address");
        require(_amount > 0, "Amount must be greater than 0");
        
        uint256 veAeroBalance = veAero.balanceOf(msg.sender);
        require(veAeroBalance >= _amount, "Insufficient veAERO balance");
        
        userVotes[msg.sender][_poolAddress] += _amount;
        
        for (uint256 i = 0; i < pools.length; i++) {
            if (pools[i].poolAddress == _poolAddress) {
                pools[i].votes += _amount;
                totalVotes += _amount;
                break;
            }
        }
        
        emit Voted(msg.sender, _poolAddress, _amount);
    }
    
    function unvote(address _poolAddress, uint256 _amount) external nonReentrant {
        require(isPool[_poolAddress], "Invalid pool address");
        require(_amount > 0, "Amount must be greater than 0");
        require(userVotes[msg.sender][_poolAddress] >= _amount, "Insufficient votes");
        
        userVotes[msg.sender][_poolAddress] -= _amount;
        
        for (uint256 i = 0; i < pools.length; i++) {
            if (pools[i].poolAddress == _poolAddress) {
                pools[i].votes -= _amount;
                totalVotes -= _amount;
                break;
            }
        }
        
        emit Voted(msg.sender, _poolAddress, 0);
    }
    
    function distributeEmissions(uint256 _totalAmount) external onlyOwner nonReentrant {
        require(_totalAmount > 0, "Amount must be greater than 0");
        require(aeroToken.balanceOf(address(this)) >= _totalAmount, "Insufficient AERO balance");
        require(totalVotes > 0, "No votes to distribute");
        
        for (uint256 i = 0; i < pools.length; i++) {
            if (pools[i].votes > 0 && block.timestamp >= pools[i].lastEmissionTime + EMISSION_PERIOD) {
                uint256 poolShare = (_totalAmount * pools[i].votes) / totalVotes;
                
                aeroToken.transfer(pools[i].poolAddress, poolShare);
                pools[i].lastEmissionTime = block.timestamp;
                
                emit EmissionsDistributed(pools[i].poolAddress, poolShare);
            }
        }
    }
    
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner(), _amount);
    }
    
    function getPools() external view returns (Pool[] memory) {
        return pools;
    }
    
    function getPoolCount() external view returns (uint256) {
        return pools.length;
    }
}
```
