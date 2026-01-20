import pandas as pd
import requests
import json
import openai

# --- CONFIGURAÇÕES INICIAIS ---
# URL base da API do Santander Dev Week 2023
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

# TODO: Insira sua chave da OpenAI aqui para testar localmente.
# IMPORTANTE: Apague a chave antes de enviar para o GitHub (git push) para não vazá-la!
openai_api_key = 'TODO'
openai.api_key = openai_api_key

# --- 1. EXTRACT (Extração) ---
print("--- INICIANDO EXTRAÇÃO ---")
# Extraia a lista de IDs de usuário a partir do arquivo CSV
df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print("IDs capturados:", user_ids)

# Função para obter dados do usuário na API
def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

# Gera a lista de objetos de usuários válidos
users = [user for id in user_ids if (user := get_user(id)) is not None]

# Imprime o JSON formatado para visualização (log)
print(json.dumps(users, indent=2))

# --- 2. TRANSFORM (Transformação) ---
print("\n--- INICIANDO TRANSFORMAÇÃO (IA) ---")

def generate_ai_news(user):
  # Utiliza a API do OpenAI GPT-4 (ou gpt-3.5-turbo) para gerar mensagem
  # Nota: Se sua conta for nova/gratuita, talvez precise mudar "gpt-4" para "gpt-3.5-turbo"
  try:
      completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
          {
              "role": "system",
              "content": "Você é um especialista em markting bancário."
          },
          {
              "role": "user",
              "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
          }
        ]
      )
      return completion.choices[0].message.content.strip('\"')
  except Exception as e:
      print(f"Erro na OpenAI: {e}")
      # Retorna mensagem padrão caso a IA falhe ou esteja sem chave
      return f"Olá {user['name']}, invista no seu futuro hoje!"

for user in users:
  news = generate_ai_news(user)
  print(f"Notícia gerada para {user['name']}: {news}")
  
  # Atualiza o objeto local
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

# --- 3. LOAD (Carga) ---
print("\n--- INICIANDO CARGA (ATUALIZAÇÃO) ---")

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")