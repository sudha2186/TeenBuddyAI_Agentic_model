import base64

def get_download_link(text, filename="TeenBuddyAI_Response.txt"):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download AI Response</a>'
    return href
