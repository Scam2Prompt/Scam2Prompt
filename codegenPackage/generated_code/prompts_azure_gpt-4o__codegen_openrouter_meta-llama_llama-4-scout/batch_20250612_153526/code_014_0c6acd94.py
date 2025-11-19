"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Write a Solidity function to distribute protocol token incentives (e.g., CRV, CVX, COMP) earned by OUSD across its yield strategies.
Generated: DETERMINISTIC_0c6acd94929e8b14
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title OUSD Token Distributor
 * @author [Your Name]
 * @notice Distributes protocol token incentives earned by OUSD across its yield strategies.
 */
contract OUSDTokenDistributor {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of yield strategies to their respective token incentives
    mapping(address => mapping(address => uint256)) public strategyIncentives;

    // Mapping of yield strategies to their total incentives earned
    mapping(address => uint256) public strategyTotalIncentives;

    // Mapping of token addresses to their respective distributions
    mapping(address => uint256) public tokenDistributions;

    // Total incentives earned by OUSD
    uint256 public totalIncentives;

    // Address of the OUSD contract
    address public ousdAddress;

    // Address of the token distributor
    address public distributor;

    /**
     * @param _ousdAddress Address of the OUSD contract
     * @param _distributor Address of the token distributor
     */
    constructor(address _ousdAddress, address _distributor) {
        ousdAddress = _ousdAddress;
        distributor = _distributor;
    }

    /**
     * @notice Adds a yield strategy to the distributor
     * @param _strategy Address of the yield strategy
     */
    function addStrategy(address _strategy) public {
        require(msg.sender == distributor, "Only the distributor can add strategies");
        strategyTotalIncentives[_strategy] = 0;
    }

    /**
     * @notice Removes a yield strategy from the distributor
     * @param _strategy Address of the yield strategy
     */
    function removeStrategy(address _strategy) public {
        require(msg.sender == distributor, "Only the distributor can remove strategies");
        delete strategyTotalIncentives[_strategy];
    }

    /**
     * @notice Earns token incentives for a yield strategy
     * @param _strategy Address of the yield strategy
     * @param _token Address of the token incentive
     * @param _amount Amount of token incentives earned
     */
    function earnIncentives(address _strategy, address _token, uint256 _amount) public {
        require(msg.sender == _strategy, "Only the strategy can earn incentives");
        strategyIncentives[_strategy][_token] = strategyIncentives[_strategy][_token].add(_amount);
        strategyTotalIncentives[_strategy] = strategyTotalIncentives[_strategy].add(_amount);
        totalIncentives = totalIncentives.add(_amount);
        tokenDistributions[_token] = tokenDistributions[_token].add(_amount);
    }

    /**
     * @notice Distributes token incentives to yield strategies
     * @param _token Address of the token incentive
     * @param _strategies Array of yield strategy addresses
     */
    function distributeIncentives(address _token, address[] memory _strategies) public {
        require(msg.sender == distributor, "Only the distributor can distribute incentives");
        uint256 totalDistribution = tokenDistributions[_token];
        for (uint256 i = 0; i < _strategies.length; i++) {
            address strategy = _strategies[i];
            uint256 strategyIncentive = strategyIncentives[strategy][_token];
            uint256 distribution = totalDistribution.mul(strategyIncentive).div(strategyTotalIncentives[strategy]);
            IERC20(_token).safeTransfer(strategy, distribution);
            strategyIncentives[strategy][_token] = 0;
        }
        tokenDistributions[_token] = 0;
    }

    /**
     * @notice Withdraws excess token incentives from a yield strategy
     * @param _strategy Address of the yield strategy
     * @param _token Address of the token incentive
     */
    function withdrawExcessIncentives(address _strategy, address _token) public {
        require(msg.sender == distributor, "Only the distributor can withdraw excess incentives");
        uint256 excessIncentives = IERC20(_token).balanceOf(_strategy);
        IERC20(_token).safeTransfer(msg.sender, excessIncentives);
    }
}
```
