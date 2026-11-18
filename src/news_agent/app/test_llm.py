from news_agent.infra.llm.llm_client import llm

response = llm.invoke(
    "Analyse the following news article "
    "and extract its main factual claims."
)

print(response.content)