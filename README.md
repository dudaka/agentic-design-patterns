# Agentic Design Patterns

Notebooks for the Agentic Design Patterns course.

## Textbook

The examples in these notebooks are adapted from:

> Gullí, A. (2025). *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*. Springer Nature Switzerland, Cham. ISBN 978-3-032-01401-6 (print), 978-3-032-01402-3 (eBook). https://doi.org/10.1007/978-3-032-01402-3

| Notebook | Chapter | Pattern |
| --- | --- | --- |
| [`notebooks/chapter-1.ipynb`](notebooks/chapter-1.ipynb) | 1 | Prompt Chaining |
| [`notebooks/chapter-2.ipynb`](notebooks/chapter-2.ipynb) | 2 | Routing |
| [`notebooks/chapter-3.ipynb`](notebooks/chapter-3.ipynb) | 3 | Parallelization |
| [`notebooks/chapter-4.ipynb`](notebooks/chapter-4.ipynb) | 4 | Reflection |
| [`notebooks/chapter-5.ipynb`](notebooks/chapter-5.ipynb) | 5 | Tool Use (Function Calling) |
| [`notebooks/chapter-6.ipynb`](notebooks/chapter-6.ipynb) | 6 | Planning |
| [`notebooks/chapter-7.ipynb`](notebooks/chapter-7.ipynb) | 7 | Multi-Agent Collaboration |
| [`notebooks/chapter-8.ipynb`](notebooks/chapter-8.ipynb) | 8 | Memory Management |
| [`notebooks/chapter-10.ipynb`](notebooks/chapter-10.ipynb) | 10 | Model Context Protocol |

Each pattern is shown in more than one framework: LangChain, Google ADK, and CrewAI. Chapter 8 adds LangGraph.

The LangChain and Google ADK listings in chapters 2-4 are by Marco Fago and are used under the MIT License, as stated in the notebook headers.

The notebooks adapt the book's listings to run in Jupyter against current library versions:

- `asyncio.run(...)`, `if __name__ == "__main__":` blocks, and `nest_asyncio` become a top-level `await`.
- ADK's `create_session` is awaited, and CrewAI's `kickoff()` becomes `await kickoff_async()`, because the sync entry points refuse to run inside the notebook's event loop.
- Retired model names are updated.
- Deprecated ADK APIs are kept and paired with a current version rather than replaced: `SequentialAgent`, `ParallelAgent` and `LoopAgent` alongside `Workflow` (chapters 3, 4 and 7), and `AgentTool` alongside `mode="single_turn"` sub-agents (chapter 7).
- Listings that only define agents, or leave the runner commented out as a "conceptual example", gain the runner and `await` needed to actually run them.
- LangChain's removed `AgentExecutor` / `create_tool_calling_agent` become `create_agent`, and CrewAI takes its own `LLM` object instead of a LangChain chat model.
- LangChain's removed `langchain.memory` and `langchain.chains` (chapter 8): `ChatMessageHistory` becomes `langchain_core`'s `InMemoryChatMessageHistory`, and `LLMChain` + `ConversationBufferMemory` become a `prompt | llm` chain with the history read and saved explicitly.
- The book's pseudo-code for procedural memory in LangGraph (chapter 8) is completed into a graph that runs.
- The MCP examples (chapter 10) use `McpToolset` with `StdioConnectionParams` / `StreamableHTTPConnectionParams`; the book's `HttpServerParameters` no longer exists. The `adk web` files are in `adk_agent_samples/`, and the notebook runs the same agents in-cell.

Some notebooks add an Ollama version of the same example.

The book itself is not included in this repository.

## Run the notebooks locally

### 1. Install git

Open a terminal on Mac or a PowerShell window on Windows, then check:

```bash
git --version
```

- Mac already has git by default.
- On Windows, if the command is not found, install git from https://git-scm.com/downloads/win. After installing, close PowerShell and open a new window before testing again.

### 2. Clone the repository

```bash
git clone https://github.com/dudaka/agentic-design-patterns
```

### 3. Install VSCode or Cursor

- VSCode: https://code.visualstudio.com/
- Cursor: https://cursor.com/home

### 4. Open the project

Open the `agentic-design-patterns` directory with VSCode or Cursor.

### 5. Install the Jupyter extension

In the Extensions view, search for `Jupyter` and install it.

