# Chatbot FURIA

Um bot do Telegram para fãs do time de CS:GO da FURIA.

## Funcionalidades
- Notícias sobre o time.
- Informações sobre próximos jogos.
- Link para a loja oficial.
- Links para as redes sociais oficiais.
- Informações sobre o elenco principal.

## Como Rodar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/pantera-box.git
   cd pantera-box
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env` com o token do seu bot do Telegram:
   ```
   TELEGRAM_BOT_TOKEN=seu_token_aqui
   ```

4. Execute o bot:
   ```bash
   python bot.py
   ```

## Tecnologias Utilizadas
- Python 3.10+
- Biblioteca `python-telegram-bot`
- Biblioteca `python-dotenv`