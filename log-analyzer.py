import sys
from pathlib import Path

def analyze_log(file_path: str) -> None:

    logpath = Path("sample.log")

    if not logpath.exists():
        print("The log path does not exist")
        return

    total_events = 0

    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
    }

    with open(logpath, "r") as logfile:
        for line in logfile:
            total_events += 1

            for level in counts:
                if level in line:
                    counts[level] += 1
                    break

    print("\nLOG SUMMARY")
    print("------------------")
    print("\nTotal Events: " + str(total_events))

    for level, counts in counts.items():
        print(f"{level}: {counts}")

if __name__ == "__main__":
    analyze_log("sample.log")
