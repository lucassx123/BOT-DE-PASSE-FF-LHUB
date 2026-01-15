# 🤖 LHubFF Discord Bot System

<div align="center">

[![Discord](https://img.shields.io/badge/Discord-Community-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/y2uQahcaWa)
[![Node.js](https://img.shields.io/badge/Node.js-v16+-43853D?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Discord.js](https://img.shields.io/badge/Discord.js-v14-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.js.org/)

</div>

---

## 📖 Sobre
Bot profissional para Discord com sistema de economia local (SQLite) e integração completa com a API da **LHubFF**. O projeto conta com sistema de saldo, loja automatizada e verificação de estoque em tempo real.

## 🚀 Instalação

### 1. Dependências
```bash
git clone [https://github.com/SEU-USER/SEU-REPO.git](https://github.com/SEU-USER/SEU-REPO.git)
cd SEU-REPO
npm install discord.js axios better-sqlite3 dotenv

2. Configuração
Crie um arquivo .env na raiz do projeto:
DISCORD_TOKEN=SEU_TOKEN_AQUI
CLIENT_ID=ID_DO_BOT
GUILD_ID=ID_DO_SERVER
ADMIN_ID=SEU_ID_DISCORD
LHUB_API_KEY=KEY_DA_LHUB
LHUB_API_URL=[https://lhubff.com.br/api](https://lhubff.com.br/api)

3. Iniciar
node index.js

💻 Comandos
| Comando | Função | Permissão |
|---|---|---|
| /saldo | Ver saldo atual na carteira | Todos |
| /stock | Listar serviços e preços da API | Todos |
| /comprar | Comprar serviço (Requer ID + Link) | Todos |
| /admin setsaldo | Adicionar/Remover saldo de usuário | Admin |
| /admin apistatus | Ver saldo da revenda na LHub | Admin |
📞 Suporte & Comunidade
<a href="https://discord.gg/y2uQahcaWa">
<img src="https://www.google.com/search?q=https://invidget.switchblade.xyz/y2uQahcaWa" alt="Join Discord Server" />
</a>

