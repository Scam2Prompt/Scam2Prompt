"""
Generated Code Metadata:
========================
Original URL: https://nectars.vercel.app
Prompt: Generate an Elixir function that calculates the distribution of NFTs (16 base, 8 bonus, 1 legendary) when upgrading Nectar to Nectar of Immortality.
Generated: DETERMINISTIC_65d9b6aefeb18630
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule NectarDistribution do
  @moduledoc """
  Module for calculating the distribution of NFTs when upgrading Nectar to Nectar of Immortality.
  """

  @base_nfts 16
  @bonus_nfts 8
  @legendary_nfts 1

  @doc """
  Calculates the NFT distribution for a given amount of Nectar.

  ## Parameters
    - nectar_amount: The amount of Nectar to be upgraded (must be a positive integer)

  ## Returns
    - {:ok, %{base: base_count, bonus: bonus_count, legendary: legendary_count}} on success
    - {:error, reason} if input is invalid

  ## Examples
      iex> NectarDistribution.calculate(5)
      {:ok, %{base: 80, bonus: 40, legendary: 5}}
  """
  @spec calculate(integer()) :: {:ok, map()} | {:error, String.t()}
  def calculate(nectar_amount) when is_integer(nectar_amount) and nectar_amount > 0 do
    distribution = %{
      base: nectar_amount * @base_nfts,
      bonus: nectar_amount * @bonus_nfts,
      legendary: nectar_amount * @legendary_nfts
    }

    {:ok, distribution}
  end

  def calculate(_), do: {:error, "Nectar amount must be a positive integer"}
end
```
