from fastapi import FastAPI

from src.auth.router import router as auth_router


app = FastAPI()
app.include_router(auth_router)

@app.get('/')
def get_main_page():
    return 'Main page data...'
