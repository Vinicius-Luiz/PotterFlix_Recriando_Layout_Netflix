import io

def titulo ():
    l = []
    arq = io.open("titulos.txt", "r", encoding = "utf8")
    linhas = arq.readlines()
    for titulo in linhas:
        l.append(titulo.replace("\n",""))
    return l

def artista ():
    l = []
    arq = io.open("artistas.txt", "r", encoding = "utf8")
    linhas = arq.readlines()
    for titulo in linhas:
        l.append(titulo.replace("\n",""))
    return l

def album ():
    l = []
    arq = io.open("albuns.txt", "r", encoding = "utf8")
    linhas = arq.readlines()
    for titulo in linhas:
        l.append(titulo.replace("\n",""))
    return l

def duracao ():
    l = []
    arq = io.open("duracao.txt", "r", encoding = "utf8")
    linhas = arq.readlines()
    for titulo in linhas:
        l.append(titulo.replace("\n",""))
    return l

def escreverTabela():
    arq = open("tabelaHTML.txt","w")
    arq.write('<table>\n')
    arq.write('<tr>\n<th>Título</th>\n<th>Artista</th>\n<th>Álbum</th>\n<th>Duração</th>\n</tr>\n')
    for i in range(len(titulos)):
        arq.write('<tr>\n')
        arq.write(f'<td> {titulos[i]} </td>\n')
        arq.write(f'<td> {artistas[i]} </td>\n')
        arq.write(f'<td> {albuns[i]} </td>\n')
        arq.write(f'<td> {duracao[i]} </td>\n')
        arq.write('</tr>\n')
    arq.write('</table>\n')

def escreverTitulo():
    arq = open("tituloHTML.txt", "w")
    c = 0
    for t in titulos:
        if c%2 == 0:
            arq.write(f'<li class = "lista1" >{t}</li>')
        else:
            arq.write(f'<li class = "lista2" >{t}</li>')
        arq.write("\n")
        c+=1
    arq.close()

def escreverArtista():
    arq = open("artistaHTML.txt", "w")
    c = 0
    for t in artistas:
        if c%2 == 0:
            arq.write(f'<li class = "lista1" >{t}</li>')
        else:
            arq.write(f'<li class = "lista2" >{t}</li>')
        arq.write("\n")
        c+=1
    arq.close()

def escreverAlbum():
    arq = open("albumHTML.txt", "w")
    c = 0
    for t in albuns:
        if c%2 == 0:
            arq.write(f'<li class = "lista1" >{t}</li>')
        else:
            arq.write(f'<li class = "lista2" >{t}</li>')
        arq.write("\n")
        c+=1
    arq.close()

def escreverDuracao():
    arq = open("duracaoHTML.txt", "w")
    c = 0
    for t in duracao:
        print(t)
        if t[0] == "0":
            t1 = t[1:]
        elif " 0" in t:
            t1 = t[2:]
        else:
            t1 = t
        if c%2 == 0:
            arq.write(f'<li class = "lista1" >{t1}</li>')
        else:
            arq.write(f'<li class = "lista2" >{t1}</li>')
        arq.write("\n")
        c+=1
    arq.close()







titulos = titulo()
artistas = artista()
albuns = album()
duracao = duracao()
escreverTabela()
'''escreverTitulo()
escreverArtista()
escreverAlbum()
escreverDuracao()'''
print('CONCLUÍDO!!!')
