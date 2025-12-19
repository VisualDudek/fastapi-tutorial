# Default recipe to display help
default:
    @just --list

# Run fastapi app main.py in dev mode
[no-cd]
dev:
    uv run fastapi dev main.py
