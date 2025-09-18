import os
from dotenv import load_dotenv
from supabase import create_client,Client

load_dotenv()

url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
sb: Client=create_client(url,key)

def add_member(name,email):
    data={'name':name,'email':email}
    resp=sb.table('members').insert(data).execute()
    return resp.data

def add_book(title,author,category,stock):
    data={'title':title,'author':author,'category':category,'stock':stock}
    resp=sb.table('books').insert(data).execute()
    return resp.data