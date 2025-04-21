import openai  # ou qualquer lib como `transformers`, `llama-index`, etc.

# Simula contexto de um Cientista de Dados
class LLMCodeGenerator:
    def __init__(self, model_name="gpt-4", temperature=0.2):
        self.model_name = model_name
        self.temperature = temperature
        import os
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Certifique-se de definir a variável de ambiente OPENAI_API_KEY

    def gerar_prompt(self, tarefa, linguagem="Python", contexto_extra=""):
        return f"""
Você é um cientista de dados sênior. Sua tarefa é gerar um código em {linguagem}
que resolva o seguinte problema:

{tarefa}

Requisitos:
- Código limpo e eficiente.
- Comentários explicativos nas partes principais.
- Evite bibliotecas desnecessárias.
{contexto_extra}
        """.strip()

    def gerar_codigo(self, prompt):
        resposta = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature
        )
        return resposta.choices[0].message["content"]

# --- USO PRÁTICO ---

if __name__ == "__main__":
    tarefa = "Carregar um CSV com dados de vendas, calcular a média mensal de faturamento e plotar um gráfico de linha com o resultado."
    contexto_extra = "Use pandas para manipulação e matplotlib para visualização."

    gerador = LLMCodeGenerator()
    prompt = gerador.gerar_prompt(tarefa, contexto_extra=contexto_extra)
    codigo = gerador.gerar_codigo(prompt)

    print("==== PROMPT ====\n", prompt)
    print("\n==== CÓDIGO GERADO ====\n", codigo)
