<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from 'axios';

// Define the type for a page item
interface PageItem {
  id: number;
  title: string;
  meta: {
    html_description?: string;
    [key: string]: unknown;
  };
  [key: string]: unknown;
}

const pages = ref<PageItem[]>([]);

onMounted(async () => {
  const res = await axios.get('http://localhost:8000/api/v2/pages/');
  pages.value = res.data.items;

  console.log(pages.value);
});
</script>

<template>
  <q-page>
    <div v-for="page in pages" :key="page.id">
      <h2>{{ page.title }}</h2>
      <p v-html="page.meta.html_description || ''" />
    </div>
  </q-page>
</template>
