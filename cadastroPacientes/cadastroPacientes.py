from funcoesCadastroPacientes import *
pacientes={}

prontuario=[]
print("SISTEMA DE CADASTRO DE PACIENTES")
opcao=apresentarMenu()
while opcao=="I" or opcao=="P"or opcao=="E" or opcao=="L":
    if opcao=="I":
       inserirPaciente(pacientes,prontuario)
    if opcao=="P":
        pesquisarPaciente(pacientes,int(input("Digite o número do prontuário: ")))
    if opcao=="E":
        excluirPaciente(pacientes,int(input("Digite o nº do prontuário: ")))
    if opcao=="L":
        listarPacientes(pacientes)
    opcao=apresentarMenu()