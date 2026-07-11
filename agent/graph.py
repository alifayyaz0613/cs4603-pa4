"""Full Document Analyst graph (Tasks 1.5 + 1.7).

TODO:
  - `load_mcp_tools(server_path=None)`: connect the GIVEN MCP server over stdio
    (see langchain-mcp-adapters) and return its tools.
  - `make_mcp_node(tools, llm)`: execute one calculation step by letting the LLM
    call exactly one MCP tool, then append the result and increment the index.
  - `build_graph(llm=None, retriever=None, tools=None)`: assemble
    planner -> supervisor -> {rag_agent | mcp_tools} -> ... -> synthesizer.
    Inject dependencies so the graph can be unit-tested offline with fakes.
"""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from agent.planner import make_planner
from agent.rag_agent import make_rag_agent
from agent.state import AnalystState
from agent.supervisor import MCP, RAG, SYNTH, make_supervisor, route_from_supervisor
from agent.synthesizer import make_synthesizer


def load_mcp_tools(server_path: str | None = None):
    raise NotImplementedError("Task 1.5: connect the MCP server and return its tools")


def make_mcp_node(tools, llm):
    def mcp_tools(state: AnalystState) -> dict:
        raise NotImplementedError("Task 1.5: implement the MCP tool node")

    return mcp_tools


def build_graph(llm=None, retriever=None, tools=None):
    raise NotImplementedError("Task 1.7: wire and compile the full graph")
