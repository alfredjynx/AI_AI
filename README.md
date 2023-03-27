# Web Crawler


### Esportes - 
`Neste caso, você irá partir de uma única url e você sabe que todos os documentos que você irá baixar que estão relacionados com esta url tem 10 links no seu conteúdo. Você também sabe que a profundidade configurada no wget para esportes será de 5. E que cada documento documento tem o tamanho de 500 KBytes. Depois de executado o wget para esportes, quantos documentos (arquivos diferentes) serão armazenados no seu computador? Qual é o espaço que eles irão ocupar em GB?`

Resposta - Se temos uma situação onde cada nodo gera 10 sucessores e uma profundidade de arvore de computação de 5, ao final do processo teremos $10^{5}$ documentos (100 mil), totalizando 50GB de informação.



### Cotidiano - 
`Neste caso, você irá partir de uma única url e você sabe que todos os documentos que você irá baixar que estão relacionados com esta url tem 3 links no seu conteúdo. Você também sabe que a profundidade configurada no wget para o tema cotidiano será de 8. E que cada documento documento tem o tamanho de 800 KBytes. Depois de executado o wget para cotidiano, quantos documentos (arquivos diferentes) serão armazenados no seu computador? Qual é o espaço que eles irão ocupar em GB?`

Resposta - Se temos uma situação onde cada nodo gera 3 sucessores e uma profundidade de árvore de computação de 8, ao final do processo teremos $3^{8}$ documentos (6561), totalizando 5,2488GB de informação.



## Total - 
`Qual é a quantidade total de arquivos armazenados no seu computador? Qual é o espaço total que eles irão ocupar em MB? Justifique a sua resposta.`

Resposta - O total de arquivos armazenados será de $106.561$, totalizando 55,2488GB de informações, ou, 55248,8MB. Isso ocorre poi cada novo sucessor gerado equivale a um novo arquivo que é armazenado no sistema. Vamos utilizar $M$ como a rapresentação da profundidade da árvore, e $N$ como a quantidade de nodos gerados a partir de um. O primeiro caso nos dá 100.000 documentos ($N = 10$, $M = 5$, $N^M$), no segundo, temos 6.561 ($N = 3$, $M = 8$, $N^M$). Após isso, multiplicamos o número de arquivos pelo seu tamanho em KB e convertemos para GB, ficando com 50GB ($\frac{(100.000*500)}{10^{6}}$) e 5,2488GB ($\frac{(6561*800)}{10^{6}}$) respectivamente.





# Grafo

#### 1 - Caminho do A*
O caminho que o algoritmo A* escolheria seria baseado no custo mais a heurística. Portanto, o caminho que nos traz o menor custo total é:

*a*; *c*; *h*; *g*; Achou!



#### 2 - Heurística
A heurística é uma estimativa do custo até a meta. Nesse caso, acho que a heurística mais próxima de explicar os valores escolhidos seria a quantidade de cidades entre um nodo e outro, sem levar em consideração a distância entre as cidades. Por isso, acho que a heurística não seria admissível, já que esse raciocínio causa o algoritmo A* a não retornar um caminho ótimo (o ótimo seria: *a*; *b*; *c*; *h*; *g*;). 


#### 3 - Busca Ganaciosa
O caminho que o algoritmo de Busca Gananciosa escolheria seria baseado exclusivamente na heurística. Portanto, sempre retirando de abertos o nodo com menor estimativa de custo (não olhando o custo real):

*a*; *c*; *d*; *g*; Achou!


#### 4 - Busca em Largura
O caminho que o algoritmo de Busca em Largura escolheria o caminho que seria mais próximo da árvore (menos etapas ou "cidades" percorridas, nesse caso), portanto, ignoraria o custo e a heurística:

*a*; *b*; *g*; Achou!


#### 5 - Solução do algoritmo de Busca em Largura
O caminho que o algoritmo de Busca em Largura, por não levar em consideração o custo, só seria ótimo em uma situação de custo uniforme entre uma etapa e outra. Infelizmente, isso não é o caso, portanto, a sua solução não é ótima já que não nos trás o caminho com menor custo ao final (o ótimo seria: *a*; *b*; *c*; *h*; *g*;). O caminho retornado tem custo 10, e o ótimo possui custo 5.