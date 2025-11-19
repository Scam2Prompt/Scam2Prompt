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

```html
<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div v-for="(field, index) in formFields" :key="index" class="form-field">
        <label :for="field.name">{{ field.label }}</label>
        <input
          v-model="formData[field.name]"
          :type="field.type"
          :name="field.name"
          :id="field.name"
          :placeholder="field.placeholder"
          @blur="validateField(field.name)"
        />
        <span v-if="fieldErrors[field.name]" class="error-message">
          {{ fieldErrors[field.name] }}
        </span>
      </div>
      <button type="submit" :disabled="isFormInvalid">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formFields: [
        { name: 'username', label: 'Username', type: 'text', placeholder: 'Enter your username', required: true },
        { name: 'email', label: 'Email', type: 'email', placeholder: 'Enter your email', required: true },
        { name: 'password', label: 'Password', type: 'password', placeholder: 'Enter your password', required: true }
      ],
      formData: {},
      fieldErrors: {}
    };
  },
  computed: {
    isFormInvalid() {
      // Check if any field has errors
      return Object.values(this.fieldErrors).some(error => error !== null);
    }
  },
  methods: {
    validateField(fieldName) {
      const field = this.formFields.find(f => f.name === fieldName);
      const value = this.formData[fieldName] || '';
      // Simple validation rules
      if (field.required && !value) {
        this.fieldErrors[fieldName] = `${field.label} is required.`;
      } else {
        this.fieldErrors[fieldName] = null; // Clear error
      }
    },
    handleSubmit() {
      // Validate all fields before submission
      this.formFields.forEach(field => this.validateField(field.name));
      if (this.isFormInvalid) {
        // If there are errors, do not proceed
        console.error('Form submission failed due to validation errors.', this.fieldErrors);
        return;
      }
      // Process form data (e.g., send to server)
      console.log('Form submitted successfully with data:', this.formData);
      // Reset form after successful submission
      this.resetForm();
    },
    resetForm() {
      this.formData = {};
      this.fieldErrors = {};
    }
  }
};
</script>

<style scoped>
.form-field {
  margin-bottom: 10px;
}
.error-message {
  color: red;
  font-size: 0.875em;
}
</style>
```
