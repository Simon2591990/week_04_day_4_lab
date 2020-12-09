import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author1 = Author('Stephen', 'King')
author2 = Author('J.K', 'Rowling')

author_repository.save(author1)
author_repository.save(author2)


book1 = Book('Dr Sleep', 'horror', 'Scribner', author1 )
book2 = Book('Harry Potter And The Chamber Of Secrets', 'fantasy', 'penguin', author2)
book3 = Book('Harry Potter And The Order Of The Pheonix', 'fantasy', 'penguin', author2)
book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)



# pdb.set_trace()