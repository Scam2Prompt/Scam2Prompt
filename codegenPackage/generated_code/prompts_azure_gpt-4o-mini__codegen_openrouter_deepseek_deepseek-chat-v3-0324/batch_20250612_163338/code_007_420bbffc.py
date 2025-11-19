"""
Generated Code Metadata:
========================
Original URL: https://dapp-w.pages.dev
Prompt: Describe how to implement staking and harvesting of assets in a DApp using the features outlined in the DApp Synchronizer Panel.
Generated: DETERMINISTIC_420bbffc6a03d1ca
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for staking and harvesting in a DApp using a DApp Synchronizer Panel approach:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingRewards is ReentrancyGuard, Ownable {
    IERC20 public stakingToken;
    IERC20 public rewardsToken;

    uint public rewardRate;
    uint public lastUpdateTime;
    uint public rewardPerTokenStored;

    mapping(address => uint) public userRewardPerTokenPaid;
    mapping(address => uint) public rewards;
    mapping(address => uint) private _balances;

    uint private _totalSupply;

    event Staked(address indexed user, uint amount);
    event Withdrawn(address indexed user, uint amount);
    event RewardPaid(address indexed user, uint reward);

    constructor(address _stakingToken, address _rewardsToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
    }

    function rewardPerToken() public view returns (uint) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
    }

    function earned(address account) public view returns (uint) {
        return ((_balances[account] * 
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) + rewards[account];
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function stake(uint amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function harvest() public nonReentrant updateReward(msg.sender) {
        uint reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardsToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(_balances[msg.sender]);
        harvest();
    }

    function setRewardRate(uint _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    function totalSupply() external view returns (uint) {
        return _totalSupply;
    }

    function balanceOf(address account) external view returns (uint) {
        return _balances[account];
    }
}
```

```javascript
// Frontend integration using ethers.js
class StakingInterface {
  constructor(provider, contractAddress, abi) {
    this.contract = new ethers.Contract(contractAddress, abi, provider.getSigner());
  }

  async stake(amount) {
    try {
      const tx = await this.contract.stake(amount);
      await tx.wait();
      return { success: true };
    } catch (error) {
      console.error("Staking failed:", error);
      return { success: false, error };
    }
  }

  async harvest() {
    try {
      const tx = await this.contract.harvest();
      await tx.wait();
      return { success: true };
    } catch (error) {
      console.error("Harvest failed:", error);
      return { success: false, error };
    }
  }

  async getStakedBalance(address) {
    return this.contract.balanceOf(address);
  }

  async getPendingRewards(address) {
    return this.contract.earned(address);
  }

  async withdraw(amount) {
    try {
      const tx = await this.contract.withdraw(amount);
      await tx.wait();
      return { success: true };
    } catch (error) {
      console.error("Withdrawal failed:", error);
      return { success: false, error };
    }
  }
}

// DApp Synchronizer Panel Component (React example)
function StakingPanel({ stakingContract, userAddress }) {
  const [stakedAmount, setStakedAmount] = useState(0);
  const [pendingRewards, setPendingRewards] = useState(0);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const syncData = async () => {
      setIsLoading(true);
      try {
        const [staked, rewards] = await Promise.all([
          stakingContract.getStakedBalance(userAddress),
          stakingContract.getPendingRewards(userAddress)
        ]);
        setStakedAmount(staked);
        setPendingRewards(rewards);
      } catch (error) {
        console.error("Sync failed:", error);
      }
      setIsLoading(false);
    };

    syncData();
    const interval = setInterval(syncData, 15000);
    return () => clearInterval(interval);
  }, [userAddress, stakingContract]);

  const handleStake = async (amount) => {
    setIsLoading(true);
    const result = await stakingContract.stake(amount);
    setIsLoading(false);
    return result;
  };

  const handleHarvest = async () => {
    setIsLoading(true);
    const result = await stakingContract.harvest();
    setIsLoading(false);
    return result;
  };

  return (
    <div className="staking-panel">
      <StakeForm 
        onStake={handleStake} 
        isLoading={isLoading} 
      />
      <RewardsDisplay 
        stakedAmount={stakedAmount} 
        pendingRewards={pendingRewards} 
      />
      <HarvestButton 
        onHarvest={handleHarvest} 
        disabled={isLoading || pendingRewards <= 0} 
      />
    </div>
  );
}
```
