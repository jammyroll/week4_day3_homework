import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author('James','Bond',40,True)
author_repository.save(author1)

author_repository.select_all()
book1= Book('Kill me',1990,'Deadly story',author1,False)
book_repository.save(book1)
