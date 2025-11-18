"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsemex.com
Prompt: Provide code examples for implementing a "Buy and Burn" mechanism in a smart contract for $PLSX tokens on PulseChain.
Generated: DETERMINISTIC_aaa9ef5cc564beec
Batch ID: 20250612_150426
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
 * @title BuyAndBurnContract
 * @dev This contract implements a "Buy and Burn" mechanism for $PLSX tokens on PulseChain.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IDEXRouter {
    function swapExactETHForTokensSupportingFeeOnTransferTokens(
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable;

    function WETH() external pure returns (address);
}

contract BuyAndBurn {
    address public immutable PLSX; // The address of the $PLSX token
    IDEXRouter public immutable router; // Address of the DEX router
    address public owner; // Owner of the contract

    event TokensBurned(uint256 amountBurned, uint256 ethUsed);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _PLSX, address _router) {
        require(_PLSX != address(0), "PLSX address cannot be zero");
        require(_router != address(0), "Router address cannot be zero");

        PLSX = _PLSX;
        router = IDEXRouter(_router);
        owner = msg.sender;
    }

    /**
     * @dev Allows the contract owner to execute the buy and burn mechanism.
     * The contract swaps received ETH for $PLSX tokens and burns them.
     */
    function buyAndBurn(uint256 minTokensToReceive) external payable onlyOwner {
        require(msg.value > 0, "ETH required to buy tokens");

        // Define the path for the swap (ETH -> PLSX)
        address[] memory path = new address[](2);
        path[0] = router.WETH(); // WETH address
        path[1] = PLSX; // $PLSX token address

        uint256 initialPLSXBalance = IERC20(PLSX).balanceOf(address(this));

        // Perform the token swap
        router.swapExactETHForTokensSupportingFeeOnTransferTokens{value: msg.value}(
            minTokensToReceive,
            path,
            address(this),
            block.timestamp + 300 // 5 minute deadline
        );

        uint256 newPLSXBalance = IERC20(PLSX).balanceOf(address(this));
        uint256 tokensPurchased = newPLSXBalance - initialPLSXBalance;

        require(tokensPurchased > 0, "No tokens were purchased");

        // Burn the tokens (by sending them to the zero address)
        _burnTokens(tokensPurchased);

        emit TokensBurned(tokensPurchased, msg.value);
    }

    /**
     * @dev Internal function to burn tokens by transferring to the zero address.
     */
    function _burnTokens(uint256 amount) internal {
        require(
            IERC20(PLSX).transfer(address(0), amount),
            "Token burn failed"
        );
    }

    /**
     * @dev Allows the owner to withdraw any leftover ETH in the contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw any leftover tokens in the contract.
     */
    function withdrawTokens(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(
            IERC20(token).transfer(owner, balance),
            "Token withdrawal failed"
        );
    }

    /**
     * @dev Fallback function to accept incoming ETH.
     */
    receive() external payable {}
}
```
