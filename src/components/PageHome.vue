<template>
    <header>
        <h1>BLOG</h1>
        <div class="buttons">
        
            <RouterLink class="button" to="/stage_B2" > Stage B2 </RouterLink>

            <RouterLink class="button" to="/a_propos"> A propos </RouterLink>

        </div>
    </header>
    <footer>
        <p>&copy; 2024 Blog</p>
    </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style lang="scss" scoped>

</style>