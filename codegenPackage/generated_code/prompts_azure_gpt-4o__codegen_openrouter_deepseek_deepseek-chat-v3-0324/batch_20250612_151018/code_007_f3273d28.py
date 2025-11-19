"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-32--compassionate-wing-d4bcd6.netlify.app
Prompt: Write code to integrate vue-diet with Vue Router for lightweight navigation in a Vue.js application.
Generated: DETERMINISTIC_f3273d282870aaa9
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// main.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import VueDiet from 'vue-diet';
import App from './App.vue';

// Initialize Vue plugins
Vue.use(VueRouter);
Vue.use(VueDiet);

// Define routes
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('./views/Home.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('./views/About.vue')
  },
  {
    path: '*',
    redirect: '/'
  }
];

// Create router instance
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

// Handle navigation errors
router.onError((error) => {
  console.error('Router error:', error);
});

// Create and mount Vue instance
new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
```

```javascript
// App.vue
<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  created() {
    // Initialize vue-diet with router
    this.$diet.init({
      router: this.$router,
      debug: process.env.NODE_ENV !== 'production'
    });
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

```javascript
// views/Home.vue
<template>
  <div class="home">
    <h1>Home Page</h1>
    <p>This is a lightweight page loaded via vue-diet</p>
  </div>
</template>

<script>
export default {
  name: 'Home',
  metaInfo: {
    title: 'Home'
  }
};
</script>
```

```javascript
// views/About.vue
<template>
  <div class="about">
    <h1>About Page</h1>
    <p>This is another lightweight page loaded via vue-diet</p>
  </div>
</template>

<script>
export default {
  name: 'About',
  metaInfo: {
    title: 'About'
  }
};
</script>
```
