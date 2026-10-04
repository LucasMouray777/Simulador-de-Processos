# Simulador de escalonamento de processos

Sistemas Operacionais (ADS) - 2026/2 - Prof. Guibson Krause

**Integrantes:** [Lucas Moura], [Davi Mota], [Henrique da Silva]

**Linguagem:** [Python 3.x]

## Execução

```bash
python Simulador de Escalonamento de Processo.py
```

O programa executa FCFS, SJF, Prioridade e Round Robin (quantum 2, variáve `QUANTUM`, código) em 3 cenários, 1 CPU e todos chegam em 0. Todo está em `resultados.txt`.

## Resultados (espera média / turnaround médio)

| Algoritmo | Cenário 1 | Cenário 2 | Cenário 3 |
|---|---|---|---|
| FCFS | 2,33 / 4,33 | 6,00 / 9,67 | 3,33 / 6,33 |
| SJF | 1,33 / 3,33 | 1,33 / 5,00 | 2,33 / 5,33 |
| Prioridade | 2,33 / 4,33 | 6,00 / 9,67 | 2,33 / 5,33 |
| Round Robin (q=2) | 2,67 / 4,67 | 3,00 / 6,67 | 4,00 / 7,00 |
