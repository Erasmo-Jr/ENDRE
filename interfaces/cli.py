from core.engine import Engine


def run():
    engine = Engine()
    print("ENDRE online. Digite 'sair' para encerrar.\n")

    while True:
        prompt = input("Você: ").strip()
        if not prompt:
            continue
        if prompt.lower() in ("sair", "exit"):
            print("ENDRE offline.")
            break

        model, stream = engine.ask(prompt)
        print(f"ENDRE [{model}]: ", end="", flush=True)

        reply = ""
        for chunk in stream:
            piece = chunk["message"]["content"]
            reply += piece
            print(piece, end="", flush=True)
        print("\n")

        engine.save_reply(reply)