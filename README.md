# Wayfound MCP Example

This project demonstrates how to use the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) with the Wayfound MCP (Model Context Protocol) remote server to create AI agents that can interact with Wayfound.

## What is the Wayfound MCP Remote Server?

The Wayfound MCP remote server is a specialized Model Context Protocol server that provides AI agents with access to organizational data and tools. It enables agents to:

- List and interact with agents in your organization
- Get details about agents including their role, goal, guidelines, etc.
- Get performance analysis of agents including guideline violations, knowledge gaps, user ratings, sentiment and more.
- Get agent improvement suggestions based on performance analysis and feedback.

MCP (Model Context Protocol) is an open standard that allows AI applications to connect to external data sources and tools in a secure, standardized way. Think of it as a universal connector that lets your AI agents interact with real-world services and data.

## Project Structure

```
wayfound-mcp-example/
├── main.py          # Main example script
├── .env             # Environment variables (create this file based on .env.example)
├── README.md        # This file
└── requirements.txt # Python dependencies
```

## Setup Instructions

### 1. Clone and Navigate

```bash
git clone https://github.com/Wayfound-AI/wayfound-mcp-example
cd wayfound-mcp-example
```

### 2. Install Dependencies

Make sure you have Python 3.10+ installed, then install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with the following configuration:

```env
# Wayfound MCP Server Configuration
WAYFOUND_MCP_API_KEY=your_api_key_here

# OpenAI Configuration (required for the Agents SDK)
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**:
- Replace `your_api_key_here` with your actual Wayfound MCP API key
- Replace `your_openai_api_key_here` with your OpenAI API key
- Keep the `.env` file secure and never commit it to version control

## Running the Example

Run the main example script:

```bash
python main.py
```

The script will:

1. Connect to the Wayfound MCP remote server using SSE (Server-Sent Events)
2. Create an AI agent with access to MCP tools
3. Execute example queries to demonstrate the available functionality
4. Display the results and provide a trace URL for debugging

### Example Output

```
View trace: https://platform.openai.com/traces/trace?trace_id=<trace_id>

Running: What are all the agents in my organization?
[Agent response with list of organizational agents]
```

## Customizing the Example

You can modify `main.py` to:

- Change the agent instructions
- Add new queries or tool calls
- Adjust model settings
- Add error handling and logging

## Troubleshooting

### Debug Mode

Enable debug logging to see more detailed information:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Learn More

- [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
