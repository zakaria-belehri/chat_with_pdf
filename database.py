import os
from dotenv import load_dotenv

# 1. Load .env
load_dotenv()

# 2. Pull each var (with sane defaults)
host            = os.getenv("PG_VECTOR_HOST",     "localhost")
user            = os.getenv("PG_VECTOR_USER",     "langchain")
password        = os.getenv("PG_VECTOR_PASSWORD", "langchain")
COLLECTION_NAME = os.getenv("PGDATABASE",         "my_documents")

# 3. Build the connection string using your env vars
CONNECTION_STRING = (
    f"postgresql+psycopg://{user}:{password}@{host}:6024/{COLLECTION_NAME}"
)