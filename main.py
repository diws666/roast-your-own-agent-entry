# This file IS the entry for the make.fun "Roast Your Own Agent" competition.
# The single roast line below is the whole entry and must stay byte-identical
# (no trailing newline) — /output/entry.txt is submitted exactly as written.

ENTRY = "I gave my agent one job. It delegated it back to me."

with open("/output/entry.txt", "w") as f:
    f.write(ENTRY)
