# 📊 Bootcamp Santander Análise de Dados com Python - Pipeline ETL com Python

Este projeto é um desafio de **Engenharia de Dados** proposto durante o bootcamp da Santander Análise de dados com Python em parceria com a DIO. O objetivo foi construir um pipeline **ETL (Extract, Transform, Load)** completo para personalizar mensagens de marketing para clientes bancários utilizando **IA Generativa**.

## 🚀 O Desafio

O script interage com uma API REST simulada do banco para realizar as seguintes etapas:

1.  **Extract (Extração):**
    * Lê um arquivo CSV (`SDW2023.csv`) contendo uma lista de IDs de usuários.
    * Consome a API do Santander Dev Week para buscar os dados cadastrais (Nome, Conta, etc.) de cada ID.

2.  **Transform (Transformação):**
    * Utiliza a API da **OpenAI (GPT-4/3.5)** para gerar mensagens de marketing personalizadas.
    * A IA cria frases engajadoras sobre a importância dos investimentos, utilizando o nome de cada cliente.

3.  **Load (Carga):**
    * Envia as mensagens geradas de volta para a API do banco, atualizando o campo `news` do cadastro do usuário.

## 🛠️ Tecnologias Utilizadas

* **Python 3**: Linguagem principal.
* **Pandas**: Manipulação do arquivo CSV.
* **Requests**: Consumo e envio de dados para a API REST.
* **OpenAI API**: Geração de texto via Inteligência Artificial.
* **Git & GitHub**: Versionamento e portfólio.

## ⚙️ Como Executar

### Pré-requisitos
* Python instalado.
* Uma chave de API da OpenAI (necessário para a etapa de Transformação).

### Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/santander-dev-week-etl-python.git](https://github.com/SEU-USUARIO/santander-dev-week-etl-python.git)

2. Instale as dependências:

Bash

pip install pandas requests openai
Configure sua API Key no código (ou utilize variáveis de ambiente):

Python

openai.api_key = 'SUA_CHAVE_AQUI'
Execute o script:

Bash

python etl.py
📄 Estrutura do Arquivo CSV
O arquivo de entrada SDW2023.csv deve seguir este formato simples:

Snippet de código

UserID
1
2
3
🤝 Contribuição
Sinta-se à vontade para fazer um fork deste projeto e submeter pull requests.

Desenvolvido por Maíra Mendonça durante o Bootcamp Santander Análise de dados com Python em parceria com a DIO.
