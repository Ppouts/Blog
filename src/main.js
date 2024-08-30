import './assets/main.css'
import { createMemoryHistory, createRouter } from 'vue-router'

import PageHome from './components/PageHome.vue'
import PageCahier from './components/PageCahier.vue'
import PageStage from './components/PageStage.vue'
import PageAPropos from './components/PageAPropos.vue'

import { createApp } from 'vue'
import App from './App.vue'

const routes = [
    { path: '/', component: PageHome },
    { path: '/stage_B2', component: PageStage },
    { path: '/cahier_des_charges', component: PageCahier },
    { path: '/a_propos', component: PageAPropos },
  ]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
