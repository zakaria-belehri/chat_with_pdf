- Project Summary :

This repository provides a streamlined Retrieval-Augmented Generation (RAG) pipeline that transforms any PDF document into actionable knowledge. I parse each file into raw text and structured tables, summarize those chunks with an LLM, index their embeddings in PostgreSQL + PGVector, and store metadata in Redis for fast lookup. When you ask a question, the system retrieves the most relevant snippets and feeds them to the language model for a concise, grounded answer.

- Parsing PDFs with Unstructured :

I use the Unstructured library to split any uploaded PDF into individual content blocks—narrative text and tables—while optionally performing high-resolution layout analysis. This gives me fine-grained elements that I can further process, without any manual preprocessing steps.

- Persisting Chunk Metadata in Redis :

Instead of storing the entire PDF, I generate a SHA-256 hash of the file and save that hash plus the raw text/table chunks (keyed by UUID) in Redis. This lets me quickly detect duplicates and retrieve the original content blocks when needed.

- Summarizing Chunks with the LLM :

Each extracted text or table chunk is sent to the LLM with a lightweight summarization prompt. I store only the concise summaries—rather than the full chunks—in my vector index, reducing storage costs and token usage downstream.

- Storing Embeddings in PGVector :

I embed each summarized chunk using OpenAI embeddings and push the resulting vectors into a PostgreSQL database enhanced with the pgvector extension. This creates a scalable, persistent vector index that supports semantic similarity search.

- Multi-Vector Retrieval :

To boost recall, I use a multi-vector retriever that queries both text- and table-based embeddings in a single request. This combined retrieval strategy ensures the language model sees all relevant context, whether narrative or tabular.

- Querying the Language Model :

When posing a question, I gather the top-k relevant summaries from PGVector, reconstruct their raw content via Redis, and feed that context into the LLM with a final answer-generation prompt. The result is a concise, context-grounded response that never hallucinates beyond the source material.

- Key Capabilities :

I automatically decompose PDFs into tables and text, run a built-in summarization step, and manage dual storage (Redis for metadata, PostgreSQL + PGVector for embeddings). The multi-vector retriever further enriches context retrieval to improve answer accuracy and reduce token waste.

- Technology Stack :
. Language: Python
. PDF Parsing: Unstructured
. Vector Database: PostgreSQL with pgvector
. Metadata Store: Redis
. Retrieval & Orchestration: LangChain
. Language Model: GPT-style models via the OpenAI API

