class AgenteSistemasEspecialistas:
    def __init__(self, base_conhecimento):
        self.base_conhecimento = base_conhecimento

    def diagnosticar_doenca(self, sintomas):
        for regra in self.base_conhecimento:
            if all(sintoma in sintomas for sintoma in regra["sintomas"]):
                return regra["doenca"]
        return "Doença desconhecida"

# Exemplo de uso:
base_conhecimento = [
    {"sintomas": ["febre", "tosse"], "doenca": "Gripe"},
    {"sintomas": ["dor de cabeça", "náuseas"], "doenca": "Enxaqueca"},
    {"sintomas": ["manchas na pele", "febre"], "doenca": "Sarampo"}
]
agente = AgenteSistemasEspecialistas(base_conhecimento)
sintomas_paciente = ["febre", "tosse"]
diagnostico = agente.diagnosticar_doenca(sintomas_paciente)
print(diagnostico)  # Saída: Gripe
