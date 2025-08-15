🚖 ETL NCR Ride Bookings

📌 Resumo do Projeto

O ETL NCR Ride Bookings é um projeto em Python que realiza o fluxo ETL (Extract, Transform, Load) em dados de corridas de táxi (NCR).

![Dashboard Preview](/assets/Dash.gif)


Pipeline do projeto:

Extração de dados → Transformação/limpeza → Carga/armazenamento → Visualização no Dashboard

Fluxo ETL do projeto:

Extract → Lê o arquivo CSV (ncr_ride_bookings.csv) com dados brutos.

Transform →

Adiciona uma coluna status com valor padrão "Pending" caso não exista.

Aplica um desconto de 10% na coluna price, criando discounted_price.

Load → Salva o resultado transformado em data/output.csv.

![ Preview](/assets/img.png)



Integração com ferramentas de BI (GIF do dashboard incluso).

📂 Estrutura do Projeto
etl_ncr_rides/
│
├── data/ 
│   ├── ncr_ride_bookings.csv 
│   └── output.csv 
│
├── notebooks/ 
│   └── etl_notebook.ipynb
│
├── src/ 
│   ├── extract.py 
│   ├── transform.py 
│   └── load.py 
│
├── venv/ 
├── Dashboard.gif 
├── requirements.txt 
└── README.md


Importante: O arquivo Dashboard.gif precisa estar na mesma pasta do README ou o caminho precisa ser ajustado corretamente.

Se estiver em outra pasta (por exemplo data/), use:



🗺 Fluxograma do Pipeline ETL

Pipeline ETL:

Extract → Transform → Load → Dashboard

🚀 Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/seuusuario/etl_ncr_rides.git
cd etl_ncr_rides

2️⃣ Criar e ativar ambiente virtual
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
.\venv\Scripts\activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Colocar o arquivo CSV de entrada

Certifique-se de que ncr_ride_bookings.csv está na pasta data/.

Se estiver em outro local:

mv /caminho/do/arquivo/ncr_ride_bookings.csv data/

5️⃣ Executar o pipeline ETL
python src/load.py


Saída esperada:

Arquivo salvo em data/output.csv

📜 Fluxo do Pipeline

Extract (extract.py)

Lê o CSV de entrada usando Pandas.

Retorna um DataFrame.

Transform (transform.py)

Adiciona coluna status se não existir.

Calcula coluna discounted_price com 10% de desconto.

Load (load.py)

Salva o DataFrame final transformado em data/output.csv.

💻 Exemplo de Uso no Jupyter Notebook
from src.extract import extract
from src.transform import transform
from src.load import load

# Pipeline completo
df = extract()
df_t = transform(df)
load(df_t)


🧑‍💻 Autor

Tatiana Kami
LinkedIn | GitHub

📄 Licença

MIT License – Sinta-se livre para usar e modificar.
