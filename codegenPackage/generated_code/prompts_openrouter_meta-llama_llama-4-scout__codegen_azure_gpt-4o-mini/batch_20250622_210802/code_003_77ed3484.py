"""
Generated Code Metadata:
========================
Original URL: https://nectars.vercel.app
Prompt: How can I use Elixir to create a system for unlocking bonus NFTs as part of an upgrade process similar to Nectars' upgrade to Nectar of Immortality?
Generated: DETERMINISTIC_77ed3484dd71e0b5
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule NFTUnlocker do
  @moduledoc """
  A module for managing the unlocking of bonus NFTs as part of an upgrade process.
  This module simulates the upgrade process similar to Nectars' upgrade to Nectar of Immortality.
  """

  @type nft :: %{
          id: integer(),
          name: String.t(),
          unlocked: boolean()
        }

  @type user :: %{
          id: integer(),
          nfts: [nft()]
        }

  @doc """
  Upgrades a user's NFT and unlocks bonus NFTs based on the upgrade type.

  ## Parameters
  - user: The user struct containing user information and their NFTs.
  - upgrade_type: A string indicating the type of upgrade.

  ## Returns
  - {:ok, updated_user} if the upgrade is successful.
  - {:error, reason} if the upgrade fails.
  """
  @spec upgrade_nft(user(), String.t()) :: {:ok, user()} | {:error, String.t()}
  def upgrade_nft(user, upgrade_type) do
    case validate_upgrade_type(upgrade_type) do
      :ok ->
        updated_nfts = unlock_bonus_nfts(user.nfts, upgrade_type)
        updated_user = %{user | nfts: updated_nfts}
        {:ok, updated_user}

      {:error, reason} ->
        {:error, reason}
    end
  end

  @doc """
  Validates the upgrade type.

  ## Parameters
  - upgrade_type: A string indicating the type of upgrade.

  ## Returns
  - :ok if the upgrade type is valid.
  - {:error, reason} if the upgrade type is invalid.
  """
  @spec validate_upgrade_type(String.t()) :: :ok | {:error, String.t()}
  defp validate_upgrade_type(upgrade_type) when upgrade_type in ["basic", "premium", "legendary"], do: :ok
  defp validate_upgrade_type(_), do: {:error, "Invalid upgrade type"}

  @doc """
  Unlocks bonus NFTs based on the upgrade type.

  ## Parameters
  - nfts: A list of NFTs owned by the user.
  - upgrade_type: A string indicating the type of upgrade.

  ## Returns
  - A list of NFTs with unlocked bonuses.
  """
  @spec unlock_bonus_nfts([nft()], String.t()) :: [nft()]
  defp unlock_bonus_nfts(nfts, "basic") do
    nfts ++ [%{id: 1, name: "Basic Bonus NFT", unlocked: true}]
  end

  defp unlock_bonus_nfts(nfts, "premium") do
    nfts ++ [%{id: 2, name: "Premium Bonus NFT", unlocked: true}]
  end

  defp unlock_bonus_nfts(nfts, "legendary") do
    nfts ++ [%{id: 3, name: "Legendary Bonus NFT", unlocked: true}]
  end

  defp unlock_bonus_nfts(nfts, _), do: nfts

  @doc """
  Example function to demonstrate the upgrade process.

  ## Example
      iex> user = %{id: 1, nfts: [%{id: 0, name: "Standard NFT", unlocked: false}]}
      iex> NFTUnlocker.upgrade_nft(user, "premium")
      {:ok, %{id: 1, nfts: [%{id: 0, name: "Standard NFT", unlocked: false}, %{id: 2, name: "Premium Bonus NFT", unlocked: true}]}}
  """
end
```
