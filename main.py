import uvicorn
from src.app import app

def main():
    uvicorn.run(app, port=8000)

if __name__ == '__main__':
    main()