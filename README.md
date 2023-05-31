Relatório **Autômato de Pilha Não-Determinístico (APND)**

**Yuri Lima dos Santos Silva - 2018106710**

Introdução:

1. O objetivo do projeto é implementar um algoritmo para reconhecer palavras em um **Autômato de Pilha Não-Determinístico** (APND). O reconhecimento de palavras é uma tarefa importante em linguagens formais e automatos, sendo amplamente aplicado em processamento de linguagens naturais, compiladores e validação de gramáticas.

A importância do algoritmo de reconhecimento de palavras em um PDA reside na sua capacidade de verificar se uma determinada palavra é aceita pelo autômato, o que pode ter aplicações em várias áreas da ciência da computação, como análise de sintaxe, validação de linguagens formais e implementação de interpretadores.

Projeto e Implementação do Algoritmo:

2. Para projetar o algoritmo, foram consideradas as seguintes etapas:

a) Definição da estrutura de dados: A classe "Estado" foi utilizada para representar os estados do autômato de pilha. Ela armazena informações relevantes, como número do estado, se é um estado inicial ou final, se já foi lido, o estado atual, a palavra lida pelo estado e as transições possíveis para outros estados. Inicialmente foi pensada a possibilidade da implementação da estrutura de um Grafo para a realização da tarefa, mas esbarrou na imperícia do aluno em realizar a atividade por meio deste método.

b)A implementação da pilha foi realizada utilizando uma lista chamada "pilha". As operações de empilhar e desempilhar foram simuladas por meio das operações "append" e "remove" da lista, respectivamente. Verificamos se o caractere a ser desempilhado está presente na pilha antes de removê-lo para garantir a consistência do autômato.

c) Gerenciamento do não determinismo: O algoritmo lida com o não-determinismo percorrendo as transições de um estado inicial até um estado final. Em cada iteração, é feita a leitura de um caractere da palavra de entrada e a busca pelas transições correspondentes ao estado atual e ao caractere lido. Em caso de transições vazias ("\*"), são verificadas as transições para estados que não exigem a leitura de um caractere específico.

Metodologia:

3. Utilizamos uma abordagem de desenvolvimento iterativo e incremental para implementar o algoritmo. O código foi escrito em uma linguagem de programação de alto nível, Python, que oferece recursos adequados para representar as estruturas de dados necessárias e facilita a implementação das regras do APND. 

Para testar o algoritmo, foram utilizados casos de teste que abrangem diferentes cenários e gramáticas. Os casos de teste devem incluir palavras válidas que devem ser reconhecidas corretamente pelo algoritmo, bem como palavras inválidas que devem ser rejeitadas. Foram utilizadas as entradas fornecidas pelo professor, que se saiu bem e outra entrada criada pelo autor, porém sem sucesso completo com essa nova entrada.

Para controlar versões do código, fora utilizada a ferramenta GitHub, a atividade em questão possui várias versões, com tentativas de melhorias em reconhecer diversas linguagens e diversas situações, mas a versão que conseguiu êxito no site *run.codes*  não é considerada a melhor.

Resultados e Conclusões:

Com base no gráfico, pode-se realizar uma regressão linear para prever o tempo de execução com base no tamanho da palavra. A regressão linear permite extrapolar e fazer estimativas sobre o desempenho do algoritmo para tamanhos de palavras maiores. 

Imagem gerada utilizando as entradas fornecidas pelo professor e as palavras:

palavras\_teste = ['ab', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']

Em conclusão, o algoritmo implementado demonstrou eficiência no reconhecimento de palavras por um APND no caso apresentado pelo professor, cabe correções futuras, como mudanças da estrutura de dados utilizada para representar o APND, mas de mesmo não obtendo completo sucesso na ferramenta run.codes a experiencia de construir um APND será de grande valia para futuras implementações e servirá de profunda análise sobre as boas práticas de Eng. de software a serem seguidas. Através da análise estatística do tempo de execução, foi possível observar o comportamento do algoritmo em diferentes cenários, fornecendo insights para melhorias futuras e otimizações.

