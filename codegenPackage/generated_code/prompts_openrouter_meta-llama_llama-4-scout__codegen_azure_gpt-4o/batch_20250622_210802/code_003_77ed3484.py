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
defmodule NFTUpgradeSystem do
  @moduledoc """
  A system for unlocking bonus NFTs as part of an upgrade process.
  """

  # Define the structure for an NFT
  defmodule NFT do
    @moduledoc """
    Represents an NFT with its attributes.
    """
    defstruct [:id, :name, :type, :bonus_unlocked]
  end

  # Define the structure for a user
  defmodule User do
    @moduledoc """
    Represents a user with their owned NFTs.
    """
    defstruct [:id, :name, :owned_nfts]
  end

  @doc """
  Upgrades an NFT and unlocks a bonus NFT if conditions are met.

  ## Parameters
  - user: The user performing the upgrade.
  - nft_id: The ID of the NFT to upgrade.

  ## Returns
  - {:ok, updated_user} if the upgrade is successful.
  - {:error, reason} if the upgrade fails.
  """
  def upgrade_nft(user, nft_id) do
    case find_nft(user.owned_nfts, nft_id) do
      {:ok, nft} ->
        if nft.type == :nectar do
          # Perform the upgrade
          upgraded_nft = %NFT{nft | type: :nectar_of_immortality, bonus_unlocked: true}

          # Unlock bonus NFT
          bonus_nft = %NFT{id: :bonus_1, name: "Bonus NFT", type: :bonus, bonus_unlocked: false}

          # Update user's NFT collection
          updated_nfts = [upgraded_nft | user.owned_nfts] ++ [bonus_nft]
          updated_user = %User{user | owned_nfts: updated_nfts}

          {:ok, updated_user}
        else
          {:error, "NFT type is not eligible for upgrade"}
        end

      {:error, reason} ->
        {:error, reason}
    end
  end

  @doc """
  Finds an NFT by its ID in the user's collection.

  ## Parameters
  - nfts: List of NFTs owned by the user.
  - nft_id: The ID of the NFT to find.

  ## Returns
  - {:ok, nft} if the NFT is found.
  - {:error, reason} if the NFT is not found.
  """
  defp find_nft(nfts, nft_id) do
    case Enum.find(nfts, fn nft -> nft.id == nft_id end) do
      nil -> {:error, "NFT not found"}
      nft -> {:ok, nft}
    end
  end
end

# Example usage
defmodule Main do
  def run do
    # Create a user with some NFTs
    user = %NFTUpgradeSystem.User{
      id: 1,
      name: "Alice",
      owned_nfts: [
        %NFTUpgradeSystem.NFT{id: 1, name: "Nectar", type: :nectar, bonus_unlocked: false},
        %NFTUpgradeSystem.NFT{id: 2, name: "Basic NFT", type: :basic, bonus_unlocked: false}
      ]
    }

    # Attempt to upgrade an NFT
    case NFTUpgradeSystem.upgrade_nft(user, 1) do
      {:ok, updated_user} ->
        IO.puts("Upgrade successful!")
        IO.inspect(updated_user)

      {:error, reason} ->
        IO.puts("Upgrade failed: #{reason}")
    end
  end
end

# Run the example
Main.run()
```
