from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dateparser.search import search_dates

app = FastAPI()

# Enable CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define some dummy available slots
available_slots = {
    "2025-06-27": ["10:00", "11:00", "14:00"],
    "2025-06-28": ["12:00", "15:00"],
    "2025-07-01": ["09:00", "13:00", "16:00"],
}


@app.post("/book")
async def book(request: Request):
    data = await request.json()
    message = data.get("message", "")

    # Use search_dates to extract date and time from sentence
    found = search_dates(message)

    if found:
        _, dt = found[0]
        date = dt.strftime("%Y-%m-%d")
        time = dt.strftime("%H:%M")

        if date in available_slots and time in available_slots[date]:
            available_slots[date].remove(time)
            return {"response": f"✅ Booked slot on {date} at {time}"}
        elif date in available_slots:
            available = ", ".join(available_slots[date])
            return {"response": f"🗓 These times are still available on {date}: {available}"}
        else:
            return {"response": f"❌ No slots on {date}. Try another day."}
    else:
        return {
            "response": "🤖 Please mention a valid date like '2025-06-27' and a time like '10:00'."
        }
