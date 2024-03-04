# Requisitos do Sistema
class Requisitos:
    def __init__(self):
        self.funcionalidades = ['Cadastro de Alunos', 'Registro de Notas', 'Gestão de Professores']
        self.integracoes = ['Módulo de Magias Avançadas', 'Caldeirão de Atividades Extracurriculares']
        self.relatorios = ['Boletins Mágicos', 'Mapa do Tesouro da Aprendizagem']

# Modelagem de Dados para o Sistema Mágico de Gerenciamento Escolar
class Aluno:
    def __init__(self, nome, idade, casa):
        self.nome = nome
        self.idade = idade
        self.casa = casa
        self.notas = {}

    def adicionar_nota(self, disciplina, nota):
        self.notas[disciplina] = nota

class Disciplina:
    def __init__(self, nome, professor, carga_horaria):
        self.nome = nome
        self.professor = professor
        self.carga_horaria = carga_horaria

# Implementação do Sistema de Gerenciamento Escolar
class SistemaEscolar:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.disciplinas = []

    def cadastrar_aluno(self, nome, idade, casa):
        aluno = Aluno(nome, idade, casa)
        self.alunos.append(aluno)
        return aluno

    def cadastrar_professor(self, nome):
        professor = nome
        self.professores.append(professor)
        return professor

    def cadastrar_disciplina(self, nome, carga_horaria):
        disciplina = Disciplina(nome, None, carga_horaria)
        self.disciplinas.append(disciplina)
        return disciplina

    def alocar_professor(self, disciplina, professor):
        disciplina.professor = professor

    def menu_principal(self):
        print("\n### Menu Principal ###")
        print("1. Ver Dados")
        print("2. Adicionar Novo Aluno")
        print("3. Adicionar Novo Professor")
        print("4. Ver Notas e Avaliações")
        print("0. Sair")

    def executar_acao(self, opcao):
        if opcao == 1:
            self.ver_dados()
        elif opcao == 2:
            self.adicionar_novo_aluno()
        elif opcao == 3:
            self.adicionar_novo_professor()
        elif opcao == 4:
            self.ver_notas_avaliacoes()

    def ver_dados(self):
        print("\n### Dados do Sistema ###")
        print("Alunos:", [aluno.nome for aluno in self.alunos])
        print("Professores:", self.professores)
        print("Disciplinas:", [disciplina.nome for disciplina in self.disciplinas])

    def adicionar_novo_aluno(self):
        nome = input("Digite o nome do novo aluno: ")
        idade = int(input("Digite a idade do novo aluno: "))
        casa = input("Digite a casa do novo aluno: ")
        self.cadastrar_aluno(nome, idade, casa)
        print("Novo aluno cadastrado com sucesso!")

    def adicionar_novo_professor(self):
        nome = input("Digite o nome do novo professor: ")
        self.cadastrar_professor(nome)
        print("Novo professor cadastrado com sucesso!")

    def ver_notas_avaliacoes(self):
        aluno_nome = input("Digite o nome do aluno: ")
        disciplina_nome = input("Digite o nome da disciplina: ")
        nota = float(input("Digite a nota do aluno na disciplina: "))
        aluno = next((aluno for aluno in self.alunos if aluno.nome == aluno_nome), None)
        disciplina = next((disciplina for disciplina in self.disciplinas if disciplina.nome == disciplina_nome), None)

        if aluno and disciplina:
            aluno.adicionar_nota(disciplina.nome, nota)
            print("Nota adicionada com sucesso!")
        else:
            print("Aluno ou disciplina não encontrados.")

# Testando o Sistema Mágico
sistema = SistemaEscolar()

while True:
    sistema.menu_principal()
    opcao = int(input("Escolha uma opção (0-4): "))
    
    if opcao == 0:
        print("Saindo do Sistema. Até logo!")
        break

    sistema.executar_acao(opcao)
