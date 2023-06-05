# adivinha
Jogo de advinhação simple em python. 
Descrição:

Este é um jogo de adivinhação simples em Python, onde você tem que tentar adivinhar um número gerado aleatoriamente. O jogo possui três níveis de dificuldade: fácil, médio e difícil.

No início do jogo, você pode escolher o nível de dificuldade entre os disponíveis. Cada nível tem um número de tentativas específico: 20 tentativas para o nível fácil, 10 tentativas para o nível médio e 5 tentativas para o nível difícil.

Durante cada rodada, você deve inserir um número de sua escolha entre 1 e 100. O jogo informará se o número escolhido é maior ou menor do que o número secreto. Se você acertar o número, receberá uma mensagem de parabéns. Caso contrário, o jogo informará se o número secreto é maior ou menor e você continuará tentando até esgotar suas tentativas.

A pontuação final é baseada nas tentativas restantes. Quanto menos tentativas você usar para acertar, maior será sua pontuação. A pontuação é calculada subtraindo-se a diferença entre o número escolhido e o número secreto do saldo de pontos iniciais.

Divirta-se jogando e veja se você consegue obter a pontuação máxima!

Instruções:

Execute o código em um ambiente Python.
Siga as instruções apresentadas no terminal para escolher o nível de dificuldade.
Digite um número entre 1 e 100 para cada tentativa.
Após o término das tentativas, sua pontuação final será exibida.
Observação:
Certifique-se de que seu ambiente Python possua a biblioteca random instalada, pois ela é usada para gerar o número secreto aleatoriamente. Caso não a possua, você pode instalá-la usando o seguinte comando: pip install random.
