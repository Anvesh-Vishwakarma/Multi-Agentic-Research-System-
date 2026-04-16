from agents import build_search_agent, build_reader_agent, writer_chain, critic_prompt

def run_search_agent(topic: str) -> dict:
    
    state = {}
    
    # 1 search agent working
    
    print("\n"+" ="*50)
    print("step-1 : Running Search Agent ...")
    print("="*50)
    search_agent = build_search_agent()
    search_result = search_agent.invoke({"messages": [("user", f"Find recent and relevant information about: {topic}")]})
    state['search_result'] = search_result["messages"][-1].content
    
    print("\n Search result: ", state['search_result'])
    
    # 2 reader agent working
    
    print("\n"+" ="*50)
    print("step-2 : Running Reader Agent ...")
    print("="*50)
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_result'][:800]}"
        )]
    })
    
    state["scrapped_content"] = reader_result["messages"][-1].content
    
    print("\n Scrapped content:\n ", state['scrapped_content'])
    
    # 3 writer chain working
    
    print("\n"+" ="*50)
    print("step-3 : Running Writer Chain ...")
    print("="*50)
    
    research_combined = (
        f"Search Results:\n{state['search_result']}\n\n"
        f"Scrapped Content:\n{state['scrapped_content']}"
    )
    
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    
    print("\n Generated Report:\n ", state['report'])
    
    # 4 critic agent working
    
    print("\n"+" ="*50)
    print("step-4 : Running Critic Agent ...")
    print("="*50)
    
    state["feedback"] = critic_prompt.invoke({
        "report": state["report"]
    })
    
    print("\n Critic Result:\n ", state["feedback"])
    
    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic: ")
    run_search_agent(topic)