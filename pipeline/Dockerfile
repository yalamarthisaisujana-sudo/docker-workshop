from python:3.13.11-slim
copy --from=ghcr.io/astral-sh/uv:latest /uv /bin/
workdir /code
env PATH="/code/.venv/bin:$PATH"
copy pyproject.toml .python-version uv.lock ./
run uv sync --locked
copy pipeline.py .
entrypoint ["python", "pipeline.py"]


