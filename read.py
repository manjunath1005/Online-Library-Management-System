import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def list_books():
    books = sb.table("books").select("*").execute().data
    borrowed = sb.table("borrow_records").select("book_id").is_("return_date", None).execute().data
    borrowed_count = {}
    for b in borrowed:
        borrowed_count[b["book_id"]] = borrowed_count.get(b["book_id"], 0) + 1
    for book in books:
        used = borrowed_count.get(book["id"], 0)
        book["available"] = book["stock"] - used
    return books

def search_books(keyword):
    resp = sb.table("books").select("*").or_(f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
    ).execute()
    return resp.data

def member_details(member_id):
    member = sb.table("members").select("*").eq("id", member_id).execute().data
    if not member:
        return None
    borrowed =sb.table("borrow_records").select("book_id, returned").eq("member_id", member_id).execute().data
    for b in borrowed:
        book = sb.table("books").select("title,author").eq("id", b["book_id"]).execute().data
        if book:
            b["book_title"] = book[0]["title"]
            b["author"] = book[0]["author"]
    return {"member": member[0], "borrowed_books": borrowed}
