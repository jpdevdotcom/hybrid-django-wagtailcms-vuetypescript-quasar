import { api } from 'src/boot/axios';

export async function fetchPages() {
  const response = await api.get('pages/?type=home.ArticlePage');
  return response.data.items;
}
