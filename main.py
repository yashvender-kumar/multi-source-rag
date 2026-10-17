from src.retrieval import ask

while True:
    query = input("user:")

    if query.lower() in ["exit", "quit","bye"]:
        print("Good bye")
        break

    answer, sources = ask(query)
    print("Ai:",answer)
    print("Sources:")
    for s in sources:
        print(" -",s)
        