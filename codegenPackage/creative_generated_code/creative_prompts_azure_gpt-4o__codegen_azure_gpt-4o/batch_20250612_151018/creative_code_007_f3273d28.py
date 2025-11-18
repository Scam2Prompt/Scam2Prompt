"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--compassionate-wing-d4bcd6.netlify.app
Prompt: Write code to integrate vue-diet with Vue Router for lightweight navigation in a Vue.js application.
Generated: DETERMINISTIC_f3273d282870aaa9
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Vue, Vue Router, and vue-diet
import Vue from 'vue';
import VueRouter from 'vue-router';
import { createRouter } from 'vue-diet';

// Enable Vue Router
Vue.use(VueRouter);

// Define your components (these would usually be imported from separate files)
const Home = { template: '<div>Home Page</div>' };
const About = { template: '<div>About Page</div>' };
const Contact = { template: '<div>Contact Page</div>' };

// Define your routes
const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/contact', component: Contact },
];

// Create the lightweight router using vue-diet
const router = createRouter({
  mode: 'history', // Use history mode for clean URLs (fallback to hash mode if unsupported)
  routes,          // Pass the defined routes
});

// Handle navigation errors (e.g., navigation to a non-existent route)
router.onError((error) => {
  console.error('Router Error:', error.message);
});

// Create the Vue instance and mount the application
new Vue({
  el: '#app',   // Mount point for the application
  router,       // Integrate the vue-diet router
  render: (h) => h('router-view'), // Render the active route
});
```
