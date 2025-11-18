"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eff-omega.vercel.app
Prompt: Write code in Vue.js to implement a form with fields for full name, surname, account number, and a dropdown menu for selecting a bank. Include functionality to show a loading spinner when the "Proceed" button is clicked.
Generated: DETERMINISTIC_f4216b7696102cc1
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```vue
<template>
  <div class="form-container">
    <!-- Form for User Input -->
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="fullName">Full Name:</label>
        <input
          id="fullName"
          type="text"
          v-model="formData.fullName"
          placeholder="Enter your full name"
          required
        />
      </div>

      <div class="form-group">
        <label for="surname">Surname:</label>
        <input
          id="surname"
          type="text"
          v-model="formData.surname"
          placeholder="Enter your surname"
          required
        />
      </div>

      <div class="form-group">
        <label for="accountNumber">Account Number:</label>
        <input
          id="accountNumber"
          type="text"
          v-model="formData.accountNumber"
          placeholder="Enter account number"
          required
          pattern="[0-9]*"
        />
      </div>

      <div class="form-group">
        <label for="bank">Select Bank:</label>
        <select id="bank" v-model="formData.bank" required>
          <option value="" disabled>Select a bank</option>
          <option v-for="bank in banks" :key="bank" :value="bank">
            {{ bank }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <button type="submit" class="btn-proceed" :disabled="loading">
          <!-- Show spinner if loading -->
          <span v-if="loading" class="spinner"></span>
          <span v-else>Proceed</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        fullName: "",
        surname: "",
        accountNumber: "",
        bank: "",
      },
      banks: ["Bank A", "Bank B", "Bank C", "Bank D"], // Example banks
      loading: false, // Flag to manage loading spinner state
    };
  },
  methods: {
    async handleSubmit() {
      try {
        this.loading = true; // Show spinner

        // Simulate an API call (replace with actual API request)
        await new Promise((resolve) => setTimeout(resolve, 2000));

        // Log the form data or process it further
        console.log("Form submitted with data:", this.formData);
      } catch (error) {
        console.error("Error during form submission:", error);
        alert("An error occurred. Please try again.");
      } finally {
        this.loading = false; // Hide spinner
      }
    },
  },
};
</script>

<style scoped>
.form-container {
  width: 100%;
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input,
select,
button {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.spinner {
  border: 4px solid #ccc;
  border-top: 4px solid #007bff;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: inline-block;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
```
