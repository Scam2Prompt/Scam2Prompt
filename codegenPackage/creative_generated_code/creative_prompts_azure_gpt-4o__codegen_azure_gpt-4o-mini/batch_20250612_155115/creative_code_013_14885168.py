"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Implement a search filter in Vue.js that allows users to select dress fits (e.g., bodycon fit, wrap fit) and skirt lengths (e.g., tea-length, floor-length) for an e-commerce platform.
Generated: DETERMINISTIC_14885168596679e3
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```vue
<template>
  <div class="search-filter">
    <h2>Dress Search Filter</h2>
    
    <div class="filter-group">
      <label for="fit-select">Select Dress Fit:</label>
      <select id="fit-select" v-model="selectedFit" @change="applyFilters">
        <option value="">All Fits</option>
        <option v-for="fit in dressFits" :key="fit" :value="fit">{{ fit }}</option>
      </select>
    </div>

    <div class="filter-group">
      <label for="length-select">Select Skirt Length:</label>
      <select id="length-select" v-model="selectedLength" @change="applyFilters">
        <option value="">All Lengths</option>
        <option v-for="length in skirtLengths" :key="length" :value="length">{{ length }}</option>
      </select>
    </div>

    <button @click="resetFilters">Reset Filters</button>

    <div class="search-results">
      <h3>Search Results:</h3>
      <ul>
        <li v-for="item in filteredResults" :key="item.id">{{ item.name }}</li>
      </ul>
      <p v-if="filteredResults.length === 0">No results found.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // Available dress fits and skirt lengths
      dressFits: ['Bodycon Fit', 'Wrap Fit', 'A-Line Fit', 'Shift Fit'],
      skirtLengths: ['Tea-Length', 'Floor-Length', 'Mini-Length', 'Midi-Length'],
      
      // Selected filters
      selectedFit: '',
      selectedLength: '',

      // Sample product data
      products: [
        { id: 1, name: 'Bodycon Dress', fit: 'Bodycon Fit', length: 'Tea-Length' },
        { id: 2, name: 'Wrap Dress', fit: 'Wrap Fit', length: 'Floor-Length' },
        { id: 3, name: 'A-Line Skirt', fit: 'A-Line Fit', length: 'Midi-Length' },
        // Additional products can be added here
      ],
    };
  },
  computed: {
    // Compute filtered results based on selected filters
    filteredResults() {
      return this.products.filter(product => {
        const fitMatch = this.selectedFit ? product.fit === this.selectedFit : true;
        const lengthMatch = this.selectedLength ? product.length === this.selectedLength : true;
        return fitMatch && lengthMatch;
      });
    },
  },
  methods: {
    // Apply filters whenever the user changes the selection
    applyFilters() {
      // The filtered results are automatically computed through computed property
    },
    
    // Reset all filters to show all products
    resetFilters() {
      this.selectedFit = '';
      this.selectedLength = '';
    },
  },
};
</script>

<style scoped>
.search-filter {
  margin: 20px;
}

.filter-group {
  margin-bottom: 10px;
}

.search-results {
  margin-top: 20px;
}
</style>
```
