"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyzwthelly.com
Prompt: Create a Solidity contract that integrates with Valantis to enable liquid staking of nBTC via the stHYPE AMM.
Generated: DETERMINISTIC_0ae393f3266355ab
Batch ID: 20250612_154115
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

/**
 * @title LiquidStakingContract
 * @author [Your Name]
 * @notice This contract enables liquid staking of nBTC via the stHYPE AMM on Valantis.
 * @dev Ensure the Valantis and stHYPE AMM interfaces are accurate and up-to-date.
 */
interface IValantis {
    function deposit(address token, uint256 amount) external returns (uint256);
    function withdraw(address token, uint256 amount) external returns (uint256);
}

interface IstHYPE {
    function swap(address inputToken, address outputToken, uint256 amount) external returns (uint256);
    function getSwapRate(address inputToken, address outputToken) external view returns (uint256);
}

contract LiquidStakingContract {
    // Address of the Valantis protocol
    address public valantisAddress;
    // Address of the stHYPE AMM
    address public stHYPEAddress;

    // Event emitted when nBTC is staked
    event Staked(address indexed user, uint256 amount, uint256 stakedTokens);

    // Event emitted when nBTC is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Mapping to keep track of user balances
    mapping(address => uint256) public userBalances;

    // Constructor to set Valantis and stHYPE addresses
    constructor(address _valantisAddress, address _stHYPEAddress) {
        require(_valantisAddress != address(0), "Invalid Valantis address");
        require(_stHYPEAddress != address(0), "Invalid stHYPE address");
        valantisAddress = _valantisAddress;
        stHYPEAddress = _stHYPEAddress;
    }

    /**
     * @notice Stakes nBTC into Valantis and converts it to stHYPE tokens.
     * @param amount The amount of nBTC to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer nBTC from the user to this contract
        require(
            IERC20(nBTC).transferFrom(msg.sender, address(this), amount),
            "Transfer of nBTC failed"
        );

        // Approve Valantis to spend nBTC
        require(
            IERC20(nBTC).approve(valantisAddress, amount),
            "Approval of nBTC failed"
        );

        // Deposit nBTC into Valantis
        uint256 stakedTokens = IValantis(valantisAddress).deposit(nBTC, amount);

        // Approve stHYPE AMM to spend stakedTokens
        require(
            IERC20(stakedTokens).approve(stHYPEAddress, stakedTokens),
            "Approval of staked tokens failed"
        );

        // Convert stakedTokens to stHYPE tokens
        uint256 stHYPEAmount = IstHYPE(stHYPEAddress).swap(stakedTokens, stHYPE, stakedTokens);

        // Update user balance
        userBalances[msg.sender] += stHYPEAmount;

        emit Staked(msg.sender, amount, stHYPEAmount);
    }

    /**
     * @notice Withdraws staked tokens from Valantis.
     * @param amount The amount of staked tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Withdraw tokens from Valantis
        uint256 withdrawnTokens = IValantis(valantisAddress).withdraw(stHYPE, amount);

        // Transfer withdrawn tokens to the user
        require(
            IERC20(stHYPE).transfer(msg.sender, withdrawnTokens),
            "Transfer of withdrawn tokens failed"
        );

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Retrieves the current swap rate between nBTC and stHYPE.
     * @return The current swap rate.
     */
    function getSwapRate() external view returns (uint256) {
        return IstHYPE(stHYPEAddress).getSwapRate(nBTC, stHYPE);
    }
}

/**
 * @notice Replace `nBTC` and `stHYPE` with the correct token contract addresses.
 */
// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
