from langchain_community.vectorstores import Neo4jVector
from embeddings.gemini_embeddings import embed_text
import os
from dotenv import load_dotenv

load_dotenv()

def query_vector_rag(question):
    vector_store = Neo4jVector.from_existing_graph(
        embedding=embed_text,
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        index_name="tweets_index",
        node_label="Tweet",
        text_node_properties=["text"],
        embedding_node_property="embedding",
    )

    
    results = vector_store.similarity_search_with_score(question, k=3)
    return results