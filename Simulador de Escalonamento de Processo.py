# Simulador de Escalonamento de Processos - Trabalho 2

cenarios = {
    "Cenário 1 (Processos curtos)": [
        {"nome": "P1", "cpu": 3, "prio": 1},
        {"nome": "P2", "cpu": 1, "prio": 1},
        {"nome": "P3", "cpu": 2, "prio": 1}
    ],
    "Cenário 2 (Curtos e longos)": [
        {"nome": "P1", "cpu": 8, "prio": 1},
        {"nome": "P2", "cpu": 2, "prio": 1},
        {"nome": "P3", "cpu": 1, "prio": 1}
    ],
    "Cenário 3 (Prioridades diferentes)": [
        {"nome": "P1", "cpu": 4, "prio": 3},
        {"nome": "P2", "cpu": 2, "prio": 1},
        {"nome": "P3", "cpu": 3, "prio": 2}
    ]
}

def imprimir_resultados(nome_algoritmo, historico, processos):
    print(f"\n--- {nome_algoritmo} ---")
    
    # Imprimir a sequência
    sequencia = "; ".join([f"{h['nome']} de {h['inicio']} a {h['fim']}" for h in historico])
    print(f"Sequência: {sequencia}")
    
    soma_espera = 0
    soma_turnaround = 0
    
    print(f"{'Processo':<10} | {'CPU':<5} | {'Turnaround':<10} | {'Espera':<10}")
    
    for p in processos:
        # Turnaround = instante em que o processo terminou (última vez que aparece no histórico)
        fim_processo = max([h['fim'] for h in historico if h['nome'] == p['nome']])
        turnaround = fim_processo
        espera = turnaround - p['cpu']
        
        soma_turnaround += turnaround
        soma_espera += espera
        
        print(f"{p['nome']:<10} | {p['cpu']:<5} | {turnaround:<10} | {espera:<10}")
        
    qtd = len(processos)
    print(f"Média:     |       | {soma_turnaround/qtd:<10.2f} | {soma_espera/qtd:<10.2f}")


def executar_fcfs(processos):
    tempo_atual = 0
    historico = []
    
    for p in processos:
        inicio = tempo_atual
        fim = inicio + p['cpu']
        historico.append({"nome": p['nome'], "inicio": inicio, "fim": fim})
        tempo_atual = fim
        
    imprimir_resultados("FCFS", historico, processos)


def executar_sjf(processos):
    # Ordena por tempo de CPU. Como o sort do Python é estável, empates mantêm a ordem original
    processos_sjf = sorted(processos, key=lambda x: x['cpu'])
    tempo_atual = 0
    historico = []
    
    for p in processos_sjf:
        inicio = tempo_atual
        fim = inicio + p['cpu']
        historico.append({"nome": p['nome'], "inicio": inicio, "fim": fim})
        tempo_atual = fim
        
    imprimir_resultados("SJF (Shortest Job First)", historico, processos)


def executar_prioridade(processos):
    # Ordena por prioridade (menor número = maior prioridade)
    processos_prio = sorted(processos, key=lambda x: x['prio'])
    tempo_atual = 0
    historico = []
    
    for p in processos_prio:
        inicio = tempo_atual
        fim = inicio + p['cpu']
        historico.append({"nome": p['nome'], "inicio": inicio, "fim": fim})
        tempo_atual = fim
        
    imprimir_resultados("Prioridade", historico, processos)


def executar_round_robin(processos, quantum=2):
    # Fila de processos com o tempo restante
    fila = [{"nome": p['nome'], "restante": p['cpu']} for p in processos]
    tempo_atual = 0
    historico = []
    
    while fila:
        p_atual = fila.pop(0) # Pega o primeiro da fila
        
        tempo_uso = min(quantum, p_atual['restante'])
        inicio = tempo_atual
        fim = tempo_atual + tempo_uso
        
        historico.append({"nome": p_atual['nome'], "inicio": inicio, "fim": fim})
        
        p_atual['restante'] -= tempo_uso
        tempo_atual = fim
        
        # Se ainda precisa de CPU, volta pro final da fila
        if p_atual['restante'] > 0:
            fila.append(p_atual)
            
    imprimir_resultados(f"Round Robin (Quantum = {quantum})", historico, processos)


# --- Execução Principal ---
print("SIMULADOR DE ESCALONAMENTO DE PROCESSOS")
for nome_cenario, dados_processos in cenarios.items():
    print(f"\n==========================================")
    print(f"Executando {nome_cenario.upper()}")
    print(f"==========================================")
    
    executar_fcfs(dados_processos)
    executar_sjf(dados_processos)
    executar_prioridade(dados_processos)
    executar_round_robin(dados_processos, quantum=2)