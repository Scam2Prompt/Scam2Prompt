"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://service.openseas.me
Prompt: Provide an example of using iview-admin to create a responsive sidebar navigation menu with dynamic routing.
Generated: DETERMINISTIC_b8333c8d6b5556ef
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/router/index.js
// Vue Router configuration for dynamic routing
import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

// Dynamic routes to be loaded
export const dynamicRoutes = [
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue'),
    meta: { title: 'Dashboard', icon: 'md-speedometer' }
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('@/views/Settings.vue'),
    meta: { title: 'Settings', icon: 'md-settings' }
  }
];

// Base routes (always loaded)
export const baseRoutes = [
  {
    path: '/',
    name: 'Home',
    redirect: '/dashboard'
  },
  {
    path: '*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue'),
    meta: { title: '404', icon: 'md-alert' }
  }
];

// Create and export the router instance
const router = new Router({
  mode: 'history',
  routes: [...baseRoutes, ...dynamicRoutes]
});

export default router;
```

```javascript
// src/store/modules/sidebar.js
// Vuex module for managing the sidebar state
const state = {
  isSidebarOpen: true // State to toggle sidebar visibility
};

const mutations = {
  TOGGLE_SIDEBAR(state) {
    state.isSidebarOpen = !state.isSidebarOpen;
  }
};

const actions = {
  toggleSidebar({ commit }) {
    commit('TOGGLE_SIDEBAR');
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};
```

```vue
<!-- src/layouts/MainLayout.vue -->
<template>
  <div :class="['main-layout', { 'sidebar-collapsed': !isSidebarOpen }]">
    <!-- Sidebar -->
    <SideMenu :routes="routes" :is-sidebar-open="isSidebarOpen" />
    <!-- Content -->
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import SideMenu from '@/components/SideMenu.vue'; // Dynamic sidebar component

export default {
  components: {
    SideMenu
  },
  computed: {
    ...mapState({
      isSidebarOpen: state => state.sidebar.isSidebarOpen
    }),
    routes() {
      // Dynamically pass routes from router configuration
      return this.$router.options.routes.filter(route => route.meta && route.meta.title);
    }
  }
};
</script>

<style scoped>
.main-layout {
  display: flex;
}
.sidebar-collapsed .content {
  margin-left: 50px;
}
.content {
  flex: 1;
  margin-left: 200px;
}
</style>
```

```vue
<!-- src/components/SideMenu.vue -->
<template>
  <div :class="['side-menu', { 'collapsed': !isSidebarOpen }]">
    <ul>
      <li v-for="route in routes" :key="route.path">
        <router-link :to="route.path">
          <Icon :type="route.meta.icon" />
          <span v-if="isSidebarOpen">{{ route.meta.title }}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import Icon from 'iview/src/components/icon';

export default {
  props: {
    routes: {
      type: Array,
      required: true
    },
    isSidebarOpen: {
      type: Boolean,
      required: true
    }
  },
  components: {
    Icon
  }
};
</script>

<style scoped>
.side-menu {
  width: 200px;
  transition: width 0.3s;
}
.side-menu.collapsed {
  width: 50px;
}
.side-menu ul {
  list-style: none;
  padding: 0;
}
.side-menu li {
  display: flex;
  align-items: center;
}
.side-menu li span {
  margin-left: 10px;
}
</style>
```

```vue
<!-- src/App.vue -->
<template>
  <MainLayout />
</template>

<script>
import MainLayout from '@/layouts/MainLayout.vue';

export default {
  components: {
    MainLayout
  }
};
</script>
```

```javascript
// src/main.js
// Main entry file for the application
import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import iView from 'iview';
import 'iview/dist/styles/iview.css'; // Import iView styles

Vue.config.productionTip = false;
Vue.use(iView);

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app');
```

```javascript
// src/store/index.js
// Vuex store configuration
import Vue from 'vue';
import Vuex from 'vuex';
import sidebar from './modules/sidebar';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    sidebar
  }
});
```
