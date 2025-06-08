from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='c:/documents loaders/langchain-document-loaders/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

#docs = loader.lazy_load() # Lazy load the documents used when too many documents are there for processing
#docs = list(loader.lazy_load())  # Convert generator to list
docs = loader.load()


#print(len(docs))

print(docs[325].page_content)
print(docs[325].metadata)
# for all documents
# for document in docs:
#     print(document.metadata)