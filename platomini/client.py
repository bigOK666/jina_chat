from jina import Client, DocumentArray, Document

c = Client(port=12345)
r = c.post("/generate", inputs=DocumentArray([Document(text="你今天心情好吗？")]))
print(r[0].text)

docs = DocumentArray([])
while True:
    docs.append(Document(text=input("我：")))
    response_docs = c.post(on="/generate", inputs=docs)
    docs.append(response_docs[0])
    print("Plato: ", response_docs[0].text)
