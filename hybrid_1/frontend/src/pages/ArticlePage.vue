<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from 'axios';

interface ArticleItem {
  id: number;
  title: string;
  intro: string;
  body: string;
  meta: {
    slug: string;
  };
}

const articles = ref<ArticleItem[]>([]);

onMounted(async () => {
  const res = await axios.get(
    'http://localhost:8000/api/v2/pages/?type=home.ArticlePage&fields=title,intro,body,slug',
  );
  articles.value = res.data.items;

  console.log(articles.value);
});
</script>

<template>
  <q-page class="q-pa-md bg-grey-1">
    <q-card v-for="article in articles" :key="article.id" class="q-mb-md">
      <q-card-section>
        <div class="text-h6">{{ article.title }}</div>
        <div class="text-subtitle2 text-grey-7 q-mt-sm" v-html="article.intro" />
        <div class="q-mt-sm" v-html="article.body" />
      </q-card-section>
    </q-card>
  </q-page>
</template>
