from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from graph.graph import graph

load_dotenv()


if __name__ == "__main__":
    events = graph.stream(
        {
            "messages": [
                HumanMessage(
                    content="Give information about what Python is and draw a bar plot comparing it with other programming languages and its usage. Once you code it up, finish."
                )
            ],
        },
        # Maximum number of steps to take in the graph
        {"recursion_limit": 150},
    )


    for event in events:
        print(event)
        print("------")







