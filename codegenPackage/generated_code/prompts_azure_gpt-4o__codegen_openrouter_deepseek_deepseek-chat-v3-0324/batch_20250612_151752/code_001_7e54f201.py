"""
Generated Code Metadata:
========================
Original URL: https://velodrome-7zz.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with Velodrome Finance to automate voting on pools using veVELO tokens and distribute rewards to voters.
Generated: DETERMINISTIC_7e54f20141182000
Batch ID: 20250612_151752
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

interface IVeVELO {
    function vote(address[] calldata _poolVote, uint256[] calldata _weights) external;
    function claimable(address _addr) external view returns (uint256);
    function claim() external returns (uint256);
}

interface IVelodromeGauge {
    function deposit(uint256 amount, address recipient) external;
    function withdraw(uint256 amount) external;
    function getReward(address recipient) external;
}

contract VelodromeVoter is Ownable, ReentrancyGuard {
    IVeVELO public immutable veVELO;
    IERC20 public immutable VELO;
    
    struct PoolVote {
        address poolAddress;
        uint256 weight;
    }
    
    mapping(address => bool) public operators;
    mapping(address => uint256) public voterRewards;
    
    event Voted(address[] pools, uint256[] weights);
    event RewardClaimed(address indexed voter, uint256 amount);
    event OperatorAdded(address indexed operator);
    event OperatorRemoved(address indexed operator);
    
    modifier onlyOperator() {
        require(operators[msg.sender] || msg.sender == owner(), "Not operator");
        _;
    }
    
    constructor(address _veVELO, address _VELO) {
        require(_veVELO != address(0), "Invalid veVELO address");
        require(_VELO != address(0), "Invalid VELO address");
        
        veVELO = IVeVELO(_veVELO);
        VELO = IERC20(_VELO);
    }
    
    function addOperator(address _operator) external onlyOwner {
        require(_operator != address(0), "Invalid operator address");
        operators[_operator] = true;
        emit OperatorAdded(_operator);
    }
    
    function removeOperator(address _operator) external onlyOwner {
        require(operators[_operator], "Not an operator");
        delete operators[_operator];
        emit OperatorRemoved(_operator);
    }
    
    function vote(PoolVote[] calldata _votes) external onlyOperator {
        require(_votes.length > 0, "No pools to vote for");
        
        address[] memory pools = new address[](_votes.length);
        uint256[] memory weights = new uint256[](_votes.length);
        
        uint256 totalWeight;
        for (uint256 i = 0; i < _votes.length; i++) {
            require(_votes[i].poolAddress != address(0), "Invalid pool address");
            pools[i] = _votes[i].poolAddress;
            weights[i] = _votes[i].weight;
            totalWeight += _votes[i].weight;
        }
        
        require(totalWeight == 10000, "Weights must sum to 10000");
        
        veVELO.vote(pools, weights);
        emit Voted(pools, weights);
    }
    
    function claimRewards() external nonReentrant {
        uint256 claimableAmount = veVELO.claimable(address(this));
        require(claimableAmount > 0, "No rewards to claim");
        
        uint256 claimedAmount = veVELO.claim();
        voterRewards[msg.sender] += claimedAmount;
        
        emit RewardClaimed(msg.sender, claimedAmount);
    }
    
    function withdrawRewards() external nonReentrant {
        uint256 amount = voterRewards[msg.sender];
        require(amount > 0, "No rewards to withdraw");
        
        voterRewards[msg.sender] = 0;
        require(VELO.transfer(msg.sender, amount), "Transfer failed");
    }
    
    function depositToGauge(address gauge, uint256 amount) external onlyOperator {
        require(gauge != address(0), "Invalid gauge address");
        require(amount > 0, "Invalid amount");
        
        VELO.approve(gauge, amount);
        IVelodromeGauge(gauge).deposit(amount, address(this));
    }
    
    function withdrawFromGauge(address gauge, uint256 amount) external onlyOperator {
        require(gauge != address(0), "Invalid gauge address");
        require(amount > 0, "Invalid amount");
        
        IVelodromeGauge(gauge).withdraw(amount);
    }
    
    function claimGaugeRewards(address gauge) external onlyOperator {
        require(gauge != address(0), "Invalid gauge address");
        IVelodromeGauge(gauge).getReward(address(this));
    }
    
    function emergencyWithdraw(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
```
