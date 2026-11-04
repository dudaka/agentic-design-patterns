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
| [`notebooks/chapter-9-codeevolve.ipynb`](notebooks/chapter-9-codeevolve.ipynb) | 9 | Learning and Adaptation (CodeEvolve) |
| [`notebooks/chapter-10.ipynb`](notebooks/chapter-10.ipynb) | 10 | Model Context Protocol |
| [`notebooks/chapter-11.ipynb`](notebooks/chapter-11.ipynb) | 11 | Goal Setting and Monitoring |
| [`notebooks/chapter-12.ipynb`](notebooks/chapter-12.ipynb) | 12 | Exception Handling and Recovery |
| [`notebooks/chapter-13.ipynb`](notebooks/chapter-13.ipynb) | 13 | Human-in-the-Loop |
| [`notebooks/chapter-14.ipynb`](notebooks/chapter-14.ipynb) | 14 | Knowledge Retrieval (RAG) |
| [`notebooks/chapter-15.ipynb`](notebooks/chapter-15.ipynb) | 15 | Inter-Agent Communication (A2A) |
| [`notebooks/chapter-16.ipynb`](notebooks/chapter-16.ipynb) | 16 | Resource-Aware Optimization |
| [`notebooks/chapter-17.ipynb`](notebooks/chapter-17.ipynb) | 17 | Reasoning Techniques |
| [`notebooks/chapter-18.ipynb`](notebooks/chapter-18.ipynb) | 18 | Guardrails/Safety Patterns |
| [`notebooks/chapter-19.ipynb`](notebooks/chapter-19.ipynb) | 19 | Evaluation and Monitoring |
| [`notebooks/chapter-20.ipynb`](notebooks/chapter-20.ipynb) | 20 | Prioritization |
| [`notebooks/chapter-21.ipynb`](notebooks/chapter-21.ipynb) | 21 | Exploration and Discovery |

Each pattern is shown in more than one framework: LangChain, Google ADK, and CrewAI. Chapter 8 adds LangGraph. Chapter 9 shows the pattern with CodeEvolve, an open-source evolutionary coding agent from the same family as the book's AlphaEvolve and OpenEvolve, evolving a TSP heuristic. Two chapters use a single framework because the framework is the subject: chapter 10 is Google ADK only, since MCP support is what it demonstrates, and chapter 11 is LangChain only. Chapters 12 and 13 are Google ADK only because the book gives only an ADK listing. Chapter 14 shows RAG twice: Google ADK grounded on Google Search, and a retrieve-then-generate pipeline in LangChain and LangGraph. Chapter 15 is Google ADK only: an ADK agent served over the A2A protocol, called by a plain HTTP client. Chapter 16 shows three routers that send each request to a cheaper or stronger model: Google ADK, the OpenAI SDK, and OpenRouter. Chapter 17 runs the book's reasoning prompts, an ADK code-execution agent, and Google's DeepSearch graph in LangGraph. Chapter 18 shows three guardrails: a CrewAI policy enforcer, a Google ADK tool callback, and an LLM safety filter. Chapter 19 shows basic metrics in plain Python and an LLM as a judge. Chapter 20 is one LangChain project manager agent, the book's only listing. Chapter 21 runs the book's excerpts of Agent Laboratory on a toy topic.

The LangChain and Google ADK listings in chapters 2-4 and chapter 18's CrewAI listing are by Marco Fago, chapter 11's is by Mahtab Syed, and chapter 21's excerpts are from Samuel Schmidgall's Agent Laboratory; all are used under the MIT License, as stated in the notebook headers.

The notebooks adapt the book's listings to run in Jupyter against current library versions:

