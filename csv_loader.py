from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='c:/documents loaders/langchain-document-loaders/Social_Network_Ads.csv')

docs = loader.lazy_load()

# print(len(docs))
# print(docs[10].page_content)
# print(docs[10].metadata)

# for all documents
for document in docs:
    print(document.metadata)
    print(document.page_content)
    print("\n\n =============================================================")