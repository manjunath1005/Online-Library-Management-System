import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_member(member_id):
    borrowed = sb.table("borrow_records") .select("*") .eq("member_id", member_id) .is_("return_date", None) .execute() .data
    if borrowed:
        return {"error": "Member has borrowed books, cannot delete"}
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    return resp.data

def delete_book(book_id):
    borrowed = sb.table("borrow_records") .select("*") .eq("book_id", book_id) .is_("return_date", None).execute().data
    if borrowed:
        return {"error": "Book is currently borrowed, cannot delete"}
    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    return resp.data
