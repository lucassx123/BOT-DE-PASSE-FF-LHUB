# 🤖 LHUB Discord Bot

Bot de Discord para integração com a API da **LHUB** - Fornecedor #1 de Passe de Elite e Likes do Brasil.

![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## ✨ Funcionalidades

- 🎮 **Envio de Passe de Elite** - Envia passe direto para o UID
- ❤️ **Envio de Likes** - Envia 100-250 likes para o perfil
- 👤 **Conta Guest** - Compra contas guest (UID:PASSWORD)
- 🚀 **Bypass UID** - Ativa bypass por 30 dias
- 💰 **Sistema de Saldo** - Controle de saldo por usuário
- 📊 **Estatísticas** - Dashboard completo para admins

## 📋 Comandos

### Usuários
| Comando | Descrição |
|---------|-----------|
| `/saldo` | Ver seu saldo atual |
| `/perfil` | Ver seu perfil completo |
| `/precos` | Ver tabela de preços |
| `/apisaldo` | Ver saldo da API LHUB |
| `/passe <uid> [mensagem]` | Enviar Passe de Elite |
| `/likes <uid>` | Enviar Likes |
| `/guest` | Comprar Conta Guest |
| `/bypass <uid> [dias]` | Ativar Bypass |
| `/ajuda` | Ver todos os comandos |

### Admin
| Comando | Descrição |
|---------|-----------|
| `/addsaldo <user> <valor>` | Adicionar saldo |
| `/removesaldo <user> <valor>` | Remover saldo |
| `/setsaldo <user> <valor>` | Definir saldo |
| `/versaldo <user>` | Ver saldo de usuário |
| `/ranking` | Ver ranking de saldo |
| `/stats` | Ver estatísticas do bot |

## 🚀 Instalação

### Pré-requisitos
- Python 3.10 ou superior
- Conta na [LHUB](https://passesff.squareweb.app)
- Bot do Discord criado no [Discord Developer Portal](https://discord.com/developers/applications)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/lucassx123/bot-vendas-passe-ff/lhub-discord-bot.git
cd lhub-discord-bot
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure o arquivo .env**
```bash
cp .env.example .env
```

4. **Edite o arquivo .env**
```env
DISCORD_TOKEN=seu_token_do_discord_aqui
LHUB_API_KEY=lhub_sua_api_key_aqui
LHUB_API_URL=https://passesff.squareweb.app
OWNER_ID=seu_id_do_discord
```

5. **Execute o bot**
```bash
python bot.py
```

## ⚙️ Configuração

### Obtendo o Token do Discord

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em **New Application**
3. Dê um nome ao seu bot e clique em **Create**
4. Vá para a aba **Bot**
5. Clique em **Reset Token** e copie o token
6. Ative as **Privileged Gateway Intents**:
   - PRESENCE INTENT
   - SERVER MEMBERS INTENT
   - MESSAGE CONTENT INTENT

### Obtendo a API Key da LHUB

1. Acesse [LHUB](https://passesff.squareweb.app)
2. Faça login ou crie uma conta
3. Vá para **Dashboard > API**
4. Gere sua API Key
5. Adicione saldo na sua conta

### Obtendo seu ID do Discord

1. Ative o **Modo Desenvolvedor** no Discord
   - Configurações > Avançado > Modo Desenvolvedor
2. Clique com o botão direito no seu perfil
3. Clique em **Copiar ID**

### Convidando o Bot

Use este link (substitua `CLIENT_ID` pelo ID do seu bot):
```
https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=8&scope=bot%20applications.commands
```

## 🌐 Hospedagem

### Railway (Recomendado)

1. Acesse [Railway](https://railway.app)
2. Faça login com GitHub
3. Clique em **New Project > Deploy from GitHub repo**
4. Selecione o repositório do bot
5. Vá em **Variables** e adicione:
   - `DISCORD_TOKEN`
   - `LHUB_API_KEY`
   - `LHUB_API_URL`
   - `OWNER_ID`
6. O bot será deployado automaticamente!

### Render

1. Acesse [Render](https://render.com)
2. Crie uma conta e conecte seu GitHub
3. Clique em **New > Background Worker**
4. Selecione o repositório
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
6. Adicione as variáveis de ambiente
7. Clique em **Create Background Worker**

### Heroku

1. Crie um arquivo `Procfile`:
```
worker: python bot.py
```

2. Crie um arquivo `runtime.txt`:
```
python-3.11.0
```

3. Deploy via CLI:
```bash
heroku login
heroku create nome-do-bot
heroku config:set DISCORD_TOKEN=seu_token
heroku config:set LHUB_API_KEY=sua_key
heroku config:set LHUB_API_URL=https://passesff.squareweb.app
heroku config:set OWNER_ID=seu_id
git push heroku main
heroku ps:scale worker=1
```

### VPS (Ubuntu/Debian)

1. **Conecte via SSH**
```bash
ssh usuario@seu-servidor
```

2. **Instale Python e Git**
```bash
sudo apt update
sudo apt install python3 python3-pip git screen -y
```

3. **Clone e configure**
```bash
git clone https://github.com/seu-usuario/lhub-discord-bot.git
cd lhub-discord-bot
pip3 install -r requirements.txt
cp .env.example .env
nano .env  # Edite com suas credenciais
```

4. **Execute com Screen**
```bash
screen -S lhub-bot
python3 bot.py
# Pressione Ctrl+A, depois D para desanexar
```

5. **Para reconectar**
```bash
screen -r lhub-bot
```

### Replit

1. Acesse [Replit](https://replit.com)
2. Crie um novo Repl Python
3. Faça upload dos arquivos do bot
4. Vá em **Secrets** e adicione as variáveis
5. Clique em **Run**

Para manter online 24/7, use [UptimeRobot](https://uptimerobot.com):
1. Crie um monitor HTTP(s)
2. Use a URL do seu Repl

## 📁 Estrutura do Projeto

```
lhub-discord-bot/
├── bot.py              # Arquivo principal
├── api.py              # Funções da API LHUB
├── config.py           # Configurações
├── database.py         # Gerenciamento de dados
├── requirements.txt    # Dependências
├── .env.example        # Exemplo de configuração
├── .gitignore          # Arquivos ignorados
├── README.md           # Documentação
├── cogs/
│   ├── commands.py     # Comandos de usuário
│   └── admin.py        # Comandos de admin
└── data/
    └── users.json      # Dados dos usuários
```

## 💰 Preços

| Produto | Preço |
|---------|-------|
| Passe de Elite | R$ 4,00 |
| Likes (100-250) | R$ 1,00 |
| Conta Guest | R$ 5,00 |
| Bypass UID (30 dias) | R$ 10,00 |

## 🔒 Segurança

- Nunca compartilhe seu token do Discord
- Nunca compartilhe sua API Key da LHUB
- Use variáveis de ambiente para credenciais
- O arquivo `.env` está no `.gitignore`

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Suporte

- **Discord LHUB**: [Entrar](https://discord.gg/qkB6sWSWJn)
- **Site**: [passesff.squareweb.app](https://lhubff.com.br)
- **Instagram**: [@lhubofc](https://instagram.com/lhubofc)

## ⭐ Créditos

Desenvolvido para integração com a API da **LHUB** - Fornecedor #1 de Passe de Elite e Likes do Brasil.

---

<p align="center">
  <b>Se este projeto te ajudou, deixe uma ⭐ no repositório!</b>
</p>
