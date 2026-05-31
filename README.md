# StudyMate

A microservices-based study companion that helps students take, summarize, paraphrase, and transcribe notes. Built as a group project for the Advanced Software Engineering course at AAU.

## Architecture

The system is composed of eight Docker containers orchestrated via `docker-compose`:

| Service | Description | Stack |
|---------|-------------|-------|
| `frontend` | Single-page web UI | React 18 / TypeScript / Vite |
| `api-gateway` | Reverse proxy routing requests to backend services | Nginx |
| `user-management` | Authentication and JWT-based session handling | Python / FastAPI |
| `summarizing-tool` | Text summarization via a local LLM | FastAPI + Ollama (Llama 3) |
| `paraphrasing-tool` | Paraphrasing via OpenAI API | Python / FastAPI |
| `character-recognition` | Handwriting OCR from uploaded images | Python / FastAPI |
| `voice-transcription` | Speech-to-text from audio uploads | Python / Vosk |
| `ollama` | Local model server for the summarizer | Ollama |

## Tech stack

- **Frontend:** React 18, TypeScript, Vite, Bootstrap 5
- **Backend services:** Python, FastAPI, Poetry
- **ML / AI:** Ollama (Llama 3), OpenAI API, Vosk
- **Infrastructure:** Docker, docker-compose, Nginx
- **CI:** GitHub Actions (character-recognition, voice-transcription)

## Getting started

```bash
# Clone the repository
git clone https://github.com/jacopobellosi/StudyMate---ASE-project.git
cd StudyMate---ASE-project

# Start all services
docker compose up --build

# Open the app
# http://localhost:3000
```

The paraphrasing service requires an `OPENAI_API_KEY` environment variable (set it in a `.env` file or export it before running).

## License

MIT
