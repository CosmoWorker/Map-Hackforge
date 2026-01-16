from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    print("Hello from server!")
    return {"msg": "Hello from server!"}

# returns response info for lat/long
@app.get("/events/stream")
def events_info():
    pass

@app.get("/summary")
def summary():
    pass

if __name__ == "__main__":
    main()
