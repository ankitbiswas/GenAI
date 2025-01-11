# GenAI
GenAI Projects

**Custom Website** -> The code base is for implementing a custom web chatbot using the ineuron sitemap. We use Pinecone as vector db and Llama model for augmented generation.

**Source Code Analysis Gen AI**-> 
Conversational AI for Codebase Exploration
Developed an interactive Q&A system to simplify understanding large codebases. The project clones a GitHub repository, processes Python files into structured chunks using LangChain, creates a searchable knowledge base with OpenAI embeddings stored in a Chroma vector database, and integrates a conversational interface using OpenAI’s ChatGPT and memory for context-aware responses. The system enables seamless querying of code insights, like understanding classes or methods, enhancing developer productivity.

Key Components of the Code
GitHub Repository Cloning:

Utilizes gitpython to clone the End-to-end-ML-Project-Implementation repository into a local directory for further processing.
Document Loading:

Uses LangChain's GenericLoader to load Python files from the repository.
Files are parsed with a LanguageParser configured for Python, ensuring efficient extraction of content.
Text Chunking:

Implements RecursiveCharacterTextSplitter to split large documents into manageable chunks of 2000 characters with 200-character overlaps.
Chunking aids in better embedding and retrieval performance.
Embeddings and Vector Store:

Creates vector representations of the document chunks using OpenAIEmbeddings.
Stores these embeddings in a persistent Chroma database for efficient retrieval.
Knowledge Base Retrieval:

Uses Chroma as a retriever to perform MMR (Maximal Marginal Relevance)-based searches, retrieving the top 3 relevant document chunks.
Conversational Memory:

Integrates a ConversationSummaryMemory module to maintain chat history and summarize conversations, providing continuity in interactions.
Q&A Workflow:

Wraps the language model (ChatOpenAI) and retriever in a ConversationalRetrievalChain.
Processes user queries by retrieving contextually relevant chunks and generating responses.

Tech Stack: Python, Git, LangChain, OpenAI API, Chroma.
Highlights: Automated knowledge extraction, semantic search, and conversational AI for efficient codebase exploration.

The code is in trials.ipynb. 
We have the necessary template ready to modularize it later.


**Telegram Bot Development with aiogram and OpenAI Integration**->

Designed and implemented a Telegram bot using the aiogram framework, integrating OpenAI's GPT-3.5 model for AI-powered conversational capabilities.
Key features of the bot include:
Command Handling: Added support for commands like /start, /help, and /clear to provide users with a seamless onboarding experience and enable clearing past conversations.
AI-Powered Responses: Leveraged OpenAI's GPT-3.5-turbo model to process user queries and generate intelligent, context-aware replies.

**Conversational AI Chatbot using LangChain, OpenAI, ChromaDB, and Chainlit**
Developed a Conversational AI Chatbot using LangChain, OpenAI, ChromaDB, and Chainlit. Implemented document-based retrieval by processing user-uploaded text files, chunking content, embedding it using OpenAI, and storing it in ChromaDB for semantic search—Integrated ConversationalRetrievalChain to enable contextual Q&A with memory. The chatbot provides answers along with cited sources, ensuring transparency.

**Key Components**:
**File Upload & Processing**: Waits for a user-uploaded text file, reads, and splits it into chunks.
**Vector Storage**: Converts text into embeddings using OpenAIEmbeddings and stores it in ChromaDB for retrieval.
**Conversational AI Chain**: Uses ConversationalRetrievalChain with GPT-3.5-turbo for contextual Q&A.
**Memory Management**: Maintains chat history using ConversationBufferMemory to provide continuity.
**User Interaction**: Built with Chainlit, enabling real-time interaction, response streaming, and source citation.
**State Management**: Implemented a reference class to manage memory and maintain a conversational context across user interactions.


Run telebot-AI.py
