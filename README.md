# Agentic Design Patterns

Notebooks for the Agentic Design Patterns course.

## Textbook

The examples in these notebooks are adapted from:

> Gullí, A. (2025). *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*. Springer Nature Switzerland, Cham. ISBN 978-3-032-01401-6 (print), 978-3-032-01402-3 (eBook). https://doi.org/10.1007/978-3-032-01402-3

| Notebook | Chapter | Pattern |
| --- | --- | --- |
| `notebooks/chapter-1.ipynb` | 1 | Prompt Chaining |
| `notebooks/chapter-2.ipynb` | 2 | Routing |
| `notebooks/chapter-3.ipynb` | 3 | Parallelization |
| `notebooks/chapter-4.ipynb` | 4 | Reflection |

The LangChain and Google ADK listings in chapters 2-4 are by Marco Fago and are used under the MIT License, as stated in the notebook headers.

The notebooks adapt the book's listings to run in Jupyter against current library versions: `asyncio.run(...)` becomes a top-level `await`, `create_session` is awaited, retired model names are updated, and the deprecated `SequentialAgent` / `ParallelAgent` examples are paired with a `Workflow` version. Some notebooks add an Ollama version of the same example.

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

The notebooks use two providers: OpenAI for the LangChain examples, and Google for the Gemini and Google ADK examples. Create both keys.

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

Open any notebook in `notebooks/`, for example `notebooks/chapter-1.ipynb`.

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

3. Run the cell marked "running on a local model served by Ollama".

The Google ADK examples reach Ollama through LiteLLM, using the `ollama_chat` provider. They need a model that is good at tool calling, so they use `qwen2.5:7b`; smaller models often mis-route the delegation.

## Google Colab notebooks

- Chapter 1: https://colab.research.google.com/drive/1-balOSStw7ASvldaOg8gqhpa4qFWDuEI?usp=sharing
