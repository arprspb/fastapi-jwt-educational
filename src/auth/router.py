from fastapi import APIRouter

router = APIRouter(
    prefix='/auth'
)

@router.get('/')
def get_auth_main():
    return 'Auth main page'

@router.get('/user/{user_id}')
def get_auth_main(user_id: int):
    return f"User id is {user_id}"
