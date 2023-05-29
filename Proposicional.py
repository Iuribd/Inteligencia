class AgenteProposicional:
    def __init__(self, base_conhecimento):
        self.base_conhecimento = base_conhecimento

    def inferir(self, consulta):
        return consulta in self.base_conhecimento

# Exemplo de uso:
base_conhecimento = ["A", "B", "A implica B"]
agente = AgenteProposicional(base_conhecimento)
resultado = agente.inferir("B")
print(resultado)  # Saída: True
