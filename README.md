# Agentic Design Patterns

Notebooks for the Agentic Design Patterns course.

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

### 7. Create an OpenAI API key

1. Go to https://platform.openai.com and log in (create an account if you don't have one).
2. Create a project, add $5 credit, and create an API key.

### 8. Create a `.env` file

Copy `.env-template` to `.env` and put your API key there:

```bash
cp .env-template .env
```

```
OPENAI_API_KEY=sk-proj-...
```

### 9. Open a notebook

Open any notebook in `notebooks/`, for example `notebooks/chapter-1.ipynb`.

### 10. Select the kernel

Click "Select Kernel" and choose the kernel named `agentic-design-patterns`, then accept any following prompt.

### 11. Run the notebook

Run the cells from top to bottom.

## Google Colab notebooks

- Chapter 1: https://colab.research.google.com/drive/1-balOSStw7ASvldaOg8gqhpa4qFWDuEI?usp=sharing
