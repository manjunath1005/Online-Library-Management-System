import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update_book_stock(book_id: int, new_stock: int):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return resp.data

def update_member_email(member_id: int, new_email: str):
    resp = sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    return resp.data
