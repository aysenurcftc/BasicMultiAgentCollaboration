from dotenv import load_dotenv
from langgraph.graph import END, StateGraph, START
from graph.chains.edge_logic import router
from graph.nodes.agent_node import research_node, chart_node
from graph.nodes.tool_node import tool_node
from graph.state import AgentState

load_dotenv()

workflow = StateGraph(AgentState)

workflow.add_node("Researcher", research_node)
workflow.add_node("chart_generator", chart_node)
workflow.add_node("call_tool", tool_node)


workflow.add_conditional_edges(
    "Researcher",
    router,
    {"continue": "chart_generator", "call_tool": "call_tool", "__end__": END},
)
workflow.add_conditional_edges(
    "chart_generator",
    router,
    {"continue": "Researcher", "call_tool": "call_tool", "__end__": END},
)

workflow.add_conditional_edges(
    "call_tool",
    # Each agent node updates the 'sender' field
    # the tool calling node does not, meaning
    # this edge will route back to the original agent
    # who invoked the tool
    lambda x: x["sender"],
    {
        "Researcher": "Researcher",
        "chart_generator": "chart_generator",
    },
)


workflow.add_edge(START, "Researcher")
graph = workflow.compile()

graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
print("Graph has START:", START in graph.get_graph().nodes)
print("Graph has END:", END in graph.get_graph().nodes)

