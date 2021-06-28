#tengo un txt con las canciones de tres playlists, algunas canciones estan repetidas
#busca generar una nueva lista con los titulos sin repetir
#el resultado se muestra en un nuevo archivo txt

file = input("Enter file: ")
if len(file) <1: file = "song.txt"
handle = open(file)
lines = handle.readlines() #cada linea se guarda como un solo indice en la lista

playlist = list()
for line in lines:
    playlist.append(line.strip('\n'))

#print(playlist)
newplaylist = list()
for title in playlist:
    if title not in newplaylist:
        newplaylist.append(title)
    else:
        continue
#print('Number of songs:', len(newplaylist))
#print('New playlist', newplaylist)

#guarda resultados en un archivo txt
results = open('results.txt', 'w')
results.write('Number of songs:%s ' %len(newplaylist)+'\n' )
results.write('New playlist:%s ' %newplaylist) #%s por ser tipo string

results.close()
