<template>
  <q-page padding>
    <div v-for="page in pages" :key="page.id">
      <h1>{{ page.title }}</h1>
      <div v-for="block in page.body" :key="block.id">
        <component :is="resolveBlock(block)" :block="block" />
      </div>
    </div>
  </q-page>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { fetchPages } from 'src/services/wagtail';

// Define types for block and page
type Block = {
  id: number | string;
  type: string;
  // other block fields as needed
};

type Page = {
  id: number | string;
  title: string;
  body: Block[];
  // other page fields as needed
};

const pages = ref<Page[]>([]);

onMounted(async () => {
  pages.value = await fetchPages();
});

function resolveBlock(block: Block) {
  if (block.type === 'heading') return 'HeadingBlock';
  if (block.type === 'paragraph') return 'ParagraphBlock';
  return 'div';
}
</script>
