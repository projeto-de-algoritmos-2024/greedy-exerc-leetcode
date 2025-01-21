## 1665. Minimum Initial Energy to Finish Tasks

### Enunciado:
You are given an array tasks where tasks[i] = [actuali, minimumi]:

- actuali is the actual amount of energy you spend to finish the ith task.
- minimumi is the minimum amount of energy you require to begin the ith task.

For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all the tasks.

### Exemplo 1
>**Input:** courses = [[1,2],[2,4],[4,8]]

>**Output:** 8

### Exemplo 2
>**Input:** courses = [[1,3],[2,4],[10,11],[10,12],[8,9]]

>**Output:** 32

### Exemplo 3
>**Input:** courses = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]

>**Output:** 27

Entradas e saídas obtidas:

Codigo de teste:
<br>

![CodigoTeste](https://github.com/projeto-de-algoritmos-2024/greedy-exerc-leetcode/blob/main/Questoes/Q1665/assets/CodigoTeste.png "CodigoTeste")

Saída obtida:
<br>

![SaidasObtidas](https://github.com/projeto-de-algoritmos-2024/greedy-exerc-leetcode/blob/main/Questoes/Q1665/assets/OutputTeste.png "SaidasObtidas")

Para o desenvolvimento do código da questão em questão, foi utilizado um algoritmo greedy, a diferença está em como é ordenado e priorizado a execução de tarefas neste algoritmo, priorizando as tarefas que requer mais esforço para ser realizado, além de também garantir custo restante para realizar as outros posteriormente.
<br>

![Submissao](https://github.com/projeto-de-algoritmos-2024/greedy-exerc-leetcode/blob/main/Questoes/Q1665/assets/Aceito.png "Exercicio Submetido")


