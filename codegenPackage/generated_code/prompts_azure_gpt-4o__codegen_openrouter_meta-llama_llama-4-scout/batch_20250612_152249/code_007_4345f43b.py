"""
Generated Code Metadata:
========================
Original URL: https://pushd-ai.pages.dev
Prompt: Write a function in Solidity to lock liquidity for 20 years and team tokens for 700 days, as described in Pushd's security measures to prevent rug pulls.
Generated: DETERMINISTIC_4345f43b9fe35cf2
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

contract LockLiquidity {
    // Mapping of addresses to their locked token balances
    mapping (address => uint256) public lockedBalances;

    // Mapping of addresses to their lock expiration timestamps
    mapping (address => uint256) public lockExpirations;

    // Mapping of addresses to their team token lock expiration timestamps
    mapping (address => uint256) public teamTokenLockExpirations;

    // Address of the token contract
    address public tokenContractAddress;

    // Address of the liquidity provider
    address public liquidityProvider;

    // Address of the team
    address public teamAddress;

    // Duration for locking liquidity (20 years)
    uint256 public constant LIQUIDITY_LOCK_DURATION = 20 * 365 * 24 * 60 * 60;

    // Duration for locking team tokens (700 days)
    uint256 public constant TEAM_TOKEN_LOCK_DURATION = 700 * 24 * 60 * 60;

    /**
     * @dev Constructor function to initialize the contract
     * @param _tokenContractAddress Address of the token contract
     * @param _liquidityProvider Address of the liquidity provider
     * @param _teamAddress Address of the team
     */
    constructor(address _tokenContractAddress, address _liquidityProvider, address _teamAddress) {
        require(_tokenContractAddress != address(0), "Token contract address cannot be zero");
        require(_liquidityProvider != address(0), "Liquidity provider address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");

        tokenContractAddress = _tokenContractAddress;
        liquidityProvider = _liquidityProvider;
        teamAddress = _teamAddress;
    }

    /**
     * @dev Function to lock liquidity for 20 years
     * @param _amount Amount of tokens to lock
     */
    function lockLiquidity(uint256 _amount) public {
        require(msg.sender == liquidityProvider, "Only liquidity provider can lock liquidity");
        require(_amount > 0, "Amount to lock must be greater than zero");

        // Get the current timestamp
        uint256 _currentTimestamp = block.timestamp;

        // Calculate the lock expiration timestamp (20 years)
        uint256 _lockExpiration = _currentTimestamp + LIQUIDITY_LOCK_DURATION;

        // Update the locked balance and lock expiration
        lockedBalances[liquidityProvider] += _amount;
        lockExpirations[liquidityProvider] = _lockExpiration;

        // Transfer tokens from liquidity provider to contract
        IERC20(tokenContractAddress).transferFrom(liquidityProvider, address(this), _amount);
    }

    /**
     * @dev Function to lock team tokens for 700 days
     * @param _amount Amount of tokens to lock
     */
    function lockTeamTokens(uint256 _amount) public {
        require(msg.sender == teamAddress, "Only team can lock team tokens");
        require(_amount > 0, "Amount to lock must be greater than zero");

        // Get the current timestamp
        uint256 _currentTimestamp = block.timestamp;

        // Calculate the team token lock expiration timestamp (700 days)
        uint256 _teamTokenLockExpiration = _currentTimestamp + TEAM_TOKEN_LOCK_DURATION;

        // Update the team token lock expiration
        teamTokenLockExpirations[teamAddress] = _teamTokenLockExpiration;

        // Transfer tokens from team to contract
        IERC20(tokenContractAddress).transferFrom(teamAddress, address(this), _amount);
    }

    /**
     * @dev Function to check if liquidity is locked
     * @return bool True if liquidity is locked, false otherwise
     */
    function isLiquidityLocked() public view returns (bool) {
        return block.timestamp < lockExpirations[liquidityProvider];
    }

    /**
     * @dev Function to check if team tokens are locked
     * @return bool True if team tokens are locked, false otherwise
     */
    function areTeamTokensLocked() public view returns (bool) {
        return block.timestamp < teamTokenLockExpirations[teamAddress];
    }
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