### 6. Install uv and sync dependencies

Install uv following https://docs.astral.sh/uv/, then open a new terminal in VSCode/Cursor (`` Ctrl+` `` on Windows, `` Cmd+` `` on Mac) and run:

```bash
uv self update
uv sync
```

### 7. Create the API keys

The notebooks use two providers: OpenAI for the LangChain and CrewAI examples, and Google for the Gemini and Google ADK examples. Create both keys.

**OpenAI**

1. Go to https://platform.openai.com and log in (create an account if you don't have one).
2. Create a project, add $5 credit, and create an API key.

**Google**

1. Go to https://aistudio.google.com/apikey and log in with a Google account.
2. Click "Create API key". The free tier is enough to run the notebooks.

### 8. Create a `.env` file

Copy `.env-template` to `.env` and put your keys there:

```bash
cp .env-template .env
```

```
OPENAI_API_KEY=sk-proj-...
GOOGLE_API_KEY=AIza...
```

### 9. Open a notebook

Open any notebook in `notebooks/`, for example [`notebooks/chapter-1.ipynb`](notebooks/chapter-1.ipynb).

### 10. Select the kernel

Click "Select Kernel" and choose the kernel named `agentic-design-patterns` or the kernel directory (`.venv/bin/python` - Mac/Linux or `.venv\Scripts\python.exe` - Windows), then accept any following prompt.

### 11. Run the notebook

Run the cells from top to bottom.

## Run the examples on a local model with Ollama

Some notebooks include an extra cell that runs the same example on a local model instead of a hosted API, so no API key is needed for those cells.

1. Install Ollama from https://ollama.com and make sure it is running.
2. Pull the models the notebooks use:

```bash
ollama pull llama3.1:8b
ollama pull qwen2.5:7b
```

3. Run the cell marked "running on a local model served by Ollama". Chapters 1-8 and 10 have one below each example that calls a hosted model.

Google ADK and CrewAI both reach Ollama through LiteLLM, so the model name carries a provider prefix: `ollama_chat/` for ADK, where it is the prefix that handles tool calling correctly, and `ollama/` for CrewAI. LangChain uses `ChatOllama` and no prefix.

Most cells work on any of the pulled models, but the ADK routing example in chapter 2 needs a model that is good at tool calling, so it uses `qwen2.5:7b`; `llama3.1:8b` writes `transfer_to_agent(...)` as plain text instead of calling it, and the delegation fails.

## Chapter 10 needs Node.js

The MCP filesystem example starts `@modelcontextprotocol/server-filesystem` with `npx`, so Node.js must be installed (https://nodejs.org). The first run downloads the server package. To run the examples the book's way, with the ADK web UI:

```bash
cd adk_agent_samples
uv run adk web            # example 1: pick mcp_agent
```

For example 2 start the server first, then the UI on another port — both default to 8000:

```bash
uv run python adk_agent_samples/fastmcp_server.py     # terminal 1
cd adk_agent_samples && uv run adk web --port 8080     # terminal 2: pick fastmcp_client_agent
```

## Cells that need more than an API key

Some cells cannot simply be run in class:

- **Chapter 5, Vertex AI Search.** Vertex AI Search is a Google Cloud service and does not accept an AI Studio `GOOGLE_API_KEY`. It needs a Google Cloud project, a data store filled with your own documents, `GOOGLE_GENAI_USE_VERTEXAI=TRUE`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, `DATASTORE_ID`, and `gcloud auth application-default login`. Without them the cell prints the missing settings and skips, so it is safe to run.
- **Chapter 6, OpenAI Deep Research.** This one makes a real research run: many web searches over several minutes, costing dollars rather than cents. It defaults to the cheaper `o4-mini-deep-research`; the book uses `o3-deep-research`.
- **Chapter 8, database and Vertex session/memory services.** The book's construct-only examples of `DatabaseSessionService`, `VertexAiSessionService` and `VertexAiRagMemoryService` are kept as written. The Vertex ones need `google-adk[gcp]` and a Google Cloud project; the database one needs the async SQLite URL (`sqlite+aiosqlite:///...`) on the current ADK. They are there to read, not to run.

## Google Colab notebooks

- Chapter 1: https://colab.research.google.com/drive/1-balOSStw7ASvldaOg8gqhpa4qFWDuEI?usp=sharing
