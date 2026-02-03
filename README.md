📊 Database Monitoring & Analysis Project (SQL + Python)

Projeto prático voltado para análise e monitoramento de banco de dados, simulando rotinas reais de um DBA / Data Analyst, utilizando SQL e Python de forma integrada.

🎯 Objetivo do Projeto

Demonstrar na prática:

Escrita de SQL limpo e portável (PostgreSQL / MySQL / Oracle)

Uso de Python como ferramenta de automação e análise

Separação clara entre:

camada de dados (SQL)

camada de orquestração (Python)

Organização de projeto profissional para ambientes corporativos

Este projeto foi pensado para ambientes reais de empresa, onde o banco de dados pode estar hospedado remotamente (cloud ou on-premises).

🧠 Conceito Arquitetural

SQL → responsável pelas consultas e regras de negócio

Python → executa as queries, analisa os resultados e gera relatórios

Banco de Dados → pode ser PostgreSQL (Supabase), Oracle ou MySQL

A troca do banco não exige mudanças no código Python, apenas na conexão.

🧱 Estrutura do Projeto
db-monitoring-postgres/
│
├── database/
│   └── schema.sql            # Estrutura do banco (exemplo)
│
├── queries/
│   └── top_customers.sql     # Query de análise SQL
│
├── scripts/
│   ├── test_connection.py    # Teste de conexão com banco
│   └── run_analysis.py       # Execução das análises
│
├── reports/
│   └── summary.txt           # Relatório gerado automaticamente
│
├── .env                      # Variáveis de ambiente (não versionado)
├── requirements.txt
└── README.md

🛠️ Tecnologias Utilizadas

SQL (PostgreSQL / MySQL / Oracle)

Python 3

psycopg2

python-dotenv

Git / GitHub

▶️ Como Executar
1️⃣ Instalar dependências
pip install -r requirements.txt

2️⃣ Configurar variáveis de ambiente

Criar um arquivo .env na raiz do projeto:

DB_HOST=localhost
DB_NAME=database_name
DB_USER=user
DB_PASSWORD=password
DB_PORT=5432

3️⃣ Testar conexão com o banco
python scripts/test_connection.py

4️⃣ Executar análise
python scripts/run_analysis.py


O relatório será gerado automaticamente em:

reports/summary.txt

📈 Exemplo de Análise

Identificação de clientes com maior volume de pedidos

Possível uso para:

auditoria

análise de comportamento

relatórios gerenciais

automações recorrentes

🧑‍💻 Contexto Profissional

Em ambientes corporativos, esse tipo de solução é utilizada para:

Monitoramento de dados

Auditoria de volumes

Validação de integridade

Geração de relatórios automatizados

Suporte à tomada de decisão

O mesmo modelo pode ser adaptado para Oracle, PostgreSQL ou MySQL, alterando apenas a camada de conexão.

📌 Próximos Passos

Integração com dashboards (Pandas / Matplotlib)

Alertas automatizados

Análises de performance

Agendamento de execuções

✅ Status

Projeto funcional e em evolução contínua.