"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://service.openseas.me
Prompt: Write code to implement role-based access control in an iview-admin application using Vue.js.
Generated: DETERMINISTIC_3d862dfa160d9ad4
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/store/modules/permission.js
import { asyncRoutes, constantRoutes } from '@/router';

/**
 * Use meta.role to determine if the current user has permission
 * @param roles
 * @param route
 */
function hasPermission(roles, route) {
  if (route.meta && route.meta.roles) {
    return roles.some(role => route.meta.roles.includes(role));
  }
  return true;
}

/**
 * Filter asynchronous routing tables by roles
 * @param routes asyncRoutes
 * @param roles
 */
export function filterAsyncRoutes(routes, roles) {
  const res = [];

  routes.forEach(route => {
    const tmp = { ...route };
    if (hasPermission(roles, tmp)) {
      if (tmp.children) {
        tmp.children = filterAsyncRoutes(tmp.children, roles);
      }
      res.push(tmp);
    }
  });

  return res;
}

const state = {
  routes: [],
  dynamicRoutes: []
};

const mutations = {
  SET_ROUTES(state, routes) {
    state.routes = constantRoutes.concat(routes);
    state.dynamicRoutes = routes;
  }
};

const actions = {
  generateRoutes({ commit }, roles) {
    return new Promise(resolve => {
      let accessedRoutes;
      if (roles.includes('admin')) {
        accessedRoutes = asyncRoutes || [];
      } else {
        accessedRoutes = filterAsyncRoutes(asyncRoutes, roles);
      }
      commit('SET_ROUTES', accessedRoutes);
      resolve(accessedRoutes);
    });
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};

// src/router/index.js
import Vue from 'vue';
import Router from 'vue-router';
import Layout from '@/layout';

Vue.use(Router);

// Define constant routes accessible to all roles
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () => import('@/views/dashboard'),
        meta: { title: 'Dashboard', icon: 'dashboard' }
      }
    ]
  }
];

// Define async routes requiring role-based access
export const asyncRoutes = [
  {
    path: '/admin',
    component: Layout,
    redirect: '/admin/manage-users',
    meta: { roles: ['admin'] }, // Only accessible to 'admin' role
    children: [
      {
        path: 'manage-users',
        name: 'ManageUsers',
        component: () => import('@/views/admin/manage-users'),
        meta: { title: 'Manage Users', icon: 'user', roles: ['admin'] }
      }
    ]
  },
  {
    path: '/user',
    component: Layout,
    redirect: '/user/profile',
    meta: { roles: ['user', 'admin'] }, // Accessible to 'user' and 'admin' roles
    children: [
      {
        path: 'profile',
        name: 'UserProfile',
        component: () => import('@/views/user/profile'),
        meta: { title: 'User Profile', icon: 'profile', roles: ['user', 'admin'] }
      }
    ]
  },
  { path: '*', redirect: '/404', hidden: true }
];

const createRouter = () =>
  new Router({
    mode: 'history', // Use history mode for clean URLs
    scrollBehavior: () => ({ y: 0 }),
    routes: constantRoutes
  });

const router = createRouter();

// Reset router (useful for dynamically adding routes based on roles)
export function resetRouter() {
  const newRouter = createRouter();
  router.matcher = newRouter.matcher; // Reset router
}

export default router;

// src/main.js
import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import '@/permission'; // Role-based access control

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
});

// src/permission.js
import router from './router';
import store from './store';
import { Message } from 'view-design';
import NProgress from 'nprogress'; // Progress bar
import 'nprogress/nprogress.css'; // Progress bar styles

NProgress.configure({ showSpinner: false }); // Progress bar config

const whiteList = ['/login']; // No role requirement

router.beforeEach(async (to, from, next) => {
  NProgress.start();

  const hasToken = store.getters.token; // Assume token is stored in Vuex store

  if (hasToken) {
    if (to.path === '/login') {
      next({ path: '/' });
      NProgress.done();
    } else {
      const hasRoles = store.getters.roles && store.getters.roles.length > 0;

      if (hasRoles) {
        next();
      } else {
        try {
          const { roles } = await store.dispatch('user/getInfo'); // Get user roles
          const accessRoutes = await store.dispatch('permission/generateRoutes', roles);

          router.addRoutes(accessRoutes); // Dynamically add accessible routes
          next({ ...to, replace: true });
        } catch (error) {
          await store.dispatch('user/resetToken');
          Message.error(error || 'Has Error');
          next(`/login?redirect=${to.path}`);
          NProgress.done();
        }
      }
    }
  } else {
    if (whiteList.includes(to.path)) {
      next();
    } else {
      next(`/login?redirect=${to.path}`);
      NProgress.done();
    }
  }
});

router.afterEach(() => {
  NProgress.done(); // Finish progress bar
});
```
