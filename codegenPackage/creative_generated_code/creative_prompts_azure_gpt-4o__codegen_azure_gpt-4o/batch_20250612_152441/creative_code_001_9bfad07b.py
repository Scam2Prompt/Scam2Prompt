"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stake.pages.dev
Prompt: Generate Solidity code for a smart contract that interacts with the Flashstake protocol to lock stETH tokens and withdraw upfront yield using fTokens for early withdrawal.
Generated: DETERMINISTIC_9bfad07b0fff6fab
Batch ID: 20250612_152441
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
 * @title FlashstakeInteractor
 * @dev A smart contract to interact with the Flashstake protocol for locking stETH tokens
 *      and withdrawing upfront yield using fTokens.
 */
interface IFlashstake {
    function stake(
        address token,
        uint256 amount,
        uint256 duration
    ) external returns (uint256 upfrontYield);

    function withdrawUpfrontYield(address recipient, uint256 amount) external;
}

interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

contract FlashstakeInteractor {
    address public owner;
    IFlashstake public flashstakeProtocol;
    IERC20 public stETH;
    IERC20 public fToken;

    event YieldWithdrawn(address indexed user, uint256 amount);
    event TokensStaked(address indexed user, uint256 amount, uint256 duration);

    constructor(
        address _flashstakeProtocol,
        address _stETH,
        address _fToken
    ) {
        require(_flashstakeProtocol != address(0), "Invalid protocol address");
        require(_stETH != address(0), "Invalid stETH address");
        require(_fToken != address(0), "Invalid fToken address");

        flashstakeProtocol = IFlashstake(_flashstakeProtocol);
        stETH = IERC20(_stETH);
        fToken = IERC20(_fToken);
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to stake stETH tokens into the Flashstake protocol.
     * @param amount The amount of stETH to stake.
     * @param duration The duration for the staking period (in seconds).
     */
    function stakeTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            stETH.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Approve Flashstake protocol to spend stETH tokens
        stETH.approve(address(flashstakeProtocol), amount);

        // Stake tokens and receive upfront yield
        uint256 upfrontYield = flashstakeProtocol.stake(
            address(stETH),
            amount,
            duration
        );

        // Emit event
        emit TokensStaked(msg.sender, amount, duration);

        // Return upfront yield (in fTokens) to the caller
        require(
            fToken.transfer(msg.sender, upfrontYield),
            "Yield transfer failed"
        );
    }

    /**
     * @dev Function to withdraw upfront yield using fTokens.
     * @param amount The amount of fTokens to withdraw.
     */
    function withdrawUpfrontYield(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            fToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Withdraw the upfront yield from the Flashstake protocol
        flashstakeProtocol.withdrawUpfrontYield(msg.sender, amount);

        // Emit event
        emit YieldWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw any mistakenly sent ERC20 tokens.
     * @param tokenAddress The address of the ERC20 token.
     * @param amount The amount of tokens to withdraw.
     */
    function rescueTokens(address tokenAddress, uint256 amount)
        external
        onlyOwner
    {
        require(amount > 0, "Amount must be greater than zero");
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(owner, amount),
            "Token rescue transfer failed"
        );
    }
}
```
