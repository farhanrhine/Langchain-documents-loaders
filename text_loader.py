# from langchain_community.document_loaders import TextLoader
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# #from dotenv import load_dotenv

# #load_dotenv()

# model = ChatOllama(model='tinydolphin', temperature=0.1)

# prompt = PromptTemplate(
#     template='Write a summary for the following poem - \n {poem}',
#     input_variables=['poem']
# )

# parser = StrOutputParser()

# loader = TextLoader('c:/documents loaders/langchain-document-loaders/cricket.txt', encoding='utf-8') # Load the text file

# docs = loader.load() # Load the text file

# print(type(docs)) # Print the type of docs

# print(len(docs)) # Print the length of docs

# print(type(docs[0]))

# print(docs[0].page_content) # Print the page content of docs

# print(docs[0].metadata) # Print the metadata of docs

# # now you can use this document loader to load any text file and work with it
# chain = prompt | model | parser

# print("\n\n =============================================================")
# print(chain.invoke({'poem':docs[0].page_content})) # Print the summary of the poem






from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# Initialize components
model = ChatOllama(model='tinydolphin')
prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)
parser = StrOutputParser()

# Load document and generate summary
loader = TextLoader('c:/documents loaders/langchain-document-loaders/cricket.txt', encoding='utf-8')
docs = loader.load()
chain = prompt | model | parser
print(chain.invoke({'poem': docs[0].page_content}))
print("\n\n =============================================================")
print(docs[0].page_content) # Print the page content of docs
print("\n\n =============================================================")
print(docs[0].metadata) # Print the metadata of docs
print("\n\n =============================================================")
