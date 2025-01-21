## 630. Course Schedule III

### Enunciado:
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

### Exemplo 1
>**Input:** courses = [[1,2]]

>**Output:** 1

### Exemplo 2
>**Input:** courses = [[3,2],[4,3]]

>**Output:** 0

Entradas e saídas obtidas:

Codigo de teste:
<br>

![CodigoTeste](https://github.com/projeto-de-algoritmos-2024/greedy-exerc-leetcode/blob/main/Questoes/Q630/assets/CodigoTeste.png "CodigoTeste")

Saída obtida:
<br>

![SaidasObtidas](https://github.com/projeto-de-algoritmos-2024/greedy-exerc-leetcode/blob/main/Questoes/Q630/assets/OutputTeste.png "SaidasObtidas")

Para o desenvolvimento do código da questão em questão, foi utilizado um algoritmo greedy, especificamente um baseado no estudado, Scheduling to Minimize Lateness, ordenando os dados pela ordem crescente de tempo e utilizando um max heap para controlar o fluxo de inserção dos cursos.
<br>

![Submissao](https://github.com/projeto-de-algoritmos-2024/greedy-exerc-leetcode/blob/main/Questoes/Q630/assets/Aceito.png "Exercicio Submetido")