- `asyncio.run(...)` and `nest_asyncio` become a top-level `await`, and `if __name__ == "__main__":` blocks become a direct call — a notebook is already `__main__`, so the guard only hides the entry point.
- ADK's `create_session` is awaited, and CrewAI's `kickoff()` becomes `await kickoff_async()`, because the sync entry points refuse to run inside the notebook's event loop.
- Retired model names are updated.
- Deprecated ADK APIs are kept and paired with a current version rather than replaced: `SequentialAgent`, `ParallelAgent` and `LoopAgent` alongside `Workflow` (chapters 3, 4, 7 and 12), and `AgentTool` alongside `mode="single_turn"` sub-agents (chapter 7).
- Listings that only define agents, or leave the runner commented out as a "conceptual example", gain the runner and `await` needed to actually run them.
- LangChain's removed `AgentExecutor` / `create_tool_calling_agent` become `create_agent`, and CrewAI takes its own `LLM` object instead of a LangChain chat model.
- LangChain's removed `langchain.memory` and `langchain.chains` (chapter 8): `ChatMessageHistory` becomes `langchain_core`'s `InMemoryChatMessageHistory`, and `LLMChain` + `ConversationBufferMemory` become a `prompt | llm` chain with the history read and saved explicitly.
- The book's pseudo-code for procedural memory in LangGraph (chapter 8) is completed into a graph that runs.
- The MCP examples (chapter 10) use `McpToolset` with `StdioConnectionParams` / `StreamableHTTPConnectionParams`; the book's `HttpServerParameters` no longer exists. The `adk web` files are in `adk_agent_samples/`, and the notebook runs the same agents in-cell.
- Chapter 11's coding agent writes its finished program to `notebooks/generated/` rather than the working directory, so a run does not leave a `.py` file in the repository.
- Chapter 12's listing uses two tools it never defines; the notebook adds mock versions so the fallback chain can run.
- Chapter 13's personalization callback is attached with `before_model_callback`, which the book never does, and adds its note with `append_instructions`: the book's `Content(role="system")` is rejected by Gemini with `400 INVALID_ARGUMENT`.
- Chapter 14's LangChain listing uses `langchain_core`'s `InMemoryVectorStore` instead of embedded Weaviate, whose v3 client API no longer exists, and downloads its document from a raw URL: the book's link is a 404.
- Chapter 15's A2A code targets protocol 1.0: the book's Agent Card fields, `sendTask` / `sendTaskSubscribe` methods and `A2AStarletteApplication` are from earlier versions. The book's Google Calendar toolset needs an OAuth client, so a mock calendar tool stands in for it.
- Chapter 16's retired `gemini-2.5-pro` and `o4-mini` become `gemini-pro-latest` and `gpt-5-mini`. Google's Custom Search API is closed to new customers, so a mock search stands in when its keys are missing, and the OpenRouter example runs only with an `OPENROUTER_API_KEY`.
- Chapter 17 sends the book's sample prompts to real models and checks the result with `len()`. The book prints only DeepSearch's graph, so its nodes are ported, shortened, from Google's `gemini-fullstack-langgraph-quickstart` (Apache-2.0). The Ollama code-execution cell uses ADK's `UnsafeLocalCodeExecutor`, which runs the model's code on your machine with no sandbox.
- Chapter 18's CrewAI example drops `provider="google"`, which made every Gemini call a 404, and awaits `kickoff_async`. Its ADK agent gains a mock tool, since the book's tools list is empty, and the book's safety prompt runs as a `before_model_callback`.
- Chapter 19's LLM judge moves from the replaced `google.generativeai` to `google.genai`. The book's three metric functions call no model, so an added section runs them on real replies, hosted and local.
- Chapter 20's project manager moves from the removed `create_react_agent`, `AgentExecutor` and `ConversationBufferMemory` to `create_agent` with a checkpointer, and its Ollama cell limits the model to one tool call per turn.
- Chapter 21's listing is a set of excerpts from Agent Laboratory, completed from upstream and run on a toy topic with invented reports. The full framework is not run, and the code its agents write is not executed.

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

The project uses Python 3.13; `uv sync` downloads it if needed. Run `uv sync` again every time you pull, then restart the kernel: new chapters add dependencies (chapter 14 needs `langchain-text-splitters`, chapter 15 the A2A SDK), and a stale environment fails with `No module named ...`. If you cloned the repository before it moved from 3.12, also re-select the kernel in VSCode/Cursor so it points at the rebuilt `.venv`.

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
ollama pull nomic-embed-text   # chapter 14 only
ollama pull qwen2.5:1.5b       # chapter 16 only, the cheap model its routers pick
```

3. Run the cell marked "running on a local model served by Ollama". Chapters 1-8 and 10-21 have one below each example that calls a hosted model.

In chapters 11-21 the Ollama cells do not depend on the hosted cells: run the setup cells and the shared cell marked "no model", then skip straight to the Ollama cell. No API key is needed. In the earlier chapters, run the hosted cell above first, because the Ollama cell reuses what it defines.

Google ADK and CrewAI both reach Ollama through LiteLLM, so the model name carries a provider prefix: `ollama_chat/` for ADK, where it is the prefix that handles tool calling correctly, and `ollama/` for CrewAI. LangChain uses `ChatOllama` and no prefix.

`nomic-embed-text` is an embedding model, not a chat model: chapter 14's LangGraph cell uses it to turn text into vectors for retrieval, and `llama3.1:8b` to write the answer. Most chat cells work on either of the other two models, but the ADK routing example in chapter 2 needs a model that is good at tool calling, so it uses `qwen2.5:7b`; `llama3.1:8b` writes `transfer_to_agent(...)` as plain text instead of calling it, and the delegation fails.

## Chapter 9 runs CodeEvolve

The CodeEvolve notebook needs nothing beyond `uv sync`: CodeEvolve is a dependency of this repository, which is why the project uses Python 3.13, and the TSP problem, run configuration and test data it evolves against are in `notebooks/chapter-9-codeevolve/` (sources and licences in `NOTICE.md` there). The hosted run uses `gpt-4.1-mini` (a few cents); the Ollama run needs `ollama pull qwen3-coder:30b` (19 GB), the paper's own open-weight model. Runs write under `notebooks/generated/codeevolve/` (gitignored).

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
- **Chapter 14, Vertex AI RAG.** Needs `google-adk[gcp]`, a Google Cloud project and a RAG corpus. Without `RAG_CORPUS_RESOURCE_NAME` the cell says so and skips.
- **Chapter 16, OpenRouter.** Needs an `OPENROUTER_API_KEY` with paid credit; without it the cell skips, and the Ollama cell below it sends the same request locally. The OpenAI router uses Google Custom Search if `GOOGLE_CUSTOM_SEARCH_API_KEY` and `GOOGLE_CSE_ID` are set, and a mock search otherwise: Google no longer gives those keys to new customers.
- **Chapter 17, local code execution.** The Ollama code-execution cell runs code the model writes on your own machine, with no sandbox. Read it before you run it.

## Google Colab notebooks

- Chapter 1: https://colab.research.google.com/drive/1-balOSStw7ASvldaOg8gqhpa4qFWDuEI?usp=sharing
