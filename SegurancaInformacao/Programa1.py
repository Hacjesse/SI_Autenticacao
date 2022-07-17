import rsa
import pickle

#I - O programa 1 deverá gerar um par de chaves,
#  sendo uma pública e uma privada;
publicKey, privateKey = rsa.newkeys(512)

#II - O programa 1 deverá salvar, em arquivo, a chave pública;
pickle.dump(publicKey, open('chave1.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
