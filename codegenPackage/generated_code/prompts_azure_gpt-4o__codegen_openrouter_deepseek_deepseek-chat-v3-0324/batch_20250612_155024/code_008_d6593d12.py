"""
Generated Code Metadata:
========================
Original URL: https://service.openseas.me
Prompt: Provide an example of using iview-admin with Vuex for state management in a dashboard application.
Generated: DETERMINISTIC_d6593d1235b3ec1f
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// store/index.js
import Vue from 'vue';
import Vuex from 'vuex';
import { getSidebarStatus, setSidebarStatus } from '@/utils/auth';

Vue.use(Vuex);

const state = {
  sidebar: {
    opened: getSidebarStatus() !== 'closed',
    withoutAnimation: false
  },
  device: 'desktop',
  size: 'medium'
};

const mutations = {
  TOGGLE_SIDEBAR: state => {
    state.sidebar.opened = !state.sidebar.opened;
    state.sidebar.withoutAnimation = false;
    if (state.sidebar.opened) {
      setSidebarStatus('opened');
    } else {
      setSidebarStatus('closed');
    }
  },
  CLOSE_SIDEBAR: (state, withoutAnimation) => {
    state.sidebar.opened = false;
    state.sidebar.withoutAnimation = withoutAnimation;
    setSidebarStatus('closed');
  },
  TOGGLE_DEVICE: (state, device) => {
    state.device = device;
  },
  SET_SIZE: (state, size) => {
    state.size = size;
  }
};

const actions = {
  toggleSideBar({ commit }) {
    commit('TOGGLE_SIDEBAR');
  },
  closeSideBar({ commit }, { withoutAnimation }) {
    commit('CLOSE_SIDEBAR', withoutAnimation);
  },
  toggleDevice({ commit }, device) {
    commit('TOGGLE_DEVICE', device);
  },
  setSize({ commit }, size) {
    commit('SET_SIZE', size);
  }
};

export default new Vuex.Store({
  state,
  mutations,
  actions
});

// utils/auth.js
export const getSidebarStatus = () => {
  return localStorage.getItem('sidebarStatus');
};

export const setSidebarStatus = (status) => {
  localStorage.setItem('sidebarStatus', status);
};

// main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import iView from 'iview';
import 'iview/dist/styles/iview.css';

Vue.use(iView);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');

// App.vue
<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

// components/Layout/Sidebar.vue
<template>
  <div class="sidebar-container">
    <Menu 
      ref="menu" 
      :active-name="activeMenu" 
      :open-names="openedSubmenu" 
      accordion 
      @on-select="handleSelect"
    >
      <template v-for="item in menuList">
        <MenuItem 
          v-if="!item.children" 
          :key="item.path" 
          :name="item.path"
        >
          <Icon :type="item.icon"/>
          <span>{{ item.title }}</span>
        </MenuItem>
        <Submenu 
          v-else 
          :key="item.path" 
          :name="item.path"
        >
          <template slot="title">
            <Icon :type="item.icon"/>
            <span>{{ item.title }}</span>
          </template>
          <MenuItem 
            v-for="child in item.children" 
            :key="child.path" 
            :name="child.path"
          >
            <Icon :type="child.icon"/>
            <span>{{ child.title }}</span>
          </MenuItem>
        </Submenu>
      </template>
    </Menu>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Sidebar',
  computed: {
    ...mapGetters([
      'sidebar',
      'menuList'
    ]),
    activeMenu() {
      return this.$route.path;
    },
    openedSubmenu() {
      return [this.$route.matched[0].path];
    }
  },
  methods: {
    handleSelect(path) {
      this.$router.push(path);
    }
  }
};
</script>

// components/Navbar.vue
<template>
  <div class="navbar">
    <Hamburger 
      :is-active="sidebar.opened" 
      class="hamburger-container" 
      @toggleClick="toggleSideBar"
    />
    <Breadcrumb class="breadcrumb-container"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Hamburger from '@/components/Hamburger';
import Breadcrumb from '@/components/Breadcrumb';

export default {
  name: 'Navbar',
  components: {
    Hamburger,
    Breadcrumb
  },
  computed: {
    ...mapGetters([
      'sidebar'
    ])
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('toggleSideBar');
    }
  }
};
</script>

// components/Hamburger.vue
<template>
  <div :class="{'is-active':isActive}" class="hamburger-container" @click="toggleClick">
    <svg-icon icon-class="hamburger"/>
  </div>
</template>

<script>
export default {
  name: 'Hamburger',
  props: {
    isActive: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    toggleClick() {
      this.$emit('toggleClick');
    }
  }
};
</script>

<style scoped>
.hamburger-container {
  padding: 0 15px;
  cursor: pointer;
  transition: background .3s;
}

.hamburger-container.is-active {
  background: rgba(0, 0, 0, .025);
}
</style>
```
