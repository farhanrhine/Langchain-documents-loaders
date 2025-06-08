from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('c:/documents loaders/langchain-document-loaders/dl-curriculum.pdf')

docs = loader.load()

print(docs)
print(type(docs))
print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)