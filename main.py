from fastapi import FastAPI



app = FastAPI()

@app.get('/')
def get_main_page():
    return 'Main page data...'
