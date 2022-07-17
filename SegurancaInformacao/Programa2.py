import hashlib
import rsa
import pickle

#III - O programa 2 deverá ler o conteúdo de um arquivo de texto e gerar um
#código hash SHA-256 sobre o conteúdo lido;

arquivo = open('arquivoDeTexto.txt')
arqAberto = arquivo.read()
hashedArquvo = hashlib.sha256(arqAberto.encode('utf-8')).hexdigest()
print(hashedArquvo)

#IV - O programa 2 deverá criptografar o código hash gerado com a chave
#pública gerada pelo programa 1;

#chavePublica = pickle.load(open('chave1.pkl', 'rb'))
#hashCriptografado = rsa.encrypt(hashedArquvo.encode(), chavePublica)

