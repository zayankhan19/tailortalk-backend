from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import re

app = FastAPI()

# Dummy calendar with availability
available_slots = {
    "2025-06-27": ["10:00", "11:00", "14:00"],
    "2025-06-28": ["09:00", "13:00", "15:00"]
}

class BookingRequest(BaseModel):
    message: str

@app.post("/book")
async def book_slot(req: BookingRequest):
    msg = req.message.lower()

    # Try to extract a date
    date_match = re.search(r"2025-06-2[7-8]", msg)
    time_match = re.search(r"(09|10|11|13|14|15):00", msg)

    if date_match and time_match:
        date = date_match.group()
        time = time_match.group()
        if date in available_slots and time in available_slots[date]:
            available_slots[date].remove(time)
            return {"response": f"✅ Booked slot on {date} at {time}"}
        else:
            return {"response": "❌ That slot is not available. Try another one."}
    elif date_match:
        date = date_match.group()
        available = ', '.join(available_slots.get(date, []))
        return {"response": f"🗓 Available times on {date}: {available}"}
    else:
        return {"response": "🤖 Please mention a valid date like '2025-06-27' and a time like '10:00'."}
