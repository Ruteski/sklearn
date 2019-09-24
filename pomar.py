from sklearn import tree

irregular = 0
lisa = 1
longa = 2

laranja = 0
maca = 1
banana = 2

pomar = [[150, lisa], [130, lisa], [90, longa], [180, irregular], [160, irregular], [50, longa]]
resultado = [maca, maca, banana, laranja, laranja, banana]

classificacao = tree.DecisionTreeClassifier()
classificacao = classificacao.fit(pomar, resultado)  # (treinamento) construção da arvore de decisao conforme treinamento

peso = input('Informe o peso: ')
superficie = input('Informe a superficie: 0 - irregular | 1 - lisa | 2 - longa: ')

resposta = classificacao.predict([[peso, superficie]])

if resposta == 0:
    print('é uma laranja')
elif resposta == 1:
    print('é uma maça')
else:
    print('é uma banana')

