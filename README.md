# 🚀 SpaceX Launch Data Pipeline

An end-to-end data engineering pipeline that ingests real SpaceX launch data from a public REST API, transforms and cleans it with Pandas, persists it in a PostgreSQL database running in Docker, and visualises it in a live Streamlit dashboard.

---

## 📐 Architecture

```
SpaceX REST API
      │
      ▼
  ingest.py        ← fetches raw JSON via requests
      │
      ▼
transform.py       ← cleans data + aggregates by year (Pandas)
      │
      ▼
   load.py         ← persists to PostgreSQL via SQLAlchemy
      │
      ▼
 dashboard.py      ← live web dashboard (Streamlit)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Data ingestion | `requests` |
| Data transformation | `pandas` |
| Database | PostgreSQL 15 (Docker) |
| ORM / DB connector | `SQLAlchemy` + `psycopg2-binary` |
| Containerisation | Docker + Docker Compose |
| Dashboard | `streamlit` |

---

## 📁 Project Structure

```
spacex-pipeline/
├── scripts/
│   ├── ingest.py        # Stage 1: fetch data from SpaceX API
│   ├── transform.py     # Stage 2: clean and aggregate data
│   ├── load.py          # Stage 3: write to PostgreSQL
│   └── dashboard.py     # Stage 4: Streamlit dashboard
├── docker-compose.yml   # PostgreSQL container config
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ How to Run

### Prerequisites
- Python 3.12+
- Docker + Docker Compose

### 1. Clone the repository
```bash
git clone https://github.com/salmadhz/spacex-pipeline.git
cd spacex-pipeline
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start PostgreSQL with Docker
```bash
docker compose up -d
```

### 5. Run the pipeline
```bash
cd scripts
python load.py
```

Expected output:
```
Data loaded successfully!
Launches table: 205 rows
Stats table: 16 rows
```

### 6. Launch the dashboard
```bash
streamlit run scripts/dashboard.py
```

Open **http://localhost:8501** in your browser.

---

## 📊 Dashboard Features

- **Total launches** — count of all SpaceX launches (2006–2022)
- **Total successes** — count of successful missions
- **First launch year** — earliest launch in the dataset
- **Bar chart** — launches per year
- **Line chart** — successful launches per year

---

## 🗄️ Database Schema

### `launches` table — 205 rows
| Column | Type | Description |
|---|---|---|
| `name` | text | Mission name |
| `date_utc` | timestamp | Launch date and time |
| `success` | boolean | Whether the launch succeeded |
| `rocket` | text | Rocket ID |
| `payloads` | text | Payload IDs |

### `daily_launch_stats` table — 16 rows
| Column | Type | Description |
|---|---|---|
| `year` | integer | Launch year |
| `total` | integer | Total launches that year |
| `successes` | integer | Successful launches that year |

---

## 💡 Key Concepts Practised

- Consuming a public REST API with `requests`
- Data cleaning and transformation with `pandas` (type conversion, null handling, `groupby`, `agg`)
- Containerising a database service with Docker Compose
- Connecting Python to PostgreSQL via SQLAlchemy connection strings
- Writing DataFrames directly to SQL tables with `.to_sql()`
- Building an interactive data dashboard with Streamlit

---

## 📌 Data Source

[r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API) — community-maintained REST API covering SpaceX launches from 2006 to 2022.

---

## 👩‍💻 Author

**Salma** — [github.com/salmadhz](https://github.com/salmadhz)
