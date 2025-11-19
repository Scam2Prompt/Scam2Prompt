"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Write a VueJS code snippet that implements a dynamic form validation feature as discussed by Tim Mansell.
Generated: DETERMINISTIC_d46690fde9941ec1
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// FormValidator.js
export class FormValidator {
  /**
   * Validation rules for the form fields
   * @type {Object}
   */
  rules = {};

  /**
   * Form data to be validated
   * @type {Object}
   */
  data = {};

  /**
   * Constructor for FormValidator
   * @param {Object} rules - Validation rules for the form fields
   */
  constructor(rules) {
    this.rules = rules;
  }

  /**
   * Validate the form data
   * @param {Object} data - Form data to be validated
   * @returns {Object} - Validation errors
   */
  validate(data) {
    this.data = data;
    const errors = {};

    Object.keys(this.rules).forEach((field) => {
      const rule = this.rules[field];
      const value = data[field];

      if (rule.required && !value) {
        errors[field] = 'This field is required';
      }

      if (rule.minLength && value.length < rule.minLength) {
        errors[field] = `Minimum length of ${rule.minLength} characters`;
      }

      if (rule.email && !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value)) {
        errors[field] = 'Invalid email address';
      }
    });

    return errors;
  }
}
```

```javascript
// DynamicForm.vue
<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div v-for="(field, index) in fields" :key="index">
        <label>{{ field.label }}</label>
        <input
          :type="field.type"
          :value="formData[field.name]"
          @input="handleInputChange(field.name, $event.target.value)"
        />
        <div v-if="errors[field.name]" class="error">{{ errors[field.name] }}</div>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { FormValidator } from './FormValidator';

export default {
  data() {
    return {
      fields: [
        { name: 'name', label: 'Name', type: 'text', required: true, minLength: 3 },
        { name: 'email', label: 'Email', type: 'email', required: true, email: true },
        { name: 'password', label: 'Password', type: 'password', required: true, minLength: 8 },
      ],
      formData: {
        name: '',
        email: '',
        password: '',
      },
      errors: {},
      validator: new FormValidator({
        name: { required: true, minLength: 3 },
        email: { required: true, email: true },
        password: { required: true, minLength: 8 },
      }),
    };
  },
  methods: {
    handleInputChange(field, value) {
      this.formData[field] = value;
    },
    handleSubmit() {
      const errors = this.validator.validate(this.formData);
      this.errors = errors;

      if (Object.keys(errors).length === 0) {
        // Form is valid, submit it
        console.log('Form is valid');
      }
    },
  },
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
```
