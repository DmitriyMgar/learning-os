import json
from datetime import datetime
from pathlib import Path

PROGRESS = Path("progress/progress.json")

def main():
    data = json.loads(PROGRESS.read_text(encoding="utf-8"))
    data["last_updated"] = datetime.utcnow().isoformat() + "Z"
    PROGRESS.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("Progress updated:", data["last_updated"])

if __name__ == "__main__":
    main()
