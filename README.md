# Binbin Office

A local, illustrated office dashboard for the existing bot board.

## Run

```sh
cd ~/Downloads/bot-office
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/ or http://127.0.0.1:8765/tracker/.

Click a teammate on the floor plan, navigate profiles with the arrows, or search the team directory. The board is read every 30 seconds, with a manual Refresh button.

Data remains in `board.json`. Edit the BOTS array in `gen_board.py` and run `python3 gen_board.py` from this directory, or pass a JSON data file. This is a saved-state dashboard, not a live agent integration. Avatar illustrations are placeholders. Existing bot names and task text are preserved.

No build or package installation is required. Optional Google Fonts fall back to system fonts when offline. The floor plan is drawn in SVG and supports keyboard selection and reduced motion.
