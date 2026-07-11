"""Supervisor node + routing edge (Task 1.3).

TODO:
  - `make_supervisor(llm)`: if current_step_index >= len(plan) -> next_agent =
    'synthesizer'; else classify the current step to 'rag_agent' or 'mcp_tools'.
  - `route_from_supervisor(state)`: return state["next_agent"] for the
    conditional edge.
"""

from __future__ import annotations

from agent.state import AnalystState

RAG = "rag_agent"
MCP = "mcp_tools"
SYNTH = "synthesizer"


def make_supervisor(llm):
    def supervisor(state: AnalystState) -> dict:
        raise NotImplementedError("Task 1.3: implement the supervisor node")

    return supervisor


def route_from_supervisor(state: AnalystState) -> str:
    raise NotImplementedError("Task 1.3: return state['next_agent']")
