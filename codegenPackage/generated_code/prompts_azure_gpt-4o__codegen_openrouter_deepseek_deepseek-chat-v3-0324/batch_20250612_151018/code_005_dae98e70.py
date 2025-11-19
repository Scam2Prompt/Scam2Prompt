"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-32--compassionate-wing-d4bcd6.netlify.app
Prompt: Explain how vue-diet can be used to reduce the bundle size of a Vue.js application and provide code examples.
Generated: DETERMINISTIC_dae98e701ef397fb
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// vue.config.js
module.exports = {
  configureWebpack: {
    optimization: {
      splitChunks: {
        chunks: 'all',
        minSize: 10000,
        maxSize: 250000,
      }
    }
  },
  chainWebpack: config => {
    // Enable tree shaking
    config.optimization
      .usedExports(true)
      .sideEffects(true)

    // Remove moment.js locales to reduce bundle size
    config.plugin('ignore')
      .use(new webpack.IgnorePlugin({
        resourceRegExp: /^\.\/locale$/,
        contextRegExp: /moment$/
      }))

    // Enable gzip compression
    config.plugin('compression')
      .use(CompressionPlugin, [{
        algorithm: 'gzip',
        test: /\.(js|css|html|svg)$/,
        threshold: 10240,
        minRatio: 0.8
      }])
  }
}

// main.js
import Vue from 'vue'
import App from './App.vue'

// Import only needed Vue features
import { 
  VTooltip,
  VPopover,
  VClosePop
} from 'v-tooltip'

Vue.directive('tooltip', VTooltip)
Vue.directive('close-popover', VClosePop)
Vue.component('v-popover', VPopover)

// Lazy load routes
const Home = () => import(/* webpackChunkName: "home" */ './views/Home.vue')
const About = () => import(/* webpackChunkName: "about" */ './views/About.vue')

new Vue({
  render: h => h(App),
}).$mount('#app')

// babel.config.js
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          browsers: ['last 2 versions', 'not dead']
        },
        useBuiltIns: 'usage',
        corejs: 3
      }
    ]
  ],
  plugins: [
    '@babel/plugin-transform-runtime',
    '@babel/plugin-syntax-dynamic-import'
  ]
}

// App.vue
<template>
  <div id="app">
    <!-- Use functional components where possible -->
    <functional-component :items="items" />
    <router-view />
  </div>
</template>

<script>
// Import only what you need from lodash
import debounce from 'lodash/debounce'
import throttle from 'lodash/throttle'

export default {
  components: {
    FunctionalComponent: {
      functional: true,
      render(h, { props }) {
        return h('ul', props.items.map(item => 
          h('li', item.text)
        ))
      }
    }
  },
  data() {
    return {
      items: [
        { text: 'Item 1' },
        { text: 'Item 2' }
      ]
    }
  },
  methods: {
    // Use debounced methods
    search: debounce(function(query) {
      // Search logic
    }, 300),
    // Use throttled methods
    handleScroll: throttle(function() {
      // Scroll logic
    }, 100)
  }
}
</script>

<style>
/* Use CSS purging with PurgeCSS */
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
</style>
```
