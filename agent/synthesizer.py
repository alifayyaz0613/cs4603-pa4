"""Synthesizer node (Task 1.6).

TODO: Implement `make_synthesizer(llm)` returning a node that combines
step_results into one cited answer and writes it to BOTH `final_answer` AND
the `messages` channel as an AIMessage (required for the OpenAI-compatible
serving contract — see spec Task 1.6).
"""

from __future__ import annotations

from agent.state import AnalystState


def make_synthesizer(llm):
    def synthesizer(state: AnalystState) -> dict:
        raise NotImplementedError("Task 1.6: implement the synthesizer node")

    return synthesizer
