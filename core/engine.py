import ollama

from . import config
from .router import choose_model


class Engine:
    def __init__(self):
        self.history = [{"role": "system", "content": config.SYSTEM_PROMPT}]

    def ask(self, prompt: str):
        """Escolhe o modelo e devolve (nome_do_modelo, resposta_em_streaming)."""
        model = choose_model(prompt)
        keep_alive = (
            config.LIGHT_KEEP_ALIVE
            if model == config.LIGHT_MODEL
            else config.HEAVY_KEEP_ALIVE
        )

        self.history.append({"role": "user", "content": prompt})
        stream = ollama.chat(
            model=model,
            messages=self.history,
            stream=True,
            keep_alive=keep_alive,
        )
        return model, stream

    def save_reply(self, reply: str):
        self.history.append({"role": "assistant", "content": reply})