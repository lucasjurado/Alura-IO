# Sempre que abrimos algum arquivo em modo w, o Python vai truncar o arquivo, isto é, limpará seu conteúdo.
# Para adicionar conteúdo a um arquivo sem apagar o que já está escrito, temos que utilizar o modo a.
# (+) --> mode de atualização do arquivo

arquivo_contatos = open('contatos-lista.csv', encoding='latin_1', mode='w+')

contatos = ['11,Carol,carol@gmail.com\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Thais,thais@hotmail.com\n',
            '14,Felipe,felipe@felipe.com.br\n']

# Para inserir uma Lista de contatos, devemos iterá-la
for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush() # Força a inserção dos dados no arquivo .csv

arquivo_contatos.seek(26) # Faz o ponteiro retornar para a primeira linha do arquivo .csv
arquivo_contatos.write('12,Ana,ana@ana.com.br\n'.upper()) # Sobrescrevendo a linha ana
arquivo_contatos.flush()
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha, end='')