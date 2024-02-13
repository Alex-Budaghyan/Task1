class DocumentManager:
    def __init__(self):
        self.documents = []

    def createDocument(self, name):
        if name in self.documents:
            print("File already exist.")
            return
        with open(name, 'w') as file:
            print(f'File {name} created successfully.')
            contents = input("Enter the contents: ")
            file.write(contents + '\n')
            self.documents.append(name)

    def editDocument(self, name, text):
        if name not in self.documents:
            print('File does not exist.')
            return
        with open(name, 'a') as file:
            file.write(text)
            print('Text added to the document successfully.')

    def viewDocument(self, name):
        if name not in self.documents:
            print('File does not exist.')
            return
        with open(name, 'r') as file:
            print(file.read())

    def showDocuments(self):
        if not self.documents:
            print("No documents available.")
        else:
            print("All documents in .:")
            for doc in self.documents:
                print(doc)





