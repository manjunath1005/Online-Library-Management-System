import insert
import read
import update
import transaction
import delete


if __name__=="__main__":
    while(True):
        n=int(input("1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n5.Transaction\nChoose: "))
        match n:
            case 1:
                n1=int(input("1.Add New Member\n2.Add New Book\n"))
                match n1:
                    case 1:
                       name=input("Enter Name:")
                       email=input("Enter email:")
                       created=insert.add_member(name,email)
                       print("Created New Member:",created)
                    case 2:
                        title=input("Enter Title of the Book:")
                        author=input("Enter Author Name:")
                        category=input("Enter the Category:")
                        stock=int(input("Enter the stock:"))
                        created=insert.add_book(title,author,category,stock)
                        print("Inserted ",created)
                    case _:
                        print('Unknown Status')
            case 2:
                n2 = int(input("1.List All Books\n2.Search Books\n3.Member Details\nChoose: "))
                match n2:
                    case 1:
                        books = read.list_books()
                        print("Books:", books)
                    case 2:
                        keyword = input("Enter keyword: ")
                        books = read.search_books(keyword)
                        print("Search Results:", books)
                    case 3:
                        member_id = int(input("Enter Member ID: "))
                        member = read.member_details(member_id)
                        print("Member Details:", member)
                    case _:
                        print("Invalid Choice")
            case 3:
                n3 = int(input("1.Update Book Stock\n2.Update Member Email\nChoose: "))
                match n3:
                    case 1:
                        book_id = int(input("Enter Book ID: "))
                        stock = int(input("Enter New Stock: "))
                        updated = update.update_book_stock(book_id, stock)
                        print("Updated Book:", updated)
                    case 2:
                        member_id = int(input("Enter Member ID: "))
                        email = input("Enter New Email: ")
                        updated = update.update_member_email(member_id, email)
                        print("Updated Member:", updated)
                    case _:
                        print("Invalid Choice")
            case 4:
                n4 = int(input("1.Delete Member\n2.Delete Book\nChoose: "))
                match n4:
                    case 1:
                        member_id = int(input("Enter Member ID to delete: "))
                        deleted = delete.delete_member(member_id)
                        print("Delete Member Result:", deleted)
                    case 2:
                        book_id = int(input("Enter Book ID to delete: "))
                        deleted = delete.delete_book(book_id)
                        print("Delete Book Result:", deleted)
                    case _:
                        print("Invalid Choice")

            case 5:
                n5 = int(input("1.Borrow Book\n2.Return Book\nChoose: "))
                match n5:
                    case 1:
                        member_id = int(input("Enter Member ID: "))
                        book_id = int(input("Enter Book ID: "))
                        result = transaction.borrow_book(member_id, book_id)
                        print("Borrow Result:", result)
                    case 2:
                        record_id = int(input("Enter Borrow Record ID: "))
                        result = transaction.return_book(record_id)
                        print("Return Result:", result)
                    case _:
                        print("Invalid Choice")
            case _:
                print("Invalid Option")