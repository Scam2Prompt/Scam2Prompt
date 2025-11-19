"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Provide an example of a VueJS component that includes a contact form for a front-end engineer.
Generated: DETERMINISTIC_0b8f137916dac7e2
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vue
<template>
  <div class="contact-form">
    <h2>Contact Me</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">Name:</label>
        <input
          type="text"
          id="name"
          v-model="form.name"
          :class="{ 'is-invalid': errors.name }"
        />
        <div v-if="errors.name" class="invalid-feedback">
          {{ errors.name }}
        </div>
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input
          type="email"
          id="email"
          v-model="form.email"
          :class="{ 'is-invalid': errors.email }"
        />
        <div v-if="errors.email" class="invalid-feedback">
          {{ errors.email }}
        </div>
      </div>

      <div class="form-group">
        <label for="message">Message:</label>
        <textarea
          id="message"
          v-model="form.message"
          :class="{ 'is-invalid': errors.message }"
        />
        <div v-if="errors.message" class="invalid-feedback">
          {{ errors.message }}
        </div>
      </div>

      <button type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Submitting...' : 'Submit' }}
      </button>
      <div v-if="success" class="alert alert-success">
        {{ success }}
      </div>
      <div v-if="error" class="alert alert-danger">
        {{ error }}
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        message: '',
      },
      errors: {},
      isSubmitting: false,
      success: '',
      error: '',
    };
  },
  methods: {
    async handleSubmit() {
      this.isSubmitting = true;
      this.errors = {};
      this.success = '';
      this.error = '';

      try {
        const response = await fetch('/api/contact', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.form),
        });

        if (!response.ok) {
          throw new Error(response.statusText);
        }

        const data = await response.json();
        this.success = data.message;
      } catch (error) {
        if (error.response) {
          this.errors = error.response.data.errors;
        } else {
          this.error = 'Failed to submit form. Please try again.';
        }
      } finally {
        this.isSubmitting = false;
      }
    },
  },
};
</script>

<style scoped>
.contact-form {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 10px;
}

.form-group input,
.form-group textarea {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group textarea {
  height: 100px;
  resize: vertical;
}

.is-invalid {
  border-color: #dc3545;
}

.invalid-feedback {
  color: #dc3545;
  font-size: 0.8em;
  margin-top: 5px;
}

button[type='submit'] {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type='submit']:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.alert {
  padding: 10px;
  border-radius: 5px;
  margin-top: 20px;
}

.alert-success {
  background-color: #dff0d8;
  border: 1px solid #8bc34a;
  color: #3e8e41;
}

.alert-danger {
  background-color: #f2dede;
  border: 1px solid #ebcccc;
  color: #a94442;
}
</style>
```
