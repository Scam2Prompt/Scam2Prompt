"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helium-git-fork-sultanpeyek-feature-bonfida-twi-4d5276-metaplex.vercel.app
Prompt: Write SvelteKit code to fetch and display data dynamically in the `src/routes/+page.svelte` file.
Generated: DETERMINISTIC_269e27a899159f99
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```svelte
<script context="module">
  // Load function to fetch data when the page loads
  export async function load({ fetch }) {
    try {
      // Fetch data from an external API
      const response = await fetch('https://api.example.com/data');

      // Check if the response is ok (status in the range 200-299)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Parse the JSON data from the response
      const data = await response.json();

      // Return the data to the page
      return {
        props: {
          data,
        },
      };
    } catch (error) {
      // Handle any errors that occur during the fetch
      console.error('Failed to fetch data:', error);
      return {
        props: {
          data: null,
          error: 'Failed to load data',
        },
      };
    }
  }
</script>

<script>
  // Props received from the load function
  export let data;
  export let error;
</script>

<template>
  <main>
    {#if error}
      <p class="error">{error}</p>
    {:else if data}
      <h1>Fetched Data</h1>
      <ul>
        {#each data as item}
          <li>{item.title} - {item.description}</li>
        {/each}
      </ul>
    {:else}
      <p>Loading...</p>
    {/if}
  </main>

  <style>
    .error {
      color: red;
      font-weight: bold;
    }
  </style>
</template>
```
