# GenAI
GenAI Projects

Custom Website -> The code base is for implementing a custom web chatbot using the ineuron sitemap. We use Pinecone as vector db and Llama model for augmented generation.

Source Code Analysis Gen AI -> This code is used for analyzing any source code, instead of text documents, and use llm (Open-AI) to retrieve any answer about the code. We utilize context-aware splitting on the code while loading the data, followed it up by chunking using RecursiveCharacterTextSplitter. Then, we OpenAIEmbeddings to convert the chunks to embeddings and store in Chroma vector db. We use LLMWrapper and ConversationalRetrievalChain to make the model focus on our specifc data and also have memory of its responses. Then we can ask the model to generate any answer related to our code.

The code is in trials.ipynb. 
We have the necessary template ready to modularize it later.
