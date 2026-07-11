"""RAG agent node (Task 1.4) — retrieves from Databricks Vector Search.

TODO: Implement `make_rag_agent(retriever, llm)` returning a node that:
  - retrieves top-k chunks for the current step,
  - formats them with [source: file, p.N] citations,
  - extracts a single cited fact via the LLM (or 'not found in documents'),
  - appends the fact to step_results and increments current_step_index.
Reuse `rag/store.py::get_retriever()` so local and deployed retrieval match.
"""

from __future__ import annotations

from agent.state import AnalystState


def format_docs(docs) -> str:
    raise NotImplementedError("Task 1.4: format retrieved docs with citations")


def make_rag_agent(retriever, llm):
    def rag_agent(state: AnalystState) -> dict:
        raise NotImplementedError("Task 1.4: implement the RAG node")

    return rag_agent
