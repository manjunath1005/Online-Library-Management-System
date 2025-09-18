import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def borrow_book(member_id: int, book_id: int):
    # Check stock
    book = sb.table("books").select("stock").eq("book_id", book_id).execute()
    if not book.data or book.data[0]["stock"] <= 0:
        return {"error": "Book not available"}

    # Insert borrow record
    borrow = sb.table("borrow_records").insert({
        "member_id": member_id,
        "book_id": book_id
    }).execute()

    # Decrease stock
    sb.table("books").update({"stock": book.data[0]["stock"] - 1}).eq("book_id", book_id).execute()

    return borrow.data

def return_book(record_id: int):
    # Find borrow record
    record = sb.table("borrow_records").select("*").eq("record_id", record_id).execute()
    if not record.data:
        return {"error": "Borrow record not found"}
    
    book_id = record.data[0]["book_id"]

    # Update return_date
    update_record = sb.table("borrow_records").update({
        "return_date": "now()"
    }).eq("record_id", record_id).execute()

    # Increase stock
    book = sb.table("books").select("stock").eq("book_id", book_id).execute()
    if book.data:
        sb.table("books").update({"stock": book.data[0]["stock"] + 1}).eq("book_id", book_id).execute()

    return update_record.data
