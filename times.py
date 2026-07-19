# Lendo a primeira linha com N (alunos) e T (times)
valores = input().split()
N = int(valores[0])
T = int(valores[1])

alunos = []


for i in range(N):
    entrada = input().split()
    nome = entrada[0]
    habilidade = int(entrada[1])
    
    # Guardando a habilidade 
    alunos.append([habilidade, nome])

# Ordenando a lista de alunos pela habilidade (do mais alto para o mais baixo)
alunos.sort(reverse=True)

# Criando uma lista de listas para representar os times vazios
times = []
for i in range(T):
    times.append([])

# Distribuindo os jogadores nos times
for i in range(N):
    
    numero_do_time = i % T
    
  
    nome_do_aluno = alunos[i][1] 
    
    times[numero_do_time].append(nome_do_aluno)

# impressao
for i in range(T):
    print(f"Time {i + 1}")
    
    # nomes em ordem alfabetica
    times[i].sort()
    
    for jogador in times[i]:
        print(jogador)
        
    
    print()