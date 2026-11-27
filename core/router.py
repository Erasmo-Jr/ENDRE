from . import config

# Palavras que indicam um pedido mais difícil -> modelo pesado
HEAVY_KEYWORDS = (
    "código", "codigo", "programa", "função", "funcao", "classe",
    "erro", "bug", "debug", "explique", "analise", "analisar",
    "resuma", "compare", "planeje", "algoritmo",
)

def choose_model(prompt: str) -> str:
    text = prompt.lower()
    if len(text) > 300 or any(word in text for word in HEAVY_KEYWORDS):
        return config.HEAVY_MODEL
    return config.LIGHT_MODEL