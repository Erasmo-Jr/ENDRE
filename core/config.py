# Modelos
LIGHT_MODEL = "qwen2.5:3b"    # leve, sempre residente na VRAM
HEAVY_MODEL = "qwen2.5:14b"   # pesado, carregado sob demanda

# Quanto tempo cada modelo fica na VRAM depois do último uso
LIGHT_KEEP_ALIVE = -1         # inteiro, sem aspas: nunca descarrega
HEAVY_KEEP_ALIVE = "5m"       # descarrega após 5 min ocioso

SYSTEM_PROMPT = (
    "Você é o ENDRE, assistente pessoal do Erasmo. "
    "Responda sempre em português do Brasil, de forma direta e útil."
)