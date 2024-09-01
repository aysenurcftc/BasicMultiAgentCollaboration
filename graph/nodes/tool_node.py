from langgraph.prebuilt import ToolNode

from graph.tool import tavily_tool, python_repl

from dotenv import load_dotenv
load_dotenv()


tools = [tavily_tool, python_repl]
tool_node = ToolNode(tools)