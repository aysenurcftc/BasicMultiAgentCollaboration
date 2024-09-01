import matplotlib.pyplot as plt
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from graph.graph import graph

load_dotenv()


if __name__ == "__main__":
    events = graph.stream(
        {
            "messages": [
                HumanMessage(
                    content="Fetch the UK's GDP over the past 5 years,"
                            " then draw a line graph of it."
                            " Once you code it up, finish."
                )
            ],
        },
        # Maximum number of steps to take in the graph
        {"recursion_limit": 150},
    )


    for s in events:
        print(s)
        print("----")






