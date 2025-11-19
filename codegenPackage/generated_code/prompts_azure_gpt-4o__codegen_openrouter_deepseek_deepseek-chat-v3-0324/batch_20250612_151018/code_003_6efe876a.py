"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: Create a VueJS project structure that incorporates best practices for front-end engineering, as highlighted by Tim Mansell's work.
Generated: DETERMINISTIC_6efe876a3df7d1fe
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import './plugins'
import '@/assets/css/main.css'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
```

```javascript
// src/router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes'
import store from '@/store'
import { middlewarePipeline } from '@/middlewares'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { x: 0, y: 0 }
  }
})

router.beforeEach((to, from, next) => {
  const middlewares = to.meta.middlewares || []
  if (!middlewares.length) return next()

  const context = { to, from, next, store }
  return middlewares[0]({
    ...context,
    next: middlewarePipeline(context, middlewares, 1)
  })
})

export default router
```

```javascript
// src/router/routes.js
import authMiddleware from '@/middlewares/auth'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Home.vue'),
    meta: {
      title: 'Home'
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/auth/Login.vue'),
    meta: {
      title: 'Login',
      guest: true
    }
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/views/Dashboard.vue'),
    meta: {
      title: 'Dashboard',
      middlewares: [authMiddleware]
    }
  },
  {
    path: '*',
    name: '404',
    component: () => import('@/views/errors/404.vue'),
    meta: {
      title: '404 Not Found'
    }
  }
]

export default routes
```

```javascript
// src/store/index.js
import Vue from 'vue'
import Vuex from 'vuex'
import modules from './modules'

Vue.use(Vuex)

export default new Vuex.Store({
  modules,
  strict: process.env.NODE_ENV !== 'production'
})
```

```javascript
// src/store/modules/auth.js
const state = {
  user: null,
  token: localStorage.getItem('token') || null
}

const mutations = {
  SET_USER(state, user) {
    state.user = user
  },
  SET_TOKEN(state, token) {
    state.token = token
    localStorage.setItem('token', token)
  },
  CLEAR_AUTH(state) {
    state.user = null
    state.token = null
    localStorage.removeItem('token')
  }
}

const actions = {
  login({ commit }, credentials) {
    return new Promise((resolve, reject) => {
      // API call would go here
      commit('SET_USER', { name: 'Test User' })
      commit('SET_TOKEN', 'sample-token')
      resolve()
    })
  },
  logout({ commit }) {
    commit('CLEAR_AUTH')
  }
}

const getters = {
  isAuthenticated: state => !!state.token,
  currentUser: state => state.user
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
```

```javascript
// src/middlewares/auth.js
export default function authMiddleware({ next, store }) {
  if (!store.getters['auth/isAuthenticated']) {
    return next({
      name: 'login',
      query: { redirect: to.fullPath }
    })
  }
  return next()
}
```

```javascript
// src/middlewares/index.js
export function middlewarePipeline(context, middlewares, index) {
  const nextMiddleware = middlewares[index]
  if (!nextMiddleware) return context.next
  
  return () => {
    const nextPipeline = middlewarePipeline(
      context, middlewares, index + 1
    )
    nextMiddleware({ ...context, next: nextPipeline })
  }
}
```

```javascript
// src/plugins/index.js
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuelidate from 'vuelidate'
import Toasted from 'vue-toasted'

Vue.use(VueAxios, axios)
Vue.use(Vuelidate)
Vue.use(Toasted, {
  duration: 3000,
  position: 'top-right'
})
```

```javascript
// src/registerServiceWorker.js
import { register } from 'register-service-worker'

if (process.env.NODE_ENV === 'production') {
  register(`${process.env.BASE_URL}service-worker.js`, {
    ready() {
      console.log('App is being served from cache by a service worker.')
    },
    registered() {
      console.log('Service worker has been registered.')
    },
    cached() {
      console.log('Content has been cached for offline use.')
    },
    updatefound() {
      console.log('New content is downloading.')
    },
    updated() {
      console.log('New content is available; please refresh.')
    },
    offline() {
      console.log('No internet connection found. App is running in offline mode.')
    },
    error(error) {
      console.error('Error during service worker registration:', error)
    }
  })
}
```

```vue
<!-- src/App.vue -->
<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  metaInfo: {
    title: 'Default Title',
    titleTemplate: '%s | My App'
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
```

```vue
<!-- src/views/Home.vue -->
<template>
  <div class="home">
    <h1>Home Page</h1>
  </div>
</template>

<script>
export default {
  name: 'Home',
  metaInfo: {
    title: 'Home'
  }
}
</script>
```

```vue
<!-- src/views/Dashboard.vue -->
<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <p>Welcome, {{ currentUser.name }}</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  metaInfo: {
    title: 'Dashboard'
  },
  computed: {
    ...mapGetters('auth', ['currentUser'])
  }
}
</script>
```

```vue
<!-- src/views/auth/Login.vue -->
<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="handleSubmit">
      <input v-model="form.email" type="email" placeholder="Email">
      <input v-model="form.password" type="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  metaInfo: {
    title: 'Login'
  },
  data() {
    return {
      form: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async handleSubmit() {
      try {
        await this.$store.dispatch('auth/login', this.form)
        const redirect = this.$route.query.redirect || 'dashboard'
        this.$router.push(redirect)
      } catch (error) {
        this.$toasted.error('Login failed')
      }
    }
  }
}
</script>
```

```vue
<!-- src/views/errors/404.vue -->
<template>
  <div class="error-404">
    <h1>404 - Page Not Found</h1>
  </div>
</template>

<script>
export default {
  name: 'Error404',
  metaInfo: {
    title: '404 Not Found'
  }
}
</script>
```
