"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--compassionate-wing-d4bcd6.netlify.app
Prompt: Provide a code example demonstrating how vue-diet simplifies state management in Vue.js projects.
Generated: DETERMINISTIC_fe2f4bf393547c88
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing Vue and VueDiet
import { createApp } from 'vue';
import { createStore } from 'vue-diet';

// Defining the initial state
const initialState = {
  counter: 0,
  message: 'Hello, VueDiet!',
};

// Creating a store using vue-diet
const store = createStore({
  state: initialState,

  // Defining actions to mutate the state
  actions: {
    increment(state) {
      state.counter += 1; // Increment counter
    },
    decrement(state) {
      state.counter -= 1; // Decrement counter
    },
    setMessage(state, newMessage) {
      state.message = newMessage; // Update the message
    },
  },
});

// Creating the root Vue component
const App = {
  template: `
    <div>
      <h1>{{ store.message }}</h1>
      <p>Counter: {{ store.counter }}</p>
      <button @click="store.increment()">Increment</button>
      <button @click="store.decrement()">Decrement</button>
      <button @click="updateMessage">Update Message</button>
    </div>
  `,
  // Using vue-diet's global state directly in the component
  computed: {
    store() {
      return store.state; // Accessing store state
    },
  },
  methods: {
    updateMessage() {
      // Using actions to update state
      store.setMessage('State management made easy with VueDiet!');
    },
  },
};

// Creating and mounting the Vue application
const app = createApp(App);
app.mount('#app');
```
