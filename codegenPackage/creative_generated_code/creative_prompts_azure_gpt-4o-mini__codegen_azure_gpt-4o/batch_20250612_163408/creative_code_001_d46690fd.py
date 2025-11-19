"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Write a VueJS code snippet that implements a dynamic form validation feature as discussed by Tim Mansell.
Generated: DETERMINISTIC_d46690fde9941ec1
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div v-for="(field, index) in formFields" :key="index" class="form-group">
        <label :for="field.name">{{ field.label }}</label>
        <input
          :type="field.type"
          :id="field.name"
          :name="field.name"
          v-model="field.value"
          @input="validateField(field)"
          :class="{ 'is-invalid': field.error }"
        />
        <div v-if="field.error" class="error-message">
          {{ field.error }}
        </div>
      </div>
      <button type="submit" :disabled="!isFormValid">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formFields: [
        {
          name: 'email',
          label: 'Email',
          type: 'email',
          value: '',
          error: null,
          validations: [
            { rule: 'required', message: 'Email is required.' },
            { rule: 'email', message: 'Must be a valid email address.' },
          ],
        },
        {
          name: 'password',
          label: 'Password',
          type: 'password',
          value: '',
          error: null,
          validations: [
            { rule: 'required', message: 'Password is required.' },
            { rule: 'minLength', value: 6, message: 'Password must be at least 6 characters long.' },
          ],
        },
      ],
    };
  },
  computed: {
    // Check if the entire form is valid
    isFormValid() {
      return this.formFields.every((field) => !field.error && field.value);
    },
  },
  methods: {
    // Handle form submission
    handleSubmit() {
      if (this.isFormValid) {
        alert('Form submitted successfully!');
        // Perform additional actions such as API calls
      }
    },
    // Validate a single field based on its rules
    validateField(field) {
      field.error = null; // Reset error before validation
      for (const validation of field.validations) {
        if (validation.rule === 'required' && !field.value) {
          field.error = validation.message;
          break;
        }
        if (validation.rule === 'email' && !this.isValidEmail(field.value)) {
          field.error = validation.message;
          break;
        }
        if (validation.rule === 'minLength' && field.value.length < validation.value) {
          field.error = validation.message;
          break;
        }
      }
    },
    // Utility method to validate email format
    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    },
  },
};
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}

.is-invalid {
  border-color: red;
}

.error-message {
  color: red;
  font-size: 0.875rem;
}
</style>
```
