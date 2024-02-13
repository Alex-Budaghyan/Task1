from DocumentManager import DocumentManager


def main():
    doc_manager = DocumentManager()
    options = """Options: \n1. Create Document \n2. Edit Document \n3. View Document \n4. Show Document \n5. Exit"""

    while True:
        print(options)
        choice = int(input('Enter your choice(1-5): '))
        if choice == 1:
            name = input('Enter file name:  ')
            doc_manager.createDocument(name)
            print()
        elif choice == 2:
            name = input('Enter file name:  ')
            text = input('Enter text to add:  ')
            doc_manager.editDocument(name, text + '\n')
            print()
        elif choice == 3:
            name = input('Enter file name for view:  ')
            doc_manager.viewDocument(name)
            print()
        elif choice == 4:
            doc_manager.showDocuments()
            print()
        elif choice == 5:
            print('Exiting program...')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5')


if __name__ == '__main__':
    main()

