#lista
nomes=['Ana', 'Beatriz', 'Talisson', 'Cinara','Bruno', 'Amilton', 'Miguel', 'Joana', 'Fernando', 'Isadora', 'Yure', 'Igor','Cecilia','Junior', 'Zoe']

#Ordem alfabética

#usuário informa o nome que deseja pesquisa
nome = input('Digite o nome a ser pesqisado: '). capitalize()

#verificação se o nome está na lista ou não
try:
    #retorna o índice do nome pesquisado
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'Nome não encontrado na lista.')