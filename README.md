# Customer Support Agent

An AI-powered customer support agent built with Google Agent Development Kit (ADK). Uses a graph-based workflow to classify and route shipping-related queries to specialized agents.

## Architecture

The agent implements a two-stage workflow:

1. **Classifier** — keyword-based routing that determines if a query is shipping-related
2. **Shipping FAQ Agent** — LLM-powered specialist that answers shipping questions (rates, tracking, delivery, returns)
3. **Decline Node** — politely redirects unrelated queries

```
User Query → Classifier → Shipping FAQ (if shipping-related)
                        → Decline Response (if unrelated)
```

## Tech Stack

- Python 3.10+
- Google ADK 2.0+
- DeepSeek Chat (via LiteLLM)
- Graph-based workflow with `FunctionNode` and `LlmAgent`

## Setup

### 1. Install dependencies

```bash
cd customer-support-agent
python -m pip install -e .
```

### 2. Set environment variables

Create a `.env` file or export:

```bash
# For DeepSeek via LiteLLM
export DEEPSEEK_API_KEY="your-api-key"
```

### 3. Run

**CLI mode:**

```bash
python -m customer_support_agent.agent
```

**Web playground (recommended):**

```powershell
# Windows (full path)
& "C:\Users\*YOUR-USERNAME*\AppData\Local\Python\pythoncore-3.14-64\Scripts\adk.exe" web customer-support-agent
```

Then open http://127.0.0.1:8000 in your browser.

> **Tip:** Add the Scripts directory to PATH to use `adk` directly:
> ```powershell
> [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\trulo\AppData\Local\Python\pythoncore-3.14-64\Scripts", "User")
> ```

## Project Structure

```
customer-support-agent/
├── customer_support_agent/
│   ├── __init__.py
│   ├── agent.py          # Root agent with workflow graph
│   ├── classifier.py     # Query classification (keyword-based)
│   └── shipping_faq.py   # Shipping FAQ specialist
├── pyproject.toml
└── README.md
```

## Example Queries

| Query | Route | Response |
|-------|-------|----------|
| "How much does shipping cost?" | shipping | FAQ agent provides rates |
| "Where is my package?" | shipping | FAQ agent explains tracking |
| "What's the weather today?" | unrelated | Polite decline |

## License

MIT
