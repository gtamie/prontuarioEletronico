from funcoesCadastroPacientes import *
pacientes={}
prontuario=[]
print("SISTEMA DE CADASTRO DE PACIENTES")
opcao=apresentarMenu()

while opcao=="I" or opcao=="P"or opcao=="E" or opcao=="L":
    gravarInDicionario(pacientes, prontuario)
    if opcao=="I":
        inserirPaciente(pacientes,prontuario)
        gravarInArquivo(pacientes)
    if opcao=="P":
        pesquisarPaciente(pacientes,int(input("Digite o número do prontuário: ")))
    if opcao=="E":
        excluirPaciente(pacientes,int(input("Digite o nº do prontuário: ")))
        gravarInArquivo(pacientes)
    if opcao=="L":
        listarPacientes(pacientes)
    opcao=apresentarMenu()