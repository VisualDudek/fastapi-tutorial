# Default recipe to display help
default:
    @just --list

# Reflex init
[no-cd]
run:
    uv run fastapi dev main.py
